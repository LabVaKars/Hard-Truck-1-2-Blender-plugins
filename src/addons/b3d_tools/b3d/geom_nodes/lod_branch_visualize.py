import bpy

#initialize lod_branch_visualize node group
def lod_branch_visualize_node_group():
    lod_branch_visualize = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "LOD_branch_visualize")

    

    #initialize lod_branch_visualize nodes
    #node Tube Resolution
    tube_resolution = lod_branch_visualize.nodes.new("FunctionNodeInputInt")
    tube_resolution.label = "Tube Resolution"
    tube_resolution.name = "Tube Resolution"
    tube_resolution.hide = True
    tube_resolution.integer = 3

    #node Circle Resolution
    circle_resolution = lod_branch_visualize.nodes.new("FunctionNodeInputInt")
    circle_resolution.label = "Circle Resolution"
    circle_resolution.name = "Circle Resolution"
    circle_resolution.hide = True
    circle_resolution.integer = 16

    #node Tube Circle
    tube_circle = lod_branch_visualize.nodes.new("GeometryNodeCurvePrimitiveCircle")
    tube_circle.name = "Tube Circle"
    tube_circle.mode = 'RADIUS'
    #Radius
    tube_circle.inputs[4].default_value = 1.0

    #node X Circle
    x_circle = lod_branch_visualize.nodes.new("GeometryNodeCurvePrimitiveCircle")
    x_circle.label = "X Circle"
    x_circle.name = "X Circle"
    x_circle.mode = 'RADIUS'

    #node Y Circle
    y_circle = lod_branch_visualize.nodes.new("GeometryNodeCurvePrimitiveCircle")
    y_circle.label = "Y Circle"
    y_circle.name = "Y Circle"
    y_circle.mode = 'RADIUS'

    #node Z Circle
    z_circle = lod_branch_visualize.nodes.new("GeometryNodeCurvePrimitiveCircle")
    z_circle.label = "Z Circle"
    z_circle.name = "Z Circle"
    z_circle.mode = 'RADIUS'

    #node X Mesh
    x_mesh = lod_branch_visualize.nodes.new("GeometryNodeCurveToMesh")
    x_mesh.label = "X Mesh"
    x_mesh.name = "X Mesh"
    #Fill Caps
    x_mesh.inputs[2].default_value = False

    #node Y Mesh
    y_mesh = lod_branch_visualize.nodes.new("GeometryNodeCurveToMesh")
    y_mesh.label = "Y Mesh"
    y_mesh.name = "Y Mesh"
    #Fill Caps
    y_mesh.inputs[2].default_value = False

    #node Z Mesh
    z_mesh = lod_branch_visualize.nodes.new("GeometryNodeCurveToMesh")
    z_mesh.label = "Z Mesh"
    z_mesh.name = "Z Mesh"
    #Fill Caps
    z_mesh.inputs[2].default_value = False

    #node X Transform
    x_transform = lod_branch_visualize.nodes.new("GeometryNodeTransform")
    x_transform.label = "X Transform"
    x_transform.name = "X Transform"
    x_transform.hide = True
    #Rotation
    x_transform.inputs[2].default_value = (1.5707963705062866, 0.0, 0.0)
    #Scale
    x_transform.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Y Transform
    y_transform = lod_branch_visualize.nodes.new("GeometryNodeTransform")
    y_transform.label = "Y Transform"
    y_transform.name = "Y Transform"
    y_transform.hide = True
    #Rotation
    y_transform.inputs[2].default_value = (0.0, 1.5707963705062866, 0.0)
    #Scale
    y_transform.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Z Transform
    z_transform = lod_branch_visualize.nodes.new("GeometryNodeTransform")
    z_transform.label = "Z Transform"
    z_transform.name = "Z Transform"
    z_transform.hide = True
    #Rotation
    z_transform.inputs[2].default_value = (0.0, 0.0, 1.5707963705062866)
    #Scale
    z_transform.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Set Material
    set_material = lod_branch_visualize.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Join Geometry
    join_geometry = lod_branch_visualize.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    #node LOD_branch_viz_GO
    lod_branch_viz_go = lod_branch_visualize.nodes.new("NodeGroupOutput")
    lod_branch_viz_go.label = "Group Output"
    lod_branch_viz_go.name = "LOD_branch_viz_GO"
    lod_branch_viz_go.is_active_output = True
    #lod_branch_visualize outputs
    #output Geometry
    lod_branch_visualize.outputs.new('NodeSocketGeometry', "Geometry")
    lod_branch_visualize.outputs[0].attribute_domain = 'POINT'



    #node LOD_branch_viz_GI
    lod_branch_viz_gi = lod_branch_visualize.nodes.new("NodeGroupInput")
    lod_branch_viz_gi.label = "Group Output"
    lod_branch_viz_gi.name = "LOD_branch_viz_GI"
    #lod_branch_visualize inputs
    #input Location
    lod_branch_visualize.inputs.new('NodeSocketVector', "Location")
    lod_branch_visualize.inputs[0].attribute_domain = 'POINT'

    #input Radius
    lod_branch_visualize.inputs.new('NodeSocketFloat', "Radius")
    lod_branch_visualize.inputs[1].attribute_domain = 'POINT'

    #input Material
    lod_branch_visualize.inputs.new('NodeSocketMaterial', "Material")
    lod_branch_visualize.inputs[2].attribute_domain = 'POINT'





    #Set locations
    tube_resolution.location = (-4804.38037109375, 6779.18212890625)
    circle_resolution.location = (-4806.86962890625, 6656.40185546875)
    tube_circle.location = (-4638.75439453125, 6803.3203125)
    x_circle.location = (-4632.52001953125, 6662.779296875)
    y_circle.location = (-4638.56494140625, 6510.2060546875)
    z_circle.location = (-4639.80810546875, 6372.072265625)
    x_mesh.location = (-4448.77587890625, 6646.96484375)
    y_mesh.location = (-4451.70751953125, 6504.47265625)
    z_mesh.location = (-4447.81298828125, 6362.9189453125)
    x_transform.location = (-4256.88037109375, 6628.8193359375)
    y_transform.location = (-4259.68896484375, 6485.9306640625)
    z_transform.location = (-4252.93701171875, 6338.02734375)
    set_material.location = (-3873.507080078125, 6419.6962890625)
    join_geometry.location = (-4054.37939453125, 6542.4951171875)
    lod_branch_viz_go.location = (-3699.537353515625, 6536.4755859375)
    lod_branch_viz_gi.location = (-4922.5146484375, 6550.20166015625)

    #initialize lod_branch_visualize links
    #set_material.Geometry -> lod_branch_viz_go.Geometry
    lod_branch_visualize.links.new(set_material.outputs[0], lod_branch_viz_go.inputs[0])
    #x_transform.Geometry -> join_geometry.Geometry
    lod_branch_visualize.links.new(x_transform.outputs[0], join_geometry.inputs[0])
    #y_transform.Geometry -> join_geometry.Geometry
    lod_branch_visualize.links.new(y_transform.outputs[0], join_geometry.inputs[0])
    #z_transform.Geometry -> join_geometry.Geometry
    lod_branch_visualize.links.new(z_transform.outputs[0], join_geometry.inputs[0])
    #z_mesh.Mesh -> z_transform.Geometry
    lod_branch_visualize.links.new(z_mesh.outputs[0], z_transform.inputs[0])
    #tube_circle.Curve -> z_mesh.Profile Curve
    lod_branch_visualize.links.new(tube_circle.outputs[0], z_mesh.inputs[1])
    #tube_resolution.Integer -> tube_circle.Resolution
    lod_branch_visualize.links.new(tube_resolution.outputs[0], tube_circle.inputs[0])
    #circle_resolution.Integer -> z_circle.Resolution
    lod_branch_visualize.links.new(circle_resolution.outputs[0], z_circle.inputs[0])
    #circle_resolution.Integer -> x_circle.Resolution
    lod_branch_visualize.links.new(circle_resolution.outputs[0], x_circle.inputs[0])
    #circle_resolution.Integer -> y_circle.Resolution
    lod_branch_visualize.links.new(circle_resolution.outputs[0], y_circle.inputs[0])
    #x_circle.Curve -> x_mesh.Curve
    lod_branch_visualize.links.new(x_circle.outputs[0], x_mesh.inputs[0])
    #y_circle.Curve -> y_mesh.Curve
    lod_branch_visualize.links.new(y_circle.outputs[0], y_mesh.inputs[0])
    #z_circle.Curve -> z_mesh.Curve
    lod_branch_visualize.links.new(z_circle.outputs[0], z_mesh.inputs[0])
    #x_mesh.Mesh -> x_transform.Geometry
    lod_branch_visualize.links.new(x_mesh.outputs[0], x_transform.inputs[0])
    #y_mesh.Mesh -> y_transform.Geometry
    lod_branch_visualize.links.new(y_mesh.outputs[0], y_transform.inputs[0])
    #tube_circle.Curve -> x_mesh.Profile Curve
    lod_branch_visualize.links.new(tube_circle.outputs[0], x_mesh.inputs[1])
    #tube_circle.Curve -> y_mesh.Profile Curve
    lod_branch_visualize.links.new(tube_circle.outputs[0], y_mesh.inputs[1])
    #join_geometry.Geometry -> set_material.Geometry
    lod_branch_visualize.links.new(join_geometry.outputs[0], set_material.inputs[0])
    #lod_branch_viz_gi.Radius -> x_circle.Radius
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[1], x_circle.inputs[4])
    #lod_branch_viz_gi.Radius -> y_circle.Radius
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[1], y_circle.inputs[4])
    #lod_branch_viz_gi.Radius -> z_circle.Radius
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[1], z_circle.inputs[4])
    #lod_branch_viz_gi.Location -> x_transform.Translation
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[0], x_transform.inputs[1])
    #lod_branch_viz_gi.Location -> y_transform.Translation
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[0], y_transform.inputs[1])
    #lod_branch_viz_gi.Location -> z_transform.Translation
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[0], z_transform.inputs[1])
    #lod_branch_viz_gi.Material -> set_material.Material
    lod_branch_visualize.links.new(lod_branch_viz_gi.outputs[2], set_material.inputs[2])
    return lod_branch_visualize
