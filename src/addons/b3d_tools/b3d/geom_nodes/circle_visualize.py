import bpy
from .pie_segment import pie_segment_node_group

#initialize circle_visualize node group
def circle_visualize_node_group():
    pie_segment = pie_segment_node_group()
    
    circle_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Circle_visualize")

    

    #initialize circle_visualize nodes
    #node Reroute
    reroute = circle_visualize.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    #node Rotate_90.001
    rotate_90_001 = circle_visualize.nodes.new("ShaderNodeMath")
    rotate_90_001.label = "PI/2"
    rotate_90_001.name = "Rotate_90.001"
    rotate_90_001.operation = 'RADIANS'
    rotate_90_001.use_clamp = False
    #Value
    rotate_90_001.inputs[0].default_value = 90.0

    #node Rotate_90
    rotate_90 = circle_visualize.nodes.new("ShaderNodeMath")
    rotate_90.label = "Rotate 90"
    rotate_90.name = "Rotate_90"
    rotate_90.operation = 'ADD'
    rotate_90.use_clamp = False

    #node Pie_segment_1
    pie_segment_1 = circle_visualize.nodes.new("GeometryNodeGroup")
    pie_segment_1.label = "Pie Segment"
    pie_segment_1.name = "Pie_segment_1"
    pie_segment_1.node_tree = pie_segment
    #Input_1
    pie_segment_1.inputs[1].default_value = "1"

    #node Join_pies
    join_pies = circle_visualize.nodes.new("GeometryNodeJoinGeometry")
    join_pies.label = "Join Pies"
    join_pies.name = "Join_pies"

    #node Pie_segment_0
    pie_segment_0 = circle_visualize.nodes.new("GeometryNodeGroup")
    pie_segment_0.label = "Pie Segment"
    pie_segment_0.name = "Pie_segment_0"
    pie_segment_0.node_tree = pie_segment
    #Input_1
    pie_segment_0.inputs[1].default_value = "0"

    #node Circle_visualize_GI.001
    circle_visualize_gi_001 = circle_visualize.nodes.new("NodeGroupOutput")
    circle_visualize_gi_001.label = "Group Output"
    circle_visualize_gi_001.name = "Circle_visualize_GI.001"
    circle_visualize_gi_001.is_active_output = True
    #circle_visualize outputs
    #output Geometry
    circle_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    circle_visualize.outputs[0].attribute_domain = 'POINT'



    #node Circle_visualize_GI
    circle_visualize_gi = circle_visualize.nodes.new("NodeGroupInput")
    circle_visualize_gi.label = "Group Input"
    circle_visualize_gi.name = "Circle_visualize_GI"
    #circle_visualize inputs
    #input Angle
    circle_visualize.inputs.new('NodeSocketFloat', "Angle")
    circle_visualize.inputs[0].attribute_domain = 'POINT'

    #input Radius
    circle_visualize.inputs.new('NodeSocketFloat', "Radius")
    circle_visualize.inputs[1].attribute_domain = 'POINT'

    #input Text Material
    circle_visualize.inputs.new('NodeSocketMaterial', "Text Material")
    circle_visualize.inputs[2].attribute_domain = 'POINT'

    #input Material 0
    circle_visualize.inputs.new('NodeSocketMaterial', "Material 0")
    circle_visualize.inputs[3].attribute_domain = 'POINT'

    #input Material 1
    circle_visualize.inputs.new('NodeSocketMaterial', "Material 1")
    circle_visualize.inputs[4].attribute_domain = 'POINT'





    #Set locations
    reroute.location = (-340.2493896484375, -282.7701416015625)
    rotate_90_001.location = (-560.0, 160.0)
    rotate_90.location = (-340.0, 160.0)
    pie_segment_1.location = (-160.0, 160.0)
    join_pies.location = (200.0, 0.0)
    pie_segment_0.location = (20.0, -80.0)
    circle_visualize_gi_001.location = (380.0, 0.0)
    circle_visualize_gi.location = (-570.9609375, 0.0)

    #initialize circle_visualize links
    #pie_segment_1.Curve -> join_pies.Geometry
    circle_visualize.links.new(pie_segment_1.outputs[0], join_pies.inputs[0])
    #pie_segment_0.Curve -> join_pies.Geometry
    circle_visualize.links.new(pie_segment_0.outputs[0], join_pies.inputs[0])
    #reroute.Output -> pie_segment_1.Text Material
    circle_visualize.links.new(reroute.outputs[0], pie_segment_1.inputs[4])
    #pie_segment_1.End -> pie_segment_0.Start
    circle_visualize.links.new(pie_segment_1.outputs[1], pie_segment_0.inputs[0])
    #reroute.Output -> pie_segment_0.Text Material
    circle_visualize.links.new(reroute.outputs[0], pie_segment_0.inputs[4])
    #circle_visualize_gi.Text Material -> reroute.Input
    circle_visualize.links.new(circle_visualize_gi.outputs[2], reroute.inputs[0])
    #circle_visualize_gi.Material 1 -> pie_segment_1.Segment Material
    circle_visualize.links.new(circle_visualize_gi.outputs[4], pie_segment_1.inputs[3])
    #circle_visualize_gi.Material 0 -> pie_segment_0.Segment Material
    circle_visualize.links.new(circle_visualize_gi.outputs[3], pie_segment_0.inputs[3])
    #circle_visualize_gi.Radius -> pie_segment_0.Radius
    circle_visualize.links.new(circle_visualize_gi.outputs[1], pie_segment_0.inputs[2])
    #circle_visualize_gi.Radius -> pie_segment_1.Radius
    circle_visualize.links.new(circle_visualize_gi.outputs[1], pie_segment_1.inputs[2])
    #join_pies.Geometry -> circle_visualize_gi_001.Geometry
    circle_visualize.links.new(join_pies.outputs[0], circle_visualize_gi_001.inputs[0])
    #circle_visualize_gi.Angle -> rotate_90.Value
    circle_visualize.links.new(circle_visualize_gi.outputs[0], rotate_90.inputs[0])
    #rotate_90.Value -> pie_segment_1.Start
    circle_visualize.links.new(rotate_90.outputs[0], pie_segment_1.inputs[0])
    #rotate_90_001.Value -> rotate_90.Value
    circle_visualize.links.new(rotate_90_001.outputs[0], rotate_90.inputs[1])
    return circle_visualize
