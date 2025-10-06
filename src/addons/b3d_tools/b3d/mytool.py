import bpy

from bpy.props import (StringProperty,
                        BoolProperty,
                        IntProperty,
                        FloatProperty,
                        EnumProperty,
                        PointerProperty,
                        FloatVectorProperty,
                        CollectionProperty
                    )

from .. import consts

from .class_descr import (
    ResBlock
)

from .classes import (
    FieldType
)

from ..compatibility import (
    make_annotations
)

from .callbacks import (
    res_modules_callback,
    modules_callback,
    rooms_callback_mytool,
    render_tree_callback,
    LOD_callback,
    event_callback
)

from ..compatibility import (
    set_active_object
)

from ..common import mytool_logger
log = mytool_logger

def set_cust_mytool_value(subtype, pname):
    def callback_func(self, context):

        mytool = context.scene.my_tool
        result = getattr(mytool, '{}_enum'.format(pname))
        if subtype == FieldType.INT:
            result = int(result)
        elif subtype == FieldType.FLOAT:
            result = float(result)
        elif subtype == FieldType.STRING:
            result = str(result)

        setattr(
            mytool,
            '{}'.format(pname),
            result
        )

    return callback_func


def select_object_on_update(pname):
    def callback_func(self, context):

        obj_name = getattr(self, pname)
        obj = bpy.data.objects.get(obj_name)
        if obj is not None:
            set_active_object(obj)

    return callback_func

@make_annotations
class PanelSettings(bpy.types.PropertyGroup):

    res_modules = CollectionProperty(type=ResBlock)

    is_importing = bpy.props.BoolProperty(
        name ='isRESImporting',
        default = False
    )

    selected_res_module = EnumProperty(
        name="RES module",
        description="Selected RES module",
        items=res_modules_callback
    )

    condition_group = bpy.props.IntProperty(
        name='Event number',
        description='Event number(object group), that should be shown/hidden. If -1, then all events are chosen. If event number is too big, closest suitable number is chosen.',
        default=-1,
        min=-1
    )

    block_name_string = bpy.props.StringProperty(
        name="Block name",
        default="",
        maxlen=30,
    )

    add_block_type_enum = bpy.props.EnumProperty(
        name="Block type",
        items= consts.blockTypeList
    )

    radius = bpy.props.FloatProperty(
        name = "Block rad",
        description = "Block rendering distance",
        default = 1.0,
        )

    cast_type_enum = bpy.props.EnumProperty(
        name="Cast type",
        items=[
            ('mesh', "Mesh", "Cast selected meshes to vertices(6,7,36,37) polygons blocks(8,35)"),
            ('colis3D', "3D collision", "Creates copy of selected mesh for 3D collision(23)"),
            ('colis2D', "2D collision", "Cast selected curve to 2D collision(20)"),
            ('way50', "Transport path segment", "Cast selected curve to transport path segment(50)"),
            ('way51', "Transport path point", "Cast selected curve to transport path point(51)"),
            ('way52', "Transport path directed point", "Cast selected curve to transport path directed point(52)"),
        ]
    )

    vertex_block_enum = bpy.props.EnumProperty(
        name="Vertex block type",
        default = '37',
        items=[
            ('6', "6(no Normals)", "Block without normals. Mostly used in HT1"),
            ('7', "7(no Normals)", "Block without normals. Mostly used in HT2"),
            ('36', "36(with Normals)", "Block with normals. Mostly used in HT1"),
            ('37', "37(with Normals)", "Block with normals. Mostly used in HT2")
        ]
    )

    poly_block_enum = bpy.props.EnumProperty(
        name="Poly block type",
        default = '8',
        items=[
            ('8', "8(multiple textures)", "Block can use multiple materials per mesh. Casn use N-gons"),
            ('35', "35(single texture)", "Block use single materials per mesh. Use triangles")
        ]
    )


    add_blocks_enum = bpy.props.EnumProperty(
        name="Assembly type",
        items=[
            ('LOD_9', "Render tree(9)", "Render tree(9)"),
            ('LOD_10', "LOD(10)", "LOD(10)"),
            ('LOD_21', "Event(21)", "Event(21)"),
            #('07', "07", "Mesh (HT1)"),
            #('10', "10", "LOD"),
            #('12', "12", "Unk"),
            #('14', "14", "Car trigger"),
            #('18', "18", "Connector"),
            #('19', "19", "Room container"),
            #('20', "20", "2D collision"),
            #('21', "21", "Event container"),
            #('23', "23", "3D collision"),
            #('24', "24", "Locator"),
            #('28', "28", "2D-sprite"),
            #('33', "33", "Light source"),
            #('37', "37", "Mesh"),
            #('40', "40", "Object generator"),
        ]
    )
    
    current_hierarchy_enum = bpy.props.EnumProperty(
        name="Hierarchy type",
        items=[
            ('LOD_9', "Render tree(9)", "Render tree(9)"),
            ('LOD_10', "LOD(10)", "LOD(10)"),
            ('LOD_21', "Event(21)", "Event(21)")
        ]
    )

    active_module_enum = EnumProperty(
        name = 'Active module',
        description = 'Active module',
        items = modules_callback,
        default = 0, # index, not value
        update = set_cust_mytool_value(FieldType.STRING, 'active_module')
    )
    
    #Active module start
    active_module_switch = BoolProperty(
        name = 'Use dropdown',
        description = 'Dropdown selection',
        default = False
    )

    active_module_enum = EnumProperty(
        name = 'Active module',
        description = 'Active module',
        items = modules_callback,
        default = 0, # index, not value
        update = set_cust_mytool_value(FieldType.STRING, 'active_module')
    )
    
    active_module = StringProperty(
        name = 'Active module',
        description = 'Active module',
        maxlen = 32
    )
    #Active module end
    
    #Active room start
    active_room_switch = BoolProperty(
        name = 'Use dropdown',
        description = 'Dropdown selection',
        default = False
    )

    active_room_enum = EnumProperty(
        name = 'Active room',
        description = 'Active room',
        items = rooms_callback_mytool,
        default = 0, # index, not value
        update = set_cust_mytool_value(FieldType.STRING, 'active_room')
    )
    
    active_room = StringProperty(
        name = 'Active room',
        description = 'Active room',
        maxlen = 32
    )
    #Active room end

    #Render tree start
    render_tree_enum = EnumProperty(
        name = 'Render tree root',
        description = 'Render tree root',
        items = render_tree_callback,
        default = 0, # index, not value
        update = select_object_on_update('render_tree_enum')
    )
    #Render tree end

    #LOD start
    LOD_enum = EnumProperty(
        name = 'LOD root',
        description = 'LOD root',
        items = LOD_callback,
        default = 0, # index, not value
        update = select_object_on_update('LOD_enum')
    )
    #LOD end

    #event start
    event_enum = EnumProperty(
        name = 'Event root',
        description = 'Event root',
        items = event_callback,
        default = 0, # index, not value
        update = select_object_on_update('event_enum')
    )
    #event end

    lod_level_int = bpy.props.IntProperty(
        name='LOD level',
        description='LOD level',
        default=0,
        min=0
    )

    add_room_name_index_string = bpy.props.StringProperty(
        name="Room name",
        description="",
        default="aa_000",
        maxlen=30,
        )

    mirror_type_enum = bpy.props.EnumProperty(
        name="Block type",
        items=[ ('x', "x", ""),
                ('y', "y", ""),
                ('z', "z", ""),
               ]
        )

    parent_str = bpy.props.StringProperty(
        name ='Selected parent',
        description = 'New object will be parented to this object'
    )

    cast_copy = bpy.props.BoolProperty(
        name ='Create copy',
        description = 'Will be created copy of selected object and casted to B3D format',
        default = True
    )

_classes = [
    PanelSettings
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=PanelSettings)

def unregister():
    del bpy.types.Scene.my_tool
    for cls in _classes[::-1]: #reversed
        bpy.utils.unregister_class(cls)