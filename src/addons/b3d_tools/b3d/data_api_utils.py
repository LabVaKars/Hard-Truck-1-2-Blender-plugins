import bpy

from .geom_nodes.render_branch_visualize import (render_branch_visualize_node_group)
from .geom_nodes.lod_branch_visualize import (lod_branch_visualize_node_group)

from ..compatibility import (
    get_context_collection_objects,
    set_empty_type,
    set_empty_size
)

from .class_descr import (
    Blk009
)

def get_lod_branch_visualize_node_group():
    result = bpy.data.node_groups.get('LOD_branch_visualize')
    if not result:
        result = lod_branch_visualize_node_group()
    return result

def get_render_branch_visualize_node_group():
    result = bpy.data.node_groups.get('Render_branch_visualize')
    if not result:
        result = render_branch_visualize_node_group()
    return result

def get_render_center_object(name, location, collection = None):
    rc_name = 'Render_center_{}'.format(name)
    result = bpy.data.objects.get(rc_name)
    if not result:
        result = bpy.data.objects.new(rc_name, None)
        result.location = location
        set_empty_type(result, 'SPHERE')
        set_empty_size(result, 30)
        if collection is None:
            get_context_collection_objects(bpy.context).link(result)
        else:
            collection.objects.link(result)
    return result


def create_color_material_node(mat_name, color, alpha=None):
    new_mat = bpy.data.materials.get(mat_name)
    if new_mat is None:
        new_mat = bpy.data.materials.new(name=mat_name)
    new_mat.use_nodes = True
        
    bsdf = new_mat.node_tree.nodes.get("Principled BSDF")
    if bsdf is None:
        bsdf = new_mat.node_tree.nodes.new("ShaderNodeBsdfPrincipled")

    mat_output = new_mat.node_tree.nodes.get("Material Output")
    if mat_output is None:
        mat_output = new_mat.node_tree.nodes.new("ShaderNodeOutputMaterial")

    new_mat.node_tree.links.new(bsdf.outputs['BSDF'], mat_output.inputs['Surface'])        

    for link in bsdf.inputs['Base Color'].links:
        new_mat.node_tree.nodes.remove(link.from_node)

    if alpha is not None:
        bsdf.inputs['Alpha'].default_value = alpha
        new_mat.blend_method = 'BLEND'
        new_mat.shadow_method = 'NONE'

    tex_color = new_mat.node_tree.nodes.new("ShaderNodeRGB")
    tex_color.outputs['Color'].default_value = color
    new_mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_color.outputs['Color'])


def create_image_material_node(mat_name, image_name):
    new_mat = bpy.data.materials.get(mat_name)
    if new_mat is None:
        new_mat = bpy.data.materials.new(name=mat_name)
    new_mat.use_nodes = True
        
    bsdf = new_mat.node_tree.nodes.get("Principled BSDF")
    if bsdf is None:
        bsdf = new_mat.node_tree.nodes.new("ShaderNodeBsdfPrincipled")

    mat_output = new_mat.node_tree.nodes.get("Material Output")
    if mat_output is None:
        mat_output = new_mat.node_tree.nodes.new("ShaderNodeOutputMaterial")

    new_mat.node_tree.links.new(bsdf.outputs['BSDF'], mat_output.inputs['Surface'])        

    for link in bsdf.inputs['Base Color'].links:
        new_mat.node_tree.nodes.remove(link.from_node)

    path = image_name
    tex_image = new_mat.node_tree.nodes.new("ShaderNodeTexImage")
    tex_image.image = bpy.data.images.get(path)
    new_mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])
    # new_mat.node_tree.links.new(bsdf.inputs['Alpha'], tex_image.outputs['Alpha'])


# ------------------------------------------------------------------------
#    drivers
# ------------------------------------------------------------------------
def create_center_driver(src_obj, edit_obj, pname):
    d = None
    for i in range(3):
        d = src_obj.driver_add('["{}"]'.format(pname), i).driver

        v = d.variables.new()
        v.name = 'location{}'.format(i)
        # v.targets[0].id_type = 'SCENE'
        # v.targets[0].id = bpy.context.scene
        # v.targets[0].data_path = 'my_tool.{}.{}[{}]'.format(bname, pname, i)
        v.targets[0].id = edit_obj
        v.targets[0].data_path = 'location[{}]'.format(i)

        d.expression = v.name

def create_rad_driver(src_obj, edit_obj, pname):
    d = src_obj.driver_add('["{}"]'.format(pname)).driver
    d.type = 'SCRIPTED'

    v1 = d.variables.new()
    v1.type = 'SINGLE_PROP'
    v1.name = 'empty_rad'
    v1.targets[0].id = edit_obj
    v1.targets[0].data_path = 'empty_display_size'

    v2 = d.variables.new()
    v2.type = 'TRANSFORMS'
    v2.name = 'empty_scale'
    v2.targets[0].id = edit_obj
    v2.targets[0].transform_type = 'SCALE_AVG'
    v2.targets[0].transform_space = 'WORLD_SPACE'

    d.expression =  'abs({}*{})'.format(v1.name, v2.name)

def create_circle_center_rad_driver(src_obj, modif_name, input_index, render_center_object):
    modifier = src_obj.modifiers[modif_name]
    input_name = modifier.node_group.inputs[input_index].identifier
    d = modifier.driver_add('["{}"]'.format(input_name)).driver
    d.type = 'SCRIPTED'

    v1 = d.variables.new()
    v1.type = 'SINGLE_PROP'
    v1.name = 'empty_rad'
    v1.targets[0].id = render_center_object
    v1.targets[0].data_path = 'empty_display_size'

    v2 = d.variables.new()
    v2.type = 'TRANSFORMS'
    v2.name = 'empty_scale'
    v2.targets[0].id = render_center_object
    v2.targets[0].transform_type = 'SCALE_AVG'
    v2.targets[0].transform_space = 'WORLD_SPACE'

    d.expression =  'abs({}*{})'.format(v1.name, v2.name)

def create_render_branch_drivers(src_obj, temp_obj, center_obj, shift_z):
    
    def set_variable(v, name, obj, pname):
        v.type = 'SINGLE_PROP'
        v.name = name
        v.targets[0].id = obj
        v.targets[0].data_path = pname

    temp_obj['eps'] = 1e-6

    drivers = {}

    temp_vars = ['r', 'dx', 'dy', 'Tx', 'Ty', 'Px', 'Py', 'wx', 'wy', 't']
    for var in temp_vars:
        if not temp_obj.get(var):
            temp_obj[var] = 0.0
            # temp_obj.id_properties_ui(var).update(min=float("inf"), max=float("-inf"))
        else:
            temp_obj.driver_remove('["{}"]'.format(var))
        drivers[var] = temp_obj.driver_add('["{}"]'.format(var)).driver
        drivers[var].type = 'SCRIPTED'

    # r driver
    d = drivers['r']
    v1 = d.variables.new()
    set_variable(v1, 'r', src_obj, '["{}"]'.format(Blk009.Unk_R.get_prop()))
    d.expression =  '-{}'.format(v1.name)

    d = drivers['dx']
    v1 = d.variables.new()
    set_variable(v1, 'ax', src_obj, '["{}"][0]'.format(Blk009.Unk_XYZ.get_prop()))
    v2 = d.variables.new()
    set_variable(v2, 'ay', src_obj, '["{}"][1]'.format(Blk009.Unk_XYZ.get_prop()))
    d.expression =  '{ax} / sqrt({ax}*{ax} + {ay}*{ay})'.format(ax=v1.name, ay=v2.name) 

    d = drivers['dy']
    v1 = d.variables.new()
    set_variable(v1, 'ax', src_obj, '["{}"][0]'.format(Blk009.Unk_XYZ.get_prop()))
    v2 = d.variables.new()
    set_variable(v2, 'ay', src_obj, '["{}"][1]'.format(Blk009.Unk_XYZ.get_prop()))
    d.expression =  '{ay} / sqrt({ax}*{ax} + {ay}*{ay})'.format(ax=v1.name, ay=v2.name) 

    d = drivers['Tx']
    v1 = d.variables.new()
    set_variable(v1, 'dy', temp_obj, '["{}"]'.format('dy'))
    v2 = d.variables.new()
    set_variable(v2, 'eps', temp_obj, '["{}"]'.format('eps'))
    d.expression =  '-{dy} + (fabs(-{dy})<{eps})*{eps}'.format(dy=v1.name, eps=v2.name) 

    d = drivers['Ty']
    v1 = d.variables.new()
    set_variable(v1, 'dx', temp_obj, '["{}"]'.format('dx'))
    v2 = d.variables.new()
    set_variable(v2, 'eps', temp_obj, '["{}"]'.format('eps'))
    d.expression =  '{dx} + (fabs({dx})<{eps})*{eps}'.format(dx=v1.name, eps=v2.name) 

    d = drivers['wx']
    v1 = d.variables.new()
    set_variable(v1, 'Tx', temp_obj, '["{}"]'.format('Tx'))
    v2 = d.variables.new()
    set_variable(v2, 'Ty', temp_obj, '["{}"]'.format('Ty'))
    d.expression =  'fabs({Tx}) / (fabs({Tx}) + fabs({Ty}))'.format(Tx=v1.name, Ty=v2.name) 

    d = drivers['wy']
    v1 = d.variables.new()
    set_variable(v1, 'Tx', temp_obj, '["{}"]'.format('Tx'))
    v2 = d.variables.new()
    set_variable(v2, 'Ty', temp_obj, '["{}"]'.format('Ty'))
    d.expression =  'fabs({Ty}) / (fabs({Tx}) + fabs({Ty}))'.format(Tx=v1.name, Ty=v2.name) 

    d = drivers['Px']
    v1 = d.variables.new()
    set_variable(v1, 'r', temp_obj, '["{}"]'.format('r'))
    v2 = d.variables.new()
    set_variable(v2, 'dx', temp_obj, '["{}"]'.format('dx'))
    d.expression =  '{}*{}'.format(v1.name, v2.name) 

    d = drivers['Py']
    v1 = d.variables.new()
    set_variable(v1, 'r', temp_obj, '["{}"]'.format('r'))
    v2 = d.variables.new()
    set_variable(v2, 'dy', temp_obj, '["{}"]'.format('dy'))
    d.expression =  '{}*{}'.format(v1.name, v2.name) 

    d = drivers['t']
    v1 = d.variables.new()
    set_variable(v1, 'cx', center_obj, '{}'.format('location.x'))
    v2 = d.variables.new()
    set_variable(v2, 'cy', center_obj, '{}'.format('location.y'))
    v3 = d.variables.new()
    set_variable(v3, 'Px', temp_obj, '["{}"]'.format('Px'))
    v4 = d.variables.new()
    set_variable(v4, 'Py', temp_obj, '["{}"]'.format('Py'))
    v5 = d.variables.new()
    set_variable(v5, 'Tx', temp_obj, '["{}"]'.format('Tx'))
    v6 = d.variables.new()
    set_variable(v6, 'Ty', temp_obj, '["{}"]'.format('Ty'))
    v7 = d.variables.new()
    set_variable(v7, 'wx', temp_obj, '["{}"]'.format('wx'))
    v8 = d.variables.new()
    set_variable(v8, 'wy', temp_obj, '["{}"]'.format('wy'))
    d.expression =  '(({cx} - {Px}) / {Tx}) * {wx} + (({cy} - {Py}) / {Ty}) * {wy}'.format(
        cx=v1.name, cy=v2.name,
        Px=v3.name, Py=v4.name,
        Tx=v5.name, Ty=v6.name,
        wx=v7.name, wy=v8.name
    ) 

    d = temp_obj.driver_add('delta_location', 0).driver
    d.type = 'SCRIPTED'
    v1 = d.variables.new()
    set_variable(v1, 'Px', temp_obj, '["{}"]'.format('Px'))
    v2 = d.variables.new()
    set_variable(v2, 'Tx', temp_obj, '["{}"]'.format('Tx'))
    v3 = d.variables.new()
    set_variable(v3, 't', temp_obj, '["{}"]'.format('t'))
    d.expression =  '{Px} + {Tx} * {t}'.format(Px=v1.name, Tx=v2.name, t=v3.name) 

    d = temp_obj.driver_add('delta_location', 1).driver
    d.type = 'SCRIPTED'
    v1 = d.variables.new()
    set_variable(v1, 'Py', temp_obj, '["{}"]'.format('Py'))
    v2 = d.variables.new()
    set_variable(v2, 'Ty', temp_obj, '["{}"]'.format('Ty'))
    v3 = d.variables.new()
    set_variable(v3, 't', temp_obj, '["{}"]'.format('t'))
    d.expression =  '{Py} + {Ty} * {t}'.format(Py=v1.name, Ty=v2.name, t=v3.name) 

    d = temp_obj.driver_add('delta_location', 2).driver
    d.type = 'SCRIPTED'
    v1 = d.variables.new()
    set_variable(v1, 'z', center_obj, '{}'.format('location.z'))
    d.expression =  '{}+{}'.format(v1.name, shift_z) 

    