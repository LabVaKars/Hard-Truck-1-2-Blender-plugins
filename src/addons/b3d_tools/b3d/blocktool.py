
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

from ..common import (
    get_block_tool
)

from ..compatibility import (
    is_before_2_80
)

from .blocktool_defs import (
    FieldType,
    BlockClassType,
    # block params
    Blk001,Blk002,Blk004,Blk005,Blk006,Blk007,Blk009,Blk010,
    Blk011,Blk012,Blk013,Blk014,Blk015,Blk016,Blk017,Blk018,Blk020,
    Blk021,Blk022,Blk023,Blk024,Blk025,Blk026,Blk027,Blk028,Blk029,Blk030,
    Blk031,Blk033,Blk034,Blk035,Blk036,Blk037,Blk039,Blk040,
    # per-face params
    Pfb008,Pfb028,Pfb035,
    # per-vertex params
    Pvb008,Pvb035,
    # way objs
    Blk050,Blk051,Blk052,
    # presets
    B40_TreeGenSimple, B40_TreeGenExtended
)

from .callbacks import (
    res_materials_callback,
    spaces_callback,
    referenceables_callback,
    rooms_callback,
    modules_callback,
    presets_callback
)

def set_cust_obj_value(subtype, bname, pname):
    def callback_func(self, context):

        blocktool = get_block_tool(context)
        result = getattr(getattr(blocktool, bname), '{}_enum'.format(pname))
        if subtype == FieldType.INT:
            result = int(result)
        elif subtype == FieldType.FLOAT:
            result = float(result)
        elif subtype == FieldType.STRING:
            result = str(result)

        setattr(
            bpy.context.object,
            '["{}"]'.format(pname),
            result
        )

    return callback_func

class BlockClassPrefix():

    PER_FACE_BLOCK = 'per_face_block'
    PER_VERTEX_BLOCK = 'per_vertex_block'
    BLOCK = 'block'
    SINGLE_BLOCK = 'single_block'


class BlockClassHandler():

    preset_classes = [
        B40_TreeGenSimple, B40_TreeGenExtended
    ]

    block_classes = [
        None, Blk001, Blk002, None, Blk004, Blk005, Blk006, Blk007, None, Blk009,
        Blk010, Blk011, Blk012, Blk013, Blk014, Blk015, Blk016, Blk017, Blk018, None,
        Blk020, Blk021, Blk022, Blk023, Blk024, Blk025, Blk026, Blk027, Blk028, Blk029,
        Blk030, Blk031, None, Blk033, Blk034, Blk035, Blk036, Blk037, None, Blk039,
        Blk040, None, None, None, None, None, None, None, None, None,
        Blk050, Blk051, Blk052, None, None, None, None, None, None, None,
    ]

    per_face_block_classes = [
        None, None, None, None, None, None, None, None, Pfb008, None,
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, Pfb028, None,
        None, None, None, None, None, Pfb035, None, None, None, None
    ]

    per_vertex_block_classes = [
        None, None, None, None, None, None, None, None, Pvb008, None,
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, None, None, None, None, None,
        None, None, None, None, None, Pvb035, None, None, None, None
    ]


    @staticmethod
    def get_block_type_from_bclass(bclass):
        return bclass.c_get_btype()

    @staticmethod
    def get_block_num_from_bclass(bclass):
        return int(bclass.c_get_bnum())

    @staticmethod
    def is_pob(cls): #per object block
        return cls.c_get_btype() == BlockClassType.BLOCK

    @staticmethod
    def is_pfb(cls): #per face block
        return cls.c_get_btype() == BlockClassType.PER_FACE_BLOCK

    @staticmethod
    def is_pvb(cls): #per vertex block
        return cls.c_get_btype() == BlockClassType.PER_VERTEX_BLOCK

    @staticmethod
    def get_block_object(bnum, btype = BlockClassType.BLOCK, multiple_edit = True):
        bname = BlockClassHandler.get_mytool_block_name(bnum, btype, multiple_edit)
        return [bname, BlockClassHandler.block_objects[bname]]

    @staticmethod
    def create_type_class(bname, fields, multiple_edit = True):

        attributes = {
            '__annotations__' : {}
        }
        for field in fields.values():
            pname = field.get_prop()
            bnum = field.get_bnum()
            prop = None

            if multiple_edit: # lock switches only for multiple edit
                # switch for locking property from editing
                lock_prop = BoolProperty(
                    name = "On./Off.",
                    description = "Enable/Disable param for editing",
                    default = True
                )
                attributes['__annotations__']["show_{}".format(pname)] = lock_prop


            if field.get_attr_type() == FieldType.STRING \
            or field.get_attr_type() == FieldType.COORD \
            or field.get_attr_type() == FieldType.FLOAT \
            or field.get_attr_type() == FieldType.INT \
            or field.get_attr_type() == FieldType.LIST:

                if field.get_attr_type() == FieldType.STRING and multiple_edit:
                    prop = StringProperty(
                        name = field.get_name(),
                        description = field.get_description(),
                        default = field.get_default(),
                        maxlen = 32
                    )

                elif field.get_attr_type() == FieldType.COORD and multiple_edit:
                    prop = FloatVectorProperty(
                        name = field.get_name(),
                        description = field.get_description(),
                        default = field.get_default()
                    )

                elif field.get_attr_type() == FieldType.FLOAT and multiple_edit:
                    prop = FloatProperty(
                        name = field.get_name(),
                        description = field.get_description(),
                        default = field.get_default()
                    )

                elif field.get_attr_type() == FieldType.INT and multiple_edit:
                    prop = IntProperty(
                        name = field.get_name(),
                        description = field.get_description(),
                        default = field.get_default()
                    )

                elif field.get_attr_type() == FieldType.LIST:
                    
                    prop_enum = EnumProperty(
                        name = "Preset",
                        description = "Dynamic parameter types preset",
                        items = presets_callback(bnum),
                        default = 0 # index, not value                     
                    )

                    prop = StringProperty(
                        name = field.get_name(),
                        description = field.get_description()
                    )
                    
                    attributes['__annotations__']["{}_enum".format(pname)] = prop_enum

                attributes['__annotations__'][pname] = prop

            elif field.get_attr_type() == FieldType.ENUM \
            or field.get_attr_type() == FieldType.ENUM_DYN:

                enum_callback = None
                subtype = field.get_subtype()

                if field.get_callback() == FieldType.SPACE_NAME:
                    enum_callback = spaces_callback
                elif field.get_callback() == FieldType.REFERENCEABLE:
                    enum_callback = referenceables_callback
                elif field.get_callback() == FieldType.MATERIAL_IND:
                    enum_callback = res_materials_callback
                elif field.get_callback() == FieldType.ROOM:
                    enum_callback = rooms_callback(bname, '{}'.format(pname)) 
                elif field.get_callback() == FieldType.RES_MODULE:
                    enum_callback = modules_callback

                prop = None
                prop_enum = None

                if field.get_manual_entry():
                    prop_switch = None
                    prop_switch = BoolProperty(
                        name = 'Use dropdown',
                        description = 'Dropdown selection',
                        default = False
                    )
                    attributes['__annotations__']['{}_switch'.format(pname)] = prop_switch

                if field.get_attr_type() == FieldType.ENUM:
                    prop_enum = EnumProperty(
                        name = field.get_name(),
                        description = field.get_description(),
                        items = field.get_items(),
                        default = field.get_default(),
                        update = set_cust_obj_value(subtype, bname, pname)
                    )

                    if multiple_edit:
                        if subtype == FieldType.STRING:
                            prop = StringProperty(
                                name = field.get_name(),
                                description = field.get_description(),
                                default = field.get_default(),
                                maxlen = 32
                            )
                        elif subtype == FieldType.INT:
                            prop = IntProperty(
                                name = field.get_name(),
                                description = field.get_description(),
                                default = field.get_default()
                            )

                elif field.get_attr_type() == FieldType.ENUM_DYN:
                    prop_enum = EnumProperty(
                        name = field.get_name(),
                        description = field.get_description(),
                        items = enum_callback,
                        default = 0, # index, not value
                        update = set_cust_obj_value(subtype, bname, pname)
                    )

                    if multiple_edit:
                        if subtype == FieldType.STRING:
                            prop = StringProperty(
                                name = field.get_name(),
                                description = field.get_description(),
                                maxlen = 32
                            )
                        elif subtype == FieldType.INT:
                            prop = IntProperty(
                                name = field.get_name(),
                                description = field.get_description()
                            )

                attributes['__annotations__']['{}_enum'.format(pname)] = prop_enum

                if multiple_edit:
                    attributes['__annotations__']['{}'.format(pname)] = prop

            elif field.get_attr_type() == FieldType.V_FORMAT: # currently only available in vertex edit

                prop0 = BoolProperty(
                    name = 'Raw edit',
                    description = 'Show raw integer',
                    default = False
                )
                attributes['__annotations__']['{}_show_int'.format(pname)] = prop0
                
                prop0 = IntProperty(
                    name = 'Format Raw',
                    description = 'Raw format integer',
                    default = 1
                )
                attributes['__annotations__']['{}_format_raw'.format(pname)] = prop0

                prop1 = BoolProperty(
                    name = 'Triangulation offset',
                    description = 'Order in which vertexes are read depends on that',
                    default = True
                )
                attributes['__annotations__']['{}_triang_offset'.format(pname)] = prop1

                prop2 = BoolProperty(
                    name = 'Use UV',
                    description = 'If active, writes UV during export.',
                    default = True
                )
                attributes['__annotations__']['{}_use_uvs'.format(pname)] = prop2

                prop3 = BoolProperty(
                    name = 'Use normals',
                    description = 'If active, writes normal during export.',
                    default = True
                )
                attributes['__annotations__']['{}_use_normals'.format(pname)] = prop3

                prop4 = BoolProperty(
                    name = 'Normal switch',
                    description = 'If active, use <float> for en(dis)abling normals. If not active use <float vector> for common normals. Is ignored if "Use normals" is inactive',
                    default = True
                )
                attributes['__annotations__']['{}_normal_flag'.format(pname)] = prop4

            elif field.get_attr_type() == FieldType.FLAGS:
                
                prop0 = BoolProperty(
                    name = 'Raw edit',
                    description = 'Show flags integer',
                    default = False
                )
                attributes['__annotations__']['{}_show_int'.format(pname)] = prop0

                prop = IntProperty(
                    name = field.get_name(),
                    description = field.get_description(),
                    default = field.get_default()
                )
                attributes['__annotations__']['{}'.format(pname)] = prop

                flag_descriptions = field.get_flag_description()
                if flag_descriptions is not None:

                    for desc in flag_descriptions:

                        prop = BoolProperty(
                            name = desc["name"],
                            description = desc["description"],
                            default = desc["default_value"]
                        )
                        attributes['__annotations__']['{}_{}'.format(pname, desc["key"])] = prop

        if is_before_2_80():
            attributes = attributes['__annotations__']

        newclass = type(bname, (bpy.types.PropertyGroup,), attributes)
        return newclass

    @staticmethod
    def create_block_properties():

        BlockClassHandler.block_objects = {}

        BlockClassHandler.blender_block_classes = []

        attributes = {
            '__annotations__' : {}
        }

        
        for bclass in [bc for bc in BlockClassHandler.preset_classes if bc is not None]:
            fields = {attr_cls.c_get_prop():attr_cls() for attr_name, attr_cls in bclass.__dict__.items() if not attr_name.startswith('__') and isinstance(attr_cls, type)}
            
            bnum = BlockClassHandler.get_block_num_from_bclass(bclass)
            btype = BlockClassHandler.get_block_type_from_bclass(bclass)
            
            for field_name, field in fields.items():
                field.c_set_bnum(bnum)
                field.c_set_btype(btype)
                field.set_bnum(bnum)
                field.set_btype(btype)
                #rename preset props to avoid name collisions
                field.set_prop("{}_{}".format(btype, field.get_prop()))

            bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(bclass, True)
            gen_class = BlockClassHandler.create_type_class(bname, fields)
            attributes['__annotations__'][bname] = PointerProperty(type=gen_class)
            BlockClassHandler.block_objects[bname] = fields
            BlockClassHandler.blender_block_classes.append(gen_class)


        for bclass in [bc for bc in BlockClassHandler.block_classes if bc is not None]:
            fields = {attr_cls.c_get_prop():attr_cls() for attr_name, attr_cls in bclass.__dict__.items() if not attr_name.startswith('__') and isinstance(attr_cls, type)}
            
            bnum = BlockClassHandler.get_block_num_from_bclass(bclass)
            btype = BlockClassHandler.get_block_type_from_bclass(bclass)
            
            for field_name, field in fields.items():
                field.c_set_bnum(bnum)
                field.c_set_btype(btype)
                field.set_bnum(bnum)
                field.set_btype(btype)

            bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(bclass, True)
            gen_class = BlockClassHandler.create_type_class(bname, fields)
            attributes['__annotations__'][bname] = PointerProperty(type=gen_class)
            BlockClassHandler.block_objects[bname] = fields
            BlockClassHandler.blender_block_classes.append(gen_class)

        for bclass in [bc for bc in BlockClassHandler.block_classes if bc is not None]:
            fields = {attr_cls.c_get_prop():attr_cls() for attr_name, attr_cls in bclass.__dict__.items() if not attr_name.startswith('__') and isinstance(attr_cls, type)}
            
            bnum = BlockClassHandler.get_block_num_from_bclass(bclass)
            btype = BlockClassHandler.get_block_type_from_bclass(bclass)
            
            for field_name, field in fields.items():
                field.c_set_bnum(bnum)
                field.c_set_btype(btype)
                field.set_bnum(bnum)
                field.set_btype(btype)

            bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(bclass, False)
            gen_class = BlockClassHandler.create_type_class(bname, fields, False)
            attributes['__annotations__'][bname] = PointerProperty(type=gen_class)
            BlockClassHandler.block_objects[bname] = fields
            BlockClassHandler.blender_block_classes.append(gen_class)

        for bclass in [bc for bc in BlockClassHandler.per_face_block_classes if bc is not None]:
            fields = {attr_cls.c_get_prop():attr_cls() for attr_name, attr_cls in bclass.__dict__.items() if not attr_name.startswith('__') and isinstance(attr_cls, type)}
            
            bnum = BlockClassHandler.get_block_num_from_bclass(bclass)
            btype = BlockClassHandler.get_block_type_from_bclass(bclass)
            
            for field_name, field in fields.items():
                field.c_set_bnum(bnum)
                field.c_set_btype(btype)
                field.set_bnum(bnum)
                field.set_btype(btype)

            bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(bclass, True)
            gen_class = BlockClassHandler.create_type_class(bname, fields)
            attributes['__annotations__'][bname] = PointerProperty(type=gen_class)
            BlockClassHandler.block_objects[bname] = fields
            BlockClassHandler.blender_block_classes.append(gen_class)

        for bclass in [bc for bc in BlockClassHandler.per_vertex_block_classes if bc is not None]:
            fields = {attr_cls.c_get_prop():attr_cls() for attr_name, attr_cls in bclass.__dict__.items() if not attr_name.startswith('__') and isinstance(attr_cls, type)}

            bnum = BlockClassHandler.get_block_num_from_bclass(bclass)
            btype = BlockClassHandler.get_block_type_from_bclass(bclass)
            
            for field_name, field in fields.items():
                field.c_set_bnum(bnum)
                field.c_set_btype(btype)
                field.set_bnum(bnum)
                field.set_btype(btype)
            
            bname, bnum = BlockClassHandler.get_mytool_block_name_by_class(bclass, True)
            gen_class = BlockClassHandler.create_type_class(bname, fields)
            attributes['__annotations__'][bname] = PointerProperty(type=gen_class)
            BlockClassHandler.block_objects[bname] = fields
            BlockClassHandler.blender_block_classes.append(gen_class)

        if is_before_2_80():
            attributes = attributes['__annotations__']

        return type("BlockSettings", (bpy.types.PropertyGroup,), attributes)

    @staticmethod
    def get_mytool_block_name_by_class(bclass, multiple_edit = True):
        bname = ''
        btype = bclass.c_get_btype()
        bnum = bclass.c_get_bnum()
        if btype == BlockClassType.BLOCK:
            if multiple_edit:
                bname = '{}_{}'.format(BlockClassPrefix.BLOCK, bnum)
            else:
                bname = '{}_{}'.format(BlockClassPrefix.SINGLE_BLOCK, bnum)
        elif btype == BlockClassType.PER_FACE_BLOCK:
            bname = '{}_{}'.format(BlockClassPrefix.PER_FACE_BLOCK, bnum)
        elif btype == BlockClassType.PER_VERTEX_BLOCK:
            bname = '{}_{}'.format(BlockClassPrefix.PER_VERTEX_BLOCK, bnum)
        else:
            bname = '{}_{}'.format(btype, bnum)

        return [bname, bnum]

    @staticmethod
    def get_mytool_block_name(bnum, btype = BlockClassType.BLOCK, multiple_edit = False):
        bname = ''
        if btype == BlockClassType.BLOCK:
            if multiple_edit:
                bname = '{}_{}'.format(BlockClassPrefix.BLOCK, bnum)
            else:
                bname = '{}_{}'.format(BlockClassPrefix.SINGLE_BLOCK, bnum)
        elif btype == BlockClassType.PER_FACE_BLOCK:
            bname = '{}_{}'.format(BlockClassPrefix.PER_FACE_BLOCK, bnum)
        elif btype == BlockClassType.PER_VERTEX_BLOCK:
            bname = '{}_{}'.format(BlockClassPrefix.PER_VERTEX_BLOCK, bnum)
        else:
            bname = '{}_{}'.format(btype, bnum)


        return bname

BlockSettings = BlockClassHandler.create_block_properties()

def register():
    for cls in BlockClassHandler.blender_block_classes:
        bpy.utils.register_class(cls)
    bpy.utils.register_class(BlockSettings)
    bpy.types.Scene.kotr_block_tool = bpy.props.PointerProperty(type=BlockSettings)

def unregister():
    del bpy.types.Scene.kotr_block_tool
    bpy.utils.unregister_class(BlockSettings)
    for cls in BlockClassHandler.blender_block_classes[::-1]: #reversed
        bpy.utils.unregister_class(cls)
