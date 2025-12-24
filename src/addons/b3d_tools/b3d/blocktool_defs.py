import enum
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


from ..consts import (
    collisionTypeList,
    generatorTypeList,
    b24FlagList,
    b33LightTypes,
    vTypeList,
    BLOCK_TYPE,
    LEVEL_GROUP
)

# Dynamic block exmaple
# block_5 = type("block_5", (bpy.types.PropertyGroup,), {
#     '__annotations__': {
#         'name': StringProperty(
#                 name="Block name",
#                 default="",
#                 maxlen=30,
#             ),
#         'XYZ': FloatVectorProperty(
#                 name='Block border coord',
#                 description='',
#                 default=(0.0, 0.0, 0.0)
#             ),
#         'r': FloatProperty(
#                 name = "Block border rad",
#                 description = "",

#             )
#     }
# })

class FieldType(enum.Enum):
    IGNORE = 0
    STRING = 1
    COORD = 2
    # RAD = 3
    INT = 4
    FLOAT = 5
    ENUM = 6
    LIST = 7
    ENUM_DYN = 8
    FLAGS = 9

    V_FORMAT = 21
    MATERIAL_IND = 22
    SPACE_NAME = 23
    REFERENCEABLE = 24
    ROOM = 25
    RES_MODULE = 26

    SPHERE_EDIT = 41

# blocktool_defs configuration:

# prop - Required - Key used to save property in Blenders custom properties.
# group - Optional - Used to determine what elements to group together.
# type - Required - Type of the field.
# Type specific configurations

# FieldType.STRING
    # 'name': 'name',
    # 'description': '',
    # 'default': ''

# FieldType.COORD
    # 'name': 'Name',
    # 'description': '',
    # 'default': (0.0, 0.0, 0.0)

# FieldType.INT
    # 'name': 'Name',
    # 'description': '',
    # 'default': 0

# FieldType.FLOAT
    # 'name': 'Name',
    # 'description': '',
    # 'default': 0.0

# FieldType.ENUM - static
    # 'subtype': FieldType.INT,
    # 'name': 'Name',
    # 'description': ''

# FieldType.LIST
    # 'name': 'Name',
    # 'description': ''

# FieldType.ENUM_DYN - dynamic
    # 'subtype': FieldType.STRING
    # 'callback': FieldType.SPACE_NAME,
    # 'name': 'Name',
    # 'description': ''

# FieldType.V_FORMAT

# Used as subtypes
# FieldType.MATERIAL_IND
# FieldType.SPACE_NAME
# FieldType.REFERENCEABLE
# FieldType.ROOM
# FieldType.RES_MODULE

# Custom operators
# FieldType.SPHERE_EDIT

class BlkParam():
    prop = None                         #Key under what property is stored in Blender object
    block_type = ''                     #Block
    name = 'Unknown'                    #Parameter name in UI
    description = 'Unknown parameter'   #Parameter description in UI
    default_value = ''                  #Default value for simple types(int, float)
    group = ''                          #Used for grouping values in UI
    # Enum specific keys
    subtype = ''                        #Type for Enumerator values
    callback = ''                       #Callback for dynamic enumerators
    items = None                        #Static enumerator values
    # Flag specific keys
    flag_description = None             #Description for flag values
    # Subgroup specific keys
    subgroup = -1                       #Block subgroup index;
                                        #Subgroup fields are shown/hidden based on specific hardcoded conditions.
    optional_group = -1                 #Values with same optional_group are considered optional

    @classmethod
    def get_prop(cls):
        if cls.prop is not None:
            return cls.prop
        return cls.__name__

    @classmethod
    def get_block_type(cls):
        return cls.block_type

    @classmethod
    def get_name(cls):
        return cls.name

    @classmethod
    def get_description(cls):
        return cls.description

    @classmethod
    def get_subtype(cls):
        return cls.subtype

    @classmethod
    def get_default(cls):
        return cls.default_value

    @classmethod
    def get_callback(cls):
        return cls.callback

    @classmethod
    def get_items(cls):
        return cls.items

    @classmethod
    def get_group(cls):
        return cls.group
    
    @classmethod
    def get_flag_description(cls):
        return cls.flag_description

    @classmethod
    def is_pob(cls): #per object block
        return cls.__name__[0:3] == 'Blk'

    @classmethod
    def is_pfb(cls): #per face block
        return cls.__name__[0:3] == 'Pfb'

    @classmethod
    def is_pvb(cls): #per vertex block
        return cls.__name__[0:3] == 'Pvb'
        

class StringParam(BlkParam):
    block_type = FieldType.STRING
    default_value = ''

class IntParam(BlkParam):
    block_type = FieldType.INT
    default_value = 0

class FloatParam(BlkParam):
    block_type = FieldType.FLOAT
    default_value = 0.0

class CoordParam(BlkParam):
    block_type = FieldType.COORD
    default_value = (0.0, 0.0, 0.0)

class EnumParam(BlkParam):
    block_type = FieldType.ENUM
    subtype = FieldType.INT
    items = []

class EnumDynParam(BlkParam):
    block_type = FieldType.ENUM_DYN
    subtype = FieldType.INT,
    callback = FieldType.SPACE_NAME
    
class FlagsParam(BlkParam):
    block_type = FieldType.FLAGS
    default_value = 0
    flag_description = None

class VFormatParam(BlkParam):
    block_type = FieldType.V_FORMAT #Integer

class SphereEditParam(BlkParam):
    block_type = FieldType.SPHERE_EDIT

class ListParam(BlkParam):
    block_type = FieldType.LIST



class Pvb008():
    pass
    # disabled for now. Reason: 1) hard to edit
    # todo: analyze more
    # Normal_Switch = {
    #     'prop': 'normal_switch',
    #     'type': FieldType.FLOAT,
    #     'name': 'Normal switcher',
    #     'description': '',
    #     'default': 0.0
    # }
    # Custom_Normal = {
    #     'prop': 'custom_normal',
    #     'type': FieldType.COORD,
    #     'name': 'Custom normal',
    #     'description': '',
    #     'default': (0.0, 0.0, 0.0)
    # }


class Pvb035():
    pass
    # disabled for now. Reason: 1) hard to edit
    # todo: analyze more
    # Normal_Switch = {
    #     'prop': 'normal_switch',
    #     'type': FieldType.FLOAT,
    #     'name': 'Normal switcher',
    #     'description': '',
    #     'default': 0.0
    # }
    # Custom_Normal = {
    #     'prop': 'custom_normal',
    #     'type': FieldType.COORD,
    #     'name': 'Custom normal',
    #     'description': '',
    #     'default': (0.0, 0.0, 0.0)
    # }


class Pfb008():
    class Format_Flags(VFormatParam):
        name = ''
        default_value = 144

    # disabled for now. Reason: 1) hard to edit 2) more or less static values
    # todo: analyze more
    # Unk_Float1 = {
    #     'prop': 'float1',
    #     'type': FieldType.FLOAT,
    #     'name': 'Unk. 1',
    #     'description': '',
    #     'default': 0.0
    # }
    # Unk_Int2 = {
    #     'prop': 'int2',
    #     'type': FieldType.INT,
    #     'name': 'Unk. 2',
    #     'description': '',
    #     'default': 0
    # }


class Pfb028():
    class Format_Flags(VFormatParam):
        name = ''
        default_value = 144

    # disabled for now. Reason: 1) hard to edit 2) more or less static values
    # todo: analyze more
    # Unk_Float1 = {
    #     'prop': 'float1',
    #     'type': FieldType.FLOAT,
    #     'name': 'Unk. 1',
    #     'description': '',
    #     'default': 0.0
    # }
    # Unk_Int2 = {
    #     'prop': 'int2',
    #     'type': FieldType.INT,
    #     'name': 'Unk. 2',
    #     'description': '',
    #     'default': 0
    # }


class Pfb035():
    class Format_Flags(VFormatParam):
        name = ''
        default_value = 144

    # disabled for now. Reason: 1) hard to edit 2) more or less static values
    # todo: analyze more
    # Unk_Float1 = {
    #     'prop': 'float1',
    #     'type': FieldType.FLOAT,
    #     'name': 'Unk. 1',
    #     'description': '',
    #     'default': 0.0
    # }
    # Unk_Int2 = {
    #     'prop': 'int2',
    #     'type': FieldType.INT,
    #     'name': 'Unk. 2',
    #     'description': '',
    #     'default': 0
    # }





class Blk001():
    class Name1(StringParam):
        name = 'Unk. name 1'
        prop = 'string1'

    class Name2(StringParam):
        name = 'Unk. name 2'
        prop = 'string2'


class Blk002():
    class Unk_XYZ(CoordParam):
        name = 'Unk. name 2'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'coord2'


class Blk004():
    class Name1(EnumDynParam):
        name = 'Place'
        prop = 'string1'
        subtype = FieldType.STRING
        callback = FieldType.SPACE_NAME
        default_value = '?'

    class Name2(StringParam):
        prop = 'string2'
        name = 'Name 2'


class Blk005():
    class Name1(StringParam):
        name = 'Block name'
        prop = 'string2'


class Blk006():
    class Name1(StringParam):
        name = 'Name 1'
        prop = 'string1'

    class Name2(StringParam):
        name = 'Name 2'
        prop = 'string2'


class Blk007():
    class Name1(StringParam):
        name = 'Group name'
        prop = 'string1'

class Blk009():
    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'
        group = 'b9_group'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'
        group = 'b9_group'


class Blk010():
    class LOD_XYZ(CoordParam):
        name = 'LOD coord'
        prop = 'coord1'
        description = 'LOD center'
        group = 'LOD_group'

    class LOD_R(FloatParam):
        name = 'LOD rad'
        prop = 'float1'
        description = 'LOD radius'
        group = 'LOD_group'

    class Set_LOD(SphereEditParam):
        name = ''
        description = ''
        group = 'LOD_group'


class Blk011():
    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord'
        prop = 'coord2'

    class Unk_R1(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'

    class Unk_R2(FloatParam):
        name = 'Unk. rad'
        prop = 'float2'


class Blk012():
    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'

    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk013():
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list2'


class Blk014():
    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float2'

    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk015():
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk016():
    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord 1'
        prop = 'coord1'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord 2'
        prop = 'coord2'

    class Unk_Float1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Float2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_Int1(IntParam):
        name = 'Unk. 3'
        prop = 'int3'

    class Unk_Int2(IntParam):
        name = 'Unk. 4'
        prop = 'int4'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk017():
    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord 1'
        prop = 'coord1'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord 2'
        prop = 'coord2'

    class Unk_Float1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Float2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_Int1(IntParam):
        name = 'Unk. 3'
        prop = 'int3'

    class Unk_Int2(IntParam):
        name = 'Unk. 4'
        prop = 'int4'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk018():
    class Space_Name(EnumDynParam):
        name = 'Place name (24)'
        prop = 'string1'
        description = 'Name of location block(24)'
        subtype = FieldType.STRING
        callback = FieldType.SPACE_NAME
        default_value = '?'

    class Add_Name(EnumDynParam):
        name = 'Transfer block name'
        prop = 'string2'
        description = 'Name of block to be relocated'
        subtype = FieldType.STRING
        callback = FieldType.REFERENCEABLE
        default_value = '?'


class Blk020():
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk021():
    class GroupCnt(IntParam):
        name = 'Group count'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'


class Blk022():
    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'


class Blk023():
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Surface(EnumParam):
        name = 'Surface type'
        prop = 'int2'
        subtype = FieldType.INT
        items = collisionTypeList
        description = 'Value from surface classificator'
        default_value = 0

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'


class Blk024():
    class Flag(EnumParam):
        name = 'Show flag'
        prop = 'int1'
        subtype = FieldType.INT
        items = b24FlagList
        description = 'Value from block24 classificator'
        default_value = 0


class Blk025():
    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Name(StringParam):
        name = 'Unk. name 1'
        prop = 'string1'

    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord 1'
        prop = 'coord2'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord 2'
        prop = 'coord3'

    class Unk_Float1(FloatParam):
        name = 'Unk. 1'
        prop = 'float1'

    class Unk_Float2(FloatParam):
        name = 'Unk. 2'
        prop = 'float2'

    class Unk_Float3(FloatParam):
        name = 'Unk. 3'
        prop = 'float3'

    class Unk_Float4(FloatParam):
        name = 'Unk. 4'
        prop = 'float4'

    class Unk_Float5(FloatParam):
        name = 'Unk. 5'
        prop = 'float5'


class Blk026():
    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord 1'
        prop = 'coord1'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord 2'
        prop = 'coord2'

    class Unk_XYZ3(CoordParam):
        name = 'Unk. coord 3'
        prop = 'coord3'


class Blk027():
    class Flag(IntParam):
        name = 'Flag'
        prop = 'int1'

    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Material(IntParam):
        name = 'Material'
        prop = 'int2'


class Blk028():
    class Sprite_Center(CoordParam):
        name = 'Sprite center coord'
        prop = 'coord1'
        description = 'Sprite center coordinates'
     #todo: check


class Blk029():
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'


class Blk030():
    class ResModule1(EnumDynParam):
        name = '1. module'
        prop = 'string1'
        subtype = FieldType.STRING
        callback = FieldType.RES_MODULE
        default_value = '?'
        group = 'resModule1'

    class RoomName1(EnumDynParam):
        name = '1. room'
        prop = 'string2'
        subtype = FieldType.STRING
        callback = FieldType.ROOM
        default_value = '?'
        group = 'resModule1'

    class ResModule2(EnumDynParam):
        name = '2. module'
        prop = 'string3'
        subtype = FieldType.STRING
        callback = FieldType.RES_MODULE
        default_value = '?'
        group = 'resModule2'

    class RoomName2(EnumDynParam):
        name = '2. room'
        prop = 'string4'
        subtype = FieldType.STRING
        callback = FieldType.ROOM
        default_value = '?'
        group = 'resModule2'


class Blk031():
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord 1'
        prop = 'coord1'

    class Unk_R(CoordParam):
        name = 'Unk. rad'
        prop = 'coord2'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord 2'
        prop = 'coord3'

    #todo: check


class Blk033():
    class Use_Lights(IntParam):
        name = 'Use lights'
        prop = 'int1'

    class Light_Type(IntParam):
        name = 'Light variable'
        prop = 'int2'

    class Flag(EnumParam):
        name = 'Light type'
        prop = 'int3'
        subtype = FieldType.INT
        items = b33LightTypes
        default_value = 1

    class Unk_XYZ1(CoordParam):
        name = 'Light location'
        prop = 'coord1'

    class Unk_XYZ2(CoordParam):
        name = 'Light direction'
        prop = 'coord2'

    class Unk_Float1(FloatParam):
        name = 'Light falloff'
        prop = 'float1'

    class Unk_Float2(FloatParam):
        name = 'Light attenuation 0'
        prop = 'float2'

    class Light_R(FloatParam):
        name = 'Light attenuation 1'
        prop = 'float3'

    class Intens(FloatParam):
        name = 'Light attenuation 2'
        prop = 'float4'

    class Unk_Float3(FloatParam):
        name = 'Light phi'
        prop = 'float5'

    class Unk_Float4(FloatParam):
        name = 'Light theta'
        prop = 'float6'

    class RGB(CoordParam):
        name = 'RGB'
        prop = 'coord3'


class Blk034():
    class UnkInt(IntParam):
        name = 'Unk. 1'
        prop = 'int1'


class Blk035():
    class MType(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class TexNum(EnumDynParam):
        name = 'Material'
        prop = 'int2'
        subtype = FieldType.INT
        callback = FieldType.MATERIAL_IND
        default_value = -1

class Blk036():
    class Name1(StringParam):
        name = 'Name 1'
        prop = 'string1'

    class Name2(StringParam):
        name = 'Name 2'
        prop = 'string2'

    class VType(EnumParam):
        name = 'Vertex type'
        prop = 'int1'
        subtype = FieldType.INT
        items = vTypeList
        default_value = 2


class Blk037():
    class Name1(StringParam):
        name = 'Name 1'
        prop = 'string1'

    class VType(EnumParam):
        name = 'Vertex type'
        prop = 'int1'
        subtype = FieldType.INT
        items = vTypeList
        default_value = 2


class Blk039():
    class Color_R(IntParam):
        name = 'Color rad'
        prop = 'int1'

    class Unk_Float1(FloatParam):
        name = 'Unk. 1'
        prop = 'float1'

    class Fog_Start(FloatParam):
        name = 'Fog Start'
        prop = 'float2'

    class Fog_End(FloatParam):
        name = 'Fog End'
        prop = 'float3'

    class Color_Id(IntParam):
        name = 'Color Id'
        prop = 'int2'


class Blk040():
    class Name1(StringParam):
        name = 'Name 1'
        prop = 'string1'

    class Name2(EnumParam):
        name = 'Generator type'
        prop = 'string2'
        subtype = FieldType.STRING
        items = generatorTypeList
        default_value = '$$TreeGenerator'

    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'
    
    class TreeMatIndex(IntParam):
        name = 'Tree Material'
        prop = 'int11'
        subgroup = 1

    class LeftMatIndex(IntParam):
        name = 'Leaf Material'
        prop = 'int12'
        subgroup = 1

    class Unk_Float11(FloatParam):
        name = 'Unk. F1'
        prop = 'float11'
        subgroup = 1
        optional_group = 1
        
    class Unk_Coord11(CoordParam):
        name = 'Unk. C1'
        prop = 'coord11'
        subgroup = 1
        optional_group = 1

    class Unk_Float12(FloatParam):
        name = 'Unk. F2'
        prop = 'float12'
        subgroup = 1
        optional_group = 1
        
    class Unk_Coord12(CoordParam):
        name = 'Unk. C1'
        prop = 'coord12'
        subgroup = 1
        optional_group = 1


# Blk050 - segment
# Blk051 - unoriented node
# Blk052 - oriented node

class Blk050():

    class Attr1(FlagsParam):
        name = 'Segment flags'
        prop = 'int1'
        description = 'Segment flags as integer'
        default_value = 1
        flag_description = [{
            "name": "Use curved path",
            "key": "is_curve",
            "description": "Path is built using a NURBS curve",
            "default_value": True,
            "bit_index": 0
        },{
            "name": "Use straight path",
            "key": "is_path",
            "description": "",
            "default_value": False,
            "bit_index": 1
        },{
            "name": "One-way right lane",
            "key": "is_right_lane",
            "description": "",
            "default_value": False,
            "bit_index": 2
        },{
            "name": "One-way left lane",
            "key": "is_left_lane",
            "description": "",
            "default_value": False,
            "bit_index": 3
        },{
            "name": "Fillable path",
            "key": "is_fillable",
            "description": "",
            "default_value": False,
            "bit_index": 4
        },{
            "name": "Hidden path",
            "key": "is_hidden",
            "description": "",
            "default_value": False,
            "bit_index": 5
        },{
            "name": "No traffic?",
            "key": "no_traffic",
            "description": "",
            "default_value": False,
            "bit_index": 6
        }]

    class Attr2(FloatParam):
        name = 'Extend multiplier'
        prop = 'float1'

    class Attr3(IntParam):
        name = 'Lane Count?'
        prop = 'int2'

    class Rten(StringParam):
        name = 'Unk. name'
        prop = 'string1'

    class Width1(FloatParam):
        name = 'Starting width'
        prop = 'float2'

    class Width2(FloatParam):
        name = 'Ending width'
        prop = 'float3'


class Blk051():
    class Flag(IntParam):
        name = 'Flag'
        prop = 'int1'

class Blk052():
    class Flag(IntParam):
        name = 'Flag'
        prop = 'int1'