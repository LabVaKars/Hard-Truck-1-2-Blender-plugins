import enum
import struct
import sys
import time
import datetime
import bpy
import os.path
import os
# from .ksy.kaitaistruct import (KaitaiStream, KaitaiStruct)
# from .ksy.ht2_b3d import Ht2B3d
# from .ksy.b3d_geometry_decode import (extract_simple_vertices, extract_complex_vertices, extract_polygon_8, iter_vec3, extract_polygon_28, iter_point_array)

from .ksy import kaitaistruct, ht2_b3d
from .ksy import b3d_geometry_decode as b3d_dec



from math import sqrt
from math import atan2

import re

from .blocktool_defs import (
    # block params
    Blk001,Blk002,Blk004,Blk005,Blk006,Blk007,Blk009,Blk010,
    Blk011,Blk012,Blk013,Blk014,Blk015,Blk016,Blk017,Blk018,Blk020,
    Blk021,Blk022,Blk023,Blk024,Blk025,Blk026,Blk027,Blk028,Blk029,Blk030,
    Blk031,Blk033,Blk034,Blk035,Blk036,Blk037,Blk039,Blk040,
    # per-face params
    Pfb008,Pfb028,Pfb035,
    # per-vertex params
    Pvb008,Pvb035,
    # other
    VertexFields, FaceFields, ContainerFields, CircleTriggerFields, CylinderTriggerFields
)

from .blocktool import (
    BlockClassHandler
)

from ..consts import (
    EMPTY_NAME,
    BLOCK_TYPE,
    BORDER_COLLECTION
)

from .scripts import (
    create_custom_attribute_c
)


from .common import (
    get_col_property_by_name,
    get_col_property_index_by_name,
    get_used_face,
    get_used_vertices_and_transform,
    get_polygons_by_selected_vertices,
    get_center_coord
)

from ..common import (
    get_res_tool,
    get_res_modules,
    recalc_to_local_coord,
    importb3d_logger
)

from ..compatibility import (
    get_context_collection_objects,
    get_or_create_collection,
    is_before_2_80,
    set_empty_type,
    set_empty_size,
    get_uv_layers,
    get_active_object,
    set_active_object
)

from .data_api_utils import (
    get_portal_visualize_node_group,
    get_vert_collision_visualize_node_group
)

from .restool import (
    get_material_index_in_res
)


#Setup module logger
log = importb3d_logger


def thread_import_b3d(self, files, context):
    for b3dfile in files:
        filepath = os.path.join(self.directory, b3dfile.name)

        log.info('Importing file {}'.format(filepath))
        t = time.mktime(datetime.datetime.now().timetuple())
        with open(filepath, 'rb') as file:
            import_b3d(file, context, self, filepath)
        t = time.mktime(datetime.datetime.now().timetuple()) - t
        log.info('Finished importing in {} seconds'.format(t))


def set_uv_values(uvObj, b3dMesh, uv):
    if is_before_2_80():
        uvLoop = b3dMesh.uv_layers[0]
        uvs_mesh = []

        for i, texpoly in enumerate(uvObj.data):
            poly = b3dMesh.polygons[i]
            for j,loop in enumerate(poly.loop_indices):
                uvs_mesh = [uv[i][j][0],1 - uv[i][j][1]]
                uvLoop.data[loop].uv = uvs_mesh
    else:
        uvs_mesh = []

        for i, texpoly in enumerate(b3dMesh.polygons):
            for j,loop in enumerate(texpoly.loop_indices):
                uvs_mesh = [uv[i][j][0],1 - uv[i][j][1]]
                uvObj.data[loop].uv = uvs_mesh


def assign_material_by_vertices(obj, vert_indexes, mat_index):
    set_active_object(obj)
    vert = obj.data.vertices
    face = obj.data.polygons
    edge = obj.data.edges
    for i in face:
        i.select=False
    for i in edge:
        i.select=False
    for i in vert:
        i.select=False

    for idx in vert_indexes:
        obj.data.vertices[idx].select = True
    selected_polygons = get_polygons_by_selected_vertices((get_active_object()).data)
    for poly in selected_polygons:
        poly.material_index = mat_index


def import_b3d(file, context, self, filepath):

    stream = kaitaistruct.KaitaiStream(file)
    b3d = ht2_b3d.Ht2B3d(stream)
    b3d._read()

    res_modules = get_res_modules()

    res_path = ''
    if len(self.res_location) > 0 and os.path.exists(self.res_location):
        res_path = self.res_location
    else:
        res_path = filepath

    res_basename = os.path.basename(res_path)[:-4] #cut extension

    if self.to_import_textures:
        res_module = get_col_property_by_name(res_modules, res_basename)

    blocks_to_import = self.blocks_to_import

    used_blocks = {}
    for block in blocks_to_import:
        used_blocks[block.name] = block.state


    imp_material_list = b3d.b3d_materials.mat_names


    # Processing vertices

    ex = 0
    i = 0
    lvl = 0
    cnt = 0
    level_groups = []
    vertexes = []
    normals = []
    formats = []
    #
    vertex_block_uvs = []
    poly_block_uvs = []
    # 30 block
    borders = {}
    current_room_name = ""

    begin_counter = 0


    uv = []

    b3d_name = os.path.basename(filepath)

    b3d_obj = bpy.data.objects.get(b3d_name)
    if b3d_obj is None:
        b3d_obj = bpy.data.objects.new(b3d_name, None)
        b3d_obj[BLOCK_TYPE] = 111
        get_context_collection_objects(context).link(b3d_obj) # root object

    parents_by_depth = {0: b3d_obj}  # The file's root object.
    group_objects = {}

    obj_string = [b3d_obj.name]

    parent_obj = context.scene.objects.get(obj_string[-1])
    block_type = None

    def ensure_group(container_obj, number):
        key = (container_obj.name, number)

        if key not in group_objects:
            group_obj = bpy.data.objects.new(f"GROUP_{number}", None)
            group_obj[BLOCK_TYPE] = 444
            group_obj.parent = container_obj
            get_context_collection_objects(context).link(group_obj)
            group_objects[key] = group_obj

        return group_objects[key]
    
    def iter_blocks(blocks, depth=0):
        group_number = 0
        for block in blocks:
            group_number += block.group_before_count
            yield block, depth, group_number

            children = getattr(block.block_data, "child_blocks", None)
            if children is not None:
                yield from iter_blocks(children.child_block, depth + 1)

    for block, depth, group_number in iter_blocks(
        b3d.data_chunks.data_blocks
    ):

        only_name = block.block_name.rstrip("\x00")
        block_type = block.block_type

        obj_name =  EMPTY_NAME if (len(only_name) == 0) else only_name
        real_name = only_name

        t1 = time.perf_counter()
        
        b3d_init = None
        if block_type in VertexFields.bnum_list:
            b3d_init = BlockClassHandler.get_object_initializer_by_class(VertexFields)
        elif block_type in FaceFields.bnum_list:
            b3d_init = BlockClassHandler.get_object_initializer_by_class(FaceFields)
        elif block_type in ContainerFields.bnum_list:
            b3d_init = BlockClassHandler.get_object_initializer_by_class(ContainerFields)
        elif block_type in CircleTriggerFields.bnum_list:
            b3d_init = BlockClassHandler.get_object_initializer_by_class(CircleTriggerFields)
        elif block_type in CylinderTriggerFields.bnum_list:
            b3d_init = BlockClassHandler.get_object_initializer_by_class(CylinderTriggerFields)
        else:
            b3d_init = BlockClassHandler.get_object_initializer_by_class(BlockClassHandler.get_block_class(block_type))
            
        # block changes

        container_obj = parents_by_depth[depth]
        parent_obj = container_obj
        parents_by_depth[depth + 1] = container_obj

        if depth > 0:
            key = (container_obj.name, group_number)
            parent_obj = group_objects.get(key, container_obj)

            if group_number > 0 and key not in group_objects:
                raise ValueError(
                    f"Missing GROUP_{group_number} under {container_obj.name}"
                )

        obj_string = [parent_obj.name, ""]
        payload = block.block_data

        if (block_type in [6, 7, 36, 37]):
            vertexes = []
            vertex_block_uvs = []
            normals = []
            intensities = []

            if block_type in [6, 7]:
                vertexes, uv0 = b3d_dec.extract_simple_vertices(payload)
                vertex_block_uvs = [uv0]
                normals = [(1.0, 1.0, 1.0) for i in range(payload.vert_count)]
                intensities = [1.0 for i in range(payload.vert_count)]
            elif block_type in [36, 37]:
                vertexes, vertex_block_uvs, normals, intensities = b3d_dec.extract_complex_vertices(payload)

            b3d_obj = bpy.data.objects.new(obj_name, None)
            b3d_init(b3d_obj, payload)
            b3d_obj[BLOCK_TYPE] = block_type

            b3d_obj.parent = parent_obj
            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = b3d_obj.name

        elif (block_type in [8, 35]):
            origin = payload.bound1.value[:3]
            polygons = payload.poly if block_type == 8 else payload.vert

            faces = []
            face_uvs = []
            face_texnums = []
            formats = []
            mesh_normals = list(normals)
            texnum = payload.texnum if block_type == 35 else None

            for polygon in polygons:
                indices, uv_layers, corner_normals, _ = b3d_dec.extract_polygon_8(polygon)

                if not polygon.use_uv:
                    # uv_layers = [[vertex_block_uvs[0][index] for index in indices]]
                    uv_layers = [
                        [layer[index] for index in indices]
                        for layer in vertex_block_uvs
                    ]
                if polygon.normal_switch == 0:
                    for index, normal in zip(indices, corner_normals):
                        mesh_normals[index] = normal

                format_raw = polygon.format_raw

                texnum = polygon.texnum

                if block_type == 8:
                    corner_faces = []
                    for t in range(len(indices) - 2):
                        if polygon.format & 0x80:
                            corners = (
                                (t, t + 2, t + 1)
                                if t % 2 else (t, t + 1, t + 2)
                            )
                        else:
                            corners = (
                                (t, t + 1, t + 2)
                                if t % 2 else (t - 1, t, t + 1)
                            )
                        corner_faces.append(corners)
                else:
                    corner_faces = [tuple(range(len(indices)))]

                for corners in corner_faces:
                    faces.append(tuple(indices[i] for i in corners))
                    face_uvs.append([
                        tuple(layer[i] for i in corners) for layer in uv_layers
                    ])
                    face_texnums.append(texnum)
                    formats.append(format_raw)

            local_vertices, local_faces, source_indices, _, _ = (
                get_used_vertices_and_transform(vertexes, faces)
            )

            b3d_mesh = bpy.data.meshes.new(obj_name)
            b3d_mesh.from_pydata(
                recalc_to_local_coord(origin, local_vertices), [], local_faces
            )

            if mesh_normals and source_indices:
                if hasattr(b3d_mesh, "use_auto_smooth"):
                    b3d_mesh.use_auto_smooth = True
                b3d_mesh.normals_split_custom_set_from_vertices(
                    [mesh_normals[index] for index in source_indices]
                )

            layer_count = max((len(layers) for layers in face_uvs), default=0)
            for layer_index in range(layer_count):
                uv_layer = get_uv_layers(b3d_mesh).new(name="UVMap")
                for face, layers in zip(b3d_mesh.polygons, face_uvs):
                    if layer_index < len(layers):
                        for loop_index, (u, v) in zip(
                            face.loop_indices, layers[layer_index]
                        ):
                            uv_layer.data[loop_index].uv = (u, 1.0 - v)

            format_field = (
                Pfb008.Format_Flags if block_type == 8 else Pfb035.Format_Flags
            )
            create_custom_attribute_c(b3d_mesh, formats, format_field)

            b3d_obj = bpy.data.objects.new(obj_name, b3d_mesh)
            b3d_init(b3d_obj, payload)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_obj.location = origin
            b3d_obj.parent = parent_obj

            if self.to_import_textures:
                texture_numbers = (
                    list(dict.fromkeys(face_texnums))
                    if block_type == 8 else [texnum]
                )
                slots = {}

                for texture_number in texture_numbers:
                    mat_name = imp_material_list[texture_number].rstrip("\x00")
                    res_index = get_material_index_in_res(mat_name, res_basename)
                    slots[texture_number] = len(b3d_mesh.materials)
                    b3d_mesh.materials.append(
                        res_module.materials[res_index].id_mat
                    )

                if block_type == 8:
                    for face, texture_number in zip(
                        b3d_mesh.polygons, face_texnums
                    ):
                        face.material_index = slots[texture_number]

            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name

        elif (block_type in [19]):
            
            current_room_name = "{}:{}".format(res_basename, obj_name)
                        
            b3d_obj = bpy.data.objects.new(obj_name, None)
            b3d_init(b3d_obj, payload)
            b3d_obj[BLOCK_TYPE] = block_type

            b3d_obj.parent = parent_obj
            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = b3d_obj.name

        elif (block_type in [20]):

            coords = list(b3d_dec.iter_vec3(payload.coords_raw))
            origin = coords[0] if coords else payload.bound1.value[:3]

            curve_data = bpy.data.curves.new("curve", type="CURVE")
            curve_data.dimensions = "3D"
            curve_data.resolution_u = 2

            if coords:
                polyline = curve_data.splines.new("POLY")
                polyline.points.add(len(coords) - 1)
                for point, (x, y, z) in zip(
                    polyline.points, recalc_to_local_coord(origin, coords)
                ):
                    point.co = (x, y, z, 1.0)

            b3d_obj = bpy.data.objects.new(obj_name, curve_data)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.location = origin
            b3d_obj.parent = parent_obj

            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = b3d_obj.name

            modifier = b3d_obj.modifiers.new("Vert_collision_node", type="NODES")
            modifier.node_group = get_vert_collision_visualize_node_group()

        
        elif block_type == 23:
            vertices = []
            faces = []

            for face_data in payload.verts:
                start = len(vertices)
                vertices.extend(b3d_dec.iter_vec3(face_data.verts_raw))
                faces.append(tuple(range(start, len(vertices))))

            centroid = get_center_coord(vertices)
            mesh = bpy.data.meshes.new(obj_name)
            mesh.from_pydata(recalc_to_local_coord(centroid, vertices), [], faces)

            b3d_obj = bpy.data.objects.new(obj_name, mesh)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.location = centroid
            b3d_obj.parent = parent_obj


            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name

        elif (block_type == 24): 

            m11, m12, _ = payload.coord1.value
            m21, m22, _ = payload.coord2.value
            m31, m32, m33 = payload.coord3.value

            cy = sqrt(m33 * m33 + m31 * m31)
            x = atan2(-m32, cy)

            if cy > 16 * sys.float_info.epsilon:
                y = atan2(m31, m33)
                z = atan2(m12, m22)
            else:
                y = 0.0
                z = atan2(-m21, m11)

            b3d_obj = bpy.data.objects.new(obj_name, None)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.rotation_euler = (x, y, z)
            b3d_obj.location = payload.pos.value
            b3d_obj.parent = parent_obj
            set_empty_type(b3d_obj, "ARROWS")
            
            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name

        elif block_type == 28:
            origin = payload.bound1.value[:3]
            sprite_center = payload.sprite_center.value
            cx, cy, cz = sprite_center

            vertices = []
            faces = []
            face_uvs = []
            formats = []
            face_texnums = []

            for polygon in payload.vert:
                scale_u, scale_v, uv_layers = b3d_dec.extract_polygon_28(polygon)
                start = len(vertices)
                vertices.extend((cx, cy - u, cz + v) for u, v in zip(scale_u, scale_v))

                for t in range(len(scale_u) - 2):
                    if polygon.format_raw & 0x80:
                        corners = (t, t + 2, t + 1) if t % 2 else (t, t + 1, t + 2)
                    else:
                        corners = (t, t + 1, t + 2) if t % 2 else (t - 1, t, t + 1)

                    # The legacy t - 1 wraps within this strip.
                    corners = tuple(i % len(scale_u) for i in corners)
                    faces.append(tuple(start + i for i in corners))
                    face_uvs.append([
                        tuple(layer[i] for i in corners) for layer in uv_layers
                    ])
                    formats.append(polygon.format_raw)
                    face_texnums.append(polygon.texnum)

            mesh = bpy.data.meshes.new(obj_name)
            mesh.from_pydata(recalc_to_local_coord(origin, vertices), [], faces)

            layer_count = max((len(layers) for layers in face_uvs), default=0)
            for layer_index in range(layer_count):
                uv_layer = get_uv_layers(mesh).new(name="UVMap")
                for face, layers in zip(mesh.polygons, face_uvs):
                    if layer_index < len(layers):
                        for loop_index, (u, v) in zip(
                            face.loop_indices, layers[layer_index]
                        ):
                            uv_layer.data[loop_index].uv = (u, 1.0 - v)

            create_custom_attribute_c(mesh, formats, Pfb028.Format_Flags)

            if self.to_import_textures:
                slots = {}
                for face, texnum in zip(mesh.polygons, face_texnums):
                    if texnum not in slots:
                        mat_name = imp_material_list[texnum]
                        res_index = get_material_index_in_res(mat_name, res_basename)
                        slots[texnum] = len(mesh.materials)
                        mesh.materials.append(res_module.materials[res_index].id_mat)
                    face.material_index = slots[texnum]

            b3d_obj = bpy.data.objects.new(obj_name, mesh)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.location = origin
            b3d_obj.parent = parent_obj

            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name

        elif block_type == 30:

            connected_room_name = payload.room_name.rstrip("\x00") or EMPTY_NAME
            parts = connected_room_name.split(":")

            if len(parts) == 2:
                module_name, room_name = parts
            elif len(parts) == 1:
                module_name, room_name = res_basename, parts[0]
            else:
                module_name, room_name = "", ""

            full_room_name = f"{module_name}:{room_name}"
            sorted_rooms = sorted((current_room_name, full_room_name))
            border_name = "|".join(sorted_rooms)

            if border_name not in borders:
                p1 = tuple(payload.point1.value)
                p2 = tuple(payload.point2.value)

                if sorted_rooms[0] == current_room_name:
                    points = [p1, p2]
                else:
                    points = [(p2[0], p2[1], p1[2]), (p1[0], p1[1], p2[2])]

                borders[border_name] = {
                    "bounding_point": p1,
                    "points": points,
                }

            continue

        elif block_type == 34:

            curve_data = bpy.data.curves.new("curve", type="CURVE")
            curve_data.dimensions = "3D"
            curve_data.resolution_u = 2
            curve_data.bevel_depth = 0.01

            unknown1 = 0
            if payload.unk_count:
                polyline = curve_data.splines.new("POLY")
                polyline.points.add(payload.unk_count - 1)

                records = b3d_dec.iter_point_array(payload.unk_floats_raw)
                for point, (x, y, z, unknown1) in zip(polyline.points, records):
                    point.co = (x, y, z, 1.0)


            b3d_obj = bpy.data.objects.new(obj_name, curve_data)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.parent = parent_obj
            
            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name

        elif block_type == 40:
            b3d_obj = bpy.data.objects.new(obj_name, None)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.location = payload.bound1.value[:3]
            b3d_obj.parent = parent_obj
            set_empty_type(b3d_obj, "SPHERE")
            set_empty_size(b3d_obj, payload.bound1.value[3])

            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name


        else: #all blocks that dont have specific handling(only block parameter initialization)
            b3d_obj = bpy.data.objects.new(obj_name, None)
            b3d_obj[BLOCK_TYPE] = block_type
            b3d_init(b3d_obj, payload)
            b3d_obj.parent = parent_obj

            get_context_collection_objects(context).link(b3d_obj)
            real_name = b3d_obj.name
            obj_string[-1] = real_name

        children = getattr(payload, "child_blocks", None)

        if children is not None:
            child_blocks = children.child_block

            marker_count = (
                sum(child.group_before_count for child in child_blocks)
                + block.group_after_count
            )
            observed_count = (
                marker_count + 1 if child_blocks or marker_count else 0
            )

            # Fixed counts follow the existing exporter's conventions.
            fixed_counts = {2: 2, 9: 2, 10: 2, 22: 2}
            declared_count = fixed_counts.get(block_type)

            if block_type == 21:
                declared_count = payload.group_cnt

            if declared_count is not None:
                if observed_count > declared_count:
                    raise ValueError(
                        f"{obj_name}: markers indicate {observed_count} groups, "
                        f"but block {block_type} declares {declared_count}"
                    )
                group_count = declared_count
            elif block_type in [29] or marker_count:
                group_count = max(1, observed_count)
            else:
                group_count = 0

            for number in range(group_count):
                ensure_group(b3d_obj, number)
        
        parents_by_depth[depth + 1] = b3d_obj
        t2 = time.perf_counter()

        log.debug("Time: {:.6f} | Block #{}: {}".format(t2-t1, block_type, real_name))

    #create room borders(30)
    transf_collection = get_or_create_collection(BORDER_COLLECTION)

    for key in borders.keys():

        border = borders[key]

        # b3d_mesh = (bpy.data.meshes.new("{}_mesh".format(key)))
        #0-x
        #1-y
        #2-z

        
        curve_data = bpy.data.curves.new('curve', type='CURVE')

        curve_data.dimensions = '3D'
        curve_data.resolution_u = 2

        # map coords to spline
        polyline = curve_data.splines.new('POLY')
        polyline.points.add(1)

        p1 = border['points'][0]
        p2 = border['points'][1]

        p1l = recalc_to_local_coord(p1, [p1])[0]
        p2l = recalc_to_local_coord(p1, [p2])[0]

        polyline.points[0].co = (p1l[0], p1l[1], p1l[2], 1)
        polyline.points[1].co = (p2l[0], p2l[1], p2l[2], 1)

        room_names = key.split("|")
        splitted1 = room_names[0].split(":")
        splitted2 = room_names[1].split(":")

        res_name1 = splitted1[0]
        room_name1 = splitted1[1]

        res_name2 = splitted2[0]
        room_name2 = splitted2[1]

        b3d_obj = bpy.data.objects.new(key, curve_data)
        b3d_obj[BLOCK_TYPE] = 30
        b3d_obj.location = p1
        b3d_init(b3d_obj) #manual init for block 30
        b3d_obj[Blk030.ResModule1.get_prop()] = res_name1
        b3d_obj[Blk030.RoomName1.get_prop()] = room_name1
        b3d_obj[Blk030.ResModule2.get_prop()] = res_name2
        b3d_obj[Blk030.RoomName2.get_prop()] = room_name2

        b3d_obj.modifiers.new('Portal_node', type='NODES')
        gnode_modifier = b3d_obj.modifiers.get('Portal_node')

        gnode_modifier.node_group = get_portal_visualize_node_group()

        b3d_obj.parent = None
        transf_collection.objects.link(b3d_obj)
