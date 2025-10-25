import bpy
import math

from ..common import (
    recalc_to_local_coord,
    operators_logger
)

from .. import consts

from .data_api_utils import (
    get_portal_visualize_node_group,
    get_vert_collision_visualize_node_group
)

from .common import (
    is_root_obj,
    get_root_obj,
    get_room_obj,
    is_inside_object,
    get_class_attributes,
    get_mult_obj_bounding_sphere
)

from .scripts import (
    show_hide_render_tree_branch,
    show_hide_lod_tree_branch,
    apply_remove_transforms,
    hide_lod,
    show_lod,
    show_conditionals,
    hide_conditionals,
    show_hide_obj_by_type,
    get_objs_by_type,
    set_objs_by_type,
    get_per_face_by_type,
    set_per_face_by_type,
    get_per_vertex_by_type,
    set_per_vertex_by_type,
    show_hide_sphere,
    get_obj_by_prop,
    set_obj_by_prop,
    create_custom_attribute,
    select_similar_objects_by_type,
    select_similar_faces_by_type,
    create_render_branch_materials
)

from .data_api_utils import (
    get_render_center_object
)

from .classes import (
    BlockClassHandler,
    FieldType
)

from .class_descr import (
    Blk009, Blk010,
    Blk020,Blk021,Blk023, Blk030,
    Pfb008, Pfb028, Pfb035, Pvb008, Pvb035,
    Blk050, Blk051, Blk052,
    ResBlock
)




from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        EnumProperty,
                        PointerProperty,
                        FloatVectorProperty,
                        CollectionProperty
                        )

from ..compatibility import (
    get_ui_region,
    get_active_object,
    set_active_object,
    make_annotations,
    layout_split,
    get_context_collection_objects,
    get_or_create_collection,
    remove_collection,
    is_before_2_80,
    is_before_2_93,
    set_empty_type,
    set_empty_size,
    get_cursor_location
)
    

#Setup module logger
log = operators_logger

# ------------------------------------------------------------------------
#    operators / buttons
# ------------------------------------------------------------------------

class SetParentOperator(bpy.types.Operator):
    bl_idname = "wm.set_parent_operator"
    bl_label = "Set parent"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        if context.object is None:
            self.report({'INFO'}, "No object selected")
            return {'FINISHED'}

        mytool.parent_str = context.object.name

        return {'FINISHED'}


class SingleAddOperator(bpy.types.Operator):
    bl_idname = "wm.single_add_operator"
    bl_label = "Add block to scene"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        block_type = int(mytool.add_block_type_enum)

        cursor_pos = get_cursor_location()

        parent_obj = get_active_object()

        object_name = mytool.block_name_string

        zclass = BlockClassHandler.get_class_def_by_type(block_type)

        # objects that are located in 0,0,0(technical empties)
        if block_type in [
            111,444,
            0,1,2,3,4,5,
            6,7,36,37, # vertexes
            # 8, 35 - polygons
            9,10,21,22, # groups
            11,12,13,14,15,16,17,18,19,
            # 20 - 2d collision
            # 23 - 3d collision
            # 28 - 2d sprite
            # 30 - portal
            # 24 - locator
            25,26,27,29,31,33,34,39,
            # 40 - generator
            51,52
        ]:
            b3d_obj = bpy.data.objects.new(object_name, None)
            b3d_obj.location=(0.0,0.0,0.0)
            b3d_obj[consts.BLOCK_TYPE] = block_type
            if parent_obj is not None and block_type != 111:
                b3d_obj.parent = parent_obj
            if block_type not in [111, 444, 0, 3, 8, 19]: # blocks without custom parameters
                set_objs_by_type(b3d_obj, zclass)
            get_context_collection_objects(context).link(b3d_obj)

            if block_type in [9,10,21,22]: #objects with subgroups

                group_cnt = 0
                if block_type in [9, 10]:
                    group_cnt = 2
                elif block_type == 21:
                    group_cnt = b3d_obj[Blk021.GroupCnt.get_prop()]

                for i in range(group_cnt):
                    group = bpy.data.objects.new("GROUP_{}".format(i), None)
                    group.location=(0.0,0.0,0.0)
                    group[consts.BLOCK_TYPE] = 444
                    group.parent = b3d_obj
                    get_context_collection_objects(context).link(group)

        elif block_type in [24, 40, 51, 52]: # empties which location is important

            b3d_obj = bpy.data.objects.new(object_name, None)
            b3d_obj.location=cursor_pos
            b3d_obj[consts.BLOCK_TYPE] = block_type
            if parent_obj is not None and block_type != 111:
                b3d_obj.parent = parent_obj
            if block_type not in [111, 444, 0, 3, 8, 19]: # blocks without custom parameters
                set_objs_by_type(b3d_obj, zclass)

            if block_type in [24, 52]:
                set_empty_type(b3d_obj, 'ARROWS')
            elif block_type == 40:
                set_empty_type(b3d_obj, 'SPHERE')
                set_empty_size(b3d_obj, 5)
            elif block_type == 51:
                set_empty_type(b3d_obj, 'PLAIN_AXES')

            get_context_collection_objects(context).link(b3d_obj)

        elif block_type == 28:

            sprite_center = cursor_pos

            l_vertexes = [
                (0.0, -1.0, -1.0),
                (0.0, -1.0, 1.0),
                (0.0, 1.0, 1.0),
                (0.0, 1.0, -1.0)
            ]

            l_faces = [(0,1,2,3)]

            b3d_mesh = (bpy.data.meshes.new(object_name))
            b3d_mesh.from_pydata(l_vertexes,[],l_faces)

            b3d_obj = bpy.data.objects.new(object_name, b3d_mesh)
            b3d_obj.location=sprite_center
            b3d_obj[consts.BLOCK_TYPE] = block_type
            if parent_obj is not None and block_type != 111:
                b3d_obj.parent = parent_obj
            if block_type not in [111, 444, 0, 3, 8, 19]: # blocks without custom parameters
                set_objs_by_type(b3d_obj, zclass)
            get_context_collection_objects(context).link(b3d_obj)

        elif block_type == 30:

            sprite_center = cursor_pos
            
            l_points = [
                (0.0, 0.0, 0.0),
                (0.0, 20.0, 40.0)
            ]

            curve_data = bpy.data.curves.new(object_name, type='CURVE')

            curve_data.dimensions = '3D'
            curve_data.resolution_u = 2

            # map coords to spline
            polyline = curve_data.splines.new('POLY')
            polyline.points.add(1)

            p1 = l_points[0]
            p2 = l_points[1]

            p1l = recalc_to_local_coord(p1, [p1])[0]
            p2l = recalc_to_local_coord(p1, [p2])[0]

            polyline.points[0].co = (p1l[0], p1l[1], p1l[2], 1)
            polyline.points[1].co = (p2l[0], p2l[1], p2l[2], 1)

            b3d_obj = bpy.data.objects.new(object_name, curve_data)
            b3d_obj[consts.BLOCK_TYPE] = block_type
            b3d_obj.location = p1
            if parent_obj is not None and block_type != 111:
                b3d_obj.parent = parent_obj
            if block_type not in [111, 444, 0, 3, 8, 19]: # blocks without custom parameters
                set_objs_by_type(b3d_obj, zclass)

            b3d_obj.modifiers.new('Portal_node', type='NODES')
            gnode_modifier = b3d_obj.modifiers.get('Portal_node')

            gnode_modifier.node_group = get_portal_visualize_node_group()

            get_context_collection_objects(bpy.context).link(b3d_obj)

        return {'FINISHED'}

class HierarchyAddOperator(bpy.types.Operator):
    bl_idname = "wm.hierarchy_add_operator"
    bl_label = "Add block hierarchy to scene"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        b3d_obj = get_active_object()

        blocktool = bpy.context.scene.block_tool
        current_hier = getattr(mytool, "current_hierarchy_enum")
        lod_level = getattr(mytool, "lod_level_int")
        block_name = getattr(mytool, "block_name_string")

        if current_hier == 'LOD_9':
            
            stack = [b3d_obj]
            group_cnt = 2
            next_stack = []
            for lvl in range(lod_level):
                while stack:
                    parent_obj = stack.pop()
                    # create object ...
                    new_b3d = bpy.data.objects.new("{}_{}".format(block_name, lvl), None)
                    new_b3d.location=(0.0,0.0,0.0)
                    new_b3d[consts.BLOCK_TYPE] = 9
                    if parent_obj is not None:
                        new_b3d.parent = parent_obj
                    set_objs_by_type(new_b3d, Blk009)
                    get_context_collection_objects(context).link(new_b3d)

                    # and its subgroups
                    for i in range(group_cnt):
                        group = bpy.data.objects.new("GROUP_{}".format(i), None)
                        group.location=(0.0,0.0,0.0)
                        group[consts.BLOCK_TYPE] = 444
                        group.parent = new_b3d
                        get_context_collection_objects(context).link(group)
                        next_stack.append(group)
                stack = next_stack.copy()
                next_stack = []

        elif current_hier == 'LOD_10':

            stack = [b3d_obj]
            group_cnt = 2
            next_stack = []
            for lvl in range(lod_level):
                while stack:
                    parent_obj = stack.pop()
                    # create object ...
                    new_b3d = bpy.data.objects.new("{}_{}".format(block_name, lvl), None)
                    new_b3d.location=(0.0,0.0,0.0)
                    new_b3d[consts.BLOCK_TYPE] = 10
                    if parent_obj is not None:
                        new_b3d.parent = parent_obj
                    set_objs_by_type(new_b3d, Blk010)
                    get_context_collection_objects(context).link(new_b3d)

                    # and its subgroups
                    for i in range(group_cnt):
                        group = bpy.data.objects.new("GROUP_{}".format(i), None)
                        group.location=(0.0,0.0,0.0)
                        group[consts.BLOCK_TYPE] = 444
                        group.parent = new_b3d
                        get_context_collection_objects(context).link(group)
                        next_stack.append(group)
                stack = next_stack.copy()
                next_stack = []

        elif current_hier == 'LOD_21':
            group_cnt = b3d_obj[Blk021.GroupCnt.get_prop()]
            pass

        return {'FINISHED'}

class CastAddOperator(bpy.types.Operator):
    bl_idname = "wm.cast_add_operator"
    bl_label = "Cast to B3D"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        cursor_pos = get_cursor_location()

        cast_type = mytool.cast_type_enum
        parent_obj = bpy.data.objects.get(mytool.parent_str)

        to_copy = int(mytool.cast_copy)

        if cast_type == 'mesh':
            vert_type = int(mytool.vertex_block_enum)
            poly_type = int(mytool.poly_block_enum)

            vertclass = BlockClassHandler.get_class_def_by_type(vert_type)
            polyclass = BlockClassHandler.get_class_def_by_type(poly_type)

            #creating vertex block
            vert_obj = bpy.data.objects.new(consts.EMPTY_NAME, None)
            vert_obj.location=(0.0,0.0,0.0)
            vert_obj[consts.BLOCK_TYPE] = vert_type
            vert_obj.parent = parent_obj
            set_objs_by_type(vert_obj, vertclass)
            get_context_collection_objects(context).link(vert_obj)

            # creating poly blocks
            for poly_obj in context.selected_objects:
                if poly_obj.type == 'MESH':

                    if to_copy:
                        new_obj = poly_obj.copy()
                        new_obj.data = poly_obj.data.copy()
                        new_obj[consts.BLOCK_TYPE] = poly_type
                        new_obj.parent = vert_obj
                        if poly_type != 8:
                            set_objs_by_type(new_obj, polyclass)

                        formats = [2]*len(new_obj.data.polygons)
                        if poly_type == 8:
                            create_custom_attribute(new_obj.data, formats, Pfb008, Pfb008.Format_Flags)
                        elif poly_type == 35:
                            create_custom_attribute(new_obj.data, formats, Pfb035, Pfb035.Format_Flags)

                        get_context_collection_objects(context).link(new_obj)

                        log.info("Created new B3D object: {}.".format(new_obj.name))
                    else:
                        poly_obj[consts.BLOCK_TYPE] = poly_type
                        poly_obj.parent = vert_obj
                        if poly_type != 8:
                            set_objs_by_type(poly_obj, polyclass)
                        formats = [2]*len(poly_obj.data.polygons)
                        if poly_type == 8:
                            create_custom_attribute(poly_obj.data, formats, Pfb008, Pfb008.Format_Flags)
                        elif poly_type == 35:
                            create_custom_attribute(poly_obj.data, formats, Pfb035, Pfb035.Format_Flags)

                        log.info("Cast existing B3D object: {}.".format(poly_obj.name))

                else:
                    log.info("Selected object {} is not 'Mesh'. Changes not applied.".format(poly_obj.name))

        elif cast_type == 'colis3D':

            for poly_obj in context.selected_objects:
                if poly_obj.type == 'MESH':

                    if to_copy:
                        new_obj = poly_obj.copy()
                        new_obj.data = poly_obj.data.copy()
                        new_obj[consts.BLOCK_TYPE] = 23
                        new_obj.parent = parent_obj
                        set_objs_by_type(new_obj, Blk023)
                        get_context_collection_objects(context).link(new_obj)
                        log.info("Created new B3D 3d collision: {}.".format(new_obj.name))
                    else:
                        poly_obj[consts.BLOCK_TYPE] = 23
                        poly_obj.parent = parent_obj
                        set_objs_by_type(poly_obj, Blk023)
                        log.info("Cast existing object to B3D 3d collision: {}.".format(poly_obj.name))
                else:
                    log.info("Selected object {} is not 'Mesh'. Changes not applied.".format(poly_obj.name))

        elif cast_type == 'colis2D':

            for poly_obj in context.selected_objects:
                if poly_obj.type == 'CURVE':
                    new_obj = None
                    if to_copy:
                        new_obj = poly_obj.copy()
                        new_obj.data = poly_obj.data.copy()
                    else: 
                        new_obj = poly_obj

                    new_obj[consts.BLOCK_TYPE] = 20
                    new_obj.parent = parent_obj
                    set_objs_by_type(new_obj, Blk020)

                    new_obj.modifiers.new('Portal_node', type='NODES')
                    gnode_modifier = new_obj.modifiers.get('Portal_node')

                    gnode_modifier.node_group = get_vert_collision_visualize_node_group()

                    if to_copy:
                        get_context_collection_objects(context).link(new_obj)
                        log.info("Created new B3D 2d colision: {}.".format(new_obj.name))
                    else:
                        log.info("Cast exiting object to B3D 2d colision: {}.".format(poly_obj.name))

                else:
                    log.info("Selected object {} is not 'Curve'. Changes not applied.".format(poly_obj.name))

        elif cast_type == 'way50':

            for poly_obj in context.selected_objects:

                if parent_obj is None or parent_obj == '':
                    parent_obj = poly_obj.parent

                block_type = int(cast_type[3:])
                zclass = None
                if block_type == 50:
                    zclass = Blk050

                if poly_obj.type == 'CURVE':

                    if to_copy:
                        new_obj = poly_obj.copy()
                        new_obj.data = poly_obj.data.copy()
                        new_obj[consts.BLOCK_TYPE] = block_type
                        new_obj.data.bevel_depth = 0.3
                        new_obj.data.bevel_mode = 'ROUND'
                        new_obj.parent = parent_obj
                        set_objs_by_type(new_obj, zclass)
                        get_context_collection_objects(context).link(new_obj)
                        log.info("Created new WAY Path: {}.".format(new_obj.name))
                    else:
                        poly_obj[consts.BLOCK_TYPE] = block_type
                        poly_obj.data.bevel_depth = 0.3
                        poly_obj.data.bevel_mode = 'ROUND'
                        poly_obj.parent = parent_obj
                        set_objs_by_type(poly_obj, zclass)
                        log.info("Cast existing object to WAY Path: {}.".format(poly_obj.name))

                else:
                    log.info("Selected object {} is not 'Curve'. Changes not applied.".format(poly_obj.name))

        elif  cast_type in ['way51', 'way52']:
            
            for poly_obj in context.selected_objects:

                if parent_obj is None or parent_obj == '':
                    parent_obj = poly_obj.parent

                block_type = int(cast_type[3:])
                zclass = None
                empty_type = 'PLAIN_AXES'
                
                if block_type == 51:
                    zclass = Blk051
                    empty_type = 'PLAIN_AXES'
                if block_type == 52:
                    zclass = Blk052
                    empty_type = 'ARROWS'

                if poly_obj.type == 'EMPTY':

                    if to_copy:
                        new_obj = poly_obj.copy()
                        new_obj[consts.BLOCK_TYPE] = block_type
                        set_empty_type(new_obj, empty_type)
                        new_obj.parent = parent_obj
                        set_objs_by_type(new_obj, zclass)
                        get_context_collection_objects(context).link(new_obj)
                        log.info("Created new WAY Path: {}.".format(new_obj.name))
                    else:
                        poly_obj[consts.BLOCK_TYPE] = block_type
                        set_empty_type(poly_obj, empty_type)
                        poly_obj.parent = parent_obj
                        set_objs_by_type(poly_obj, zclass)
                        log.info("Cast existing object to WAY Path: {}.".format(poly_obj.name))

                else:
                    log.info("Selected object {} is not 'Empty'. Changes not applied.".format(poly_obj.name))


        return {'FINISHED'}

class GetVertexValuesOperator(bpy.types.Operator):
    bl_idname = "wm.get_vertex_values_operator"
    bl_label = "Get vertex params"

    def execute(self, context):
        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        if block_type == 8:
            get_per_vertex_by_type(b3d_obj.data, Pvb008)
        elif block_type == 35:
            get_per_vertex_by_type(b3d_obj.data, Pvb035)

        return {'FINISHED'}

class GetFaceValuesOperator(bpy.types.Operator):
    bl_idname = "wm.get_face_values_operator"
    bl_label = "Get face params"

    def execute(self, context):
        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        if block_type == 8:
            get_per_face_by_type(b3d_obj.data, Pfb008)
        elif block_type == 28:
            get_per_face_by_type(b3d_obj.data, Pfb028)
        elif block_type == 35:
            get_per_face_by_type(b3d_obj.data, Pfb035)

        return {'FINISHED'}

class GetValuesOperator(bpy.types.Operator):
    bl_idname = "wm.get_block_values_operator"
    bl_label = "Get object params"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        zclass = BlockClassHandler.get_class_def_by_type(block_type)

        if zclass is not None:
            get_objs_by_type(b3d_obj, zclass)

        return {'FINISHED'}

@make_annotations
class GetPropValueOperator(bpy.types.Operator):
    bl_idname = "wm.get_prop_value_operator"
    bl_label = "Get param value"

    pname = StringProperty()

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        zclass = BlockClassHandler.get_class_def_by_type(block_type)

        if zclass is not None:
            get_obj_by_prop(b3d_obj, zclass, self.pname)

        return {'FINISHED'}

class SetFaceValuesOperator(bpy.types.Operator):
    bl_idname = "wm.set_face_values_operator"
    bl_label = "Save face params"

    def execute(self, context):
        curtype = get_active_object()[consts.BLOCK_TYPE]
        objects = [cn for cn in bpy.context.selected_objects if cn[consts.BLOCK_TYPE] is not None and cn[consts.BLOCK_TYPE] == curtype]

        for i in range(len(objects)):

            b3d_obj = objects[i]
            block_type = b3d_obj[consts.BLOCK_TYPE]

            if block_type == 8:
                set_per_face_by_type(b3d_obj.data, Pfb008)
            elif block_type == 28:
                set_per_face_by_type(b3d_obj.data, Pfb028)
            elif block_type == 35:
                set_per_face_by_type(b3d_obj.data, Pfb035)

        return {'FINISHED'}

class SetVertexValuesOperator(bpy.types.Operator):
    bl_idname = "wm.set_vertex_values_operator"
    bl_label = "Save vertex params"

    def execute(self, context):
        curtype = get_active_object()[consts.BLOCK_TYPE]
        objects = [cn for cn in bpy.context.selected_objects if cn[consts.BLOCK_TYPE] is not None and cn[consts.BLOCK_TYPE] == curtype]

        for i in range(len(objects)):

            b3d_obj = objects[i]
            block_type = b3d_obj[consts.BLOCK_TYPE]

            if block_type == 8:
                set_per_vertex_by_type(b3d_obj.data, Pvb008)
            elif block_type == 35:
                set_per_vertex_by_type(b3d_obj.data, Pvb035)

        return {'FINISHED'}

class SetRoomAndModuleOperator(bpy.types.Operator):
    bl_idname = "wm.set_room_and_module_operator"
    bl_label = "Get current module/room"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        active_obj = get_active_object()

        if active_obj is not None:
            current_module = get_root_obj(active_obj)
            if current_module is not None:
                setattr(mytool, 'active_module', current_module.name[:-4])
            else:
                setattr(mytool, 'active_module', '')
            current_room = get_room_obj(active_obj)
            if current_room is not None:
                setattr(mytool, 'active_room', current_room.name)
            else:
                setattr(mytool, 'active_room', '')

        return {'FINISHED'}

class SetValuesOperator(bpy.types.Operator):
    bl_idname = "wm.set_block_values_operator"
    bl_label = "Save object params"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        block_type = ''

        active_obj = get_active_object()

        curtype = active_obj[consts.BLOCK_TYPE]

        objects = [cn for cn in bpy.context.selected_objects if cn[consts.BLOCK_TYPE] is not None and cn[consts.BLOCK_TYPE] == curtype]
        
        for i in range(len(objects)):

            b3d_obj = objects[i]

            if consts.BLOCK_TYPE in b3d_obj:
                block_type = b3d_obj[consts.BLOCK_TYPE]
            else:
                block_type = 0

            b3d_obj[consts.BLOCK_TYPE] = block_type

            zclass = BlockClassHandler.get_class_def_by_type(block_type)

            if zclass is not None:
                set_objs_by_type(b3d_obj, zclass)

        return {'FINISHED'}

@make_annotations
class SetPropValueOperator(bpy.types.Operator):
    bl_idname = "wm.set_prop_value_operator"
    bl_label = "Save param value"

    pname = StringProperty()

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        zclass = BlockClassHandler.get_class_def_by_type(block_type)

        if zclass is not None:
            set_obj_by_prop(b3d_obj, zclass, self.pname)

        return {'FINISHED'}


class ApplyTransformsOperator(bpy.types.Operator):
    bl_idname = "wm.apply_transforms_operator"
    bl_label = "Arrange/Remove objects"
    bl_description = "Creates copies of objects and arrange them at places(24) specified in connector(18)"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        apply_remove_transforms(self)

        return {'FINISHED'}

class ShowHide2DCollisionsOperator(bpy.types.Operator):
    bl_idname = "wm.show_hide_2d_collisions_operator"
    bl_label = "Show/Hide 2D collisions"
    bl_description = "If all 2D collisions(20) are hidden, shows them. otherwise - hide."

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        show_hide_obj_by_type(self, 20)

        return {'FINISHED'}

class ShowHideCollisionsOperator(bpy.types.Operator):
    bl_idname = "wm.show_hide_collisions_operator"
    bl_label = "Show/Hide collisions"
    bl_description = "If all 3d collisions(23) are hidden, shows them. otherwise - hide."

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        show_hide_obj_by_type(self, 23)

        return {'FINISHED'}

class ShowHideRoomBordersOperator(bpy.types.Operator):
    bl_idname = "wm.show_hide_room_borders_operator"
    bl_label = "Show/Hide portals"
    bl_description = "If all portals(30) are hidden, shows them. Otherwise - hide."

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        show_hide_obj_by_type(self, 30)

        return {'FINISHED'}

class ShowHideGeneratorsOperator(bpy.types.Operator):
    bl_idname = "wm.show_hide_generator_operator"
    bl_label = "Show/Hide generator blocks"
    bl_description = "If all generator blocks(40) are hidden, shows them. Otherwise - hide."

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        show_hide_obj_by_type(self, 40)

        return {'FINISHED'}

class ShowLODOperator(bpy.types.Operator):
    bl_idname = "wm.show_lod_operator"
    bl_label = "Show LOD"
    bl_description = "Shows LOD(10) of selected object. " + \
                    "If there is no active object, show LOD of all scene objects."

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        objs = context.selected_objects
        if not len(objs):
            objs = [cn for cn in bpy.data.objects if is_root_obj(cn)]

        for obj in objs:
            show_lod(obj)
        self.report({'INFO'}, "{} LOD objects(block 10) are shown".format(len(objs)))

        return {'FINISHED'}

class HideLODOperator(bpy.types.Operator):
    bl_idname = "wm.hide_lod_operator"
    bl_label = "Hide LOD"
    bl_description = "Hides LOD(10) of selected object. " + \
                    "If there is no active object, hide LOD of all scene objects."

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        objs = context.selected_objects
        if not len(objs):
            objs = [cn for cn in bpy.data.objects if is_root_obj(cn)]

        for obj in objs:
            hide_lod(obj)
        self.report({'INFO'}, "{} LOD objects(block 10) are hidden".format(len(objs)))

        return {'FINISHED'}

@make_annotations
class ShowConditionalsOperator(bpy.types.Operator):
    bl_idname = "wm.show_conditional_operator"
    bl_label = "Show events"
    bl_description = "Show event from selected event block(21). " + \
                    "If there is no active event block, show event of all scene event objects(21)"

    group  = bpy.props.IntProperty()

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        objs = context.selected_objects
        if not len(objs):
            objs = [cn for cn in bpy.data.objects if is_root_obj(cn)]

        for obj in objs:
            show_conditionals(obj, self.group)
        self.report({'INFO'}, "{} Conditional objects(block 21) are shown".format(len(objs)))


        return {'FINISHED'}

@make_annotations
class HideConditionalsOperator(bpy.types.Operator):
    bl_idname = "wm.hide_conditional_operator"
    bl_label = "Hide events"
    bl_description = "Hide event from selected event block(21). " + \
                    "If there is no active event block, hide event of all scene event objects(21)"

    group  = bpy.props.IntProperty()

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        objs = context.selected_objects
        if not len(objs):
            objs = [cn for cn in bpy.data.objects if is_root_obj(cn)]

        for obj in objs:
            hide_conditionals(obj, self.group)
        self.report({'INFO'}, "{} Conditional objects(block 21) are hidden".format(len(objs)))

        return {'FINISHED'}

@make_annotations
class ShowHideSphereOperator(bpy.types.Operator):
    bl_idname = "wm.show_hide_sphere_operator"
    bl_label = "Show/Hide sphere"
    bl_description = "Shows/Hides sphere"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        obj = context.object

        block_type = obj.get(consts.BLOCK_TYPE)
        if block_type in [10]:

            center_prop = Blk010.LOD_XYZ.get_prop()
            rad_prop = Blk010.LOD_R.get_prop()

            show_hide_sphere(obj, center_prop, rad_prop)

        self.report({'INFO'}, "Sphere shown or hidden")

        return {'FINISHED'}

@make_annotations
class SelectSimilarObjectsOperator(bpy.types.Operator):
    bl_idname = "wm.select_similar_objects_operator"
    bl_label = "Select similar objects"
    bl_description = "Select objects with same parameters"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        zclass = BlockClassHandler.get_class_def_by_type(block_type)

        if zclass is not None:
            select_similar_objects_by_type(b3d_obj, zclass)

            self.report({'INFO'}, "Similar object selected")

        return {'FINISHED'}

@make_annotations
class SelectSimilarFacesOperator(bpy.types.Operator):
    bl_idname = "wm.select_similar_faces_operator"
    bl_label = "Select similar faces"
    bl_description = "Select faces with same parameters"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = get_active_object()
        block_type = b3d_obj[consts.BLOCK_TYPE]

        zclass = BlockClassHandler.get_pfb_class_def_by_type(block_type)

        if zclass is not None:
            select_similar_faces_by_type(b3d_obj, zclass)

            self.report({'INFO'}, "Similar faces selected")

        return {'FINISHED'}

@make_annotations
class VisualiseRenderTreeOperator(bpy.types.Operator):
    bl_idname = "wm.visualise_render_tree_operator"
    bl_label = "Show/Hide render tree"
    bl_description = "Show/Hide render tree"

    node_name = bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = bpy.data.objects.get(self.node_name)

        collection_name = 'RenderTree_{}'.format(b3d_obj.name)
        temp_collection = get_or_create_collection(collection_name)

        if len(temp_collection.objects) > 0:
            remove_collection(temp_collection.name)
            return {'FINISHED'}

        #Create needed objects and materials

        def get_level(src_obj, dest_obj):
            obj = src_obj
            level = 1
            while obj != dest_obj:
                if obj.name[:5] == 'GROUP':
                    level += 1
                obj = obj.parent
            return level

        def get_group(src_obj):
            if src_obj.parent.name[:5] == 'GROUP':
                return src_obj.parent.name[6]
            return '0'

        # get list of tree branches
        branch_list = [{'obj':o, 'lvl':get_level(o, b3d_obj), 'grp':get_group(o)} for o in bpy.data.objects if o.get('block_type') == 9 and is_inside_object(o, b3d_obj)]

        max_lvl = sorted([o['lvl'] for o in branch_list])[-1]
        create_render_branch_materials(max_lvl)

        #Set Render center initial location in a room if possible
        location = (0.0,0.0,0.0)
        room = get_room_obj(b3d_obj)
        if room is not None:
            borders = [{'obj':o.name,'transf':o.name} for o in bpy.data.objects if o.get(consts.BLOCK_TYPE) == 30 and 
                (o.get(Blk030.RoomName1.get_prop()) == room.name or o.get(Blk030.RoomName2.get_prop()) == room.name)]

            bbox_params = get_mult_obj_bounding_sphere(borders)
            location = bbox_params[0]
        

        render_center_object = get_render_center_object(b3d_obj.name, location, temp_collection)

        level_mult = -5.0
        for i, branch_obj in enumerate(branch_list):
            material_a = bpy.data.materials.get('RenderBranchTransp')
            material_b = bpy.data.materials.get('RenderBranchMat_{}_{}'.format(branch_obj['lvl'], max_lvl))
            if branch_obj['grp'] == "0":
                material_text = bpy.data.materials.get('RenderBranchText0')
            else:
                material_text = bpy.data.materials.get('RenderBranchText1')

            shift_z = branch_obj['lvl'] * level_mult + (1.0 if branch_obj['grp'] == "0" else -1.0)

            show_hide_render_tree_branch(branch_obj['obj'], temp_collection, render_center_object, shift_z, material_text, material_a, material_b)

        self.report({'INFO'}, "Render Tree visualiser created!")

        return {'FINISHED'}

@make_annotations
class ApplyRenderTreeChangesOperator(bpy.types.Operator):
    bl_idname = "wm.apply_render_tree_changes_operator"
    bl_label = "Apply changes"
    bl_description = "Apply render tree changes"
    
    def execute(self, context):

        branches = [o for o in bpy.data.objects if o.name[:9] == 'RT_Branch']

        for branch_obj in branches:
            obj_name = branch_obj.name.split("||")[1]
            b3d_obj = bpy.data.objects[obj_name]
            ax = b3d_obj[Blk009.Unk_XYZ.get_prop()][0]
            ay = b3d_obj[Blk009.Unk_XYZ.get_prop()][1]
            length = math.sqrt(ax**2 + ay**2)
            axn = ax / length
            ayn = ay / length
            angle = math.atan2(ayn, axn) + math.pi/2 
            # + math.pi/4
            # Given
            Px = branch_obj.delta_location[0] + branch_obj.location[0]
            Py = branch_obj.delta_location[1] + branch_obj.location[1]

            theta = angle + branch_obj.rotation_euler[2] #only z axis rotation

            # Step 1: compute lambda
            lam = Px*math.cos(theta) + Py*math.sin(theta)

            # Step 2: compute tangent point
            Tx = Px - lam*math.cos(theta)
            Ty = Py - lam*math.sin(theta)

            # Step 3: compute radius
            R = math.sqrt(Tx**2 + Ty**2)

            new_vec = (Tx/R, Ty/R, 0.0)

            b3d_obj[Blk009.Unk_XYZ.get_prop()][0] = new_vec[0]
            b3d_obj[Blk009.Unk_XYZ.get_prop()][1] = new_vec[1]
            b3d_obj[Blk009.Unk_XYZ.get_prop()][2] = new_vec[2]
            b3d_obj[Blk009.Unk_R.get_prop()] = -R
            b3d_obj.update_tag(refresh={'OBJECT'})

            branch_obj.location[0] = 0.0
            branch_obj.location[1] = 0.0
            branch_obj.location[2] = 0.0
            branch_obj.rotation_euler[2] = 0.0

        return {'FINISHED'}


@make_annotations
class VisualiseLODTreeOperator(bpy.types.Operator):
    bl_idname = "wm.visualise_lod_tree_operator"
    bl_label = "Show/Hide LOD tree"
    bl_description = "Show/Hide LOD tree"

    node_name = bpy.props.StringProperty()

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        b3d_obj = bpy.data.objects.get(self.node_name)

        collection_name = 'LODTree_{}'.format(b3d_obj.name)
        temp_collection = get_or_create_collection(collection_name)

        if len(temp_collection.objects) > 0:
            remove_collection(temp_collection.name)
            return {'FINISHED'}
        
        #Create needed objects and materials
        def get_level(src_obj, dest_obj):
            obj = src_obj
            level = 1
            while obj != dest_obj:
                if obj.name[:5] == 'GROUP':
                    level += 1
                obj = obj.parent
            return level

        def get_group(src_obj):
            return src_obj.parent.name[6]

        # get list of tree branches
        branch_list = [{'obj':o, 'lvl':get_level(o, b3d_obj), 'grp':get_group(o)} for o in bpy.data.objects if o.get('block_type') == 10 and is_inside_object(o, b3d_obj)]

        max_lvl = sorted([o['lvl'] for o in branch_list])[-1]
        create_render_branch_materials(max_lvl)

        for i, branch_obj in enumerate(branch_list):
            material = bpy.data.materials.get('RenderBranchMat_{}_{}'.format(branch_obj['lvl'], max_lvl))

            show_hide_lod_tree_branch(branch_obj['obj'], temp_collection, material)

        self.report({'INFO'}, "LOD Tree visualiser created!")

        return {'FINISHED'}

@make_annotations
class ApplyLODTreeChangesOperator(bpy.types.Operator):
    bl_idname = "wm.apply_lod_tree_changes_operator"
    bl_label = "Apply changes"
    bl_description = "Apply LOD tree changes"
    
    def execute(self, context):

        branches = [o for o in bpy.data.objects if o.name[:10] == 'LOD_Branch']

        for branch_obj in branches:
            obj_name = branch_obj.name.split("||")[1]
            b3d_obj = bpy.data.objects[obj_name]

            R = (branch_obj.scale[0] + branch_obj.scale[1] + branch_obj.scale[2]) / 3 * b3d_obj[Blk010.LOD_R.get_prop()]

            b3d_obj[Blk010.LOD_XYZ.get_prop()][0] = branch_obj.delta_location[0] + branch_obj.location[0]
            b3d_obj[Blk010.LOD_XYZ.get_prop()][1] = branch_obj.delta_location[1] + branch_obj.location[1]
            b3d_obj[Blk010.LOD_XYZ.get_prop()][2] = branch_obj.delta_location[2] + branch_obj.location[2]
            b3d_obj[Blk010.LOD_R.get_prop()] = R
            b3d_obj.update_tag(refresh={'OBJECT'})

            branch_obj.location[0] = 0.0
            branch_obj.location[1] = 0.0
            branch_obj.location[2] = 0.0
            
            branch_obj.scale[0] = 1.0
            branch_obj.scale[1] = 1.0
            branch_obj.scale[2] = 1.0

        return {'FINISHED'}


# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

_classes = [
    SetParentOperator,
    SingleAddOperator,
    HierarchyAddOperator,
    CastAddOperator,
    # getters
    GetValuesOperator,
    GetPropValueOperator,
    GetFaceValuesOperator,
    GetVertexValuesOperator,
    # setters
    SetRoomAndModuleOperator,
    SetValuesOperator,
    SetPropValueOperator,
    SetFaceValuesOperator,
    SetVertexValuesOperator,
    # additional options
    ApplyTransformsOperator,
    ShowHide2DCollisionsOperator,
    ShowHideCollisionsOperator,
    ShowHideRoomBordersOperator,
    ShowHideGeneratorsOperator,
    ShowLODOperator,
    HideLODOperator,
    ShowConditionalsOperator,
    HideConditionalsOperator,
    ShowHideSphereOperator,
    SelectSimilarObjectsOperator,
    SelectSimilarFacesOperator,
    VisualiseRenderTreeOperator,
    ApplyRenderTreeChangesOperator,
    VisualiseLODTreeOperator,
    ApplyLODTreeChangesOperator,
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in _classes[::-1]:
        bpy.utils.unregister_class(cls)
