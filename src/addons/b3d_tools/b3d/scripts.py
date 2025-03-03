import bpy
import re

from .class_descr import (
    Blk018,
    Blk021
)
from ..common import (
    scripts_logger
)
from .common import (
    get_polygons_by_selected_vertices,
    get_selected_vertices,
    is_root_obj,
    is_mesh_block,
    get_root_obj,
    get_all_children,
    get_level_group
)
from .class_descr import (
    FieldType
)

from .classes import (
    BlockClassHandler
)

from ..consts import (
    BLOCK_TYPE,
    EMPTY_NAME,
    TRANSF_COLLECTION,
    TEMP_COLLECTION
)

from ..compatibility import (
    get_context_collection_objects,
    get_or_create_collection,
    is_before_2_80,
    is_before_2_93,
    set_empty_type,
    set_empty_size,
    get_object_hidden,
    set_object_hidden
)

log = scripts_logger

reb3d_space = re.compile(r'.*b3dSpaceCopy.*')
reb3d_mesh = re.compile(r'.*b3dcopy.*')

class Graph:

    def __init__(self, graph):
        self.graph = graph

    def dfs_util(self, val, visited):

        visited[val]["in"] += 1
        for v in self.graph[val]:
            if self.graph.get(v) is not None:
                visited[val]["out"] += 1
                self.dfs_util(v, visited)

    def dfs(self, start=None):
        visited = {}
        for val in self.graph.keys():
            visited[val] = {
                "in": 0,
                "out": 0
            }

        search_in = []
        if start is not None:
            search_in.append(start.name)
        else:
            search_in = self.graph.keys()

        for val in search_in:
            for v in self.graph[val]:
                if self.graph.get(v) is not None:
                    visited[val]["out"] += 1
                    self.dfs_util(v, visited)

        return visited


def apply_transforms():
    roots = [cn for cn in bpy.data.objects if is_root_obj(cn)]
    for root in roots:
        hroots = get_hierarchy_roots(root)
        for hroot in hroots:
            obj = bpy.data.objects.get(hroot)
            if obj is not None:
                apply_transform(obj)

def apply_transform(root):

    transf_collection = get_or_create_collection(TRANSF_COLLECTION)
    if not is_before_2_80():
        if transf_collection.name not in bpy.context.scene.collection.children:
            bpy.context.scene.collection.children.link(transf_collection)

    if bpy.data.objects.get('b3dCenterSpace') is None:
        b3d_obj = bpy.data.objects.new('b3dCenterSpace', None)
        b3d_obj[BLOCK_TYPE] = 24
        b3d_obj.rotation_euler[0] = 0.0
        b3d_obj.rotation_euler[1] = 0.0
        b3d_obj.rotation_euler[2] = 0.0
        b3d_obj.location = (0.0, 0.0, 0.0)
        transf_collection.objects.link(b3d_obj)

    if bpy.data.objects.get('b3dCenterSpace' + '_b3dSpaceCopy') is None:
        b3d_obj = bpy.data.objects.new('b3dCenterSpace' + '_b3dSpaceCopy', None)
        b3d_obj[BLOCK_TYPE] = 24
        b3d_obj.rotation_euler[0] = 0.0
        b3d_obj.rotation_euler[1] = 0.0
        b3d_obj.rotation_euler[2] = 0.0
        b3d_obj.location = (0.0, 0.0, 0.0)
        transf_collection.objects.link(b3d_obj)

    stack = [[root, 'b3dCenterSpace', 'b3dCenterSpace' + '_b3dSpaceCopy']]

    while stack:
        block, prev_space, prev_space_copy = stack.pop()

        prev_space_obj = bpy.data.objects.get(prev_space)
        prev_space_copy_obj = bpy.data.objects.get(prev_space_copy)

        # log.debug("{} {}".format(block[BLOCK_TYPE], block.name))
        # log.debug(prev_space)
        # log.debug(prev_space_copy)

        if block[BLOCK_TYPE] == 18:
            obj_name = block[Blk018.Add_Name.get_prop()]
            space_name = block[Blk018.Space_Name.get_prop()]

            dest_obj = bpy.data.objects.get(obj_name)

            if not get_object_hidden(block):

                if space_name == EMPTY_NAME:
                    space_name = prev_space

                space_obj = bpy.data.objects.get(space_name)

                if(space_obj == None):
                    log.warn("Transformation object not found in " + block.name)
                    return

                if(dest_obj == None):
                    log.warn("Destination object not found in " + block.name)
                    return

                space_copy = None
                if bpy.data.objects.get(space_obj.name + "_b3dSpaceCopy"):
                    space_copy = bpy.data.objects[space_obj.name + "_b3dSpaceCopy"]
                else:
                    space_copy = space_obj.copy()
                    space_copy.parent = prev_space_copy_obj
                    space_copy.rotation_euler[0] = space_obj.rotation_euler[0]
                    space_copy.rotation_euler[1] = space_obj.rotation_euler[1]
                    space_copy.rotation_euler[2] = space_obj.rotation_euler[2]
                    space_copy.location = space_obj.location
                    space_copy.name = space_obj.name + "_b3dSpaceCopy"
                    transf_collection.objects.link(space_copy)
                stack.append([dest_obj, space_obj.name, space_copy.name])
            # else:
            #     stack.append([dest_obj, prev_space, prev_space_copy])

            continue

        if is_mesh_block(block) and not get_object_hidden(block):
            # block.hide_set(True)
            # log.debug(block.name)
            # log.debug(prev_space)
            newmesh = block.copy()
            # newmesh.data = mesh.data.copy() # for NOT linked copy
            newmesh.parent = prev_space_copy_obj
            newmesh.name = "{}_b3dcopy".format(block.name)
            # log.info("Linking {}".format(newmesh.name))
            transf_collection.objects.link(newmesh)
            # newmesh.hide_set(False)

        for direct_child in block.children:
            stack.append([direct_child, prev_space, prev_space_copy])


def apply_remove_transforms(self):
    to_remove = False
    for obj in (bpy.data.objects):
        if reb3d_space.search(obj.name):
            to_remove = True
            break
    if to_remove:
        remove_transforms()
        self.report({'INFO'}, "Transforms removed")
    else:
        apply_transforms()
        self.report({'INFO'}, "Transforms applied")

def remove_transforms():
    spaces = [cn for cn in bpy.data.objects if reb3d_space.search(cn.name)]
    meshes = [cn for cn in bpy.data.objects if reb3d_mesh.search(cn.name)]

    reb3d_pos = re.compile(r'b3dcopy')

    bpy.ops.object.select_all(action = 'DESELECT')

    for mesh in meshes:
        # res = reb3d_pos.search(mesh.name)
        # postfixStart = res.start()
        # original = bpy.data.objects[mesh.name[:postfixStart-1]]
        # original.hide_set(False)
        mesh.select_set(True)
    bpy.ops.object.delete()

    for space in spaces:
        space.select_set(True)
    bpy.ops.object.delete()


def show_hide_obj_by_type(self, block_type):
    objs = [cn for cn in bpy.data.objects if cn.get("block_type") is not None and cn["block_type"]==block_type]
    hidden_obj = [cn for cn in bpy.data.objects if cn.get("block_type") is not None and cn["block_type"]==block_type and get_object_hidden(cn)]
    if len(objs) == len(hidden_obj):
        for obj in objs:
            set_object_hidden(obj, False)
        self.report({'INFO'}, "{} (block {}) objects are shown".format(len(objs), block_type))
    else:
        for obj in objs:
            set_object_hidden(obj, True)
        self.report({'INFO'}, "{} (block {}) objects are hidden".format(len(objs), block_type))

def show_hide_obj_tree_by_type(block_type):
    objs = [cn for cn in bpy.data.objects if cn.get("block_type") is not None and cn["block_type"]==block_type]
    hidden_obj = [cn for cn in bpy.data.objects if cn.get("block_type") is not None and cn["block_type"]==block_type and get_object_hidden(cn)]
    if len(objs) == len(hidden_obj):
        for obj in objs:
            children = get_all_children(obj)
            for child in children:
                set_object_hidden(child, False)
            set_object_hidden(obj, False)
    else:
        for obj in objs:
            children = get_all_children(obj)
            for child in children:
                set_object_hidden(child, True)
            set_object_hidden(obj, True)

def get_hierarchy_roots(root):
    global_root = root
    while global_root.parent is not None:
        global_root = global_root.parent

    blocks18 = [cn for cn in bpy.data.objects if cn.get(BLOCK_TYPE) is not None and cn.get(BLOCK_TYPE) == 18 and get_root_obj(cn) == global_root]
    ref_set = set()
    for cn in blocks18:
        #out refs
        if bpy.data.objects.get(cn.get(Blk018.Add_Name.get_prop())) is not None:
            ref_set.add(cn.get(Blk018.Add_Name.get_prop()))

        #in refs
        temp = cn
        while temp.parent != global_root:
            temp = temp.parent
        ref_set.add(temp.name)

    referenceables = list(ref_set)
    referenceables.sort()

    other = [cn.name for cn in global_root.children if cn[BLOCK_TYPE] is not None \
        and (cn.get(BLOCK_TYPE) in [4, 5, 19]) \
        and cn.name not in referenceables ]

    no_dub_graph = {}
    graph = {}
    for r in referenceables:
        no_dub_graph[r] = set()

    for r in referenceables:
        references = [cn for cn in get_all_children(bpy.data.objects.get(r)) if cn[BLOCK_TYPE] is not None and cn[BLOCK_TYPE] == 18]
        for ref_obj in references:
            no_dub_graph[r].add(ref_obj[Blk018.Add_Name.get_prop()])

    for r in referenceables:
        graph[r] = list(no_dub_graph[r])

    zgraph = Graph(graph)

    closest_root = root
    if closest_root != global_root:
        if closest_root.name not in graph:
            while (closest_root.parent[BLOCK_TYPE] is not None and closest_root.parent[BLOCK_TYPE] != 5 \
            and closest_root.parent.name not in graph) or closest_root.parent is None: # closest or global
                closest_root = closest_root.parent
    else:
        closest_root = None

    visited = zgraph.dfs(closest_root)

    roots = [cn for cn in visited.keys() if (visited[cn]["in"] == 0) and (visited[cn]["out"] > 0)]

    res = other
    res.extend(roots)

    return res


def process_lod(root, state, explevel = 0, curlevel = -1):

    stack = [[root, curlevel, False]]

    while stack:
        bl_children = []
        block, clevel, is_active = stack.pop()

        if block[BLOCK_TYPE] == 18:
            ref_obj = bpy.data.objects.get(block[Blk018.Add_Name.get_prop()])
            if ref_obj is not None:
                stack.append([ref_obj, clevel, is_active])
                if is_active:
                    set_object_hidden(block, state)

        if block[BLOCK_TYPE] == 10:
            clevel += 1

        if block[BLOCK_TYPE] in [9, 10, 21]:
            for ch in block.children:
                bl_children.extend(ch.children)
        else:
            bl_children = block.children

        if is_active and is_mesh_block(block):
            set_object_hidden(block, state)

        for direct_child in bl_children:

            # if direct_child[BLOCK_TYPE] == 444:
            #     log.debug("Skipping {}".format(direct_child.name))
            #     for ch in direct_child.children:
            #         stack.append([ch, clevel, is_active])
            #     continue

            if clevel == explevel:
                # if direct_child[LEVEL_GROUP] == 1:
                if get_level_group(direct_child) == 1:
                    stack.append([direct_child, clevel, True])
                else:
                    stack.append([direct_child, -1, is_active])
            elif clevel > explevel:
                stack.append([direct_child, clevel, True])
            else:
                stack.append([direct_child, clevel, is_active])


def show_lod(root):
    if root.parent is None:
        hroots = get_hierarchy_roots(root)
        for hroot in hroots:
            obj = bpy.data.objects.get(hroot)
            if obj is not None:
                process_lod(obj, False, 0, -1)
    else:
        process_lod(root, False, 0, -1)

def hide_lod(root):
    if root.parent is None:
        hroots = get_hierarchy_roots(root)
        for hroot in hroots:
            obj = bpy.data.objects.get(hroot)
            if obj is not None:
                process_lod(obj, True, 0, -1)
    else:
        process_lod(root, True, 0, -1)


def process_cond(root, group, state):

    curlevel = 0
    globlevel = 0

    stack = [[root, curlevel, globlevel, 0, False]]

    while stack:
        bl_children = []
        block, clevel, glevel, group_max, is_active = stack.pop()

        l_group = group

        if block[BLOCK_TYPE] == 18:
            ref_obj = bpy.data.objects.get(block[Blk018.Add_Name.get_prop()])
            if ref_obj is not None:
                stack.append([ref_obj, clevel+1, glevel, group_max, is_active])
                if is_active:
                    set_object_hidden(block, state)

        if block[BLOCK_TYPE] == 21:
            glevel += 1
            clevel = 1
            group_max = block[Blk021.GroupCnt.get_prop()]
            if l_group > group_max-1:
                l_group = group_max-1


        if block[BLOCK_TYPE] in [9, 10, 21]:
            for ch in block.children:
                bl_children.extend(ch.children)
        else:
            bl_children = block.children

        if is_active and is_mesh_block(block):
            set_object_hidden(block, state)

        for direct_child in bl_children:
            log.debug("Processing {}".format(direct_child.name))
            next_state = False
            if glevel == 1:
                next_state = True
            elif glevel > 1:
                next_state = is_active and True
            if clevel == 1:
                # if direct_child[LEVEL_GROUP] == l_group or l_group == -1:
                if get_level_group(direct_child) == l_group or l_group == -1:
                    stack.append([direct_child, clevel+1, glevel, group_max, next_state])
                else:
                    stack.append([direct_child, clevel+1, glevel, group_max, False])
            elif clevel > 1:
                stack.append([direct_child, clevel+1, glevel, group_max, is_active])
            else:
                stack.append([direct_child, clevel+1, glevel, group_max, False])

def show_conditionals(root, group):

    if root.parent is None:
        hroots = get_hierarchy_roots(root)
        for hroot in hroots:
            obj = bpy.data.objects.get(hroot)
            if obj is not None:
                process_cond(obj, group, False)
    else:
        process_cond(root, group, False)


def hide_conditionals(root, group):

    if root.parent is None:
        hroots = get_hierarchy_roots(root)
        for hroot in hroots:
            obj = bpy.data.objects.get(hroot)
            if obj is not None:
                process_cond(obj, group, True)
    else:
        process_cond(root, group, True)

def create_center_driver(src_obj, bname, pname):
    d = None
    for i in range(3):

        d = src_obj.driver_add('location', i).driver

        v = d.variables.new()
        v.name = 'location{}'.format(i)
        # v.targets[0].id_type = 'SCENE'
        # v.targets[0].id = bpy.context.scene
        # v.targets[0].data_path = 'my_tool.{}.{}[{}]'.format(bname, pname, i)
        v.targets[0].id = bpy.context.object
        v.targets[0].data_path = '["{}"][{}]'.format(pname, i)

        d.expression = v.name

def create_rad_driver(src_obj, bname, pname):
    d = src_obj.driver_add('empty_display_size').driver

    v1 = d.variables.new()
    v1.name = 'rad'
    # v1.targets[0].id_type = 'SCENE'
    # v1.targets[0].id = bpy.context.scene
    # v1.targets[0].data_path = 'my_tool.{}.{}'.format(bname, pname)
    v1.targets[0].id = bpy.context.object
    v1.targets[0].data_path = '["{}"]'.format(pname)

    d.expression = v1.name

def show_hide_sphere(context, root, pname):

    transf_collection = get_or_create_collection(TEMP_COLLECTION)
    if not is_before_2_80():
        if transf_collection.name not in bpy.context.scene.collection.children:
            bpy.context.scene.collection.children.link(transf_collection)

    obj_name = "{}||{}||temp".format(root.name, pname)

    b3d_obj = bpy.data.objects.get(obj_name)

    if b3d_obj is not None:
        bpy.data.objects.remove(b3d_obj, do_unlink=True)
    else:

        bnum = root.get(BLOCK_TYPE)

        center_name = "{}_center".format(pname)
        rad_name = "{}_rad".format(pname)

        center = root.get(center_name)
        rad = root.get(rad_name)

        # creating object

        b3d_obj = bpy.data.objects.new(obj_name, None)
        set_empty_type(b3d_obj, 'SPHERE')
        set_empty_size(b3d_obj, rad)
        b3d_obj.location = center
        b3d_obj.parent = root.parent

        transf_collection.objects.link(b3d_obj)

        # center driver
        bname = BlockClassHandler.get_mytool_block_name('Blk', bnum)

        create_center_driver(b3d_obj, bname, center_name)

        # rad driver
        create_rad_driver(b3d_obj, bname, rad_name)



def get_obj_by_prop(context, b3d_obj, zclass, pname):

    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]
    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass, True)

    blocktool = context.scene.block_tool
    for attr_class_name in attrs_cls:
        attr_class = zclass.__dict__[attr_class_name]

        if attr_class.get_prop() == pname:

            if attr_class.get_block_type() == FieldType.LIST:

                col = getattr(getattr(blocktool, bname), attr_class.get_prop())

                col.clear()
                for i, obj in enumerate(b3d_obj[attr_class.get_prop()]):
                    item = col.add()
                    item.index = i
                    item.value = obj

def get_all_objs_by_type(context, b3d_obj, zclass):
    get_objs_by_type(context, b3d_obj, zclass)

def get_objs_by_type(context, b3d_obj, zclass):
    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]
    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass)

    blocktool = context.scene.block_tool
    for attr_class_name in attrs_cls:
        attr_class = zclass.__dict__[attr_class_name]

        if attr_class.get_block_type() != FieldType.SPHERE_EDIT:
            blk = getattr(blocktool, bname) if hasattr(blocktool, bname) else None
            if getattr(blk, "show_"+attr_class.get_prop()):

                if attr_class.get_block_type() == FieldType.FLOAT \
                or attr_class.get_block_type() == FieldType.RAD:
                    setattr(
                        blk,
                        attr_class.get_prop(),
                        float(b3d_obj[attr_class.get_prop()])
                    )

                elif attr_class.get_block_type() == FieldType.INT:
                    setattr(
                        blk,
                        attr_class.get_prop(),
                        int(b3d_obj[attr_class.get_prop()])
                    )

                elif attr_class.get_block_type() == FieldType.STRING:
                    blk[attr_class.get_prop()] = str(b3d_obj[attr_class.get_prop()])

                elif attr_class.get_block_type() == FieldType.ENUM \
                or attr_class.get_block_type() == FieldType.ENUM_DYN:
                    setattr(
                        blk,
                        attr_class.get_prop(),
                        str(b3d_obj[attr_class.get_prop()])
                    )

                elif attr_class.get_block_type() == FieldType.LIST:

                    col = getattr(blk, attr_class.get_prop())

                    col.clear()
                    for i, obj in enumerate(b3d_obj[attr_class.get_prop()]):
                        item = col.add()
                        item.index = i
                        item.value = obj

                else:
                    setattr(
                        blk,
                        attr_class.get_prop(),
                        b3d_obj[attr_class.get_prop()]
                    )

def set_obj_by_prop(context, b3d_obj, zclass, pname):

    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]
    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass, True)

    blocktool = context.scene.block_tool
    for attr_class_name in attrs_cls:
        attr_class = zclass.__dict__[attr_class_name]

        if attr_class.get_Prop() == pname:

            if attr_class.get_block_type() == FieldType.LIST:
                collect = getattr(getattr(blocktool, bname), attr_class.get_prop())

                arr = []
                for item in list(collect):
                    arr.append(item.value)

                b3d_obj[attr_class.get_prop()] = arr

def set_all_objs_by_type(context, b3d_obj, zclass):
    set_objs_by_type(context, b3d_obj, zclass)

# def setObjsDefaultByType(context, b3d_obj, zclass):

def set_objs_by_type(context, b3d_obj, zclass):
    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]

    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass)
    blocktool = context.scene.block_tool
    for attr_class_name in attrs_cls:
        attr_class = zclass.__dict__[attr_class_name]
        if attr_class.get_block_type() != FieldType.SPHERE_EDIT:
            blk = getattr(blocktool, bname) if getattr(blocktool, bname) else None
            if blk is not None:
            # if getattr(getattr(mytool, bname), "show_"+attr_class.get_prop()) is not None \
            #     and getattr(getattr(mytool, bname), "show_"+attr_class.get_prop()):

                if attr_class.get_block_type() == FieldType.FLOAT or attr_class.get_block_type() == FieldType.RAD:
                    b3d_obj[attr_class.get_prop()] = float(getattr(blk, attr_class.get_prop()))

                elif attr_class.get_block_type() == FieldType.INT:
                    b3d_obj[attr_class.get_prop()] = int(getattr(blk, attr_class.get_prop()))

                # elif attr_class.get_block_type() == FieldType.MATERIAL_IND:
                #     b3d_obj[attr_class.get_prop()] = int(getattr(getattr(mytool, bname), attr_class.get_prop()))

                elif attr_class.get_block_type() == FieldType.STRING:
                    b3d_obj[attr_class.get_prop()] = str(getattr(blk, attr_class.get_prop()))

                # elif attr_class.get_block_type() == FieldType.SPACE_NAME \
                # or attr_class.get_block_type() == FieldType.REFERENCEABLE:
                #     b3d_obj[attr_class.get_prop()] = str(getattr(getattr(mytool, bname), attr_class.get_prop()))

                elif attr_class.get_block_type() == FieldType.ENUM:

                    if attr_class.get_subtype() == FieldType.INT:
                        b3d_obj[attr_class.get_prop()] = int(getattr(blk, attr_class.get_prop()))

                    elif attr_class.get_subtype() == FieldType.STRING:
                        b3d_obj[attr_class.get_prop()] = str(getattr(blk, attr_class.get_prop()))

                    elif attr_class.get_subtype() == FieldType.FLOAT:
                        b3d_obj[attr_class.get_prop()] = float(getattr(blk, attr_class.get_prop()))

                elif attr_class.get_block_type() == FieldType.ENUM_DYN:
                    b3d_obj[attr_class.get_prop()] = str(getattr(blk, attr_class.get_prop()))

                elif attr_class.get_block_type() == FieldType.COORD:
                    xyz = getattr(blk, attr_class.get_prop())
                    b3d_obj[attr_class.get_prop()] = (xyz[0],xyz[1],xyz[2])

                elif attr_class.get_block_type() == FieldType.LIST:
                    collect = getattr(blk, attr_class.get_prop())

                    arr = []
                    for item in list(collect):
                        arr.append(item.value)

                    b3d_obj[attr_class.get_prop()] = arr

                else:
                    b3d_obj[attr_class.get_prop()] = getattr(blk, attr_class.get_prop())

def get_from_attributes(context, attr_class, attrs, bname, index):

    blocktool = context.scene.block_tool

    blk = getattr(blocktool, bname) if hasattr(blocktool, bname) else None

    if hasattr(blk, "show_"+attr_class.get_prop()):

        if attr_class.get_block_type() == FieldType.FLOAT:
            blk[attr_class.get_prop()] = float(getattr(attrs[index], "value"))

        elif attr_class.get_block_type() == FieldType.COORD:
            blk[attr_class.get_prop()] = getattr(attrs[index], "vector")

        elif attr_class.get_block_type() == FieldType.INT:
            blk[attr_class.get_prop()] = int(getattr(attrs[index], "value"))

        elif attr_class.get_block_type() == FieldType.V_FORMAT:
            v_format = getattr(attrs[index], "value") ^ 1
            triang_offset = v_format & 0b10000000
            use_uv = v_format & 0b10
            use_normals = v_format & 0b10000 and v_format & 0b100000
            normal_flag = v_format & 1

            blk['{}_triang_offset'.format(attr_class.get_prop())] = triang_offset
            blk['{}_use_uvs'.format(attr_class.get_prop())] = use_uv
            blk['{}_use_normals'.format(attr_class.get_prop())] = use_normals
            blk['{}_normal_flag'.format(attr_class.get_prop())] = normal_flag

def set_from_attributes(context, attr_class, attrs, bname, index):

    blocktool = context.scene.block_tool

    blk = getattr(blocktool, bname) if hasattr(blocktool, bname) else None

    if getattr(blk, "show_"+attr_class.get_prop()):

        if attr_class.get_block_type() == FieldType.FLOAT:
            attrs[index].value = blk[attr_class.get_prop()]

        elif attr_class.get_block_type() == FieldType.INT:
            attrs[index].value = blk[attr_class.get_prop()]

        elif attr_class.get_block_type() == FieldType.COORD:
            attrs[index].vector = blk[attr_class.get_prop()]

        elif attr_class.get_block_type() == FieldType.V_FORMAT:
            value = 0
            triang_offset = blk['{}_triang_offset'.format(attr_class.get_prop())]
            use_uv = blk['{}_use_uvs'.format(attr_class.get_prop())]
            use_normals = blk['{}_use_normals'.format(attr_class.get_prop())]
            normal_flag = blk['{}_normal_flag'.format(attr_class.get_prop())]

            if triang_offset:
                value = value ^ 0b10000000
            if use_uv:
                value = value ^ 0b10
            if use_normals:
                value = value ^ 0b110000
            if normal_flag:
                value = value ^ 0b1

            value = value ^ 1

            attrs[index].value = value

def get_per_face_by_type(context, b3d_obj, zclass):
    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]

    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass)

    mesh = b3d_obj.data
    bpy.ops.object.mode_set(mode = 'OBJECT')
    polygons = get_polygons_by_selected_vertices(b3d_obj)
    indexes = [cn.index for cn in polygons]

    if len(indexes) > 0:
        index = indexes[0]
        for attr_class_name in attrs_cls:
            attr_class = zclass.__dict__[attr_class_name]
            attrs = mesh.attributes[attr_class.get_prop()].data
            get_from_attributes(context, attr_class, attrs, bname, index)

    bpy.ops.object.mode_set(mode = 'EDIT')

def get_per_vertex_by_type(context, b3d_obj, zclass):
    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]

    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass)

    mesh = b3d_obj.data
    bpy.ops.object.mode_set(mode = 'OBJECT')
    vertices = get_selected_vertices(b3d_obj)
    indexes = [cn.index for cn in vertices]

    if len(indexes) > 0:
        index = indexes[0]
        for attr_class_name in attrs_cls:
            attr_class = zclass.__dict__[attr_class_name]
            attrs = mesh.attributes[attr_class.get_prop()].data
            get_from_attributes(context, attr_class, attrs, bname, index)

    bpy.ops.object.mode_set(mode = 'EDIT')

def set_per_vertex_by_type(context, b3d_obj, zclass):
    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]

    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass)

    mesh = b3d_obj.data
    bpy.ops.object.mode_set(mode = 'OBJECT')
    vertices = get_selected_vertices(b3d_obj)
    indexes = [cn.index for cn in vertices]

    for index in indexes:
        for attr_class_name in attrs_cls:
            attr_class = zclass.__dict__[attr_class_name]
            attrs = mesh.attributes[attr_class.get_prop()].data
            set_from_attributes(context, attr_class, attrs, bname, index)

    bpy.ops.object.mode_set(mode = 'EDIT')

def set_per_face_by_type(context, b3d_obj, zclass):
    attrs_cls = [obj for obj in zclass.__dict__.keys() if not obj.startswith('__')]

    bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(zclass)

    mesh = b3d_obj.data
    bpy.ops.object.mode_set(mode = 'OBJECT')
    polygons = get_polygons_by_selected_vertices(b3d_obj)
    indexes = [cn.index for cn in polygons]

    for index in indexes:
        for attr_class_name in attrs_cls:
            attr_class = zclass.__dict__[attr_class_name]
            attrs = mesh.attributes[attr_class.get_prop()].data
            set_from_attributes(context, attr_class, attrs, bname, index)

    bpy.ops.object.mode_set(mode = 'EDIT')

def create_custom_attribute(mesh, values, zclass, zobj):
    if is_before_2_93():
        return
    ctype = BlockClassHandler.get_block_type_from_bclass(zclass)
    domain = ''
    if ctype == 'Pvb':
        domain = 'POINT'
    elif ctype == 'Pfb':
        domain = 'FACE'

    if zobj.get_block_type() == FieldType.FLOAT:
        ztype = 'FLOAT'
        mesh.attributes.new(name=zobj.get_prop(), type=ztype, domain=domain)
        attr = mesh.attributes[zobj.get_prop()].data
        for i in range(len(attr)):
            setattr(attr[i], "value", values[i])

    elif zobj.get_block_type() == FieldType.COORD:
        ztype = 'FLOAT_VECTOR'
        mesh.attributes.new(name=zobj.get_prop(), type=ztype, domain=domain)
        attr = mesh.attributes[zobj.get_prop()].data
        for i in range(len(attr)):
            setattr(attr[i], "vector", values[i])

    elif zobj.get_block_type() == FieldType.INT:
        ztype = 'INT'
        mesh.attributes.new(name=zobj.get_prop(), type=ztype, domain=domain)
        attr = mesh.attributes[zobj.get_prop()].data
        for i in range(len(attr)):
            setattr(attr[i], "value", values[i])

    elif zobj.get_block_type() == FieldType.V_FORMAT:
        ztype = 'INT'
        mesh.attributes.new(name=zobj.get_prop(), type=ztype, domain=domain)
        attr = mesh.attributes[zobj.get_prop()].data
        for i in range(len(attr)):
            setattr(attr[i], "value", values[i])

