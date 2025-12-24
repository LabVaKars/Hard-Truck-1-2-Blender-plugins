import bpy

from bpy.props import (
    StringProperty,
    BoolProperty,
    IntProperty,
    FloatProperty,
    EnumProperty,
    PointerProperty,
    FloatVectorProperty,
    CollectionProperty
)

from .common import (
    get_col_property_index_by_name,
    get_col_property_index,
    get_col_property_by_name,
    get_current_res_index,
    update_color_preview
)

from ..common import (
    get_panel_tool,
    get_res_modules
)

from ..compatibility import (
    make_annotations
)

def get_material_index_in_res(mat_name, res_module_name):
    res_modules = get_res_modules()
    cur_module = get_col_property_by_name(res_modules, res_module_name)
    cur_material_ind = get_col_property_index_by_name(cur_module.materials, mat_name, 'mat_name')
    if cur_material_ind == -1:
        cur_material_ind = 1
    return cur_material_ind

def get_current_res_module():
    res_modules = get_res_modules()
    res_module = None
    ind = get_current_res_index()
    if ind > -1:
        res_module = res_modules[ind]
    return res_module

def get_active_palette_module(res_module):
    res_modules = get_res_modules()
    if res_module:
        if len(res_module.palette_colors) > 0:
            return res_module

        common_res_module = get_col_property_by_name(res_modules, 'COMMON')
        if len(common_res_module.palette_colors) > 0:
            return common_res_module
    return None

def update_palette_index(self, context):

    mytool = get_panel_tool()
    if not mytool.is_importing:
        index = get_col_property_index(self)
        res_module = get_current_res_module()
        if res_module is not None:
            update_color_preview(res_module, index)

def get_image_index_in_module(field, image_name, col_name='id_value'):

    res_module = get_current_res_module()
    if res_module is not None:
        for i, t in enumerate(getattr(res_module, field)): #maskfiles, textures, materials
            id_value = getattr(t, col_name)
            if id_value and id_value.name == image_name:
                return i
        return -1

def callback_only_maskfiles(self, context):

    ind = get_current_res_index()
    if(ind > -1):
        return (get_image_index_in_module('maskfiles', context.name, 'id_msk') > -1)


def callback_only_materials(self, context):

    ind = get_current_res_index()
    if(ind > -1):
        return (get_image_index_in_module('materials', context.name, 'id_mat') > -1)


def callback_only_textures(self, context):

    ind = get_current_res_index()
    if(ind > -1):
        return (get_image_index_in_module('textures', context.name, 'id_tex') > -1)


def callback_only_colors(self, context):
    res_modules = get_res_modules()

    res_module = get_current_res_module()
    if res_module is not None:
        common_res_module = get_col_property_by_name(res_modules, 'COMMON')

        name_split = context.name.split('_')
        if len(name_split) != 3:
            return False
        ind = -1
        module = "COMMON"
        try:
            ind = int(name_split[2])
        except:
            return False
        max_ind = len(common_res_module.palette_colors)
        if len(res_module.palette_colors) > 0:
            module = res_module.value
            max_ind = len(res_module.palette_colors)

        return name_split[0] == 'col' and name_split[1] == module and ind <= max_ind


def set_tex_ind(self, context):
    index = get_image_index_in_module("textures", self.id_tex.name, 'id_tex')
    if index:
        self.tex = index + 1

def set_msk_ind(self, context):
    index = get_image_index_in_module("maskfiles", self.id_msk.name, 'id_msk')
    if index:
        self.msk = index + 1

def set_mat_ind(self, context):
    index = get_image_index_in_module("materials", self.id_att.name, 'id_mat')
    if index:
        self.att = index + 1

def set_col_ind(self, context):
    if self.id_col is not None:
        name_split = self.id_col.name.split('_')
    ind = 0
    try:
        ind = int(name_split[2])
    except:
        pass
    self.col = ind


@make_annotations
class PaletteColorBlock(bpy.types.PropertyGroup):
    value = FloatVectorProperty(
        name = 'Palette color',
        subtype = 'COLOR',
        default = (1, 1, 1, 1),
        size = 4,
        min = 0,
        max = 1,
        update = update_palette_index
    )

def on_msk_changed(self, context):
    if self.id_msk:
        self.msk_name = self.id_msk.name
    else:
        self.msk_name = ""

@make_annotations
class MaskfileBlock(bpy.types.PropertyGroup):
    subpath = StringProperty(default = "")
    msk_name = StringProperty(default = "")
    id_msk = PointerProperty(
        name='Image',
        type=bpy.types.Image,
        update=on_msk_changed
    )

    is_noload = BoolProperty(default=False)
    is_someint = BoolProperty(default=False)
    someint = IntProperty(default=0)

def on_tex_changed(self, context):
    if self.id_tex:
        self.tex_name = self.id_tex.name
    else:
        self.tex_name = ""

@make_annotations
class TextureBlock(bpy.types.PropertyGroup):
    subpath = StringProperty(default = "")
    tex_name = StringProperty(default = "")
    id_tex = PointerProperty(
        name='Image',
        type=bpy.types.Image,
        update=on_tex_changed
    )

    has_mipmap = BoolProperty(default=False)
    img_format = EnumProperty(
        name="Image color map",
        default = '0565',
        items=[
            ('0565', "ARGB(0565)", "Color without transparency"),
            ('4444', "ARGB(4444)", "Color with transparency(A)")
        ])

    img_type = EnumProperty(
        name="Image type",
        default='TIMG',
        items=[
            ('TIMG', "True-color image", "Store each pixel value"),
            ('CMAP', "Color mapped(palette) image", "Store indexes of palette")
        ]
    )

    is_memfix = BoolProperty(default=False)
    is_noload = BoolProperty(default=False)
    is_bumpcoord = BoolProperty(default=False)
    is_someint = BoolProperty(default=False)
    someint = IntProperty()

def on_mat_changed(self, context):
    if self.id_mat:
        self.mat_name = self.id_mat.name
    else:
        self.mat_name = ""

@make_annotations
class MaterialBlock(bpy.types.PropertyGroup):
    mat_name = StringProperty(default = "")
    id_mat = PointerProperty(
        name='Material',
        type=bpy.types.Material,
        update=on_mat_changed
    )

    is_reflect = BoolProperty(default=False)
    reflect = FloatProperty(default=0.0)

    is_specular = BoolProperty(default=False)
    specular = FloatProperty(default=0.0)

    is_transp = BoolProperty(default=False)
    transp = FloatProperty(default=0.0)

    is_rot = BoolProperty(default=False)
    rot = FloatProperty(default=0.0)

    is_col = BoolProperty(default=False)
    col_switch = BoolProperty(
        name = 'Use dropdown',
        description = 'Dropdown selection',
        default = True
    )
    id_col = PointerProperty(
        name='Colors',
        type=bpy.types.Image,
        poll=callback_only_colors,
        update=set_col_ind
    )
    col = IntProperty(default=0)

    is_tex = BoolProperty(default=False)
    tex_type = EnumProperty(
        name="Texture type",
        items=[
            ('tex', "Tex", "Tex"),
            ('ttx', "Ttx", "Ttx"),
            ('itx', "Itx", "Itx"),
        ])
    tex_switch = BoolProperty(
        name = 'Use dropdown',
        description = 'Dropdown selection',
        default = True
    )
    id_tex = PointerProperty(
        name='Texture',
        type=bpy.types.Image,
        poll=callback_only_textures,
        update=set_tex_ind
    )
    tex = IntProperty(default=0)

    is_att = BoolProperty(default=False)
    att_switch = BoolProperty(
        name = 'Use dropdown',
        description = 'Dropdown selection',
        default = True
    )
    id_att = PointerProperty(
        name='Material',
        type=bpy.types.Material,
        poll=callback_only_materials,
        update=set_mat_ind
    )
    att = IntProperty(default=0)

    is_msk = BoolProperty(default=False)
    msk_switch = BoolProperty(
        name = 'Use dropdown',
        description = 'Dropdown selection',
        default = True
    )
    id_msk = PointerProperty(
        name='Maskfile',
        type=bpy.types.Image,
        poll=callback_only_maskfiles,
        update=set_msk_ind
    )
    msk = IntProperty(default=0)

    is_power = BoolProperty(default=False)
    power = IntProperty(default=0)

    is_coord = BoolProperty(default=False)
    coord = IntProperty(default=0)

    is_envId = BoolProperty(default=False)
    envId = IntProperty(default=0)

    is_env = BoolProperty(default=False)
    env = FloatVectorProperty(default=(0.0, 0.0), size=2)

    is_RotPoint = BoolProperty(default=False)
    RotPoint = FloatVectorProperty(default=(0.0, 0.0), size=2)

    is_move = BoolProperty(default=False)
    move = FloatVectorProperty(default=(0.0, 0.0), size=2)

    is_noz = BoolProperty(default=False)
    is_nof = BoolProperty(default=False)
    is_notile = BoolProperty(default=False)
    is_notileu = BoolProperty(default=False)
    is_notilev = BoolProperty(default=False)
    is_alphamirr = BoolProperty(default=False)
    is_bumpcoord = BoolProperty(default=False)
    is_usecol = BoolProperty(default=False)
    is_wave = BoolProperty(default=False)

@make_annotations
class ResBlock(bpy.types.PropertyGroup):
    value = StringProperty()
    palette_subpath = StringProperty()
    palette_name = StringProperty()
    palette_colors = CollectionProperty(type=PaletteColorBlock)
    textures = CollectionProperty(type=TextureBlock)
    materials = CollectionProperty(type=MaterialBlock)
    maskfiles = CollectionProperty(type=MaskfileBlock)

@make_annotations
class ResSettings(bpy.types.PropertyGroup):
    res_modules = CollectionProperty(type=ResBlock)

_classes = [
    PaletteColorBlock,
    TextureBlock,
    MaskfileBlock,
    MaterialBlock,
    ResBlock
]

def register():

    for cls in _classes:
        bpy.utils.register_class(cls)
    bpy.utils.register_class(ResSettings)
    bpy.types.Scene.res_tool = bpy.props.PointerProperty(type=ResSettings)

def unregister():
    del bpy.types.Scene.res_tool
    bpy.utils.unregister_class(ResSettings)
    for cls in _classes[::-1]: #reversed
        bpy.utils.unregister_class(cls)
    
