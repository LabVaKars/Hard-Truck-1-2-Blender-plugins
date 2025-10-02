import bpy

#initialize get_tangent_point_xy node group
def get_tangent_point_xy_node_group():
    get_tangent_point_xy = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "get_tangent_point_xy")

    

    #initialize get_tangent_point_xy nodes
    #node Render_branch_visualize_GO
    render_branch_visualize_go = get_tangent_point_xy.nodes.new("NodeGroupOutput")
    render_branch_visualize_go.label = "Group Output"
    render_branch_visualize_go.name = "Render_branch_visualize_GO"
    render_branch_visualize_go.is_active_output = True
    #get_tangent_point_xy outputs
    #output P
    get_tangent_point_xy.outputs.new('NodeSocketVectorXYZ', "P")
    get_tangent_point_xy.outputs[0].attribute_domain = 'POINT'

    #output Angle_rad
    get_tangent_point_xy.outputs.new('NodeSocketFloat', "Angle_rad")
    get_tangent_point_xy.outputs[1].attribute_domain = 'POINT'



    #node dy_
    dy_ = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    dy_.label = "dy_"
    dy_.name = "dy_"
    dy_.hide = True
    dy_.operation = 'MULTIPLY'
    dy_.use_clamp = False
    #Value_001
    dy_.inputs[1].default_value = 1.0

    #node dx_
    dx_ = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    dx_.label = "dx_"
    dx_.name = "dx_"
    dx_.hide = True
    dx_.operation = 'MULTIPLY'
    dx_.use_clamp = False
    #Value_001
    dx_.inputs[1].default_value = 1.0

    #node Render_branch_visualize_GI
    render_branch_visualize_gi = get_tangent_point_xy.nodes.new("NodeGroupInput")
    render_branch_visualize_gi.label = "Group Input"
    render_branch_visualize_gi.name = "Render_branch_visualize_GI"
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



    #node Length_dx_dy_dz
    length_dx_dy_dz = get_tangent_point_xy.nodes.new("ShaderNodeVectorMath")
    length_dx_dy_dz.label = "Length_dx_dy_dz"
    length_dx_dy_dz.name = "Length_dx_dy_dz"
    length_dx_dy_dz.hide = True
    length_dx_dy_dz.operation = 'DISTANCE'
    #Vector_001
    length_dx_dy_dz.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node Combine_dx_dy_dz
    combine_dx_dy_dz = get_tangent_point_xy.nodes.new("ShaderNodeCombineXYZ")
    combine_dx_dy_dz.label = "Combine_dx_dy_dz"
    combine_dx_dy_dz.name = "Combine_dx_dy_dz"
    combine_dx_dy_dz.hide = True
    #Z
    combine_dx_dy_dz.inputs[2].default_value = 0.0

    #node Div_dy
    div_dy = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    div_dy.label = "dy"
    div_dy.name = "Div_dy"
    div_dy.hide = True
    div_dy.operation = 'DIVIDE'
    div_dy.use_clamp = False

    #node Div_dx
    div_dx = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    div_dx.label = "dx"
    div_dx.name = "Div_dx"
    div_dx.hide = True
    div_dx.operation = 'DIVIDE'
    div_dx.use_clamp = False

    #node Angle_XY
    angle_xy = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    angle_xy.label = "Angle"
    angle_xy.name = "Angle_XY"
    angle_xy.hide = True
    angle_xy.operation = 'ARCTAN2'
    angle_xy.use_clamp = False

    #node Tx
    tx = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    tx.label = "Tx"
    tx.name = "Tx"
    tx.hide = True
    tx.operation = 'MULTIPLY'
    tx.use_clamp = False
    #Value_001
    tx.inputs[1].default_value = -1.0

    #node Ty
    ty = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    ty.label = "Ty"
    ty.name = "Ty"
    ty.hide = True
    ty.operation = 'MULTIPLY'
    ty.use_clamp = False
    #Value_001
    ty.inputs[1].default_value = 1.0

    #node Px
    px = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    px.label = "Px"
    px.name = "Px"
    px.hide = True
    px.operation = 'MULTIPLY'
    px.use_clamp = False

    #node Py
    py = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    py.label = "Py"
    py.name = "Py"
    py.hide = True
    py.operation = 'MULTIPLY'
    py.use_clamp = False

    #node Abs_tx
    abs_tx = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    abs_tx.label = "Abs(Tx)"
    abs_tx.name = "Abs_tx"
    abs_tx.hide = True
    abs_tx.operation = 'ABSOLUTE'
    abs_tx.use_clamp = False

    #node Abs_ty
    abs_ty = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    abs_ty.label = "Abs(Ty)"
    abs_ty.name = "Abs_ty"
    abs_ty.hide = True
    abs_ty.operation = 'ABSOLUTE'
    abs_ty.use_clamp = False

    #node Abs_ty_lt_eps
    abs_ty_lt_eps = get_tangent_point_xy.nodes.new("FunctionNodeCompare")
    abs_ty_lt_eps.label = "abs(Ty) < eps"
    abs_ty_lt_eps.name = "Abs_ty_lt_eps"
    abs_ty_lt_eps.hide = True
    abs_ty_lt_eps.data_type = 'FLOAT'
    abs_ty_lt_eps.mode = 'ELEMENT'
    abs_ty_lt_eps.operation = 'LESS_THAN'

    #node Abs_tx_lt_eps
    abs_tx_lt_eps = get_tangent_point_xy.nodes.new("FunctionNodeCompare")
    abs_tx_lt_eps.label = "abs(Tx) < eps"
    abs_tx_lt_eps.name = "Abs_tx_lt_eps"
    abs_tx_lt_eps.hide = True
    abs_tx_lt_eps.data_type = 'FLOAT'
    abs_tx_lt_eps.mode = 'ELEMENT'
    abs_tx_lt_eps.operation = 'LESS_THAN'

    #node sTx
    stx = get_tangent_point_xy.nodes.new("GeometryNodeSwitch")
    stx.label = "sTx"
    stx.name = "sTx"
    stx.hide = True
    stx.input_type = 'FLOAT'
    #True
    stx.inputs[3].default_value = 1.0

    #node sTy
    sty = get_tangent_point_xy.nodes.new("GeometryNodeSwitch")
    sty.label = "sTy"
    sty.name = "sTy"
    sty.hide = True
    sty.input_type = 'FLOAT'
    #True
    sty.inputs[3].default_value = 1.0

    #node x_minus_Px
    x_minus_px = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    x_minus_px.label = "x-Px"
    x_minus_px.name = "x_minus_Px"
    x_minus_px.hide = True
    x_minus_px.operation = 'SUBTRACT'
    x_minus_px.use_clamp = False

    #node y_minus_Py
    y_minus_py = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    y_minus_py.label = "y-Py"
    y_minus_py.name = "y_minus_Py"
    y_minus_py.hide = True
    y_minus_py.operation = 'SUBTRACT'
    y_minus_py.use_clamp = False

    #node Abs_tx_gte_abs_ty
    abs_tx_gte_abs_ty = get_tangent_point_xy.nodes.new("FunctionNodeCompare")
    abs_tx_gte_abs_ty.label = "abs(Tx) >= abs(Ty)"
    abs_tx_gte_abs_ty.name = "Abs_tx_gte_abs_ty"
    abs_tx_gte_abs_ty.hide = True
    abs_tx_gte_abs_ty.data_type = 'FLOAT'
    abs_tx_gte_abs_ty.mode = 'ELEMENT'
    abs_tx_gte_abs_ty.operation = 'GREATER_EQUAL'

    #node t2
    t2 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    t2.label = "t2 = (y-Py) / Ty"
    t2.name = "t2"
    t2.hide = True
    t2.operation = 'DIVIDE'
    t2.use_clamp = False

    #node t1
    t1 = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    t1.label = "t1 = (x-Px) / Tx"
    t1.name = "t1"
    t1.hide = True
    t1.operation = 'DIVIDE'
    t1.use_clamp = False

    #node switch_t
    switch_t = get_tangent_point_xy.nodes.new("GeometryNodeSwitch")
    switch_t.label = "switch_t"
    switch_t.name = "switch_t"
    switch_t.hide = True
    switch_t.input_type = 'FLOAT'

    #node tx_mult_t
    tx_mult_t = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    tx_mult_t.label = "Tx*t"
    tx_mult_t.name = "tx_mult_t"
    tx_mult_t.hide = True
    tx_mult_t.operation = 'MULTIPLY'
    tx_mult_t.use_clamp = False

    #node Ty_mult_t
    ty_mult_t = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    ty_mult_t.label = "Ty*t"
    ty_mult_t.name = "Ty_mult_t"
    ty_mult_t.hide = True
    ty_mult_t.operation = 'MULTIPLY'
    ty_mult_t.use_clamp = False

    #node Px_plus_Tx_mult_t
    px_plus_tx_mult_t = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    px_plus_tx_mult_t.label = "Px + Tx*t"
    px_plus_tx_mult_t.name = "Px_plus_Tx_mult_t"
    px_plus_tx_mult_t.hide = True
    px_plus_tx_mult_t.operation = 'ADD'
    px_plus_tx_mult_t.use_clamp = False

    #node Py_plus_Ty_mult_t
    py_plus_ty_mult_t = get_tangent_point_xy.nodes.new("ShaderNodeMath")
    py_plus_ty_mult_t.label = "Py + Ty*t"
    py_plus_ty_mult_t.name = "Py_plus_Ty_mult_t"
    py_plus_ty_mult_t.hide = True
    py_plus_ty_mult_t.operation = 'ADD'
    py_plus_ty_mult_t.use_clamp = False

    #node Combine_P
    combine_p = get_tangent_point_xy.nodes.new("ShaderNodeCombineXYZ")
    combine_p.label = "P"
    combine_p.name = "Combine_P"
    combine_p.hide = True



    #Set locations
    render_branch_visualize_go.location = (262.1426086425781, 105.40538787841797)
    dy_.location = (-2252.601806640625, 78.76036071777344)
    dx_.location = (-2254.718505859375, 128.2964630126953)
    render_branch_visualize_gi.location = (-2449.834716796875, 83.74897766113281)
    length_dx_dy_dz.location = (-2067.8818359375, -132.85516357421875)
    combine_dx_dy_dz.location = (-2071.47802734375, -79.78509521484375)
    div_dy.location = (-1836.9747314453125, 168.88699340820312)
    div_dx.location = (-1839.1451416015625, 213.9760284423828)
    angle_xy.location = (-1817.9239501953125, 5.013556480407715)
    tx.location = (-1624.0460205078125, -79.62294006347656)
    ty.location = (-1621.9293212890625, -129.15904235839844)
    px.location = (-1619.9881591796875, -187.0582275390625)
    py.location = (-1618.655517578125, -233.82467651367188)
    abs_tx.location = (-1432.6092529296875, -256.81280517578125)
    abs_ty.location = (-1434.609130859375, -305.6598205566406)
    abs_ty_lt_eps.location = (-1159.44677734375, 297.7275390625)
    abs_tx_lt_eps.location = (-1164.778564453125, 349.5951232910156)
    stx.location = (-982.9664306640625, 271.38482666015625)
    sty.location = (-985.5628662109375, 176.93887329101562)
    x_minus_px.location = (-980.0999755859375, 226.00155639648438)
    y_minus_py.location = (-985.4927978515625, 133.63079833984375)
    abs_tx_gte_abs_ty.location = (-793.8845825195312, -122.5412826538086)
    t2.location = (-780.565673828125, 67.53253936767578)
    t1.location = (-782.0009155273438, 130.10182189941406)
    switch_t.location = (-573.0861206054688, -18.686120986938477)
    tx_mult_t.location = (-354.04443359375, 132.81881713867188)
    ty_mult_t.location = (-351.10443115234375, 61.246604919433594)
    px_plus_tx_mult_t.location = (-165.53045654296875, 131.01614379882812)
    py_plus_ty_mult_t.location = (-170.2501220703125, 66.63573455810547)
    combine_p.location = (39.724769592285156, 125.01004791259766)

    #initialize get_tangent_point_xy links
    #render_branch_visualize_gi.X -> dx_.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[0], dx_.inputs[0])
    #render_branch_visualize_gi.Y -> dy_.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[1], dy_.inputs[0])
    #dx_.Value -> combine_dx_dy_dz.X
    get_tangent_point_xy.links.new(dx_.outputs[0], combine_dx_dy_dz.inputs[0])
    #dy_.Value -> combine_dx_dy_dz.Y
    get_tangent_point_xy.links.new(dy_.outputs[0], combine_dx_dy_dz.inputs[1])
    #combine_dx_dy_dz.Vector -> length_dx_dy_dz.Vector
    get_tangent_point_xy.links.new(combine_dx_dy_dz.outputs[0], length_dx_dy_dz.inputs[0])
    #dx_.Value -> div_dx.Value
    get_tangent_point_xy.links.new(dx_.outputs[0], div_dx.inputs[0])
    #length_dx_dy_dz.Value -> div_dx.Value
    get_tangent_point_xy.links.new(length_dx_dy_dz.outputs[1], div_dx.inputs[1])
    #dy_.Value -> div_dy.Value
    get_tangent_point_xy.links.new(dy_.outputs[0], div_dy.inputs[0])
    #length_dx_dy_dz.Value -> div_dy.Value
    get_tangent_point_xy.links.new(length_dx_dy_dz.outputs[1], div_dy.inputs[1])
    #div_dx.Value -> px.Value
    get_tangent_point_xy.links.new(div_dx.outputs[0], px.inputs[0])
    #render_branch_visualize_gi.R -> px.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[3], px.inputs[1])
    #div_dy.Value -> py.Value
    get_tangent_point_xy.links.new(div_dy.outputs[0], py.inputs[0])
    #render_branch_visualize_gi.R -> py.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[3], py.inputs[1])
    #div_dx.Value -> ty.Value
    get_tangent_point_xy.links.new(div_dx.outputs[0], ty.inputs[0])
    #div_dy.Value -> tx.Value
    get_tangent_point_xy.links.new(div_dy.outputs[0], tx.inputs[0])
    #tx.Value -> abs_tx.Value
    get_tangent_point_xy.links.new(tx.outputs[0], abs_tx.inputs[0])
    #ty.Value -> abs_ty.Value
    get_tangent_point_xy.links.new(ty.outputs[0], abs_ty.inputs[0])
    #abs_tx.Value -> abs_tx_gte_abs_ty.A
    get_tangent_point_xy.links.new(abs_tx.outputs[0], abs_tx_gte_abs_ty.inputs[0])
    #abs_ty.Value -> abs_tx_gte_abs_ty.B
    get_tangent_point_xy.links.new(abs_ty.outputs[0], abs_tx_gte_abs_ty.inputs[1])
    #abs_tx_gte_abs_ty.Result -> switch_t.Switch
    get_tangent_point_xy.links.new(abs_tx_gte_abs_ty.outputs[0], switch_t.inputs[0])
    #render_branch_visualize_gi.eps -> abs_tx_lt_eps.B
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[6], abs_tx_lt_eps.inputs[1])
    #abs_tx.Value -> abs_tx_lt_eps.A
    get_tangent_point_xy.links.new(abs_tx.outputs[0], abs_tx_lt_eps.inputs[0])
    #abs_tx_lt_eps.Result -> stx.Switch
    get_tangent_point_xy.links.new(abs_tx_lt_eps.outputs[0], stx.inputs[1])
    #abs_tx_lt_eps.Result -> stx.Switch
    get_tangent_point_xy.links.new(abs_tx_lt_eps.outputs[0], stx.inputs[0])
    #tx.Value -> stx.False
    get_tangent_point_xy.links.new(tx.outputs[0], stx.inputs[2])
    #render_branch_visualize_gi.eps -> abs_ty_lt_eps.B
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[6], abs_ty_lt_eps.inputs[1])
    #abs_ty.Value -> abs_ty_lt_eps.A
    get_tangent_point_xy.links.new(abs_ty.outputs[0], abs_ty_lt_eps.inputs[0])
    #abs_ty_lt_eps.Result -> sty.Switch
    get_tangent_point_xy.links.new(abs_ty_lt_eps.outputs[0], sty.inputs[0])
    #ty.Value -> sty.False
    get_tangent_point_xy.links.new(ty.outputs[0], sty.inputs[2])
    #px.Value -> x_minus_px.Value
    get_tangent_point_xy.links.new(px.outputs[0], x_minus_px.inputs[1])
    #py.Value -> y_minus_py.Value
    get_tangent_point_xy.links.new(py.outputs[0], y_minus_py.inputs[1])
    #x_minus_px.Value -> t1.Value
    get_tangent_point_xy.links.new(x_minus_px.outputs[0], t1.inputs[0])
    #stx.Output -> t1.Value
    get_tangent_point_xy.links.new(stx.outputs[0], t1.inputs[1])
    #sty.Output -> t2.Value
    get_tangent_point_xy.links.new(sty.outputs[0], t2.inputs[1])
    #tx.Value -> tx_mult_t.Value
    get_tangent_point_xy.links.new(tx.outputs[0], tx_mult_t.inputs[0])
    #ty.Value -> ty_mult_t.Value
    get_tangent_point_xy.links.new(ty.outputs[0], ty_mult_t.inputs[0])
    #px.Value -> px_plus_tx_mult_t.Value
    get_tangent_point_xy.links.new(px.outputs[0], px_plus_tx_mult_t.inputs[0])
    #tx_mult_t.Value -> px_plus_tx_mult_t.Value
    get_tangent_point_xy.links.new(tx_mult_t.outputs[0], px_plus_tx_mult_t.inputs[1])
    #ty_mult_t.Value -> py_plus_ty_mult_t.Value
    get_tangent_point_xy.links.new(ty_mult_t.outputs[0], py_plus_ty_mult_t.inputs[1])
    #py.Value -> py_plus_ty_mult_t.Value
    get_tangent_point_xy.links.new(py.outputs[0], py_plus_ty_mult_t.inputs[0])
    #px_plus_tx_mult_t.Value -> combine_p.X
    get_tangent_point_xy.links.new(px_plus_tx_mult_t.outputs[0], combine_p.inputs[0])
    #py_plus_ty_mult_t.Value -> combine_p.Y
    get_tangent_point_xy.links.new(py_plus_ty_mult_t.outputs[0], combine_p.inputs[1])
    #render_branch_visualize_gi.Z -> combine_p.Z
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[2], combine_p.inputs[2])
    #t1.Value -> switch_t.True
    get_tangent_point_xy.links.new(t1.outputs[0], switch_t.inputs[3])
    #t2.Value -> switch_t.False
    get_tangent_point_xy.links.new(t2.outputs[0], switch_t.inputs[2])
    #switch_t.Output -> ty_mult_t.Value
    get_tangent_point_xy.links.new(switch_t.outputs[0], ty_mult_t.inputs[1])
    #switch_t.Output -> tx_mult_t.Value
    get_tangent_point_xy.links.new(switch_t.outputs[0], tx_mult_t.inputs[1])
    #combine_p.Vector -> render_branch_visualize_go.P
    get_tangent_point_xy.links.new(combine_p.outputs[0], render_branch_visualize_go.inputs[0])
    #angle_xy.Value -> render_branch_visualize_go.Angle_rad
    get_tangent_point_xy.links.new(angle_xy.outputs[0], render_branch_visualize_go.inputs[1])
    #render_branch_visualize_gi.px -> x_minus_px.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[4], x_minus_px.inputs[0])
    #render_branch_visualize_gi.py -> y_minus_py.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[5], y_minus_py.inputs[0])
    #y_minus_py.Value -> t2.Value
    get_tangent_point_xy.links.new(y_minus_py.outputs[0], t2.inputs[0])
    #render_branch_visualize_gi.Y -> angle_xy.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[1], angle_xy.inputs[0])
    #render_branch_visualize_gi.X -> angle_xy.Value
    get_tangent_point_xy.links.new(render_branch_visualize_gi.outputs[0], angle_xy.inputs[1])
    return get_tangent_point_xy
