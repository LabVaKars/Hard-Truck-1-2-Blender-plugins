import math
import bpy

from ..consts import (
    BLOCK_TYPE
)

from ..common import (
    get_block_tool,
    get_panel_tool
)

from .blocktool_defs import (
    FieldType,
    BlockClassType
)

from .blocktool import (
    BlockClassHandler
)

from .common import (
    get_level_group
)
from ..compatibility import (
    layout_split
)

def draw_enum(box, pname):
    mytool = get_panel_tool()

    switch_attr = getattr(mytool, '{}_switch'.format(pname))
    if switch_attr is not None:
        box.prop(mytool, '{}_switch'.format(pname))
        
        if switch_attr:
            box.prop(mytool, '{}_enum'.format(pname))

        else:
            if hasattr(mytool, pname):
                box.prop(mytool, pname)


def draw_multi_select_list(self, layout, list_name, per_row):

    i = 0
    list_obj = getattr(self, list_name)
    rowcnt = math.floor(len(list_obj)/per_row)

    if len(list_obj) > 0:

        for j in range(rowcnt):
            row = layout.row()
            for block in list_obj[i:i+per_row]:
                row.prop(block, 'state', text=block['name'], toggle=True)
            i+=per_row
        row = layout.row()
        for block in list_obj[i:]:
            row.prop(block, 'state', text=block['name'], toggle=True)
    else:
        layout.label(text='No items')


def draw_common(l_self, obj):
    block_type = None
    level_group = None
    if BLOCK_TYPE in obj:
        block_type = obj[BLOCK_TYPE]
        
    object_name = '' if obj is None else obj.name

    level_group = get_level_group(obj)

    len_str = str(len(obj.children))

    box = l_self.layout

    split = layout_split(box, 0.25)
    split.column().label(text = "Name:")
    split.column().label(text = str(object_name))
    
    split = layout_split(box, 0.25)
    split.column().label(text = "Type:")
    split.column().label(text = str(block_type))

    split = layout_split(box, 0.25)
    split.column().label(text = "Children:")
    split.column().label(text = str(len_str))

    split = layout_split(box, 0.25)
    split.column().label(text = "Group:")
    split.column().label(text = str(level_group))

    box = l_self.layout.box()

    draw_enum(box, 'active_module')
    draw_enum(box, 'active_room')

    box.operator("wm.set_room_and_module_operator")

def draw_fields_by_type(layout, bnum, btype = BlockClassType.BLOCK, multiple_edit = True):

    boxes = {}

    bname, fields = BlockClassHandler.get_block_object(bnum, btype, multiple_edit)

    for field in fields.values():

        ftype = field.get_attr_type()
        subtype = field.get_subtype()
        cur_group_name = field.get_group()
        prop_text = field.get_name()
        no_single_edit = field.get_no_single_edit()
        pname = field.get_prop()
        blocktool = get_block_tool()
        cur_layout = layout

        if not multiple_edit and no_single_edit:
            continue # skip no single edit panels

        if cur_group_name is not None or len(cur_group_name) > 0:
            if boxes.get(cur_group_name) is None:
                boxes[cur_group_name] = layout.box()
            cur_layout = boxes[cur_group_name]


        if ftype == FieldType.SPHERE_EDIT:
            if not multiple_edit: # sphere edit available only in single object edit
                box = cur_layout.box()
                col = box.column()

                props = col.operator("wm.show_hide_sphere_operator")

        elif ftype == FieldType.STRING \
        or ftype == FieldType.COORD \
        or ftype == FieldType.INT \
        or ftype == FieldType.FLOAT \
        or ftype == FieldType.ENUM \
        or ftype == FieldType.ENUM_DYN \
        or ftype == FieldType.LIST:
            
            blk = getattr(blocktool, bname) if hasattr(blocktool, bname) else None
            if blk is not None:

                box = cur_layout.box()

                show_attr = getattr(blk, 'show_{}'.format(pname)) if hasattr(blk, 'show_{}'.format(pname)) else None

                if multiple_edit:
                    if hasattr(blk, 'show_{}'.format(pname)):
                        box.prop(blk, "show_{}".format(pname))

                col = box.column()
                if ftype in [
                    FieldType.STRING,
                    FieldType.COORD,
                    FieldType.INT,
                    FieldType.FLOAT
                ]:
                    if multiple_edit: # getting from panel_tool
                        col.prop(blk, pname)
                    else:
                        col.prop(bpy.context.object, '["{}"]'.format(pname), text=prop_text)

                elif ftype in [FieldType.ENUM_DYN, FieldType.ENUM]:
                    
                    switch_attr = getattr(blk, '{}_switch'.format(pname)) if hasattr(blk, '{}_switch'.format(pname)) else None
                    enum_attr = getattr(blk, '{}_enum'.format(pname)) if hasattr(blk, '{}_enum'.format(pname)) else None

                    if switch_attr is not None:
                        col.prop(blk, '{}_switch'.format(pname))
                        
                        if switch_attr:
                            # if enum_attr:
                            col.prop(blk, '{}_enum'.format(pname))

                        else:
                            if multiple_edit:
                                if hasattr(blk, pname):
                                    col.prop(blk, pname)
                            else:
                                col.prop(bpy.context.object, '["{}"]'.format(pname), text=prop_text)

                    else: # no manual entry
                        col.prop(blk, '{}_enum'.format(pname))

                elif ftype == FieldType.LIST:

                    box.prop(blk, '{}_enum'.format(pname))
                    box.prop(blk, '{}'.format(pname))

                    list_key = getattr(blk, '{}_enum'.format(pname))
                    if list_key != '?':
                        draw_fields_by_type(cur_layout, bnum, list_key)

                if multiple_edit:
                    if show_attr:
                        col.enabled = True
                    else:
                        col.enabled = False

        elif ftype == FieldType.V_FORMAT:
            if multiple_edit:
                blk = getattr(blocktool, bname) if hasattr(blocktool, bname) else None
                if blk is not None:
                    box = cur_layout.box()

                    if hasattr(blk, "show_{}".format(pname)):
                        box.prop(blk, "show_{}".format(pname))
                    
                    if hasattr(blk, "{}_show_int".format(pname)):
                        box.prop(blk, "{}_show_int".format(pname))
                        
                    col1 = box.column()
                    if getattr(blk, "{}_show_int".format(pname)) == True:
                        
                        if hasattr(blk, "{}_format_raw".format(pname)):
                            col1.prop(blk, "{}_format_raw".format(pname))
                    else:

                        if hasattr(blk, "{}_triang_offset".format(pname)):
                            col1.prop(blk, "{}_triang_offset".format(pname))

                        if hasattr(blk, "{}_use_uvs".format(pname)):
                            col1.prop(blk, "{}_use_uvs".format(pname))

                        if hasattr(blk, "{}_use_normals".format(pname)):
                            col1.prop(blk, "{}_use_normals".format(pname))

                        if hasattr(blk, "{}_normal_flag".format(pname)):
                            col1.prop(blk, "{}_normal_flag".format(pname))

                    if hasattr(blk, "show_{}".format(pname)):
                        col1.enabled = getattr(blk, "show_{}".format(pname))

        elif ftype == FieldType.FLAGS:
            blk = getattr(blocktool, bname) if hasattr(blocktool, bname) else None
            if blk is not None:
                box = cur_layout.box()
                if multiple_edit:

                    if hasattr(blk, "show_{}".format(pname)):
                        box.prop(blk, "show_{}".format(pname))
                    
                    if hasattr(blk, "{}_show_int".format(pname)):
                        box.prop(blk, "{}_show_int".format(pname))

                    col1 = box.column()
                    if getattr(blk, "{}_show_int".format(pname)) == True:
                        
                        if hasattr(blk, "{}".format(pname)):
                            col1.prop(blk, "{}".format(pname))

                    else:

                        flag_descriptions = field.get_flag_description()
                        if flag_descriptions is not None:

                            for desc in flag_descriptions:
                                if hasattr(blk, "{}_{}".format(pname, desc["key"])):
                                    col1.prop(blk, "{}_{}".format(pname, desc["key"]))

                    if hasattr(blk, "show_{}".format(pname)):
                        col1.enabled = getattr(blk, "show_{}".format(pname))

                else:
                    col = box.column()
                    col.prop(bpy.context.object, '["{}"]'.format(pname), text=prop_text)
