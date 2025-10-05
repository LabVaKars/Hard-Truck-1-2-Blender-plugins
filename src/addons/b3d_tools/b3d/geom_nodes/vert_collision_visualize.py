import bpy

#initialize vert_collision_visualize node group
def vert_collision_visualize_node_group():
    vert_collision_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Vert_collision_visualize")

    

    #initialize vert_collision_visualize nodes
    #node Group Input
    group_input = vert_collision_visualize.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    #vert_collision_visualize inputs
    #input Geometry
    vert_collision_visualize.inputs.new('NodeSocketGeometry', "Geometry")
    vert_collision_visualize.inputs[0].attribute_domain = 'POINT'



    #node Curve to Mesh
    curve_to_mesh = vert_collision_visualize.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    #Fill Caps
    curve_to_mesh.inputs[2].default_value = False

    #node Extrude Mesh
    extrude_mesh = vert_collision_visualize.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'EDGES'
    #Selection
    extrude_mesh.inputs[1].default_value = True

    #node Group Output
    group_output = vert_collision_visualize.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    #vert_collision_visualize outputs
    #output Geometry
    vert_collision_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    vert_collision_visualize.outputs[0].attribute_domain = 'POINT'



    #node Combine XYZ
    combine_xyz = vert_collision_visualize.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.hide = True
    #X
    combine_xyz.inputs[0].default_value = 0.0
    #Y
    combine_xyz.inputs[1].default_value = 0.0
    #Z
    combine_xyz.inputs[2].default_value = 1.0

    #node Value
    value = vert_collision_visualize.nodes.new("ShaderNodeValue")
    value.label = "Height"
    value.name = "Value"

    value.outputs[0].default_value = 10.0


    #Set locations
    group_input.location = (-700.0, 0.0)
    curve_to_mesh.location = (-480.0, 20.0)
    extrude_mesh.location = (-240.0, 20.0)
    group_output.location = (60.0, 20.0)
    combine_xyz.location = (-480.0, -120.0)
    value.location = (-480.0, -160.0)

    #initialize vert_collision_visualize links
    #curve_to_mesh.Mesh -> extrude_mesh.Mesh
    vert_collision_visualize.links.new(curve_to_mesh.outputs[0], extrude_mesh.inputs[0])
    #combine_xyz.Vector -> extrude_mesh.Offset
    vert_collision_visualize.links.new(combine_xyz.outputs[0], extrude_mesh.inputs[2])
    #group_input.Geometry -> curve_to_mesh.Curve
    vert_collision_visualize.links.new(group_input.outputs[0], curve_to_mesh.inputs[0])
    #extrude_mesh.Mesh -> group_output.Geometry
    vert_collision_visualize.links.new(extrude_mesh.outputs[0], group_output.inputs[0])
    #value.Value -> extrude_mesh.Offset Scale
    vert_collision_visualize.links.new(value.outputs[0], extrude_mesh.inputs[3])
    return vert_collision_visualize

