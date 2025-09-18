import bpy

from .geom_nodes import (
    render_branch_visualize_node_group
)

from ..compatibility import (
    get_context_collection_objects,
    set_empty_type,
    set_empty_size
)

def get_render_branch_visualize_node_group():
    result = bpy.data.node_groups.get('Render_branch_visualize')
    if not result:
        result = render_branch_visualize_node_group()
    return result

def get_render_center_object():
    result = bpy.data.objects.get('Render_center')
    if not result:
        result = bpy.data.objects.new('Render_center', None)
        set_empty_type(result, 'SPHERE')
        set_empty_size(result, 50)
        get_context_collection_objects(bpy.context).link(result)
    return result


def create_color_material_node(mat_name, color):
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

    # for link in bsdf.inputs['Alpha'].links:
    #     new_mat.node_tree.nodes.remove(link.from_node)

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

    # for link in bsdf.inputs['Alpha'].links:
    #     new_mat.node_tree.nodes.remove(link.from_node)

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

def create_circle_center_rad_driver(src_obj, modif_name, input_index):
    modifier = src_obj.modifiers[modif_name]
    input_name = modifier.node_group.inputs[input_index].identifier
    d = modifier.driver_add('["{}"]'.format(input_name)).driver
    d.type = 'SCRIPTED'

    v1 = d.variables.new()
    v1.type = 'SINGLE_PROP'
    v1.name = 'empty_rad'
    v1.targets[0].id = get_render_center_object()
    v1.targets[0].data_path = 'empty_display_size'

    v2 = d.variables.new()
    v2.type = 'TRANSFORMS'
    v2.name = 'empty_scale'
    v2.targets[0].id = get_render_center_object()
    v2.targets[0].transform_type = 'SCALE_AVG'
    v2.targets[0].transform_space = 'WORLD_SPACE'

    d.expression =  'abs({}*{})'.format(v1.name, v2.name)

