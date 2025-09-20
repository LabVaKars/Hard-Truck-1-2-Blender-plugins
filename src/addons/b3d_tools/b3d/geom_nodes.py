import bpy 


#initialize get_tangent_point_xy node group
def get_tangent_point_xy_node_group():
    get_tangent_point_xy = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "get_tangent_point_xy")

    

    #initialize get_tangent_point_xy nodes
    #node Math.004
    math_004 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_004.label = "Ty"
    math_004.name = "Math.004"
    math_004.hide = True
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    #Value_001
    math_004.inputs[1].default_value = 1.0

    #node Math.005
    math_005 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_005.label = "Tx"
    math_005.name = "Math.005"
    math_005.hide = True
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    #Value_001
    math_005.inputs[1].default_value = -1.0

    #node Math.045
    math_045 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_045.label = "Py"
    math_045.name = "Math.045"
    math_045.hide = True
    math_045.operation = 'MULTIPLY'
    math_045.use_clamp = False

    #node Math.001
    math_001 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_001.label = "Abs(Ty)"
    math_001.name = "Math.001"
    math_001.hide = True
    math_001.operation = 'ABSOLUTE'
    math_001.use_clamp = False

    #node Math
    math = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math.label = "Abs(Tx)"
    math.name = "Math"
    math.hide = True
    math.operation = 'ABSOLUTE'
    math.use_clamp = False

    #node Math.011
    math_011 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_011.label = "Ty*t"
    math_011.name = "Math.011"
    math_011.hide = True
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False

    #node Math.008
    math_008 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_008.label = "t1 = (x-Px) / Tx"
    math_008.name = "Math.008"
    math_008.hide = True
    math_008.operation = 'DIVIDE'
    math_008.use_clamp = False

    #node Compare.001
    compare_001 = get_tangent_point_xy.nodes.new("FunctionNodeCompare")
    compare_001.label = "abs(Tx) < eps"
    compare_001.name = "Compare.001"
    compare_001.hide = True
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'LESS_THAN'

    #node Compare.002
    compare_002 = get_tangent_point_xy.nodes.new("FunctionNodeCompare")
    compare_002.label = "abs(Ty) < eps"
    compare_002.name = "Compare.002"
    compare_002.hide = True
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'LESS_THAN'

    #node Math.009
    math_009 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_009.label = "t2 = (y-Py) / Ty"
    math_009.name = "Math.009"
    math_009.hide = True
    math_009.operation = 'DIVIDE'
    math_009.use_clamp = False

    #node Math.010
    math_010 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_010.label = "Tx*t"
    math_010.name = "Math.010"
    math_010.hide = True
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False

    #node Math.012
    math_012 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_012.label = "Px + Tx*t"
    math_012.name = "Math.012"
    math_012.hide = True
    math_012.operation = 'ADD'
    math_012.use_clamp = False

    #node Math.013
    math_013 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_013.label = "Py + Ty*t"
    math_013.name = "Math.013"
    math_013.hide = True
    math_013.operation = 'ADD'
    math_013.use_clamp = False

    #node Math.023
    math_023 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_023.label = "Px"
    math_023.name = "Math.023"
    math_023.hide = True
    math_023.operation = 'MULTIPLY'
    math_023.use_clamp = False

    #node Switch.002
    switch_002 = get_tangent_point_xy.nodes.new("GeometryNodeSwitch")
    switch_002.label = "switch_t"
    switch_002.name = "Switch.002"
    switch_002.hide = True
    switch_002.input_type = 'FLOAT'

    #node Math.044
    math_044 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_044.label = "dy"
    math_044.name = "Math.044"
    math_044.hide = True
    math_044.operation = 'DIVIDE'
    math_044.use_clamp = False

    #node Math.022
    math_022 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_022.label = "dx"
    math_022.name = "Math.022"
    math_022.hide = True
    math_022.operation = 'DIVIDE'
    math_022.use_clamp = False

    #node Math.003
    math_003 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_003.label = "dy_"
    math_003.name = "Math.003"
    math_003.hide = True
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = 1.0

    #node Math.002
    math_002 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_002.label = "dx_"
    math_002.name = "Math.002"
    math_002.hide = True
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    #Value_001
    math_002.inputs[1].default_value = 1.0

    #node Group Input.001
    group_input_001 = get_tangent_point_xy.nodes.new("NodeGroupInput")
    group_input_001.label = "eps"
    group_input_001.name = "Group Input.001"
    #get_tangent_point_xy inputs
    #input X
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "X")
    get_tangent_point_xy.inputs[0].attribute_domain = 'POINT'

    #input Y
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "Y")
    get_tangent_point_xy.inputs[1].attribute_domain = 'POINT'

    #input Z
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "Z")
    get_tangent_point_xy.inputs[2].attribute_domain = 'POINT'

    #input R
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "R")
    get_tangent_point_xy.inputs[3].attribute_domain = 'POINT'

    #input px
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "px")
    get_tangent_point_xy.inputs[4].attribute_domain = 'POINT'

    #input py
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "py")
    get_tangent_point_xy.inputs[5].attribute_domain = 'POINT'

    #input eps
    get_tangent_point_xy.inputs.new('NodeSocketFloat', "eps")
    get_tangent_point_xy.inputs[6].attribute_domain = 'POINT'



    #node Compare
    compare = get_tangent_point_xy.nodes.new("FunctionNodeCompare")
    compare.label = "abs(Tx) >= abs(Ty)"
    compare.name = "Compare"
    compare.hide = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'GREATER_EQUAL'

    #node Combine XYZ.003
    combine_xyz_003 = get_tangent_point_xy.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.hide = True
    #Z
    combine_xyz_003.inputs[2].default_value = 0.0

    #node Math.006
    math_006 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_006.label = "x-Px"
    math_006.name = "Math.006"
    math_006.hide = True
    math_006.operation = 'SUBTRACT'
    math_006.use_clamp = False

    #node Switch.005
    switch_005 = get_tangent_point_xy.nodes.new("GeometryNodeSwitch")
    switch_005.label = "sTy"
    switch_005.name = "Switch.005"
    switch_005.hide = True
    switch_005.input_type = 'FLOAT'
    #True
    switch_005.inputs[3].default_value = 1.0

    #node Switch.004
    switch_004 = get_tangent_point_xy.nodes.new("GeometryNodeSwitch")
    switch_004.label = "sTx"
    switch_004.name = "Switch.004"
    switch_004.hide = True
    switch_004.input_type = 'FLOAT'
    #True
    switch_004.inputs[3].default_value = 1.0

    #node Math.007
    math_007 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_007.label = "y-Py"
    math_007.name = "Math.007"
    math_007.hide = True
    math_007.operation = 'SUBTRACT'
    math_007.use_clamp = False

    #node Vector Math
    vector_math = get_tangent_point_xy.nodes.new("ShaderNodeVectorMath")
    vector_math.label = "length"
    vector_math.name = "Vector Math"
    vector_math.hide = True
    vector_math.operation = 'DISTANCE'
    #Vector_001
    vector_math.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Combine XYZ.004
    combine_xyz_004 = get_tangent_point_xy.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.label = "P"
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.hide = True

    #node Math.014
    math_014 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    math_014.label = "Angle"
    math_014.name = "Math.014"
    math_014.hide = True
    math_014.operation = 'ARCTAN2'
    math_014.use_clamp = False

    #node Group Output
    group_output = get_tangent_point_xy.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    #get_tangent_point_xy outputs
    #output P
    get_tangent_point_xy.outputs.new('NodeSocketVectorXYZ', "P")
    get_tangent_point_xy.outputs[0].attribute_domain = 'POINT'

    #output Angle_rad
    get_tangent_point_xy.outputs.new('NodeSocketFloat', "Angle_rad")
    get_tangent_point_xy.outputs[1].attribute_domain = 'POINT'





    #Set locations
    math_004.location = (-1621.9293212890625, -129.15904235839844)
    math_005.location = (-1624.0460205078125, -79.62294006347656)
    math_045.location = (-1618.655517578125, -233.82467651367188)
    math_001.location = (-1434.609130859375, -305.6598205566406)
    math.location = (-1432.6092529296875, -256.81280517578125)
    math_011.location = (-351.10443115234375, 61.246604919433594)
    math_008.location = (-782.0009155273438, 130.10182189941406)
    compare_001.location = (-1164.778564453125, 349.5951232910156)
    compare_002.location = (-1159.44677734375, 297.7275390625)
    math_009.location = (-780.565673828125, 67.53253936767578)
    math_010.location = (-354.04443359375, 132.81881713867188)
    math_012.location = (-165.53045654296875, 131.01614379882812)
    math_013.location = (-170.2501220703125, 66.63573455810547)
    math_023.location = (-1619.9881591796875, -187.0582275390625)
    switch_002.location = (-573.0861206054688, -18.686120986938477)
    math_044.location = (-1836.9747314453125, 168.88699340820312)
    math_022.location = (-1839.1451416015625, 213.9760284423828)
    math_003.location = (-2252.601806640625, 78.76036071777344)
    math_002.location = (-2254.718505859375, 128.2964630126953)
    group_input_001.location = (-2449.834716796875, 83.74897766113281)
    compare.location = (-793.8845825195312, -122.5412826538086)
    combine_xyz_003.location = (-2071.47802734375, -79.78509521484375)
    math_006.location = (-980.0999755859375, 226.00155639648438)
    switch_005.location = (-985.5628662109375, 176.93887329101562)
    switch_004.location = (-982.9664306640625, 271.38482666015625)
    math_007.location = (-985.4927978515625, 133.63079833984375)
    vector_math.location = (-2067.8818359375, -132.85516357421875)
    combine_xyz_004.location = (39.724769592285156, 125.01004791259766)
    math_014.location = (-1817.9239501953125, 5.013556480407715)
    group_output.location = (262.1426086425781, 105.40538787841797)

    #initialize get_tangent_point_xy links
    #group_input_001.X -> math_002.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[0], math_002.inputs[0])
    #group_input_001.Y -> math_003.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[1], math_003.inputs[0])
    #math_002.Value -> combine_xyz_003.X
    get_tangent_point_xy.links.new(math_002.outputs[0], combine_xyz_003.inputs[0])
    #math_003.Value -> combine_xyz_003.Y
    get_tangent_point_xy.links.new(math_003.outputs[0], combine_xyz_003.inputs[1])
    #combine_xyz_003.Vector -> vector_math.Vector
    get_tangent_point_xy.links.new(combine_xyz_003.outputs[0], vector_math.inputs[0])
    #math_002.Value -> math_022.Value
    get_tangent_point_xy.links.new(math_002.outputs[0], math_022.inputs[0])
    #vector_math.Value -> math_022.Value
    get_tangent_point_xy.links.new(vector_math.outputs[1], math_022.inputs[1])
    #math_003.Value -> math_044.Value
    get_tangent_point_xy.links.new(math_003.outputs[0], math_044.inputs[0])
    #vector_math.Value -> math_044.Value
    get_tangent_point_xy.links.new(vector_math.outputs[1], math_044.inputs[1])
    #math_022.Value -> math_023.Value
    get_tangent_point_xy.links.new(math_022.outputs[0], math_023.inputs[0])
    #group_input_001.R -> math_023.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[3], math_023.inputs[1])
    #math_044.Value -> math_045.Value
    get_tangent_point_xy.links.new(math_044.outputs[0], math_045.inputs[0])
    #group_input_001.R -> math_045.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[3], math_045.inputs[1])
    #math_022.Value -> math_004.Value
    get_tangent_point_xy.links.new(math_022.outputs[0], math_004.inputs[0])
    #math_044.Value -> math_005.Value
    get_tangent_point_xy.links.new(math_044.outputs[0], math_005.inputs[0])
    #math_005.Value -> math.Value
    get_tangent_point_xy.links.new(math_005.outputs[0], math.inputs[0])
    #math_004.Value -> math_001.Value
    get_tangent_point_xy.links.new(math_004.outputs[0], math_001.inputs[0])
    #math.Value -> compare.A
    get_tangent_point_xy.links.new(math.outputs[0], compare.inputs[0])
    #math_001.Value -> compare.B
    get_tangent_point_xy.links.new(math_001.outputs[0], compare.inputs[1])
    #compare.Result -> switch_002.Switch
    get_tangent_point_xy.links.new(compare.outputs[0], switch_002.inputs[0])
    #group_input_001.eps -> compare_001.B
    get_tangent_point_xy.links.new(group_input_001.outputs[6], compare_001.inputs[1])
    #math.Value -> compare_001.A
    get_tangent_point_xy.links.new(math.outputs[0], compare_001.inputs[0])
    #compare_001.Result -> switch_004.Switch
    get_tangent_point_xy.links.new(compare_001.outputs[0], switch_004.inputs[1])
    #compare_001.Result -> switch_004.Switch
    get_tangent_point_xy.links.new(compare_001.outputs[0], switch_004.inputs[0])
    #math_005.Value -> switch_004.False
    get_tangent_point_xy.links.new(math_005.outputs[0], switch_004.inputs[2])
    #group_input_001.eps -> compare_002.B
    get_tangent_point_xy.links.new(group_input_001.outputs[6], compare_002.inputs[1])
    #math_001.Value -> compare_002.A
    get_tangent_point_xy.links.new(math_001.outputs[0], compare_002.inputs[0])
    #compare_002.Result -> switch_005.Switch
    get_tangent_point_xy.links.new(compare_002.outputs[0], switch_005.inputs[0])
    #math_004.Value -> switch_005.False
    get_tangent_point_xy.links.new(math_004.outputs[0], switch_005.inputs[2])
    #math_023.Value -> math_006.Value
    get_tangent_point_xy.links.new(math_023.outputs[0], math_006.inputs[1])
    #math_045.Value -> math_007.Value
    get_tangent_point_xy.links.new(math_045.outputs[0], math_007.inputs[1])
    #math_006.Value -> math_008.Value
    get_tangent_point_xy.links.new(math_006.outputs[0], math_008.inputs[0])
    #switch_004.Output -> math_008.Value
    get_tangent_point_xy.links.new(switch_004.outputs[0], math_008.inputs[1])
    #switch_005.Output -> math_009.Value
    get_tangent_point_xy.links.new(switch_005.outputs[0], math_009.inputs[1])
    #math_005.Value -> math_010.Value
    get_tangent_point_xy.links.new(math_005.outputs[0], math_010.inputs[0])
    #math_004.Value -> math_011.Value
    get_tangent_point_xy.links.new(math_004.outputs[0], math_011.inputs[0])
    #math_023.Value -> math_012.Value
    get_tangent_point_xy.links.new(math_023.outputs[0], math_012.inputs[0])
    #math_010.Value -> math_012.Value
    get_tangent_point_xy.links.new(math_010.outputs[0], math_012.inputs[1])
    #math_011.Value -> math_013.Value
    get_tangent_point_xy.links.new(math_011.outputs[0], math_013.inputs[1])
    #math_045.Value -> math_013.Value
    get_tangent_point_xy.links.new(math_045.outputs[0], math_013.inputs[0])
    #math_012.Value -> combine_xyz_004.X
    get_tangent_point_xy.links.new(math_012.outputs[0], combine_xyz_004.inputs[0])
    #math_013.Value -> combine_xyz_004.Y
    get_tangent_point_xy.links.new(math_013.outputs[0], combine_xyz_004.inputs[1])
    #group_input_001.Z -> combine_xyz_004.Z
    get_tangent_point_xy.links.new(group_input_001.outputs[2], combine_xyz_004.inputs[2])
    #math_008.Value -> switch_002.True
    get_tangent_point_xy.links.new(math_008.outputs[0], switch_002.inputs[3])
    #math_009.Value -> switch_002.False
    get_tangent_point_xy.links.new(math_009.outputs[0], switch_002.inputs[2])
    #switch_002.Output -> math_011.Value
    get_tangent_point_xy.links.new(switch_002.outputs[0], math_011.inputs[1])
    #switch_002.Output -> math_010.Value
    get_tangent_point_xy.links.new(switch_002.outputs[0], math_010.inputs[1])
    #combine_xyz_004.Vector -> group_output.P
    get_tangent_point_xy.links.new(combine_xyz_004.outputs[0], group_output.inputs[0])
    #math_014.Value -> group_output.Angle_rad
    get_tangent_point_xy.links.new(math_014.outputs[0], group_output.inputs[1])
    #group_input_001.px -> math_006.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[4], math_006.inputs[0])
    #group_input_001.py -> math_007.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[5], math_007.inputs[0])
    #math_007.Value -> math_009.Value
    get_tangent_point_xy.links.new(math_007.outputs[0], math_009.inputs[0])
    #group_input_001.Y -> math_014.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[1], math_014.inputs[0])
    #group_input_001.X -> math_014.Value
    get_tangent_point_xy.links.new(group_input_001.outputs[0], math_014.inputs[1])
    return get_tangent_point_xy

#initialize pie_segment node group
def pie_segment_node_group():
    pie_segment = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Pie_segment")

    

    #initialize pie_segment nodes
    #node Reroute.002
    reroute_002 = pie_segment.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    #node Set Material
    set_material = pie_segment.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Set Material.002
    set_material_002 = pie_segment.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    #Selection
    set_material_002.inputs[1].default_value = True

    #node Set Material.001
    set_material_001 = pie_segment.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    #Selection
    set_material_001.inputs[1].default_value = True

    #node Math.002
    math_002_1 = pie_segment.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'ADD'
    math_002_1.use_clamp = False

    #node Math.001
    math_001_1 = pie_segment.nodes.new("ShaderNodeMath")
    math_001_1.label = "2Pi/2"
    math_001_1.name = "Math.001"
    math_001_1.operation = 'MULTIPLY'
    math_001_1.use_clamp = False
    #Value
    math_001_1.inputs[0].default_value = 0.5
    #Value_001
    math_001_1.inputs[1].default_value = 6.2831854820251465

    #node Arc
    arc = pie_segment.nodes.new("GeometryNodeCurveArc")
    arc.name = "Arc"
    arc.mode = 'RADIUS'
    #Resolution
    arc.inputs[0].default_value = 12
    #Connect Center
    arc.inputs[8].default_value = True
    #Invert Arc
    arc.inputs[9].default_value = False

    #node Extrude Mesh
    extrude_mesh = pie_segment.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'FACES'
    #Selection
    extrude_mesh.inputs[1].default_value = True
    #Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Offset Scale
    extrude_mesh.inputs[3].default_value = -0.10000000149011612
    #Individual
    extrude_mesh.inputs[4].default_value = True

    #node Math.004
    math_004_1 = pie_segment.nodes.new("ShaderNodeMath")
    math_004_1.label = "Abs(R)"
    math_004_1.name = "Math.004"
    math_004_1.operation = 'ABSOLUTE'
    math_004_1.use_clamp = False

    #node Math.003
    math_003_1 = pie_segment.nodes.new("ShaderNodeMath")
    math_003_1.label = "R/20"
    math_003_1.name = "Math.003"
    math_003_1.operation = 'DIVIDE'
    math_003_1.use_clamp = False
    #Value_001
    math_003_1.inputs[1].default_value = 1.5

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

    #node Fill Curve.001
    fill_curve_001 = pie_segment.nodes.new("GeometryNodeFillCurve")
    fill_curve_001.name = "Fill Curve.001"
    fill_curve_001.mode = 'TRIANGLES'

    #node Extrude Mesh.001
    extrude_mesh_001 = pie_segment.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_001.name = "Extrude Mesh.001"
    extrude_mesh_001.mode = 'FACES'
    #Selection
    extrude_mesh_001.inputs[1].default_value = True
    #Offset
    extrude_mesh_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Offset Scale
    extrude_mesh_001.inputs[3].default_value = 0.02500000037252903
    #Individual
    extrude_mesh_001.inputs[4].default_value = True

    #node Position
    position = pie_segment.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Fill Curve
    fill_curve = pie_segment.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.mode = 'TRIANGLES'

    #node Set Position
    set_position = pie_segment.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Selection
    set_position.inputs[1].default_value = True
    #Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Join Geometry
    join_geometry = pie_segment.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Group Input
    group_input = pie_segment.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    #pie_segment inputs
    #input Start
    pie_segment.inputs.new('NodeSocketFloat', "Start")
    pie_segment.inputs[0].attribute_domain = 'POINT'

    #input String
    pie_segment.inputs.new('NodeSocketString', "String")
    pie_segment.inputs[1].attribute_domain = 'POINT'

    #input Position
    pie_segment.inputs.new('NodeSocketVectorXYZ', "Position")
    pie_segment.inputs[2].attribute_domain = 'POINT'

    #input Radius
    pie_segment.inputs.new('NodeSocketFloat', "Radius")
    pie_segment.inputs[3].attribute_domain = 'POINT'

    #input Segment Material
    pie_segment.inputs.new('NodeSocketMaterial', "Segment Material")
    pie_segment.inputs[4].attribute_domain = 'POINT'

    #input Text Material
    pie_segment.inputs.new('NodeSocketMaterial', "Text Material")
    pie_segment.inputs[5].attribute_domain = 'POINT'



    #node Group Output
    group_output_1 = pie_segment.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    #pie_segment outputs
    #output Curve
    pie_segment.outputs.new('NodeSocketGeometry', "Curve")
    pie_segment.outputs[0].attribute_domain = 'POINT'

    #output End
    pie_segment.outputs.new('NodeSocketFloat', "End")
    pie_segment.outputs[1].attribute_domain = 'POINT'



    #node Set Position.001
    set_position_001 = pie_segment.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    #Selection
    set_position_001.inputs[1].default_value = True
    #Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Attribute Statistic
    attribute_statistic = pie_segment.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'FACE'
    #Selection
    attribute_statistic.inputs[1].default_value = True



    #Set locations
    reroute_002.location = (1079.40283203125, 58.553653717041016)
    set_material.location = (1410.216552734375, 416.6747741699219)
    set_material_002.location = (1419.2493896484375, 272.2935485839844)
    set_material_001.location = (1421.6993408203125, 121.72770690917969)
    math_002_1.location = (41.61524200439453, -111.32077026367188)
    math_001_1.location = (-321.22784423828125, -89.43610382080078)
    arc.location = (104.90206146240234, 510.955322265625)
    extrude_mesh.location = (707.877685546875, 148.20428466796875)
    math_004_1.location = (-420.0712585449219, 458.00067138671875)
    math_003_1.location = (-94.88426208496094, 656.8350830078125)
    string_to_curves.location = (519.9778442382812, 625.878173828125)
    fill_curve_001.location = (827.8894653320312, 601.7162475585938)
    extrude_mesh_001.location = (1006.8871459960938, 603.0018920898438)
    position.location = (461.33984375, -279.41729736328125)
    fill_curve.location = (272.2713623046875, 282.3844909667969)
    set_position.location = (1220.502197265625, 479.3816833496094)
    join_geometry.location = (1671.9873046875, 251.46034240722656)
    group_input.location = (-511.33013916015625, 81.83856201171875)
    group_output_1.location = (2081.9248046875, -126.84184265136719)
    set_position_001.location = (1855.50732421875, 95.57281494140625)
    attribute_statistic.location = (868.60888671875, -132.26499938964844)

    #initialize pie_segment links
    #math_001_1.Value -> arc.Sweep Angle
    pie_segment.links.new(math_001_1.outputs[0], arc.inputs[6])
    #math_001_1.Value -> math_002_1.Value
    pie_segment.links.new(math_001_1.outputs[0], math_002_1.inputs[0])
    #group_input.Start -> math_002_1.Value
    pie_segment.links.new(group_input.outputs[0], math_002_1.inputs[1])
    #math_002_1.Value -> group_output_1.End
    pie_segment.links.new(math_002_1.outputs[0], group_output_1.inputs[1])
    #group_input.Start -> arc.Start Angle
    pie_segment.links.new(group_input.outputs[0], arc.inputs[5])
    #set_material_001.Geometry -> join_geometry.Geometry
    pie_segment.links.new(set_material_001.outputs[0], join_geometry.inputs[0])
    #set_material.Geometry -> join_geometry.Geometry
    pie_segment.links.new(set_material.outputs[0], join_geometry.inputs[0])
    #arc.Curve -> fill_curve.Curve
    pie_segment.links.new(arc.outputs[0], fill_curve.inputs[0])
    #string_to_curves.Curve Instances -> fill_curve_001.Curve
    pie_segment.links.new(string_to_curves.outputs[0], fill_curve_001.inputs[0])
    #fill_curve.Mesh -> extrude_mesh.Mesh
    pie_segment.links.new(fill_curve.outputs[0], extrude_mesh.inputs[0])
    #set_material_002.Geometry -> join_geometry.Geometry
    pie_segment.links.new(set_material_002.outputs[0], join_geometry.inputs[0])
    #fill_curve_001.Mesh -> extrude_mesh_001.Mesh
    pie_segment.links.new(fill_curve_001.outputs[0], extrude_mesh_001.inputs[0])
    #extrude_mesh_001.Mesh -> set_position.Geometry
    pie_segment.links.new(extrude_mesh_001.outputs[0], set_position.inputs[0])
    #set_position.Geometry -> set_material.Geometry
    pie_segment.links.new(set_position.outputs[0], set_material.inputs[0])
    #extrude_mesh.Mesh -> set_material_001.Geometry
    pie_segment.links.new(extrude_mesh.outputs[0], set_material_001.inputs[0])
    #fill_curve.Mesh -> set_material_002.Geometry
    pie_segment.links.new(fill_curve.outputs[0], set_material_002.inputs[0])
    #group_input.Text Material -> set_material.Material
    pie_segment.links.new(group_input.outputs[5], set_material.inputs[2])
    #reroute_002.Output -> set_material_001.Material
    pie_segment.links.new(reroute_002.outputs[0], set_material_001.inputs[2])
    #group_input.Segment Material -> reroute_002.Input
    pie_segment.links.new(group_input.outputs[4], reroute_002.inputs[0])
    #reroute_002.Output -> set_material_002.Material
    pie_segment.links.new(reroute_002.outputs[0], set_material_002.inputs[2])
    #set_position_001.Geometry -> group_output_1.Curve
    pie_segment.links.new(set_position_001.outputs[0], group_output_1.inputs[0])
    #group_input.String -> string_to_curves.String
    pie_segment.links.new(group_input.outputs[1], string_to_curves.inputs[0])
    #math_003_1.Value -> string_to_curves.Size
    pie_segment.links.new(math_003_1.outputs[0], string_to_curves.inputs[1])
    #group_input.Radius -> math_004_1.Value
    pie_segment.links.new(group_input.outputs[3], math_004_1.inputs[0])
    #math_004_1.Value -> math_003_1.Value
    pie_segment.links.new(math_004_1.outputs[0], math_003_1.inputs[0])
    #math_004_1.Value -> arc.Radius
    pie_segment.links.new(math_004_1.outputs[0], arc.inputs[4])
    #position.Position -> attribute_statistic.Attribute
    pie_segment.links.new(position.outputs[0], attribute_statistic.inputs[2])
    #position.Position -> attribute_statistic.Attribute
    pie_segment.links.new(position.outputs[0], attribute_statistic.inputs[3])
    #fill_curve.Mesh -> attribute_statistic.Geometry
    pie_segment.links.new(fill_curve.outputs[0], attribute_statistic.inputs[0])
    #attribute_statistic.Mean -> set_position.Offset
    pie_segment.links.new(attribute_statistic.outputs[8], set_position.inputs[3])
    #join_geometry.Geometry -> set_position_001.Geometry
    pie_segment.links.new(join_geometry.outputs[0], set_position_001.inputs[0])
    #group_input.Position -> set_position_001.Offset
    pie_segment.links.new(group_input.outputs[2], set_position_001.inputs[3])
    return pie_segment

#initialize circle_visualize node group
def circle_visualize_node_group():
    circle_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Circle_visualize")

    

    #initialize circle_visualize nodes
    #node Reroute
    reroute = circle_visualize.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    #node Group Output
    group_output_2 = circle_visualize.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    #circle_visualize outputs
    #output Geometry
    circle_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    circle_visualize.outputs[0].attribute_domain = 'POINT'

    pie_segment = pie_segment_node_group()

    #node Join Geometry
    join_geometry_1 = circle_visualize.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_1.name = "Join Geometry"

    #node Group.001
    group_001 = circle_visualize.nodes.new("GeometryNodeGroup")
    group_001.label = "Pie Segment"
    group_001.name = "Group.001"
    group_001.node_tree = pie_segment
    #Input_1
    group_001.inputs[1].default_value = "0"

    #node Group
    group = circle_visualize.nodes.new("GeometryNodeGroup")
    group.label = "Pie Segment"
    group.name = "Group"
    group.node_tree = pie_segment
    #Input_1
    group.inputs[1].default_value = "1"

    #node Math
    math_1 = circle_visualize.nodes.new("ShaderNodeMath")
    math_1.label = "Rotate 90"
    math_1.name = "Math"
    math_1.operation = 'ADD'
    math_1.use_clamp = False
    #Value_001
    math_1.inputs[1].default_value = 1.5707963705062866

    #node Group Input
    group_input_1 = circle_visualize.nodes.new("NodeGroupInput")
    group_input_1.label = "Text Material"
    group_input_1.name = "Group Input"
    #circle_visualize inputs
    #input Position
    circle_visualize.inputs.new('NodeSocketVectorXYZ', "Position")
    circle_visualize.inputs[0].attribute_domain = 'POINT'

    #input Angle
    circle_visualize.inputs.new('NodeSocketFloat', "Angle")
    circle_visualize.inputs[1].attribute_domain = 'POINT'

    #input Radius
    circle_visualize.inputs.new('NodeSocketFloat', "Radius")
    circle_visualize.inputs[2].attribute_domain = 'POINT'

    #input Text Material
    circle_visualize.inputs.new('NodeSocketMaterial', "Text Material")
    circle_visualize.inputs[3].attribute_domain = 'POINT'

    #input Material 0
    circle_visualize.inputs.new('NodeSocketMaterial', "Material 0")
    circle_visualize.inputs[4].attribute_domain = 'POINT'

    #input Material 1
    circle_visualize.inputs.new('NodeSocketMaterial', "Material 1")
    circle_visualize.inputs[5].attribute_domain = 'POINT'





    #Set locations
    reroute.location = (-340.2493896484375, -282.7701416015625)
    group_output_2.location = (560.9609375, 0.0)
    join_geometry_1.location = (370.9609375, 52.043426513671875)
    group_001.location = (103.57568359375, -70.7313461303711)
    group.location = (-118.287109375, 112.02267456054688)
    math_1.location = (-369.956298828125, 162.6209259033203)
    group_input_1.location = (-570.9609375, 0.0)

    #initialize circle_visualize links
    #group.Curve -> join_geometry_1.Geometry
    circle_visualize.links.new(group.outputs[0], join_geometry_1.inputs[0])
    #group_001.Curve -> join_geometry_1.Geometry
    circle_visualize.links.new(group_001.outputs[0], join_geometry_1.inputs[0])
    #reroute.Output -> group.Text Material
    circle_visualize.links.new(reroute.outputs[0], group.inputs[5])
    #group.End -> group_001.Start
    circle_visualize.links.new(group.outputs[1], group_001.inputs[0])
    #reroute.Output -> group_001.Text Material
    circle_visualize.links.new(reroute.outputs[0], group_001.inputs[5])
    #group_input_1.Text Material -> reroute.Input
    circle_visualize.links.new(group_input_1.outputs[3], reroute.inputs[0])
    #group_input_1.Material 1 -> group.Segment Material
    circle_visualize.links.new(group_input_1.outputs[5], group.inputs[4])
    #group_input_1.Material 0 -> group_001.Segment Material
    circle_visualize.links.new(group_input_1.outputs[4], group_001.inputs[4])
    #group_input_1.Radius -> group_001.Radius
    circle_visualize.links.new(group_input_1.outputs[2], group_001.inputs[3])
    #group_input_1.Radius -> group.Radius
    circle_visualize.links.new(group_input_1.outputs[2], group.inputs[3])
    #join_geometry_1.Geometry -> group_output_2.Geometry
    circle_visualize.links.new(join_geometry_1.outputs[0], group_output_2.inputs[0])
    #group_input_1.Position -> group.Position
    circle_visualize.links.new(group_input_1.outputs[0], group.inputs[2])
    #group_input_1.Position -> group_001.Position
    circle_visualize.links.new(group_input_1.outputs[0], group_001.inputs[2])
    #group_input_1.Angle -> math_1.Value
    circle_visualize.links.new(group_input_1.outputs[1], math_1.inputs[0])
    #math_1.Value -> group.Start
    circle_visualize.links.new(math_1.outputs[0], group.inputs[0])
    return circle_visualize

#initialize render_branch_visualize node group
def render_branch_visualize_node_group():
    render_branch_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Render_branch_visualize")

    

    #initialize render_branch_visualize nodes
    #node Math.044
    math_044_1 = render_branch_visualize.nodes.new("ShaderNodeMath")
    math_044_1.label = "-R"
    math_044_1.name = "Math.044"
    math_044_1.hide = True
    math_044_1.operation = 'MULTIPLY'
    math_044_1.use_clamp = False
    #Value_001
    math_044_1.inputs[1].default_value = -1.0

    #node Vector Math.001
    vector_math_001 = render_branch_visualize.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.hide = True
    vector_math_001.operation = 'LENGTH'

    #node Separate XYZ
    separate_xyz = render_branch_visualize.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.hide = True

    #node Object Info
    object_info = render_branch_visualize.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.hide = True
    object_info.transform_space = 'ORIGINAL'
    #As Instance
    object_info.inputs[1].default_value = False

    #node Value.002
    value_002 = render_branch_visualize.nodes.new("ShaderNodeValue")
    value_002.label = "eps"
    value_002.name = "Value.002"
    value_002.hide = True

    value_002.outputs[0].default_value = 9.999999960041972e-13
    #node Math.006
    math_006_1 = render_branch_visualize.nodes.new("ShaderNodeMath")
    math_006_1.label = "Norm_X"
    math_006_1.name = "Math.006"
    math_006_1.hide = True
    math_006_1.operation = 'DIVIDE'
    math_006_1.use_clamp = False

    #node Math.007
    math_007_1 = render_branch_visualize.nodes.new("ShaderNodeMath")
    math_007_1.label = "Norm_Y"
    math_007_1.name = "Math.007"
    math_007_1.hide = True
    math_007_1.operation = 'DIVIDE'
    math_007_1.use_clamp = False

    #node Math.008
    math_008_1 = render_branch_visualize.nodes.new("ShaderNodeMath")
    math_008_1.label = "Norm_Z"
    math_008_1.name = "Math.008"
    math_008_1.hide = True
    math_008_1.operation = 'DIVIDE'
    math_008_1.use_clamp = False

    #node Math.009
    math_009_1 = render_branch_visualize.nodes.new("ShaderNodeMath")
    math_009_1.label = "Norm_R"
    math_009_1.name = "Math.009"
    math_009_1.hide = True
    math_009_1.operation = 'DIVIDE'
    math_009_1.use_clamp = False

    #node Group Output
    group_output_3 = render_branch_visualize.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True
    #render_branch_visualize outputs
    #output Geometry
    render_branch_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    render_branch_visualize.outputs[0].attribute_domain = 'POINT'



    #node Group.002
    group_002 = render_branch_visualize.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = get_tangent_point_xy_node_group()

    #node Group.001
    group_001_1 = render_branch_visualize.nodes.new("GeometryNodeGroup")
    group_001_1.name = "Group.001"
    group_001_1.node_tree = circle_visualize_node_group()

    #node Group Input
    group_input_2 = render_branch_visualize.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
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



    #node Separate XYZ.001
    separate_xyz_001 = render_branch_visualize.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.label = "cx,cy,cz"
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.hide = True

    #node Math
    math_2 = render_branch_visualize.nodes.new("ShaderNodeMath")
    math_2.label = "Shift Z"
    math_2.name = "Math"
    math_2.hide = True
    math_2.operation = 'ADD'
    math_2.use_clamp = False



    #Set locations
    math_044_1.location = (-429.8410949707031, 65.2533950805664)
    vector_math_001.location = (-411.7771301269531, 152.63455200195312)
    separate_xyz.location = (-413.8541564941406, 206.00833129882812)
    object_info.location = (-423.79144287109375, -44.29651641845703)
    value_002.location = (-227.41383361816406, -48.059120178222656)
    math_006_1.location = (-219.10365295410156, 208.31396484375)
    math_007_1.location = (-219.10365295410156, 165.54180908203125)
    math_008_1.location = (-218.03614807128906, 117.42318725585938)
    math_009_1.location = (-216.95651245117188, 68.70800018310547)
    group_output_3.location = (510.9173278808594, -5.075558662414551)
    group_002.location = (-18.656234741210938, 163.33322143554688)
    group_001_1.location = (222.2908172607422, 9.503557205200195)
    group_input_2.location = (-652.7306518554688, 0.0)
    separate_xyz_001.location = (-421.10443115234375, 4.136842727661133)
    math_2.location = (-224.37274169921875, 15.625839233398438)

    #initialize render_branch_visualize links
    #separate_xyz_001.Y -> group_002.py
    render_branch_visualize.links.new(separate_xyz_001.outputs[1], group_002.inputs[5])
    #separate_xyz_001.X -> group_002.px
    render_branch_visualize.links.new(separate_xyz_001.outputs[0], group_002.inputs[4])
    #math_006_1.Value -> group_002.X
    render_branch_visualize.links.new(math_006_1.outputs[0], group_002.inputs[0])
    #group_002.Angle_rad -> group_001_1.Angle
    render_branch_visualize.links.new(group_002.outputs[1], group_001_1.inputs[1])
    #math_009_1.Value -> group_002.R
    render_branch_visualize.links.new(math_009_1.outputs[0], group_002.inputs[3])
    #value_002.Value -> group_002.eps
    render_branch_visualize.links.new(value_002.outputs[0], group_002.inputs[6])
    #separate_xyz.Z -> math_008_1.Value
    render_branch_visualize.links.new(separate_xyz.outputs[2], math_008_1.inputs[0])
    #separate_xyz.X -> math_006_1.Value
    render_branch_visualize.links.new(separate_xyz.outputs[0], math_006_1.inputs[0])
    #vector_math_001.Value -> math_006_1.Value
    render_branch_visualize.links.new(vector_math_001.outputs[1], math_006_1.inputs[1])
    #math_044_1.Value -> math_009_1.Value
    render_branch_visualize.links.new(math_044_1.outputs[0], math_009_1.inputs[0])
    #object_info.Location -> separate_xyz_001.Vector
    render_branch_visualize.links.new(object_info.outputs[0], separate_xyz_001.inputs[0])
    #vector_math_001.Value -> math_007_1.Value
    render_branch_visualize.links.new(vector_math_001.outputs[1], math_007_1.inputs[1])
    #vector_math_001.Value -> math_008_1.Value
    render_branch_visualize.links.new(vector_math_001.outputs[1], math_008_1.inputs[1])
    #separate_xyz.Y -> math_007_1.Value
    render_branch_visualize.links.new(separate_xyz.outputs[1], math_007_1.inputs[0])
    #math_007_1.Value -> group_002.Y
    render_branch_visualize.links.new(math_007_1.outputs[0], group_002.inputs[1])
    #vector_math_001.Value -> math_009_1.Value
    render_branch_visualize.links.new(vector_math_001.outputs[1], math_009_1.inputs[1])
    #group_002.P -> group_001_1.Position
    render_branch_visualize.links.new(group_002.outputs[0], group_001_1.inputs[0])
    #group_input_2.Tangent Radius -> math_044_1.Value
    render_branch_visualize.links.new(group_input_2.outputs[1], math_044_1.inputs[0])
    #group_input_2.Tangent Angle -> vector_math_001.Vector
    render_branch_visualize.links.new(group_input_2.outputs[0], vector_math_001.inputs[0])
    #group_input_2.Tangent Angle -> separate_xyz.Vector
    render_branch_visualize.links.new(group_input_2.outputs[0], separate_xyz.inputs[0])
    #group_001_1.Geometry -> group_output_3.Geometry
    render_branch_visualize.links.new(group_001_1.outputs[0], group_output_3.inputs[0])
    #group_input_2.Render Center -> object_info.Object
    render_branch_visualize.links.new(group_input_2.outputs[3], object_info.inputs[0])
    #group_input_2.Circle Radius -> group_001_1.Radius
    render_branch_visualize.links.new(group_input_2.outputs[4], group_001_1.inputs[2])
    #group_input_2.Text Material -> group_001_1.Text Material
    render_branch_visualize.links.new(group_input_2.outputs[5], group_001_1.inputs[3])
    #group_input_2.Material A -> group_001_1.Material 0
    render_branch_visualize.links.new(group_input_2.outputs[6], group_001_1.inputs[4])
    #group_input_2.Material B -> group_001_1.Material 1
    render_branch_visualize.links.new(group_input_2.outputs[7], group_001_1.inputs[5])
    #separate_xyz_001.Z -> math_2.Value
    render_branch_visualize.links.new(separate_xyz_001.outputs[2], math_2.inputs[0])
    #group_input_2.Shift Z -> math_2.Value
    render_branch_visualize.links.new(group_input_2.outputs[2], math_2.inputs[1])
    #math_2.Value -> group_002.Z
    render_branch_visualize.links.new(math_2.outputs[0], group_002.inputs[2])
    return render_branch_visualize
