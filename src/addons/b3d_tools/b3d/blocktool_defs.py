
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

class BlockClassType():

    PER_FACE_BLOCK = 'Pfb'
    PER_VERTEX_BLOCK = 'Pvb'
    BLOCK = 'Blk'

class FieldType():
    IGNORE = 0
    STRING = 1
    COORD = 2
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
# ui_group - Optional - Used to determine what elements to group together.
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

class BlkBase():
    bnum = 0
    btype = BlockClassType.BLOCK

    # --- btype ---
    @classmethod
    def c_get_btype(cls):
        return cls.btype

    # --- bnum ---
    @classmethod
    def c_get_bnum(cls):
        return cls.bnum

class BlkParam():
    bnum = None                         #Block number
    btype = None                        #Block type
    prop = None                         #Key under what property is stored in Blender object
    attr_type = ''                      #Attribute type
    name = 'Unknown'                    #Parameter name in UI
    description = 'Unknown parameter'   #Parameter description in UI
    default_value = ''                  #Default value for simple types(int, float)
    ui_group = ''                       #Used for grouping values in UI
    no_single_edit = False              #Determines if field is shown in "Single block edit"
    # Enum specific keys
    subtype = ''                        #Type for Enumerator values
    callback = ''                       #Callback for dynamic enumerators
    items = None                        #Static enumerator values
    manual_entry = True                 #If True Enumeration gives an option to enter value manually
    # Flag specific keys
    flag_description = None             #Description for flag values

    def __init__(self, init_empty = False):
        if not init_empty:
            cls = type(self)
            cls_attribs = [name for name in dir(cls) \
                if not name.startswith("__")\
                and not callable(getattr(cls, name))
            ]
            for attrib in cls_attribs:
                setattr(self, "_{}".format(attrib), getattr(cls, attrib))
    
    # --- btype ---
    @classmethod
    def c_get_btype(cls):
        return cls.btype
    
    @classmethod
    def c_set_btype(cls, value):
        cls.btype = value
    
    def get_btype(self):
        return self._btype

    def set_btype(self, value):
        self._btype = value
    
    # --- bnum ---
    @classmethod
    def c_get_bnum(cls):
        return cls.bnum

    @classmethod
    def c_set_bnum(cls, value):
        cls.bnum = value

    def get_bnum(self):
        return self._bnum

    def set_bnum(self, value):
        self._bnum = value

    # --- prop ---
    @classmethod
    def c_get_prop(cls):
        if cls.prop is not None:
            return cls.prop
        return cls.__name__
    
    def get_prop(self):
        return self._prop

    def set_prop(self, value):
        self._prop = value
        
    # --- attr_type ---
    @classmethod
    def c_get_attr_type(cls):
        return cls.attr_type
    
    def get_attr_type(self):
        return self._attr_type

    def set_attr_type(self, value):
        self._attr_type = value

    # --- name ---
    @classmethod
    def c_get_name(cls):
        return cls.name
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    # --- description ---
    @classmethod
    def c_get_description(cls):
        return cls.description
    
    def get_description(self):
        return self._description

    def set_description(self, value):
        self._description = value

    # --- subtype ---
    @classmethod
    def c_get_subtype(cls):
        return cls.subtype
    
    def get_subtype(self):
        return self._subtype

    def set_subtype(self, value):
        self._subtype = value

    # --- default_value ---
    @classmethod
    def c_get_default(cls):
        return cls.default_value
    
    def get_default(self):
        return self._default_value

    def set_default(self, value):
        self._default_value = value

    # --- callback ---
    @classmethod
    def c_get_callback(cls):
        return cls.callback
    
    def get_callback(self):
        return self._callback

    def set_callback(self, value):
        self._callback = value


    # --- items ---
    @classmethod
    def c_get_items(cls):
        return cls.items
    
    def get_items(self):
        return self._items

    def set_items(self, value):
        self._items = value

    # --- ui_group ---
    @classmethod
    def c_get_group(cls):
        return cls.ui_group
    
    def get_group(self):
        return self._ui_group

    def set_group(self, value):
        self._ui_group = value
    
    # --- no_single_edit ---
    @classmethod
    def c_get_no_single_edit(cls):
        return cls.no_single_edit
    
    def get_no_single_edit(self):
        return self._no_single_edit

    def set_no_single_edit(self, value):
        self._no_single_edit = value

        
    # --- flag_description ---
    @classmethod
    def c_get_flag_description(cls):
        return cls.flag_description
    
    def get_flag_description(self):
        return self._flag_description

    def set_flag_description(self, value):
        self._flag_description = value
    
    # --- manual_entry ---
    @classmethod
    def c_get_manual_entry(cls):
        return cls.manual_entry
    
    def get_manual_entry(self):
        return self._manual_entry

    def set_manual_entry(self, value):
        self._manual_entry = value


class StringParam(BlkParam):
    attr_type = FieldType.STRING
    default_value = ''

class IntParam(BlkParam):
    attr_type = FieldType.INT
    default_value = 0

class FloatParam(BlkParam):
    attr_type = FieldType.FLOAT
    default_value = 0.0

class CoordParam(BlkParam):
    attr_type = FieldType.COORD
    default_value = (0.0, 0.0, 0.0)

class EnumParam(BlkParam):
    attr_type = FieldType.ENUM
    subtype = FieldType.INT
    items = []

class EnumDynParam(BlkParam):
    attr_type = FieldType.ENUM_DYN
    subtype = FieldType.INT,
    callback = FieldType.SPACE_NAME
    
class FlagsParam(BlkParam):
    attr_type = FieldType.FLAGS
    default_value = 0
    flag_description = None

class VFormatParam(BlkParam):
    attr_type = FieldType.V_FORMAT #Integer

class SphereEditParam(BlkParam):
    attr_type = FieldType.SPHERE_EDIT

class ListParam(BlkParam):
    attr_type = FieldType.LIST



class Pvb008(BlkBase):
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


class Pvb035(BlkBase):
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


class Pfb008(BlkBase):
    bnum = 8
    btype = BlockClassType.PER_FACE_BLOCK
    class Format_Flags(VFormatParam):
        name = ''
        prop = 'format_flags'
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


class Pfb028(BlkBase):
    bnum = 28
    btype = BlockClassType.PER_FACE_BLOCK
    class Format_Flags(VFormatParam):
        name = ''
        prop = 'format_flags'
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


class Pfb035(BlkBase):
    bnum = 35
    btype = BlockClassType.PER_FACE_BLOCK
    class Format_Flags(VFormatParam):
        name = ''
        prop = 'format_flags'
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





class Blk001(BlkBase):
    bnum = 1
    btype = BlockClassType.PER_FACE_BLOCK
    class Name1(StringParam):
        name = 'Unk. name 1'
        prop = 'string1'

    class Name2(StringParam):
        name = 'Unk. name 2'
        prop = 'string2'


class Blk002(BlkBase):
    bnum = 2
    class Unk_XYZ(CoordParam):
        name = 'Unk. name 2'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'coord2'


class Blk004(BlkBase):
    bnum = 4
    class Name1(EnumDynParam):
        name = 'Place'
        prop = 'string1'
        subtype = FieldType.STRING
        callback = FieldType.SPACE_NAME
        default_value = '?'

    class Name2(StringParam):
        prop = 'string2'
        name = 'Name 2'


class Blk005(BlkBase):
    bnum = 5
    class Name1(StringParam):
        name = 'Block name'
        prop = 'string2'


class Blk006(BlkBase):
    bnum = 6
    class Name1(StringParam):
        name = 'Name 1'
        prop = 'string1'

    class Name2(StringParam):
        name = 'Name 2'
        prop = 'string2'


class Blk007(BlkBase):
    bnum = 7
    class Name1(StringParam):
        name = 'Group name'
        prop = 'string1'

class Blk009(BlkBase):
    bnum = 9
    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'
        ui_group = 'b9_group'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'
        ui_group = 'b9_group'


class Blk010(BlkBase):
    bnum = 10
    class LOD_XYZ(CoordParam):
        name = 'LOD coord'
        prop = 'coord1'
        description = 'LOD center'
        ui_group = 'LOD_group'

    class LOD_R(FloatParam):
        name = 'LOD rad'
        prop = 'float1'
        description = 'LOD radius'
        ui_group = 'LOD_group'

    class Set_LOD(SphereEditParam):
        name = ''
        description = ''
        ui_group = 'LOD_group'


class Blk011(BlkBase):
    bnum = 11
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


class Blk012(BlkBase):
    bnum = 12
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
        no_single_edit = True


class Blk013(BlkBase):
    bnum = 13
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'
        no_single_edit = True


class Blk014(BlkBase):
    bnum = 14
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
        no_single_edit = True


class Blk015(BlkBase):
    bnum = 15
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'
        no_single_edit = True


class Blk016(BlkBase):
    bnum = 16
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
        no_single_edit = True


class Blk017(BlkBase):
    bnum = 17
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
        no_single_edit = True


class Blk018(BlkBase):
    bnum = 18
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


class Blk020(BlkBase):
    bnum = 20
    class Unk_Int1(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'

    class Unk_List(ListParam):
        name = 'Unk. params'
        prop = 'list1'
        no_single_edit = True


class Blk021(BlkBase):
    bnum = 21
    class GroupCnt(IntParam):
        name = 'Group count'
        prop = 'int1'

    class Unk_Int2(IntParam):
        name = 'Unk. 2'
        prop = 'int2'


class Blk022(BlkBase):
    bnum = 22
    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Unk_R(FloatParam):
        name = 'Unk. rad'
        prop = 'float1'


class Blk023(BlkBase):
    bnum = 23
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
        no_single_edit = True


class Blk024(BlkBase):
    bnum = 24
    class Flag(EnumParam):
        name = 'Show flag'
        prop = 'int1'
        subtype = FieldType.INT
        items = b24FlagList
        description = 'Value from block24 classificator'
        default_value = 0


class Blk025(BlkBase):
    bnum = 25
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


class Blk026(BlkBase):
    bnum = 26
    class Unk_XYZ1(CoordParam):
        name = 'Unk. coord 1'
        prop = 'coord1'

    class Unk_XYZ2(CoordParam):
        name = 'Unk. coord 2'
        prop = 'coord2'

    class Unk_XYZ3(CoordParam):
        name = 'Unk. coord 3'
        prop = 'coord3'


class Blk027(BlkBase):
    bnum = 27
    class Flag(IntParam):
        name = 'Flag'
        prop = 'int1'

    class Unk_XYZ(CoordParam):
        name = 'Unk. coord'
        prop = 'coord1'

    class Material(IntParam):
        name = 'Material'
        prop = 'int2'


class Blk028(BlkBase):
    bnum = 28
    class Sprite_Center(CoordParam):
        name = 'Sprite center coord'
        prop = 'coord1'
        description = 'Sprite center coordinates'
     #todo: check


class Blk029(BlkBase):
    bnum = 29
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


class Blk030(BlkBase):
    bnum = 30
    class ResModule1(EnumDynParam):
        name = '1. module'
        prop = 'string1'
        subtype = FieldType.STRING
        callback = FieldType.RES_MODULE
        default_value = '?'
        ui_group = 'resModule1'

    class RoomName1(EnumDynParam):
        name = '1. room'
        prop = 'string2'
        subtype = FieldType.STRING
        callback = FieldType.ROOM
        default_value = '?'
        ui_group = 'resModule1'

    class ResModule2(EnumDynParam):
        name = '2. module'
        prop = 'string3'
        subtype = FieldType.STRING
        callback = FieldType.RES_MODULE
        default_value = '?'
        ui_group = 'resModule2'

    class RoomName2(EnumDynParam):
        name = '2. room'
        prop = 'string4'
        subtype = FieldType.STRING
        callback = FieldType.ROOM
        default_value = '?'
        ui_group = 'resModule2'


class Blk031(BlkBase):
    bnum = 31
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


class Blk033(BlkBase):
    bnum = 33
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


class Blk034(BlkBase):
    bnum = 34
    class UnkInt(IntParam):
        name = 'Unk. 1'
        prop = 'int1'


class Blk035(BlkBase):
    bnum = 35
    class MType(IntParam):
        name = 'Unk. 1'
        prop = 'int1'

    class TexNum(EnumDynParam):
        name = 'Material'
        prop = 'int2'
        subtype = FieldType.INT
        callback = FieldType.MATERIAL_IND
        default_value = -1

class Blk036(BlkBase):
    bnum = 36
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


class Blk037(BlkBase):
    bnum = 37
    class Name1(StringParam):
        name = 'Name 1'
        prop = 'string1'

    class VType(EnumParam):
        name = 'Vertex type'
        prop = 'int1'
        subtype = FieldType.INT
        items = vTypeList
        default_value = 2


class Blk039(BlkBase):
    bnum = 39
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


class Blk040(BlkBase):
    bnum = 40
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
        no_single_edit = True

# Blk050 - segment
# Blk051 - unoriented node
# Blk052 - oriented node

class Blk050(BlkBase):
    bnum = 50

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


class Blk051(BlkBase):
    bnum = 51
    class Flag(IntParam):
        name = 'Flag'
        prop = 'int1'

class Blk052(BlkBase):
    bnum = 52
    class Flag(IntParam):
        name = 'Flag'
        prop = 'int1'

#Preset definitions

class B40_TreeGenSimple(BlkBase):
    bnum = 40
    btype = 'tgs'
    class TreeMatIndex(IntParam):
        name = 'Tree Material'
        prop = 'int1'
        no_single_edit = True

    class LeafMatIndex(IntParam):
        name = 'Leaf Material'
        prop = 'int2'
        no_single_edit = True

class B40_TreeGenExtended(BlkBase):
    bnum = 40
    btype = 'tge'
    class TreeMatIndex(IntParam):
        name = 'Tree Material'
        prop = 'int1'
        no_single_edit = True

    class LeafMatIndex(IntParam):
        name = 'Leaf Material'
        prop = 'int2'
        no_single_edit = True
    
    class Unk_Float21(FloatParam):
        name = 'Unk. F1'
        prop = 'float1'
        no_single_edit = True
        
    class Unk_Coord21(CoordParam):
        name = 'Unk. C1'
        prop = 'coord1'
        no_single_edit = True
    
    class Unk_Float22(FloatParam):
        name = 'Unk. F2'
        prop = 'float2'
        no_single_edit = True
        
    class Unk_Coord22(CoordParam):
        name = 'Unk. C1'
        prop = 'coord2'
        no_single_edit = True
    