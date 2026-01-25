import bpy

#initialize portal_visualize node group
def portal_visualize_node_group():
    portal_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Portal_visualize")

    

    #initialize portal_visualize nodes
    #node Resample Curve
    resample_curve = portal_visualize.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.mode = 'COUNT'
    #Selection
    resample_curve.inputs[1].default_value = True
    #Count
    resample_curve.inputs[2].default_value = 2

    #node Curve to Points
    curve_to_points = portal_visualize.nodes.new("GeometryNodeCurveToPoints")
    curve_to_points.name = "Curve to Points"
    curve_to_points.mode = 'EVALUATED'

    #node Position
    position = portal_visualize.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Group Input
    group_input = portal_visualize.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    #portal_visualize inputs
    #input Geometry
    portal_visualize.inputs.new('NodeSocketGeometry', "Geometry")
    portal_visualize.inputs[0].attribute_domain = 'POINT'



    #node Separate XYZ.001
    separate_xyz_001 = portal_visualize.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.hide = True

    #node Separate XYZ
    separate_xyz = portal_visualize.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.hide = True

    #node Position.001
    position_001 = portal_visualize.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    #node Index
    index = portal_visualize.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"

    #node Group Output
    group_output = portal_visualize.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    #portal_visualize outputs
    #output Geometry
    portal_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    portal_visualize.outputs[0].attribute_domain = 'POINT'



    #node Sample Index.002
    sample_index_002 = portal_visualize.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'

    #node Grid
    grid = portal_visualize.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    #Size X
    grid.inputs[0].default_value = 1.0
    #Size Y
    grid.inputs[1].default_value = 1.0
    #Vertices X
    grid.inputs[2].default_value = 2
    #Vertices Y
    grid.inputs[3].default_value = 2

    #node Set Position
    set_position = portal_visualize.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Selection
    set_position.inputs[1].default_value = True
    #Offset
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)

    #node Sample Index.001
    sample_index_001 = portal_visualize.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.hide = True
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'
    #Index
    sample_index_001.inputs[6].default_value = 1

    #node Combine XYZ
    combine_xyz = portal_visualize.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.hide = True

    #node Sample Index
    sample_index = portal_visualize.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.hide = True
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'
    #Index
    sample_index.inputs[6].default_value = 0

    #node Combine XYZ.001
    combine_xyz_001 = portal_visualize.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.hide = True

    #node Quadrilateral
    quadrilateral = portal_visualize.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    quadrilateral.name = "Quadrilateral"
    quadrilateral.mode = 'POINTS'



    #Set locations
    resample_curve.location = (-560.0, 100.0)
    curve_to_points.location = (-360.0, 100.0)
    position.location = (-360.0, -100.0)
    group_input.location = (-740.0, 100.0)
    separate_xyz_001.location = (40.0, 180.0)
    separate_xyz.location = (40.0, 240.0)
    position_001.location = (400.0, 0.0)
    index.location = (400.0, -60.0)
    group_output.location = (1140.0, 80.0)
    sample_index_002.location = (620.0, 160.0)
    grid.location = (620.0, 360.0)
    set_position.location = (840.0, 260.0)
    sample_index_001.location = (-140.0, 120.0)
    combine_xyz.location = (220.0, 240.0)
    sample_index.location = (-140.0, 60.0)
    combine_xyz_001.location = (220.0, 180.0)
    quadrilateral.location = (400.0, 200.0)

    #Set dimensions
    resample_curve.width, resample_curve.height = 140.0, 100.0
    curve_to_points.width, curve_to_points.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    sample_index_002.width, sample_index_002.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    sample_index_001.width, sample_index_001.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    sample_index.width, sample_index.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    quadrilateral.width, quadrilateral.height = 140.0, 100.0

    #initialize portal_visualize links
    #resample_curve.Curve -> curve_to_points.Curve
    portal_visualize.links.new(resample_curve.outputs[0], curve_to_points.inputs[0])
    #group_input.Geometry -> resample_curve.Curve
    portal_visualize.links.new(group_input.outputs[0], resample_curve.inputs[0])
    #curve_to_points.Points -> sample_index.Geometry
    portal_visualize.links.new(curve_to_points.outputs[0], sample_index.inputs[0])
    #position.Position -> sample_index.Value
    portal_visualize.links.new(position.outputs[0], sample_index.inputs[3])
    #position.Position -> sample_index_001.Value
    portal_visualize.links.new(position.outputs[0], sample_index_001.inputs[3])
    #curve_to_points.Points -> sample_index_001.Geometry
    portal_visualize.links.new(curve_to_points.outputs[0], sample_index_001.inputs[0])
    #sample_index.Value -> separate_xyz_001.Vector
    portal_visualize.links.new(sample_index.outputs[2], separate_xyz_001.inputs[0])
    #separate_xyz.X -> combine_xyz.X
    portal_visualize.links.new(separate_xyz.outputs[0], combine_xyz.inputs[0])
    #separate_xyz.Y -> combine_xyz.Y
    portal_visualize.links.new(separate_xyz.outputs[1], combine_xyz.inputs[1])
    #separate_xyz_001.Z -> combine_xyz.Z
    portal_visualize.links.new(separate_xyz_001.outputs[2], combine_xyz.inputs[2])
    #separate_xyz.Z -> combine_xyz_001.Z
    portal_visualize.links.new(separate_xyz.outputs[2], combine_xyz_001.inputs[2])
    #separate_xyz_001.X -> combine_xyz_001.X
    portal_visualize.links.new(separate_xyz_001.outputs[0], combine_xyz_001.inputs[0])
    #separate_xyz_001.Y -> combine_xyz_001.Y
    portal_visualize.links.new(separate_xyz_001.outputs[1], combine_xyz_001.inputs[1])
    #quadrilateral.Curve -> sample_index_002.Geometry
    portal_visualize.links.new(quadrilateral.outputs[0], sample_index_002.inputs[0])
    #position_001.Position -> sample_index_002.Value
    portal_visualize.links.new(position_001.outputs[0], sample_index_002.inputs[1])
    #index.Index -> sample_index_002.Index
    portal_visualize.links.new(index.outputs[0], sample_index_002.inputs[6])
    #position_001.Position -> sample_index_002.Value
    portal_visualize.links.new(position_001.outputs[0], sample_index_002.inputs[3])
    #sample_index_002.Value -> set_position.Position
    portal_visualize.links.new(sample_index_002.outputs[2], set_position.inputs[2])
    #grid.Mesh -> set_position.Geometry
    portal_visualize.links.new(grid.outputs[0], set_position.inputs[0])
    #set_position.Geometry -> group_output.Geometry
    portal_visualize.links.new(set_position.outputs[0], group_output.inputs[0])
    #sample_index_001.Value -> separate_xyz.Vector
    portal_visualize.links.new(sample_index_001.outputs[2], separate_xyz.inputs[0])
    #sample_index_001.Value -> quadrilateral.Point 1
    portal_visualize.links.new(sample_index_001.outputs[2], quadrilateral.inputs[7])
    #combine_xyz.Vector -> quadrilateral.Point 2
    portal_visualize.links.new(combine_xyz.outputs[0], quadrilateral.inputs[8])
    #sample_index.Value -> quadrilateral.Point 4
    portal_visualize.links.new(sample_index.outputs[2], quadrilateral.inputs[10])
    #combine_xyz_001.Vector -> quadrilateral.Point 3
    portal_visualize.links.new(combine_xyz_001.outputs[0], quadrilateral.inputs[9])
    return portal_visualize
