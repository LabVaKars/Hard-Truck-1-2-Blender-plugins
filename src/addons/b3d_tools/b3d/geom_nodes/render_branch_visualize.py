import bpy
from .get_tangent_point_xy import get_tangent_point_xy_node_group
from .circle_visualize import circle_visualize_node_group

#initialize render_branch_visualize node group
def render_branch_visualize_node_group():
    # get_tangent_point_xy = get_tangent_point_xy_node_group()
    circle_visualize = circle_visualize_node_group()

    render_branch_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Render_branch_visualize")

    

    #initialize render_branch_visualize nodes
    #node Angle_XYZ
    angle_xyz = render_branch_visualize.nodes.new("ShaderNodeSeparateXYZ")
    angle_xyz.label = "Angle_XYZ"
    angle_xyz.name = "Angle_XYZ"
    angle_xyz.hide = True

    #node Angle_Length
    angle_length = render_branch_visualize.nodes.new("ShaderNodeVectorMath")
    angle_length.label = "Angle_Length"
    angle_length.name = "Angle_Length"
    angle_length.hide = True
    angle_length.operation = 'LENGTH'

    #node Norm_X
    norm_x = render_branch_visualize.nodes.new("ShaderNodeMath")
    norm_x.label = "Norm_X"
    norm_x.name = "Norm_X"
    norm_x.hide = True
    norm_x.operation = 'DIVIDE'
    norm_x.use_clamp = False

    #node Norm_Y
    norm_y = render_branch_visualize.nodes.new("ShaderNodeMath")
    norm_y.label = "Norm_Y"
    norm_y.name = "Norm_Y"
    norm_y.hide = True
    norm_y.operation = 'DIVIDE'
    norm_y.use_clamp = False

    #node Norm_X.001
    norm_x_001 = render_branch_visualize.nodes.new("ShaderNodeMath")
    norm_x_001.label = "Angle"
    norm_x_001.name = "Norm_X.001"
    norm_x_001.hide = True
    norm_x_001.operation = 'ARCTAN2'
    norm_x_001.use_clamp = False

    #node Render_branch_vis_GO
    render_branch_vis_go = render_branch_visualize.nodes.new("NodeGroupOutput")
    render_branch_vis_go.name = "Render_branch_vis_GO"
    render_branch_vis_go.is_active_output = True
    #render_branch_visualize outputs
    #output Geometry
    render_branch_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    render_branch_visualize.outputs[0].attribute_domain = 'POINT'



    #node Circle_visualize_group
    circle_visualize_group = render_branch_visualize.nodes.new("GeometryNodeGroup")
    circle_visualize_group.name = "Circle_visualize_group"
    circle_visualize_group.node_tree = circle_visualize

    #node Render_branch_vis_GI
    render_branch_vis_gi = render_branch_visualize.nodes.new("NodeGroupInput")
    render_branch_vis_gi.name = "Render_branch_vis_GI"
    #render_branch_visualize inputs
    #input Tangent Angle
    render_branch_visualize.inputs.new('NodeSocketVector', "Tangent Angle")
    render_branch_visualize.inputs[0].attribute_domain = 'POINT'

    #input Circle Radius
    render_branch_visualize.inputs.new('NodeSocketFloat', "Circle Radius")
    render_branch_visualize.inputs[1].attribute_domain = 'POINT'

    #input Text Material
    render_branch_visualize.inputs.new('NodeSocketMaterial', "Text Material")
    render_branch_visualize.inputs[2].attribute_domain = 'POINT'

    #input Material A
    render_branch_visualize.inputs.new('NodeSocketMaterial', "Material A")
    render_branch_visualize.inputs[3].attribute_domain = 'POINT'

    #input Material B
    render_branch_visualize.inputs.new('NodeSocketMaterial', "Material B")
    render_branch_visualize.inputs[4].attribute_domain = 'POINT'





    #Set locations
    angle_xyz.location = (-280.0, -20.0)
    angle_length.location = (-280.0, -60.0)
    norm_x.location = (-120.0, -20.0)
    norm_y.location = (-120.0, -60.0)
    norm_x_001.location = (40.0, -20.0)
    render_branch_vis_go.location = (400.0, -20.0)
    circle_visualize_group.location = (220.0, -20.0)
    render_branch_vis_gi.location = (-480.0, -20.0)

    #initialize render_branch_visualize links
    #angle_xyz.X -> norm_x.Value
    render_branch_visualize.links.new(angle_xyz.outputs[0], norm_x.inputs[0])
    #angle_length.Value -> norm_x.Value
    render_branch_visualize.links.new(angle_length.outputs[1], norm_x.inputs[1])
    #angle_length.Value -> norm_y.Value
    render_branch_visualize.links.new(angle_length.outputs[1], norm_y.inputs[1])
    #angle_xyz.Y -> norm_y.Value
    render_branch_visualize.links.new(angle_xyz.outputs[1], norm_y.inputs[0])
    #render_branch_vis_gi.Tangent Angle -> angle_length.Vector
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[0], angle_length.inputs[0])
    #render_branch_vis_gi.Tangent Angle -> angle_xyz.Vector
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[0], angle_xyz.inputs[0])
    #circle_visualize_group.Geometry -> render_branch_vis_go.Geometry
    render_branch_visualize.links.new(circle_visualize_group.outputs[0], render_branch_vis_go.inputs[0])
    #render_branch_vis_gi.Circle Radius -> circle_visualize_group.Radius
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[1], circle_visualize_group.inputs[1])
    #render_branch_vis_gi.Text Material -> circle_visualize_group.Text Material
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[2], circle_visualize_group.inputs[2])
    #render_branch_vis_gi.Material A -> circle_visualize_group.Material 0
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[3], circle_visualize_group.inputs[3])
    #render_branch_vis_gi.Material B -> circle_visualize_group.Material 1
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[4], circle_visualize_group.inputs[4])
    #norm_x.Value -> norm_x_001.Value
    render_branch_visualize.links.new(norm_x.outputs[0], norm_x_001.inputs[1])
    #norm_y.Value -> norm_x_001.Value
    render_branch_visualize.links.new(norm_y.outputs[0], norm_x_001.inputs[0])
    #norm_x_001.Value -> circle_visualize_group.Angle
    render_branch_visualize.links.new(norm_x_001.outputs[0], circle_visualize_group.inputs[0])
    return render_branch_visualize
