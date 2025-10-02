import bpy
from .get_tangent_point_xy import get_tangent_point_xy_node_group
from .circle_visualize import circle_visualize_node_group

#initialize render_branch_visualize node group
def render_branch_visualize_node_group():
    get_tangent_point_xy = get_tangent_point_xy_node_group()
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

    #node Render_Center_Into
    render_center_into = render_branch_visualize.nodes.new("GeometryNodeObjectInfo")
    render_center_into.name = "Render_Center_Into"
    render_center_into.hide = True
    render_center_into.transform_space = 'ORIGINAL'
    #As Instance
    render_center_into.inputs[1].default_value = False

    #node RC_Position
    rc_position = render_branch_visualize.nodes.new("ShaderNodeSeparateXYZ")
    rc_position.label = "cx,cy,cz"
    rc_position.name = "RC_Position"
    rc_position.hide = True

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

    #node Norm_Z
    norm_z = render_branch_visualize.nodes.new("ShaderNodeMath")
    norm_z.label = "Norm_Z"
    norm_z.name = "Norm_Z"
    norm_z.hide = True
    norm_z.operation = 'DIVIDE'
    norm_z.use_clamp = False

    #node Norm_R
    norm_r = render_branch_visualize.nodes.new("ShaderNodeMath")
    norm_r.label = "Norm_R"
    norm_r.name = "Norm_R"
    norm_r.hide = True
    norm_r.operation = 'DIVIDE'
    norm_r.use_clamp = False

    #node Shift_Z
    shift_z = render_branch_visualize.nodes.new("ShaderNodeMath")
    shift_z.label = "Shift_Z"
    shift_z.name = "Shift_Z"
    shift_z.hide = True
    shift_z.operation = 'ADD'
    shift_z.use_clamp = False

    #node eps
    eps = render_branch_visualize.nodes.new("ShaderNodeValue")
    eps.label = "eps"
    eps.name = "eps"
    eps.hide = True

    eps.outputs[0].default_value = 9.999999960041972e-13
    #node MinusR
    minusr = render_branch_visualize.nodes.new("ShaderNodeMath")
    minusr.label = "-R"
    minusr.name = "MinusR"
    minusr.hide = True
    minusr.operation = 'MULTIPLY'
    minusr.use_clamp = False
    #Value_001
    minusr.inputs[1].default_value = -1.0

    #node get_tangent_point_group
    get_tangent_point_group = render_branch_visualize.nodes.new("GeometryNodeGroup")
    get_tangent_point_group.name = "get_tangent_point_group"
    get_tangent_point_group.node_tree = get_tangent_point_xy

    #node Circle_visualize_group
    circle_visualize_group = render_branch_visualize.nodes.new("GeometryNodeGroup")
    circle_visualize_group.name = "Circle_visualize_group"
    circle_visualize_group.node_tree = circle_visualize

    #node Render_branch_vis_GO
    render_branch_vis_go = render_branch_visualize.nodes.new("NodeGroupOutput")
    render_branch_vis_go.name = "Render_branch_vis_GO"
    render_branch_vis_go.is_active_output = True
    #render_branch_visualize outputs
    #output Geometry
    render_branch_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    render_branch_visualize.outputs[0].attribute_domain = 'POINT'



    #node Render_branch_vis_GI
    render_branch_vis_gi = render_branch_visualize.nodes.new("NodeGroupInput")
    render_branch_vis_gi.name = "Render_branch_vis_GI"
    #render_branch_visualize inputs
    #input Tangent Angle
    render_branch_visualize.inputs.new('NodeSocketVector', "Tangent Angle")
    render_branch_visualize.inputs[0].attribute_domain = 'POINT'

    #input Tangent Radius
    render_branch_visualize.inputs.new('NodeSocketFloat', "Tangent Radius")
    render_branch_visualize.inputs[1].attribute_domain = 'POINT'

    #input Shift Z
    render_branch_visualize.inputs.new('NodeSocketFloat', "Shift Z")
    render_branch_visualize.inputs[2].attribute_domain = 'POINT'

    #input Render Center
    render_branch_visualize.inputs.new('NodeSocketObject', "Render Center")
    render_branch_visualize.inputs[3].attribute_domain = 'POINT'

    #input Circle Radius
    render_branch_visualize.inputs.new('NodeSocketFloat', "Circle Radius")
    render_branch_visualize.inputs[4].attribute_domain = 'POINT'

    #input Text Material
    render_branch_visualize.inputs.new('NodeSocketMaterial', "Text Material")
    render_branch_visualize.inputs[5].attribute_domain = 'POINT'

    #input Material A
    render_branch_visualize.inputs.new('NodeSocketMaterial', "Material A")
    render_branch_visualize.inputs[6].attribute_domain = 'POINT'

    #input Material B
    render_branch_visualize.inputs.new('NodeSocketMaterial', "Material B")
    render_branch_visualize.inputs[7].attribute_domain = 'POINT'





    #Set locations
    angle_xyz.location = (-413.8541564941406, 206.00833129882812)
    angle_length.location = (-411.7771301269531, 152.63455200195312)
    render_center_into.location = (-423.79144287109375, -44.29651641845703)
    rc_position.location = (-421.10443115234375, 4.136842727661133)
    norm_x.location = (-219.10365295410156, 208.31396484375)
    norm_y.location = (-219.10365295410156, 165.54180908203125)
    norm_z.location = (-218.03614807128906, 117.42318725585938)
    norm_r.location = (-216.95651245117188, 68.70800018310547)
    shift_z.location = (-224.37274169921875, 15.625839233398438)
    eps.location = (-227.41383361816406, -48.059120178222656)
    minusr.location = (-429.8410949707031, 65.2533950805664)
    get_tangent_point_group.location = (-18.656234741210938, 163.33322143554688)
    circle_visualize_group.location = (222.2908172607422, 9.503557205200195)
    render_branch_vis_go.location = (510.9173278808594, -5.075558662414551)
    render_branch_vis_gi.location = (-652.7306518554688, 0.0)

    #initialize render_branch_visualize links
    #rc_position.Y -> get_tangent_point_group.py
    render_branch_visualize.links.new(rc_position.outputs[1], get_tangent_point_group.inputs[5])
    #rc_position.X -> get_tangent_point_group.px
    render_branch_visualize.links.new(rc_position.outputs[0], get_tangent_point_group.inputs[4])
    #norm_x.Value -> get_tangent_point_group.X
    render_branch_visualize.links.new(norm_x.outputs[0], get_tangent_point_group.inputs[0])
    #get_tangent_point_group.Angle_rad -> circle_visualize_group.Angle
    render_branch_visualize.links.new(get_tangent_point_group.outputs[1], circle_visualize_group.inputs[1])
    #norm_r.Value -> get_tangent_point_group.R
    render_branch_visualize.links.new(norm_r.outputs[0], get_tangent_point_group.inputs[3])
    #eps.Value -> get_tangent_point_group.eps
    render_branch_visualize.links.new(eps.outputs[0], get_tangent_point_group.inputs[6])
    #angle_xyz.Z -> norm_z.Value
    render_branch_visualize.links.new(angle_xyz.outputs[2], norm_z.inputs[0])
    #angle_xyz.X -> norm_x.Value
    render_branch_visualize.links.new(angle_xyz.outputs[0], norm_x.inputs[0])
    #angle_length.Value -> norm_x.Value
    render_branch_visualize.links.new(angle_length.outputs[1], norm_x.inputs[1])
    #minusr.Value -> norm_r.Value
    render_branch_visualize.links.new(minusr.outputs[0], norm_r.inputs[0])
    #render_center_into.Location -> rc_position.Vector
    render_branch_visualize.links.new(render_center_into.outputs[0], rc_position.inputs[0])
    #angle_length.Value -> norm_y.Value
    render_branch_visualize.links.new(angle_length.outputs[1], norm_y.inputs[1])
    #angle_length.Value -> norm_z.Value
    render_branch_visualize.links.new(angle_length.outputs[1], norm_z.inputs[1])
    #angle_xyz.Y -> norm_y.Value
    render_branch_visualize.links.new(angle_xyz.outputs[1], norm_y.inputs[0])
    #norm_y.Value -> get_tangent_point_group.Y
    render_branch_visualize.links.new(norm_y.outputs[0], get_tangent_point_group.inputs[1])
    #angle_length.Value -> norm_r.Value
    render_branch_visualize.links.new(angle_length.outputs[1], norm_r.inputs[1])
    #get_tangent_point_group.P -> circle_visualize_group.Position
    render_branch_visualize.links.new(get_tangent_point_group.outputs[0], circle_visualize_group.inputs[0])
    #render_branch_vis_gi.Tangent Radius -> minusr.Value
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[1], minusr.inputs[0])
    #render_branch_vis_gi.Tangent Angle -> angle_length.Vector
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[0], angle_length.inputs[0])
    #render_branch_vis_gi.Tangent Angle -> angle_xyz.Vector
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[0], angle_xyz.inputs[0])
    #circle_visualize_group.Geometry -> render_branch_vis_go.Geometry
    render_branch_visualize.links.new(circle_visualize_group.outputs[0], render_branch_vis_go.inputs[0])
    #render_branch_vis_gi.Render Center -> render_center_into.Object
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[3], render_center_into.inputs[0])
    #render_branch_vis_gi.Circle Radius -> circle_visualize_group.Radius
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[4], circle_visualize_group.inputs[2])
    #render_branch_vis_gi.Text Material -> circle_visualize_group.Text Material
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[5], circle_visualize_group.inputs[3])
    #render_branch_vis_gi.Material A -> circle_visualize_group.Material 0
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[6], circle_visualize_group.inputs[4])
    #render_branch_vis_gi.Material B -> circle_visualize_group.Material 1
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[7], circle_visualize_group.inputs[5])
    #rc_position.Z -> shift_z.Value
    render_branch_visualize.links.new(rc_position.outputs[2], shift_z.inputs[0])
    #render_branch_vis_gi.Shift Z -> shift_z.Value
    render_branch_visualize.links.new(render_branch_vis_gi.outputs[2], shift_z.inputs[1])
    #shift_z.Value -> get_tangent_point_group.Z
    render_branch_visualize.links.new(shift_z.outputs[0], get_tangent_point_group.inputs[2])
    return render_branch_visualize
