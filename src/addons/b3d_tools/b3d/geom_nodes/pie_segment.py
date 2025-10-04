import bpy

#initialize pie_segment node group
def pie_segment_node_group():
    pie_segment = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Pie_segment")

    

    #initialize pie_segment nodes
    #node Pie_segment_GI
    pie_segment_gi = pie_segment.nodes.new("NodeGroupInput")
    pie_segment_gi.label = "Group Input"
    pie_segment_gi.name = "Pie_segment_GI"
    #pie_segment inputs
    #input Start
    pie_segment.inputs.new('NodeSocketFloat', "Start")
    pie_segment.inputs[0].attribute_domain = 'POINT'

    #input String
    pie_segment.inputs.new('NodeSocketString', "String")
    pie_segment.inputs[1].attribute_domain = 'POINT'

    #input Radius
    pie_segment.inputs.new('NodeSocketFloat', "Radius")
    pie_segment.inputs[2].attribute_domain = 'POINT'

    #input Segment Material
    pie_segment.inputs.new('NodeSocketMaterial', "Segment Material")
    pie_segment.inputs[3].attribute_domain = 'POINT'

    #input Text Material
    pie_segment.inputs.new('NodeSocketMaterial', "Text Material")
    pie_segment.inputs[4].attribute_domain = 'POINT'



    #node Abs_R
    abs_r = pie_segment.nodes.new("ShaderNodeMath")
    abs_r.label = "Abs(R)"
    abs_r.name = "Abs_R"
    abs_r.hide = True
    abs_r.operation = 'ABSOLUTE'
    abs_r.use_clamp = False

    #node Pi
    pi = pie_segment.nodes.new("ShaderNodeMath")
    pi.label = "PI"
    pi.name = "Pi"
    pi.hide = True
    pi.operation = 'RADIANS'
    pi.use_clamp = False
    #Value
    pi.inputs[0].default_value = 180.0

    #node Arc
    arc = pie_segment.nodes.new("GeometryNodeCurveArc")
    arc.name = "Arc"
    arc.hide = True
    arc.mode = 'RADIUS'
    #Resolution
    arc.inputs[0].default_value = 12
    #Connect Center
    arc.inputs[8].default_value = True
    #Invert Arc
    arc.inputs[9].default_value = False

    #node Fill_Arc
    fill_arc = pie_segment.nodes.new("GeometryNodeFillCurve")
    fill_arc.label = "Fill Arc"
    fill_arc.name = "Fill_Arc"
    fill_arc.hide = True
    fill_arc.mode = 'TRIANGLES'

    #node Start_plus_PI
    start_plus_pi = pie_segment.nodes.new("ShaderNodeMath")
    start_plus_pi.name = "Start_plus_PI"
    start_plus_pi.hide = True
    start_plus_pi.operation = 'ADD'
    start_plus_pi.use_clamp = False

    #node Extrude_Arc
    extrude_arc = pie_segment.nodes.new("GeometryNodeExtrudeMesh")
    extrude_arc.label = "Extrude Arc"
    extrude_arc.name = "Extrude_Arc"
    extrude_arc.hide = True
    extrude_arc.mode = 'FACES'
    #Selection
    extrude_arc.inputs[1].default_value = True
    #Offset
    extrude_arc.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Offset Scale
    extrude_arc.inputs[3].default_value = -0.10000000149011612
    #Individual
    extrude_arc.inputs[4].default_value = True

    #node Reroute.002
    reroute_002 = pie_segment.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    #node Extrude_Numbers
    extrude_numbers = pie_segment.nodes.new("GeometryNodeExtrudeMesh")
    extrude_numbers.label = "Extrude Numbers"
    extrude_numbers.name = "Extrude_Numbers"
    extrude_numbers.mode = 'FACES'
    #Selection
    extrude_numbers.inputs[1].default_value = True
    #Offset
    extrude_numbers.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Offset Scale
    extrude_numbers.inputs[3].default_value = 0.02500000037252903
    #Individual
    extrude_numbers.inputs[4].default_value = True

    #node Position_Numbers
    position_numbers = pie_segment.nodes.new("GeometryNodeSetPosition")
    position_numbers.label = "Position Numbers"
    position_numbers.name = "Position_Numbers"
    #Selection
    position_numbers.inputs[1].default_value = True
    #Position
    position_numbers.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Material_Numbers
    material_numbers = pie_segment.nodes.new("GeometryNodeSetMaterial")
    material_numbers.label = "Material Numbers"
    material_numbers.name = "Material_Numbers"
    #Selection
    material_numbers.inputs[1].default_value = True

    #node Material_Fill
    material_fill = pie_segment.nodes.new("GeometryNodeSetMaterial")
    material_fill.label = "Material Fill"
    material_fill.name = "Material_Fill"
    #Selection
    material_fill.inputs[1].default_value = True

    #node Join Geometry
    join_geometry = pie_segment.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Material_Extrude
    material_extrude = pie_segment.nodes.new("GeometryNodeSetMaterial")
    material_extrude.label = "Material Extrude"
    material_extrude.name = "Material_Extrude"
    #Selection
    material_extrude.inputs[1].default_value = True

    #node Fill_Numbers
    fill_numbers = pie_segment.nodes.new("GeometryNodeFillCurve")
    fill_numbers.label = "Fill Numbers"
    fill_numbers.name = "Fill_Numbers"
    fill_numbers.mode = 'TRIANGLES'

    #node String to Curves
    string_to_curves = pie_segment.nodes.new("GeometryNodeStringToCurves")
    string_to_curves.name = "String to Curves"
    string_to_curves.align_x = 'CENTER'
    string_to_curves.align_y = 'MIDDLE'
    string_to_curves.overflow = 'OVERFLOW'
    string_to_curves.pivot_mode = 'BOTTOM_LEFT'
    #Character Spacing
    string_to_curves.inputs[2].default_value = 1.0
    #Word Spacing
    string_to_curves.inputs[3].default_value = 1.0
    #Line Spacing
    string_to_curves.inputs[4].default_value = 1.0
    #Text Box Width
    string_to_curves.inputs[5].default_value = 0.0

    #node Attribute Statistic
    attribute_statistic = pie_segment.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.hide = True
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'FACE'
    #Selection
    attribute_statistic.inputs[1].default_value = True

    #node R_div_20
    r_div_20 = pie_segment.nodes.new("ShaderNodeMath")
    r_div_20.label = "R/20"
    r_div_20.name = "R_div_20"
    r_div_20.hide = True
    r_div_20.operation = 'DIVIDE'
    r_div_20.use_clamp = False
    #Value_001
    r_div_20.inputs[1].default_value = 1.5

    #node Pie_segment_GO
    pie_segment_go = pie_segment.nodes.new("NodeGroupOutput")
    pie_segment_go.label = "Group Output"
    pie_segment_go.name = "Pie_segment_GO"
    pie_segment_go.is_active_output = True
    #pie_segment outputs
    #output Curve
    pie_segment.outputs.new('NodeSocketGeometry', "Curve")
    pie_segment.outputs[0].attribute_domain = 'POINT'

    #output End
    pie_segment.outputs.new('NodeSocketFloat', "End")
    pie_segment.outputs[1].attribute_domain = 'POINT'



    #node Position
    position = pie_segment.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"



    #Set locations
    pie_segment_gi.location = (-400.0, 80.0)
    abs_r.location = (-200.0, 120.0)
    pi.location = (-400.0, -120.0)
    arc.location = (20.0, 120.0)
    fill_arc.location = (200.0, 120.0)
    start_plus_pi.location = (-120.0, -120.0)
    extrude_arc.location = (580.0, 100.0)
    reroute_002.location = (640.0, -20.0)
    extrude_numbers.location = (500.0, 560.0)
    position_numbers.location = (700.0, 440.0)
    material_numbers.location = (900.0, 380.0)
    material_fill.location = (900.0, 240.0)
    join_geometry.location = (1160.0, 220.0)
    material_extrude.location = (900.0, 80.0)
    fill_numbers.location = (340.0, 560.0)
    string_to_curves.location = (120.0, 620.0)
    attribute_statistic.location = (500.0, 200.0)
    r_div_20.location = (-40.0, 220.0)
    pie_segment_go.location = (1320.0, -40.0)
    position.location = (160.0, 220.0)

    #initialize pie_segment links
    #pi.Value -> arc.Sweep Angle
    pie_segment.links.new(pi.outputs[0], arc.inputs[6])
    #pi.Value -> start_plus_pi.Value
    pie_segment.links.new(pi.outputs[0], start_plus_pi.inputs[0])
    #pie_segment_gi.Start -> start_plus_pi.Value
    pie_segment.links.new(pie_segment_gi.outputs[0], start_plus_pi.inputs[1])
    #start_plus_pi.Value -> pie_segment_go.End
    pie_segment.links.new(start_plus_pi.outputs[0], pie_segment_go.inputs[1])
    #pie_segment_gi.Start -> arc.Start Angle
    pie_segment.links.new(pie_segment_gi.outputs[0], arc.inputs[5])
    #material_extrude.Geometry -> join_geometry.Geometry
    pie_segment.links.new(material_extrude.outputs[0], join_geometry.inputs[0])
    #material_numbers.Geometry -> join_geometry.Geometry
    pie_segment.links.new(material_numbers.outputs[0], join_geometry.inputs[0])
    #arc.Curve -> fill_arc.Curve
    pie_segment.links.new(arc.outputs[0], fill_arc.inputs[0])
    #string_to_curves.Curve Instances -> fill_numbers.Curve
    pie_segment.links.new(string_to_curves.outputs[0], fill_numbers.inputs[0])
    #fill_arc.Mesh -> extrude_arc.Mesh
    pie_segment.links.new(fill_arc.outputs[0], extrude_arc.inputs[0])
    #material_fill.Geometry -> join_geometry.Geometry
    pie_segment.links.new(material_fill.outputs[0], join_geometry.inputs[0])
    #fill_numbers.Mesh -> extrude_numbers.Mesh
    pie_segment.links.new(fill_numbers.outputs[0], extrude_numbers.inputs[0])
    #extrude_numbers.Mesh -> position_numbers.Geometry
    pie_segment.links.new(extrude_numbers.outputs[0], position_numbers.inputs[0])
    #position_numbers.Geometry -> material_numbers.Geometry
    pie_segment.links.new(position_numbers.outputs[0], material_numbers.inputs[0])
    #extrude_arc.Mesh -> material_extrude.Geometry
    pie_segment.links.new(extrude_arc.outputs[0], material_extrude.inputs[0])
    #pie_segment_gi.Text Material -> material_numbers.Material
    pie_segment.links.new(pie_segment_gi.outputs[4], material_numbers.inputs[2])
    #reroute_002.Output -> material_extrude.Material
    pie_segment.links.new(reroute_002.outputs[0], material_extrude.inputs[2])
    #pie_segment_gi.Segment Material -> reroute_002.Input
    pie_segment.links.new(pie_segment_gi.outputs[3], reroute_002.inputs[0])
    #reroute_002.Output -> material_fill.Material
    pie_segment.links.new(reroute_002.outputs[0], material_fill.inputs[2])
    #pie_segment_gi.String -> string_to_curves.String
    pie_segment.links.new(pie_segment_gi.outputs[1], string_to_curves.inputs[0])
    #r_div_20.Value -> string_to_curves.Size
    pie_segment.links.new(r_div_20.outputs[0], string_to_curves.inputs[1])
    #pie_segment_gi.Radius -> abs_r.Value
    pie_segment.links.new(pie_segment_gi.outputs[2], abs_r.inputs[0])
    #abs_r.Value -> r_div_20.Value
    pie_segment.links.new(abs_r.outputs[0], r_div_20.inputs[0])
    #abs_r.Value -> arc.Radius
    pie_segment.links.new(abs_r.outputs[0], arc.inputs[4])
    #position.Position -> attribute_statistic.Attribute
    pie_segment.links.new(position.outputs[0], attribute_statistic.inputs[2])
    #position.Position -> attribute_statistic.Attribute
    pie_segment.links.new(position.outputs[0], attribute_statistic.inputs[3])
    #fill_arc.Mesh -> attribute_statistic.Geometry
    pie_segment.links.new(fill_arc.outputs[0], attribute_statistic.inputs[0])
    #attribute_statistic.Mean -> position_numbers.Offset
    pie_segment.links.new(attribute_statistic.outputs[8], position_numbers.inputs[3])
    #fill_arc.Mesh -> material_fill.Geometry
    pie_segment.links.new(fill_arc.outputs[0], material_fill.inputs[0])
    #join_geometry.Geometry -> pie_segment_go.Curve
    pie_segment.links.new(join_geometry.outputs[0], pie_segment_go.inputs[0])
    return pie_segment
