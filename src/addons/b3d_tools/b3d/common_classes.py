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

from ..compatibility import (
    make_annotations
)


@make_annotations
class BoolBlock(bpy.types.PropertyGroup):
    name = StringProperty()
    state = BoolProperty()


@make_annotations
class FloatBlock(bpy.types.PropertyGroup):
    value = FloatProperty()

    
_classes = [
    BoolBlock,
    FloatBlock
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in _classes[::-1]: #reversed
        bpy.utils.unregister_class(cls)