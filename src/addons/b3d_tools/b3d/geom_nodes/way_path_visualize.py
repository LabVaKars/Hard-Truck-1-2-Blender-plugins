import bpy

#initialize way_path_visualize node group
def way_path_visualize_node_group():
    way_path_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Way_path_visualize")

    

    #initialize way_path_visualize nodes
    #node Math.010
    math_010 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'SINE'
    math_010.use_clamp = False

    #node Math.009
    math_009 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'COSINE'
    math_009.use_clamp = False

    #node Reroute.005
    reroute_005 = way_path_visualize.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    #node Reroute.007
    reroute_007 = way_path_visualize.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    #node Reroute.008
    reroute_008 = way_path_visualize.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    #node Reroute.010
    reroute_010 = way_path_visualize.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    #node Math.012
    math_012 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_012.label = "Step_decimal"
    math_012.name = "Math.012"
    math_012.operation = 'DIVIDE'
    math_012.use_clamp = False

    #node Domain Size
    domain_size = way_path_visualize.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.component = 'CURVE'

    #node Reroute.012
    reroute_012 = way_path_visualize.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    #node Math.003
    math_003 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'ADD'
    math_003.use_clamp = False

    #node Position.001
    position_001 = way_path_visualize.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    #node Vector Math.004
    vector_math_004 = way_path_visualize.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'MULTIPLY'

    #node Vector Math.002
    vector_math_002 = way_path_visualize.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'MULTIPLY'

    #node Value.004
    value_004 = way_path_visualize.nodes.new("ShaderNodeValue")
    value_004.label = "-1"
    value_004.name = "Value.004"
    value_004.hide = True

    value_004.outputs[0].default_value = -1.0
    #node Value.003
    value_003 = way_path_visualize.nodes.new("ShaderNodeValue")
    value_003.label = "-1"
    value_003.name = "Value.003"
    value_003.hide = True

    value_003.outputs[0].default_value = -1.0
    #node Math.013
    math_013 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'ADD'
    math_013.use_clamp = False

    #node Math.016
    math_016 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False

    #node Math
    math = way_path_visualize.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ROUND'
    math.use_clamp = False

    #node Math.008
    math_008 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_008.label = "Pi/4"
    math_008.name = "Math.008"
    math_008.operation = 'DIVIDE'
    math_008.use_clamp = False
    #Value_001
    math_008.inputs[1].default_value = 4.0

    #node Math.002
    math_002 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False

    #node Math.005
    math_005 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False

    #node Math.006
    math_006 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'ARCTAN2'
    math_006.use_clamp = False

    #node Math.004
    math_004 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    #Value_001
    math_004.inputs[1].default_value = -1.0

    #node Value.001
    value_001 = way_path_visualize.nodes.new("ShaderNodeValue")
    value_001.label = "Pi"
    value_001.name = "Value.001"

    value_001.outputs[0].default_value = 3.1415927410125732
    #node Separate XYZ.001
    separate_xyz_001 = way_path_visualize.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    #node Curve Tangent
    curve_tangent = way_path_visualize.nodes.new("GeometryNodeInputTangent")
    curve_tangent.name = "Curve Tangent"

    #node Math.015
    math_015 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'SUBTRACT'
    math_015.use_clamp = False

    #node Reroute.018
    reroute_018 = way_path_visualize.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    #node Index
    index = way_path_visualize.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    #node Compare
    compare = way_path_visualize.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    #B_INT
    compare.inputs[3].default_value = 0

    #node Boolean Math
    boolean_math = way_path_visualize.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'OR'

    #node Compare.001
    compare_001 = way_path_visualize.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'

    #node Math.011
    math_011 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'SUBTRACT'
    math_011.use_clamp = False
    #Value_001
    math_011.inputs[1].default_value = 1.0

    #node Vector Math.003
    vector_math_003 = way_path_visualize.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'MULTIPLY'
    #Vector_001
    vector_math_003.inputs[1].default_value = (-1.0, 1.0, 0.0)

    #node Math.014
    math_014 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'ADD'
    math_014.use_clamp = False

    #node Vector Math.001
    vector_math_001 = way_path_visualize.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'

    #node Position
    position = way_path_visualize.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Switch
    switch = way_path_visualize.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'VECTOR'

    #node Vector Math
    vector_math = way_path_visualize.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'

    #node Combine XYZ.001
    combine_xyz_001 = way_path_visualize.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    #Z
    combine_xyz_001.inputs[2].default_value = 0.0

    #node Index.001
    index_001 = way_path_visualize.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"

    #node Math.007
    math_007 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_007.label = "Index+1"
    math_007.name = "Math.007"
    math_007.hide = True
    math_007.operation = 'ADD'
    math_007.use_clamp = False
    #Value_001
    math_007.inputs[1].default_value = 1.0

    #node Combine XYZ
    combine_xyz = way_path_visualize.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    #Z
    combine_xyz.inputs[2].default_value = 0.0

    #node Reroute.009
    reroute_009 = way_path_visualize.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    #node Reroute.011
    reroute_011 = way_path_visualize.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    #node Reroute.014
    reroute_014 = way_path_visualize.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    #node Reroute.019
    reroute_019 = way_path_visualize.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    #node Reroute.006
    reroute_006 = way_path_visualize.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    #node Reroute.017
    reroute_017 = way_path_visualize.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    #node Reroute.016
    reroute_016 = way_path_visualize.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    #node Reroute.015
    reroute_015 = way_path_visualize.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    #node Reroute.013
    reroute_013 = way_path_visualize.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    #node Set Position
    set_position = way_path_visualize.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Selection
    set_position.inputs[1].default_value = True

    #node Set Position.001
    set_position_001 = way_path_visualize.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    #Selection
    set_position_001.inputs[1].default_value = True

    #node Reroute.030
    reroute_030 = way_path_visualize.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    #node Set Position.002
    set_position_002 = way_path_visualize.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    #Selection
    set_position_002.inputs[1].default_value = True

    #node Set Spline Type
    set_spline_type = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type.label = "Set NURBS"
    set_spline_type.name = "Set Spline Type"
    set_spline_type.hide = True
    set_spline_type.spline_type = 'NURBS'
    #Selection
    set_spline_type.inputs[1].default_value = True

    #node Set Spline Type.001
    set_spline_type_001 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_001.label = "Set Poly"
    set_spline_type_001.name = "Set Spline Type.001"
    set_spline_type_001.hide = True
    set_spline_type_001.spline_type = 'POLY'
    #Selection
    set_spline_type_001.inputs[1].default_value = True

    #node Set Spline Type.002
    set_spline_type_002 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_002.label = "Set NURBS"
    set_spline_type_002.name = "Set Spline Type.002"
    set_spline_type_002.hide = True
    set_spline_type_002.spline_type = 'NURBS'
    #Selection
    set_spline_type_002.inputs[1].default_value = True

    #node Set Spline Type.003
    set_spline_type_003 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_003.label = "Set Poly"
    set_spline_type_003.name = "Set Spline Type.003"
    set_spline_type_003.hide = True
    set_spline_type_003.spline_type = 'POLY'
    #Selection
    set_spline_type_003.inputs[1].default_value = True

    #node Set Spline Type.004
    set_spline_type_004 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_004.label = "Set NURBS"
    set_spline_type_004.name = "Set Spline Type.004"
    set_spline_type_004.hide = True
    set_spline_type_004.spline_type = 'NURBS'
    #Selection
    set_spline_type_004.inputs[1].default_value = True

    #node Set Spline Type.005
    set_spline_type_005 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_005.label = "Set Poly"
    set_spline_type_005.name = "Set Spline Type.005"
    set_spline_type_005.hide = True
    set_spline_type_005.spline_type = 'POLY'
    #Selection
    set_spline_type_005.inputs[1].default_value = True

    #node Set Spline Type.009
    set_spline_type_009 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_009.label = "Set Poly"
    set_spline_type_009.name = "Set Spline Type.009"
    set_spline_type_009.hide = True
    set_spline_type_009.spline_type = 'POLY'
    #Selection
    set_spline_type_009.inputs[1].default_value = True

    #node Reroute.022
    reroute_022 = way_path_visualize.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    #node Switch.003
    switch_003 = way_path_visualize.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.input_type = 'GEOMETRY'

    #node Reroute.023
    reroute_023 = way_path_visualize.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    #node Reroute.024
    reroute_024 = way_path_visualize.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    #node Reroute.025
    reroute_025 = way_path_visualize.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    #node Switch.004
    switch_004 = way_path_visualize.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.input_type = 'GEOMETRY'

    #node Reroute.020
    reroute_020 = way_path_visualize.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    #node Reroute.028
    reroute_028 = way_path_visualize.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    #node Reroute.027
    reroute_027 = way_path_visualize.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    #node Reroute.026
    reroute_026 = way_path_visualize.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    #node Reroute.021
    reroute_021 = way_path_visualize.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    #node Reroute.029
    reroute_029 = way_path_visualize.nodes.new("NodeReroute")
    reroute_029.name = "Reroute.029"
    #node Set Material
    set_material = way_path_visualize.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Set Material.001
    set_material_001 = way_path_visualize.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    #Selection
    set_material_001.inputs[1].default_value = True

    #node Set Material.004
    set_material_004 = way_path_visualize.nodes.new("GeometryNodeSetMaterial")
    set_material_004.name = "Set Material.004"
    #Selection
    set_material_004.inputs[1].default_value = True

    #node Set Material.002
    set_material_002 = way_path_visualize.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    #Selection
    set_material_002.inputs[1].default_value = True

    #node Join Geometry
    join_geometry = way_path_visualize.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node Group Output
    group_output = way_path_visualize.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    #way_path_visualize outputs
    #output Geometry
    way_path_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    way_path_visualize.outputs[0].attribute_domain = 'POINT'



    #node Set Material.003
    set_material_003 = way_path_visualize.nodes.new("GeometryNodeSetMaterial")
    set_material_003.name = "Set Material.003"
    #Selection
    set_material_003.inputs[1].default_value = True

    #node Reroute.003
    reroute_003 = way_path_visualize.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    #node Reroute.004
    reroute_004 = way_path_visualize.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    #node Reroute.002
    reroute_002 = way_path_visualize.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    #node Reroute
    reroute = way_path_visualize.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    #node Reroute.001
    reroute_001 = way_path_visualize.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    #node Set Spline Type.007
    set_spline_type_007 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_007.label = "Set Poly"
    set_spline_type_007.name = "Set Spline Type.007"
    set_spline_type_007.hide = True
    set_spline_type_007.spline_type = 'POLY'
    #Selection
    set_spline_type_007.inputs[1].default_value = True

    #node Curve Circle
    curve_circle = way_path_visualize.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    #Resolution
    curve_circle.inputs[0].default_value = 3
    #Radius
    curve_circle.inputs[4].default_value = 0.10000000149011612

    #node Set Spline Type.008
    set_spline_type_008 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_008.label = "Set NURBS"
    set_spline_type_008.name = "Set Spline Type.008"
    set_spline_type_008.hide = True
    set_spline_type_008.spline_type = 'NURBS'
    #Selection
    set_spline_type_008.inputs[1].default_value = True

    #node Set Spline Type.006
    set_spline_type_006 = way_path_visualize.nodes.new("GeometryNodeCurveSplineType")
    set_spline_type_006.label = "Set NURBS"
    set_spline_type_006.name = "Set Spline Type.006"
    set_spline_type_006.hide = True
    set_spline_type_006.spline_type = 'NURBS'
    #Selection
    set_spline_type_006.inputs[1].default_value = True

    #node Switch.002
    switch_002 = way_path_visualize.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = 'GEOMETRY'

    #node Switch.001
    switch_001 = way_path_visualize.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'GEOMETRY'

    #node Switch.005
    switch_005 = way_path_visualize.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.input_type = 'GEOMETRY'

    #node Curve to Mesh
    curve_to_mesh = way_path_visualize.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    #Fill Caps
    curve_to_mesh.inputs[2].default_value = False

    #node Curve to Mesh.002
    curve_to_mesh_002 = way_path_visualize.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_002.name = "Curve to Mesh.002"
    #Fill Caps
    curve_to_mesh_002.inputs[2].default_value = False

    #node Curve to Mesh.001
    curve_to_mesh_001 = way_path_visualize.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    #Fill Caps
    curve_to_mesh_001.inputs[2].default_value = False

    #node Curve to Mesh.003
    curve_to_mesh_003 = way_path_visualize.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_003.name = "Curve to Mesh.003"
    #Fill Caps
    curve_to_mesh_003.inputs[2].default_value = False

    #node Curve to Mesh.004
    curve_to_mesh_004 = way_path_visualize.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_004.name = "Curve to Mesh.004"
    #Fill Caps
    curve_to_mesh_004.inputs[2].default_value = False

    #node Set Position.003
    set_position_003 = way_path_visualize.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    #Selection
    set_position_003.inputs[1].default_value = True

    #node Math.001
    math_001 = way_path_visualize.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Value
    value = way_path_visualize.nodes.new("ShaderNodeValue")
    value.label = "Roadside_const"
    value.name = "Value"

    value.outputs[0].default_value = 20.0
    #node Group Input
    group_input = way_path_visualize.nodes.new("NodeGroupInput")
    group_input.label = "Roadside_multiplier"
    group_input.name = "Group Input"
    #way_path_visualize inputs
    #input Geometry
    way_path_visualize.inputs.new('NodeSocketGeometry', "Geometry")
    way_path_visualize.inputs[0].attribute_domain = 'POINT'

    #input Roadside_multiplier
    way_path_visualize.inputs.new('NodeSocketFloat', "Roadside_multiplier")
    way_path_visualize.inputs[1].attribute_domain = 'POINT'

    #input Start_Width
    way_path_visualize.inputs.new('NodeSocketFloat', "Start_Width")
    way_path_visualize.inputs[2].attribute_domain = 'POINT'

    #input End_Width
    way_path_visualize.inputs.new('NodeSocketFloat', "End_Width")
    way_path_visualize.inputs[3].attribute_domain = 'POINT'

    #input Is_Bezier
    way_path_visualize.inputs.new('NodeSocketBool', "Is_Bezier")
    way_path_visualize.inputs[4].attribute_domain = 'POINT'

    #input Center_material
    way_path_visualize.inputs.new('NodeSocketMaterial', "Center_material")
    way_path_visualize.inputs[5].attribute_domain = 'POINT'

    #input Border_material
    way_path_visualize.inputs.new('NodeSocketMaterial', "Border_material")
    way_path_visualize.inputs[6].attribute_domain = 'POINT'

    #input Side_material
    way_path_visualize.inputs.new('NodeSocketMaterial', "Side_material")
    way_path_visualize.inputs[7].attribute_domain = 'POINT'





    #Set locations
    math_010.location = (-1504.513916015625, -74.47493743896484)
    math_009.location = (-1504.0213623046875, 79.25114440917969)
    reroute_005.location = (-1280.0, -220.0)
    reroute_007.location = (-1120.0, -100.0)
    reroute_008.location = (-1120.0, -240.0)
    reroute_010.location = (-1120.0, -400.0)
    math_012.location = (-1020.0, 60.0)
    domain_size.location = (-1260.0, 320.0)
    reroute_012.location = (-1060.0, -700.0)
    math_003.location = (-840.0, -320.0)
    position_001.location = (-440.0, -300.0)
    vector_math_004.location = (-440.0, -560.0)
    vector_math_002.location = (-440.0, -360.0)
    value_004.location = (-440.0, -520.0)
    value_003.location = (-440.0, -100.0)
    math_013.location = (-640.0, -340.0)
    math_016.location = (-840.0, -140.0)
    math.location = (-1780.0, 100.0)
    math_008.location = (-1940.0, 100.0)
    math_002.location = (-1880.0, -80.0)
    math_005.location = (-1720.0, -80.0)
    math_006.location = (-1880.0, -260.0)
    math_004.location = (-1720.0, -260.0)
    value_001.location = (-2120.0, -40.0)
    separate_xyz_001.location = (-2040.0, -260.0)
    curve_tangent.location = (-2200.0, -320.0)
    math_015.location = (-1020.0, -140.0)
    reroute_018.location = (-1120.0, -560.0)
    index.location = (-1078.1119384765625, 418.9790344238281)
    compare.location = (-860.0, 520.0)
    boolean_math.location = (-660.0, 520.0)
    compare_001.location = (-860.0, 340.0)
    math_011.location = (-1074.93408203125, 343.1658020019531)
    vector_math_003.location = (-860.0, 160.0)
    math_014.location = (-660.0, -20.0)
    vector_math_001.location = (-440.0, -140.0)
    position.location = (-440.0, 120.0)
    switch.location = (-660.0, 340.0)
    vector_math.location = (-440.0, 60.0)
    combine_xyz_001.location = (-1280.0, 0.0)
    index_001.location = (-1280.0, 160.0)
    math_007.location = (-1280.0, 80.0)
    combine_xyz.location = (-1280.0, -240.0)
    reroute_009.location = (-1080.0, -680.0)
    reroute_011.location = (-1100.0, -660.0)
    reroute_014.location = (-1080.0, -280.0)
    reroute_019.location = (-1100.0, -460.0)
    reroute_006.location = (-1120.0, 60.0)
    reroute_017.location = (-1060.0, -140.0)
    reroute_016.location = (-1060.0, 20.0)
    reroute_015.location = (-1100.0, -620.0)
    reroute_013.location = (-1060.0, -720.0)
    set_position.location = (-235.03012084960938, 119.72059631347656)
    set_position_001.location = (-233.0858154296875, -36.77120590209961)
    reroute_030.location = (-80.0, -240.0)
    set_position_002.location = (-240.0, -320.0)
    set_spline_type.location = (-20.0, -560.0)
    set_spline_type_001.location = (-20.0, -500.0)
    set_spline_type_002.location = (-20.0, -400.0)
    set_spline_type_003.location = (-20.0, -340.0)
    set_spline_type_004.location = (-20.0, -240.0)
    set_spline_type_005.location = (-20.0, -180.0)
    set_spline_type_009.location = (-20.0, 140.0)
    reroute_022.location = (240.0, -440.0)
    switch_003.location = (200.0, -180.0)
    reroute_023.location = (240.0, -280.0)
    reroute_024.location = (240.0, -100.0)
    reroute_025.location = (240.0, 40.0)
    switch_004.location = (200.0, -20.0)
    reroute_020.location = (160.0, -700.0)
    reroute_028.location = (160.0, 120.0)
    reroute_027.location = (160.0, -60.0)
    reroute_026.location = (160.0, -200.0)
    reroute_021.location = (160.0, -360.0)
    reroute_029.location = (160.0, -520.0)
    set_material.location = (700.0, 120.0)
    set_material_001.location = (700.0, -40.0)
    set_material_004.location = (700.0, -180.0)
    set_material_002.location = (700.0, -500.0)
    join_geometry.location = (980.0, -200.0)
    group_output.location = (1200.0, -200.0)
    set_material_003.location = (700.0, -340.0)
    reroute_003.location = (420.0, -440.0)
    reroute_004.location = (420.0, -600.0)
    reroute_002.location = (420.0, -280.0)
    reroute.location = (420.0, 20.0)
    reroute_001.location = (420.0, -140.0)
    set_spline_type_007.location = (-20.0, -20.0)
    curve_circle.location = (200.0, 280.0)
    set_spline_type_008.location = (-20.0, 80.0)
    set_spline_type_006.location = (-20.0, -80.0)
    switch_002.location = (200.0, -340.0)
    switch_001.location = (200.0, -500.0)
    switch_005.location = (200.0, 140.0)
    curve_to_mesh.location = (460.0, 120.0)
    curve_to_mesh_002.location = (460.0, -180.0)
    curve_to_mesh_001.location = (460.0, -40.0)
    curve_to_mesh_003.location = (460.0, -340.0)
    curve_to_mesh_004.location = (460.0, -500.0)
    set_position_003.location = (-240.0, -500.0)
    math_001.location = (-1020.0, -320.0)
    value.location = (-1320.0, -440.0)
    group_input.location = (-1320.0, -540.0)

    #initialize way_path_visualize links
    #separate_xyz_001.X -> math_006.Value
    way_path_visualize.links.new(separate_xyz_001.outputs[0], math_006.inputs[0])
    #separate_xyz_001.Y -> math_006.Value
    way_path_visualize.links.new(separate_xyz_001.outputs[1], math_006.inputs[1])
    #join_geometry.Geometry -> group_output.Geometry
    way_path_visualize.links.new(join_geometry.outputs[0], group_output.inputs[0])
    #set_material.Geometry -> join_geometry.Geometry
    way_path_visualize.links.new(set_material.outputs[0], join_geometry.inputs[0])
    #position.Position -> set_position.Position
    way_path_visualize.links.new(position.outputs[0], set_position.inputs[2])
    #curve_tangent.Tangent -> separate_xyz_001.Vector
    way_path_visualize.links.new(curve_tangent.outputs[0], separate_xyz_001.inputs[0])
    #math_004.Value -> combine_xyz.X
    way_path_visualize.links.new(math_004.outputs[0], combine_xyz.inputs[0])
    #separate_xyz_001.X -> combine_xyz.Y
    way_path_visualize.links.new(separate_xyz_001.outputs[0], combine_xyz.inputs[1])
    #set_material_001.Geometry -> join_geometry.Geometry
    way_path_visualize.links.new(set_material_001.outputs[0], join_geometry.inputs[0])
    #index.Index -> compare.A
    way_path_visualize.links.new(index.outputs[0], compare.inputs[2])
    #compare.Result -> switch.Switch
    way_path_visualize.links.new(compare.outputs[0], switch.inputs[1])
    #value_001.Value -> math_008.Value
    way_path_visualize.links.new(value_001.outputs[0], math_008.inputs[0])
    #math_008.Value -> math_002.Value
    way_path_visualize.links.new(math_008.outputs[0], math_002.inputs[1])
    #math_002.Value -> math.Value
    way_path_visualize.links.new(math_002.outputs[0], math.inputs[0])
    #math.Value -> math_005.Value
    way_path_visualize.links.new(math.outputs[0], math_005.inputs[0])
    #math_008.Value -> math_005.Value
    way_path_visualize.links.new(math_008.outputs[0], math_005.inputs[1])
    #math_005.Value -> math_009.Value
    way_path_visualize.links.new(math_005.outputs[0], math_009.inputs[0])
    #math_005.Value -> math_010.Value
    way_path_visualize.links.new(math_005.outputs[0], math_010.inputs[0])
    #separate_xyz_001.Y -> math_004.Value
    way_path_visualize.links.new(separate_xyz_001.outputs[1], math_004.inputs[0])
    #math_009.Value -> combine_xyz_001.X
    way_path_visualize.links.new(math_009.outputs[0], combine_xyz_001.inputs[0])
    #math_010.Value -> combine_xyz_001.Y
    way_path_visualize.links.new(math_010.outputs[0], combine_xyz_001.inputs[1])
    #vector_math.Vector -> set_position.Offset
    way_path_visualize.links.new(vector_math.outputs[0], set_position.inputs[3])
    #combine_xyz.Vector -> switch.False
    way_path_visualize.links.new(combine_xyz.outputs[0], switch.inputs[8])
    #vector_math_003.Vector -> switch.True
    way_path_visualize.links.new(vector_math_003.outputs[0], switch.inputs[9])
    #combine_xyz_001.Vector -> vector_math_003.Vector
    way_path_visualize.links.new(combine_xyz_001.outputs[0], vector_math_003.inputs[0])
    #math_006.Value -> math_002.Value
    way_path_visualize.links.new(math_006.outputs[0], math_002.inputs[0])
    #domain_size.Point Count -> math_011.Value
    way_path_visualize.links.new(domain_size.outputs[0], math_011.inputs[0])
    #math_011.Value -> compare_001.B
    way_path_visualize.links.new(math_011.outputs[0], compare_001.inputs[3])
    #index.Index -> compare_001.A
    way_path_visualize.links.new(index.outputs[0], compare_001.inputs[2])
    #boolean_math.Boolean -> switch.Switch
    way_path_visualize.links.new(boolean_math.outputs[0], switch.inputs[0])
    #compare_001.Result -> boolean_math.Boolean
    way_path_visualize.links.new(compare_001.outputs[0], boolean_math.inputs[1])
    #compare.Result -> boolean_math.Boolean
    way_path_visualize.links.new(compare.outputs[0], boolean_math.inputs[0])
    #vector_math_001.Vector -> set_position_001.Offset
    way_path_visualize.links.new(vector_math_001.outputs[0], set_position_001.inputs[3])
    #set_material_004.Geometry -> join_geometry.Geometry
    way_path_visualize.links.new(set_material_004.outputs[0], join_geometry.inputs[0])
    #group_input.Roadside_multiplier -> math_001.Value
    way_path_visualize.links.new(group_input.outputs[1], math_001.inputs[0])
    #value_003.Value -> vector_math_001.Vector
    way_path_visualize.links.new(value_003.outputs[0], vector_math_001.inputs[1])
    #vector_math_002.Vector -> vector_math_004.Vector
    way_path_visualize.links.new(vector_math_002.outputs[0], vector_math_004.inputs[0])
    #value_004.Value -> vector_math_004.Vector
    way_path_visualize.links.new(value_004.outputs[0], vector_math_004.inputs[1])
    #math_001.Value -> math_003.Value
    way_path_visualize.links.new(math_001.outputs[0], math_003.inputs[1])
    #group_input.Start_Width -> math_003.Value
    way_path_visualize.links.new(group_input.outputs[2], math_003.inputs[0])
    #vector_math_002.Vector -> set_position_002.Offset
    way_path_visualize.links.new(vector_math_002.outputs[0], set_position_002.inputs[3])
    #vector_math_004.Vector -> set_position_003.Offset
    way_path_visualize.links.new(vector_math_004.outputs[0], set_position_003.inputs[3])
    #set_material_002.Geometry -> join_geometry.Geometry
    way_path_visualize.links.new(set_material_002.outputs[0], join_geometry.inputs[0])
    #set_material_003.Geometry -> join_geometry.Geometry
    way_path_visualize.links.new(set_material_003.outputs[0], join_geometry.inputs[0])
    #domain_size.Point Count -> math_012.Value
    way_path_visualize.links.new(domain_size.outputs[0], math_012.inputs[1])
    #index_001.Index -> math_007.Value
    way_path_visualize.links.new(index_001.outputs[0], math_007.inputs[0])
    #group_input.Start_Width -> math_014.Value
    way_path_visualize.links.new(group_input.outputs[2], math_014.inputs[0])
    #math_014.Value -> vector_math.Vector
    way_path_visualize.links.new(math_014.outputs[0], vector_math.inputs[1])
    #math_003.Value -> math_013.Value
    way_path_visualize.links.new(math_003.outputs[0], math_013.inputs[0])
    #math_016.Value -> math_013.Value
    way_path_visualize.links.new(math_016.outputs[0], math_013.inputs[1])
    #math_013.Value -> vector_math_002.Vector
    way_path_visualize.links.new(math_013.outputs[0], vector_math_002.inputs[1])
    #math_012.Value -> math_016.Value
    way_path_visualize.links.new(math_012.outputs[0], math_016.inputs[1])
    #group_input.End_Width -> math_015.Value
    way_path_visualize.links.new(group_input.outputs[3], math_015.inputs[0])
    #group_input.Start_Width -> math_015.Value
    way_path_visualize.links.new(group_input.outputs[2], math_015.inputs[1])
    #math_016.Value -> math_014.Value
    way_path_visualize.links.new(math_016.outputs[0], math_014.inputs[1])
    #curve_circle.Curve -> reroute.Input
    way_path_visualize.links.new(curve_circle.outputs[0], reroute.inputs[0])
    #reroute.Output -> curve_to_mesh.Profile Curve
    way_path_visualize.links.new(reroute.outputs[0], curve_to_mesh.inputs[1])
    #reroute.Output -> reroute_001.Input
    way_path_visualize.links.new(reroute.outputs[0], reroute_001.inputs[0])
    #reroute_001.Output -> curve_to_mesh_001.Profile Curve
    way_path_visualize.links.new(reroute_001.outputs[0], curve_to_mesh_001.inputs[1])
    #reroute_001.Output -> reroute_002.Input
    way_path_visualize.links.new(reroute_001.outputs[0], reroute_002.inputs[0])
    #reroute_002.Output -> curve_to_mesh_002.Profile Curve
    way_path_visualize.links.new(reroute_002.outputs[0], curve_to_mesh_002.inputs[1])
    #reroute_002.Output -> reroute_003.Input
    way_path_visualize.links.new(reroute_002.outputs[0], reroute_003.inputs[0])
    #reroute_003.Output -> curve_to_mesh_003.Profile Curve
    way_path_visualize.links.new(reroute_003.outputs[0], curve_to_mesh_003.inputs[1])
    #reroute_003.Output -> reroute_004.Input
    way_path_visualize.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    #reroute_004.Output -> curve_to_mesh_004.Profile Curve
    way_path_visualize.links.new(reroute_004.outputs[0], curve_to_mesh_004.inputs[1])
    #position_001.Position -> set_position_003.Position
    way_path_visualize.links.new(position_001.outputs[0], set_position_003.inputs[2])
    #position_001.Position -> set_position_002.Position
    way_path_visualize.links.new(position_001.outputs[0], set_position_002.inputs[2])
    #reroute_018.Output -> reroute_005.Input
    way_path_visualize.links.new(reroute_018.outputs[0], reroute_005.inputs[0])
    #reroute_005.Output -> domain_size.Geometry
    way_path_visualize.links.new(reroute_005.outputs[0], domain_size.inputs[0])
    #reroute_007.Output -> reroute_006.Input
    way_path_visualize.links.new(reroute_007.outputs[0], reroute_006.inputs[0])
    #reroute_006.Output -> set_position.Geometry
    way_path_visualize.links.new(reroute_006.outputs[0], set_position.inputs[0])
    #reroute_008.Output -> reroute_007.Input
    way_path_visualize.links.new(reroute_008.outputs[0], reroute_007.inputs[0])
    #reroute_007.Output -> set_position_001.Geometry
    way_path_visualize.links.new(reroute_007.outputs[0], set_position_001.inputs[0])
    #reroute_010.Output -> reroute_008.Input
    way_path_visualize.links.new(reroute_010.outputs[0], reroute_008.inputs[0])
    #math_015.Value -> math_016.Value
    way_path_visualize.links.new(math_015.outputs[0], math_016.inputs[0])
    #reroute_010.Output -> set_position_002.Geometry
    way_path_visualize.links.new(reroute_010.outputs[0], set_position_002.inputs[0])
    #math_007.Value -> math_012.Value
    way_path_visualize.links.new(math_007.outputs[0], math_012.inputs[0])
    #group_input.Center_material -> reroute_009.Input
    way_path_visualize.links.new(group_input.outputs[5], reroute_009.inputs[0])
    #group_input.Border_material -> reroute_011.Input
    way_path_visualize.links.new(group_input.outputs[6], reroute_011.inputs[0])
    #group_input.Side_material -> reroute_012.Input
    way_path_visualize.links.new(group_input.outputs[7], reroute_012.inputs[0])
    #reroute_009.Output -> reroute_014.Input
    way_path_visualize.links.new(reroute_009.outputs[0], reroute_014.inputs[0])
    #reroute_011.Output -> reroute_015.Input
    way_path_visualize.links.new(reroute_011.outputs[0], reroute_015.inputs[0])
    #reroute_017.Output -> reroute_016.Input
    way_path_visualize.links.new(reroute_017.outputs[0], reroute_016.inputs[0])
    #reroute_012.Output -> reroute_017.Input
    way_path_visualize.links.new(reroute_012.outputs[0], reroute_017.inputs[0])
    #group_input.Geometry -> reroute_018.Input
    way_path_visualize.links.new(group_input.outputs[0], reroute_018.inputs[0])
    #reroute_018.Output -> reroute_010.Input
    way_path_visualize.links.new(reroute_018.outputs[0], reroute_010.inputs[0])
    #reroute_018.Output -> set_position_003.Geometry
    way_path_visualize.links.new(reroute_018.outputs[0], set_position_003.inputs[0])
    #position.Position -> set_position_001.Position
    way_path_visualize.links.new(position.outputs[0], set_position_001.inputs[2])
    #switch.Output -> vector_math.Vector
    way_path_visualize.links.new(switch.outputs[3], vector_math.inputs[0])
    #vector_math.Vector -> vector_math_001.Vector
    way_path_visualize.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
    #switch.Output -> vector_math_002.Vector
    way_path_visualize.links.new(switch.outputs[3], vector_math_002.inputs[0])
    #reroute_015.Output -> reroute_019.Input
    way_path_visualize.links.new(reroute_015.outputs[0], reroute_019.inputs[0])
    #reroute_014.Output -> set_material_004.Material
    way_path_visualize.links.new(reroute_014.outputs[0], set_material_004.inputs[2])
    #reroute_019.Output -> set_material_003.Material
    way_path_visualize.links.new(reroute_019.outputs[0], set_material_003.inputs[2])
    #reroute_015.Output -> set_material_002.Material
    way_path_visualize.links.new(reroute_015.outputs[0], set_material_002.inputs[2])
    #reroute_016.Output -> set_material.Material
    way_path_visualize.links.new(reroute_016.outputs[0], set_material.inputs[2])
    #reroute_017.Output -> set_material_001.Material
    way_path_visualize.links.new(reroute_017.outputs[0], set_material_001.inputs[2])
    #reroute_013.Output -> reroute_020.Input
    way_path_visualize.links.new(reroute_013.outputs[0], reroute_020.inputs[0])
    #set_spline_type.Curve -> switch_001.True
    way_path_visualize.links.new(set_spline_type.outputs[0], switch_001.inputs[15])
    #set_spline_type_001.Curve -> switch_001.False
    way_path_visualize.links.new(set_spline_type_001.outputs[0], switch_001.inputs[14])
    #set_spline_type_002.Curve -> switch_002.True
    way_path_visualize.links.new(set_spline_type_002.outputs[0], switch_002.inputs[15])
    #set_spline_type_003.Curve -> switch_002.False
    way_path_visualize.links.new(set_spline_type_003.outputs[0], switch_002.inputs[14])
    #reroute_029.Output -> reroute_021.Input
    way_path_visualize.links.new(reroute_029.outputs[0], reroute_021.inputs[0])
    #reroute_021.Output -> switch_002.Switch
    way_path_visualize.links.new(reroute_021.outputs[0], switch_002.inputs[1])
    #set_spline_type_004.Curve -> switch_003.True
    way_path_visualize.links.new(set_spline_type_004.outputs[0], switch_003.inputs[15])
    #set_spline_type_005.Curve -> switch_003.False
    way_path_visualize.links.new(set_spline_type_005.outputs[0], switch_003.inputs[14])
    #set_spline_type_006.Curve -> switch_004.True
    way_path_visualize.links.new(set_spline_type_006.outputs[0], switch_004.inputs[15])
    #set_spline_type_007.Curve -> switch_004.False
    way_path_visualize.links.new(set_spline_type_007.outputs[0], switch_004.inputs[14])
    #set_spline_type_008.Curve -> switch_005.True
    way_path_visualize.links.new(set_spline_type_008.outputs[0], switch_005.inputs[15])
    #set_spline_type_009.Curve -> switch_005.False
    way_path_visualize.links.new(set_spline_type_009.outputs[0], switch_005.inputs[14])
    #reroute_021.Output -> reroute_026.Input
    way_path_visualize.links.new(reroute_021.outputs[0], reroute_026.inputs[0])
    #reroute_026.Output -> switch_003.Switch
    way_path_visualize.links.new(reroute_026.outputs[0], switch_003.inputs[1])
    #reroute_026.Output -> reroute_027.Input
    way_path_visualize.links.new(reroute_026.outputs[0], reroute_027.inputs[0])
    #reroute_027.Output -> switch_004.Switch
    way_path_visualize.links.new(reroute_027.outputs[0], switch_004.inputs[1])
    #reroute_027.Output -> reroute_028.Input
    way_path_visualize.links.new(reroute_027.outputs[0], reroute_028.inputs[0])
    #reroute_028.Output -> switch_005.Switch
    way_path_visualize.links.new(reroute_028.outputs[0], switch_005.inputs[1])
    #group_input.Is_Bezier -> reroute_013.Input
    way_path_visualize.links.new(group_input.outputs[4], reroute_013.inputs[0])
    #reroute_020.Output -> reroute_029.Input
    way_path_visualize.links.new(reroute_020.outputs[0], reroute_029.inputs[0])
    #reroute_029.Output -> switch_001.Switch
    way_path_visualize.links.new(reroute_029.outputs[0], switch_001.inputs[1])
    #set_position.Geometry -> set_spline_type_009.Curve
    way_path_visualize.links.new(set_position.outputs[0], set_spline_type_009.inputs[0])
    #set_position.Geometry -> set_spline_type_008.Curve
    way_path_visualize.links.new(set_position.outputs[0], set_spline_type_008.inputs[0])
    #set_position_001.Geometry -> set_spline_type_007.Curve
    way_path_visualize.links.new(set_position_001.outputs[0], set_spline_type_007.inputs[0])
    #set_position_001.Geometry -> set_spline_type_006.Curve
    way_path_visualize.links.new(set_position_001.outputs[0], set_spline_type_006.inputs[0])
    #reroute_008.Output -> reroute_030.Input
    way_path_visualize.links.new(reroute_008.outputs[0], reroute_030.inputs[0])
    #reroute_030.Output -> set_spline_type_005.Curve
    way_path_visualize.links.new(reroute_030.outputs[0], set_spline_type_005.inputs[0])
    #reroute_030.Output -> set_spline_type_004.Curve
    way_path_visualize.links.new(reroute_030.outputs[0], set_spline_type_004.inputs[0])
    #set_position_002.Geometry -> set_spline_type_003.Curve
    way_path_visualize.links.new(set_position_002.outputs[0], set_spline_type_003.inputs[0])
    #set_position_002.Geometry -> set_spline_type_002.Curve
    way_path_visualize.links.new(set_position_002.outputs[0], set_spline_type_002.inputs[0])
    #set_position_003.Geometry -> set_spline_type_001.Curve
    way_path_visualize.links.new(set_position_003.outputs[0], set_spline_type_001.inputs[0])
    #set_position_003.Geometry -> set_spline_type.Curve
    way_path_visualize.links.new(set_position_003.outputs[0], set_spline_type.inputs[0])
    #switch_002.Output -> curve_to_mesh_003.Curve
    way_path_visualize.links.new(switch_002.outputs[6], curve_to_mesh_003.inputs[0])
    #switch_001.Output -> curve_to_mesh_004.Curve
    way_path_visualize.links.new(switch_001.outputs[6], curve_to_mesh_004.inputs[0])
    #switch_003.Output -> curve_to_mesh_002.Curve
    way_path_visualize.links.new(switch_003.outputs[6], curve_to_mesh_002.inputs[0])
    #switch_004.Output -> curve_to_mesh_001.Curve
    way_path_visualize.links.new(switch_004.outputs[6], curve_to_mesh_001.inputs[0])
    #switch_005.Output -> curve_to_mesh.Curve
    way_path_visualize.links.new(switch_005.outputs[6], curve_to_mesh.inputs[0])
    #curve_to_mesh.Mesh -> set_material.Geometry
    way_path_visualize.links.new(curve_to_mesh.outputs[0], set_material.inputs[0])
    #curve_to_mesh_001.Mesh -> set_material_001.Geometry
    way_path_visualize.links.new(curve_to_mesh_001.outputs[0], set_material_001.inputs[0])
    #curve_to_mesh_002.Mesh -> set_material_004.Geometry
    way_path_visualize.links.new(curve_to_mesh_002.outputs[0], set_material_004.inputs[0])
    #curve_to_mesh_003.Mesh -> set_material_003.Geometry
    way_path_visualize.links.new(curve_to_mesh_003.outputs[0], set_material_003.inputs[0])
    #curve_to_mesh_004.Mesh -> set_material_002.Geometry
    way_path_visualize.links.new(curve_to_mesh_004.outputs[0], set_material_002.inputs[0])
    #value.Value -> math_001.Value
    way_path_visualize.links.new(value.outputs[0], math_001.inputs[1])
    return way_path_visualize
