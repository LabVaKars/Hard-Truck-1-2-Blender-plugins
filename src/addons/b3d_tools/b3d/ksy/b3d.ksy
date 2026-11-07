# Fast Python variant with per-sibling block groups (444 delimiters).
# Captures both leading and trailing 444 values while retaining byte buffers.
# Fast Python variant: fixed-stride data is stored as raw bytes.
# `size` below is only on raw bytes or primitive strings: no extra substreams.
# See b3d_geometry_decode.py to decode geometry lazily with struct.
meta:
  id: ht2_b3d
  application: Дальнобойщики 2 (8.x) / Hard Truck 2 King of The Road 1.3
  file-extension: b3d
  license: MIT
  endian: le
doc: 'Models, game logic objects (Optimized for Python: mesh and numeric arrays stored as raw byte buffers for on-demand
  decoding.)'
enums:
  identifiers:
    111: nodes_section_start
    222: nodes_section_end
    333: nodes_end
    444: nodes_group
    555: nodes_start

types:
  file_header:
    seq:
      - id: magic
        contents: [0x62, 0x33, 0x64, 0x00]
      - id: len_file
        type: s4
      - id: ofc_materials
        type: s4
      - id: len_materials_section
        type: s4
      - id: ofc_nodes
        type: s4
      - id: len_nodes
        type: s4
# a
  point:
    seq:
      - id: value
        type: f4
        repeat: expr
        repeat-expr: 3

  color:
    seq:
      - id: value
        type: f4
        repeat: expr
        repeat-expr: 3

  sphere:
    seq:
      - id: value
        type: f4
        repeat: expr
        repeat-expr: 4

  materials_list:
    seq:
      - id: mat_count
        type: s4
      - id: mat_names
        type: str
        repeat: expr
        repeat-expr: mat_count

        encoding: UTF-8
        size: 32

  children:
    seq:
      - id: child_cnt
        type: s4
      - id: child_block
        # Group numbers are local to this list of children.
        # The previous sibling has already been parsed when this is evaluated.
        type: 'block(_index == 0 ? 0 : child_block[_index - 1].next_group, _io.pos)'
        repeat: expr
        repeat-expr: child_cnt

  polygon_8:
    params:
      - id: p_start_pos
        type: s4
    instances:
      start_pos:
        value: 'p_start_pos'
      texnum_pos1:
        value: 'p_start_pos + 12'
      format:
        value: 'format_raw ^ 1'
      use_uv:
        value: 'format & 0b10 > 0'
      use_normal:
        value: '((format & 0b100000) > 0) and ((format & 0b10000) > 0)'
      uv_count:
        value: '((format & 0xff00) >> 8) + (use_uv ? 1 : 0)'
      normal_switch:
        value: 'not (use_normal) ? -1 : (format & 1) > 0 ? 0 : 1'
      verts_pos:
        value: p_start_pos + 20
    seq:
      - id: format_raw
        type: s4
      - id: unk_f
        type: f4
      - id: unk_i
        type: s4
      - id: texnum
        type: s4
      - id: vert_count
        type: s4
      - id: verts_raw
        size: 'vert_count * (4 + (use_uv ? uv_count * 8 : 0) + (use_normal ? (normal_switch == 0 ? 12 : 4) : 0))'
  
  polygon_28:
    params:
      - id: p_start_pos
        type: s4
    instances:
      format:
        value: 'format_raw'
      use_uv:
        value: 'format & 0b10 > 0'
      use_normal:
        value: '((format & 0b100000) > 0) and ((format & 0b10000) > 0)'
      uv_count:
        value: '((format & 0xff00) >> 8) + 1'
      normal_switch:
        value: 'not (use_normal) ? -1 : (format & 1) > 0 ? 0 : 1'
      start_pos:
        value: p_start_pos
      verts_pos:
        value: p_start_pos + 20
    seq:
      - id: format_raw
        type: s4
      - id: unk_f
        type: f4
      - id: unk_i
        type: s4
      - id: texnum
        type: s4
      - id: vert_count
        type: s4
      - id: verts_raw
        size: 'vert_count * (8 + (use_uv ? uv_count * 8 : 0))'

  b_unused:
    seq:
      - id: content
        type: f4
        repeat: expr
        repeat-expr: 11

  b_observer:
    instances:
      string1:
        value: 'name1'
      string2:
        value: 'name2'
    seq:
      - id: name1
        type: str
        encoding: UTF-8
        size: 32
      - id: name2
        type: str

        encoding: UTF-8
        size: 32

  b_render_order:
    instances:
      vector1:
        value: 'center'
      float1:
        value: 'length'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: length
        type: f4
      - id: child_blocks
        type: children

  b_container_ordered:
    seq:
      - id: bound1
        type: sphere
      - id: child_blocks
        type: children

  b_container_spaced:
    instances:
      string1:
        value: 'space_name'
      string2:
        value: 'collision_name'
    seq:
      - id: bound1
        type: sphere
      - id: space_name
        type: str
        encoding: UTF-8
        size: 32
      - id: collision_name
        type: str
        encoding: UTF-8
        size: 32
      - id: child_blocks
        type: children

  b_container_simple:
    instances:
      string2:
        value: 'collision_name'
    seq:
      - id: bound1
        type: sphere
      - id: collision_name
        type: str
        encoding: UTF-8
        size: 32
      - id: child_blocks
        type: children

  b_vertex_simple:
    params:
      - id: p_is_spaced
        type: bool
      - id: p_start_pos
        type: s4
    instances:
      string1:
        value: 'space_name'
      string2:
        value: 'collision_name'
      start_pos:
        value: p_start_pos
      verts_pos:
        value: 'p_start_pos + 52 + (p_is_spaced ? 32 : 0)'
    seq:
      - id: bound1
        type: sphere
      - id: space_name
        type: str
        if: p_is_spaced
        encoding: UTF-8
        size: 32
      - id: collision_name
        type: str
        encoding: UTF-8
        size: 32
      - id: vert_count
        type: s4
      - id: vert_raw
        size: vert_count * 20
      - id: child_blocks
        type: children

  b_vertex_extended:
    params:
      - id: p_is_spaced
        type: bool
      - id: p_start_pos
        type: s4
    instances:
      string1:
        value: 'space_name'
      string2:
        value: 'collision_name'
      int1:
        value: 'format_raw'
      format:
        value: 'format_raw & 0xff'
      uv_count:
        value: 'format_raw >> 8'
      normal_switch:
        value: '(format == 1 or format == 2) ? 0 : 1'
      start_pos:
        value: p_start_pos
      verts_pos:
        value: 'p_start_pos + 56 + (p_is_spaced ? 32 : 0)'
    seq:
      - id: bound1
        type: sphere
      - id: space_name
        type: str
        if: p_is_spaced
        encoding: UTF-8
        size: 32
      - id: collision_name
        type: str
        encoding: UTF-8
        size: 32
      - id: format_raw
        type: s4
      - id: poly_count
        type: s4
      - id: poly_raw
        size: 'poly_count * (12 + 8 * (uv_count + 1) + (normal_switch == 0 ? 12 : 4))'
      - id: child_blocks
        type: children

  b_polygon_simple:
    seq:
      - id: bound1
        type: sphere
      - id: poly_count
        type: s4
      - id: poly
        type: polygon_8(_io.pos)
        repeat: expr
        repeat-expr: poly_count

  b_render_switch_plane:
    instances:
      vector1:
        value: 'center'
      float1:
        value: 'length'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: length
        type: f4
      - id: child_blocks
        type: children

  b_render_switch_circle:
    instances:
      vector1:
        value: 'center'
      float1:
        value: 'length'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: length
        type: f4
      - id: child_blocks
        type: children

  b_render_switch_cylinder:
    instances:
      vector1:
        value: 'center'
      vector2:
        value: 'center2'
      float1:
        value: 'length'
      float2:
        value: 'length2'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: center2
        type: point
      - id: length
        type: f4
      - id: length2
        type: f4
      - id: child_blocks
        type: children

  b_collision_plane:
    instances:
      vector1:
        value: 'center'
      float1:
        value: 'length'
      int1:
        value: 'trigger_type'
      int2:
        value: 'trigger_id'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: length
        type: f4
      - id: trigger_type
        type: s4
      - id: trigger_id
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4

  b_trigger_room:
    instances:
      int1:
        value: 'trigger_type'
      int2:
        value: 'trigger_id'
    seq:
      - id: bound1
        type: sphere
      - id: trigger_type
        type: s4
      - id: trigger_id
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4

  b_trigger_circle:
    instances:
      vector1:
        value: 'center'
      float1:
        value: 'length'
      int1:
        value: 'trigger_type'
      int2:
        value: 'trigger_id'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: length
        type: f4
      - id: trigger_type
        type: s4
      - id: trigger_id
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4

  b_trigger_cylinder:
    instances:
      vector1:
        value: 'center'
      vector2:
        value: 'axis'
      int1:
        value: 'half_length'
      int2:
        value: 'radius'
      int3:
        value: 'trigger_type'
      int4:
        value: 'trigger_id'
    seq:
      - id: bound1
        type: sphere
      - id: center
        type: point
      - id: axis
        type: point
      - id: half_length
        type: f4
      - id: radius
        type: f4
      - id: trigger_type
        type: s4
      - id: trigger_id
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4

  b_connector:
    instances:
      string1:
        value: 'space_name'
      string2:
        value: 'add_name'
    seq:
      - id: bound1
        type: sphere
      - id: space_name
        type: str
        encoding: UTF-8
        size: 32
      - id: add_name
        type: str
        encoding: UTF-8
        size: 32

  b_room:
    seq:
      - id: child_blocks
        type: children

  b_collision_wall:
    instances:
      int1:
        value: 'trigger_type'
      int2:
        value: 'trigger_id'
    seq:
      - id: bound1
        type: sphere
      - id: coords_count
        type: s4
      - id: trigger_type
        type: s4
      - id: trigger_id
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4
      - id: coords_raw
        size: coords_count * 12

  b_state_machine:
    instances:
      int1:
        value: 'group_cnt'
      int2:
        value: 'unk_i1'
    seq:
      - id: bound1
        type: sphere
      - id: group_cnt
        type: s4
      - id: unk_i1
        type: s4
      - id: child_blocks
        type: children

  b_collision:
    instances:
      int1:
        value: 'unk_i1'
      int2:
        value: 'surface'
    types:
      vert_23:
        seq:
          - id: vert_count
            type: s4
          - id: verts_raw
            size: vert_count * 12
    seq:
      - id: unk_i1
        type: s4
      - id: surface
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4
      - id: verts_count
        type: s4
      - id: verts
        type: vert_23
        repeat: expr
        repeat-expr: verts_count

  b_space:
    instances:
      int1:
        value: 'flag'
    seq:
      - id: coord1
        type: point
      - id: coord2
        type: point
      - id: coord3
        type: point
      - id: pos
        type: point
      - id: flag
        type: s4
      - id: child_blocks
        type: children

  b_sound:
    instances:
      int1:
        value: 'unk_i1'
      int2:
        value: 'unk_i2'
      int3:
        value: 'unk_i3'
      string1:
        value: 'name'
      vector1:
        value: 'unk_p1'
      vector2:
        value: 'unk_p2'
      float1:
        value: 'unk_f11'
      float2:
        value: 'unk_f12'
      float3:
        value: 'unk_f13'
      float4:
        value: 'unk_f14'
      float5:
        value: 'unk_f15'
    seq:
      - id: unk_i1
        type: s4
      - id: unk_i2
        type: s4
      - id: unk_i3
        type: s4
      - id: name
        type: str
        encoding: UTF-8
        size: 32
      - id: unk_p1
        type: point
      - id: unk_p2
        type: point
      - id: unk_f11
        type: f4
      - id: unk_f12
        type: f4
      - id: unk_f13
        type: f4
      - id: unk_f14
        type: f4
      - id: unk_f15
        type: f4

  b_render_insphere:
    instances:
      vector1:
        value: 'unk_p1'
      vector2:
        value: 'unk_p2'
      vector3:
        value: 'unk_p3'
    seq:
      - id: bound1
        type: sphere
      - id: unk_p1
        type: point
      - id: unk_p2
        type: point
      - id: unk_p3
        type: point
      - id: child_blocks
        type: children

  b_sprite_simple:
    instances:
      int1:
        value: 'flag'
      vector1:
        value: 'unk_p1'
      int2:
        value: 'material'
    seq:
      - id: bound1
        type: sphere
      - id: flag
        type: s4
      - id: unk_p1
        type: point
      - id: material
        type: s4

  b_sprite_polygon:
    instances:
      vector1:
        value: 'sprite_center'
    seq:
      - id: bound1
        type: sphere
      - id: sprite_center
        type: point
      - id: poly_count
        type: s4
      - id: vert
        type: polygon_28(_io.pos)
        repeat: expr
        repeat-expr: poly_count

  b_render_switch_distance:
    instances:
      int1:
        value: 'unk_i1'
      int2:
        value: 'unk_i2'
      vector1:
        value: 'unk_p1'
      float1:
        value: 'unk_f1'
    seq:
      - id: bound1
        type: sphere
      - id: unk_i1
        type: s4
      - id: unk_i2
        type: s4
      - id: unk_p1
        type: point
      - id: unk_f1
        type: f4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4
      - id: child_blocks
        type: children

  b_portal:
    seq:
      - id: bound1
        type: sphere
      - id: room_name
        type: str
        encoding: UTF-8
        size: 32
      - id: point1
        type: point
      - id: point2
        type: point

  b_sprite_with_lods:
    instances:
      int1:
        value: 'unk_count'
      vector1:
        value: 'unk_p1'
      float1:
        value: 'unk_f1'
      int2:
        value: 'unk_i2'
      vector2:
        value: 'unk_p2'
    types:
      unk_fi:
        seq:
          - id: unkf
            type: f4
          - id: unki
            type: s4
    seq:
      - id: bound1
        type: sphere
      - id: unk_count
        type: s4
      - id: unk_p1
        type: point
      - id: unk_f1
        type: f4
      - id: unk_i2
        type: s4
      - id: unk_p2
        type: point
      - id: unk_floats_raw
        size: unk_count * 8

  b_container_lamp:
    instances:
      int1:
        value: 'use_lights'
      int2:
        value: 'light_type'
      int3:
        value: 'flag'
      vector1:
        value: 'unk_p1'
      vector2:
        value: 'unk_p2'
      float1:
        value: 'light_falloff'
      float2:
        value: 'light_att1'
      float3:
        value: 'light_att2'
      float4:
        value: 'light_att3'
      float5:
        value: 'light_phi'
      float6:
        value: 'light_theta'
      vector3:
        value: 'rgb'
    seq:
      - id: bound1
        type: sphere
      - id: use_lights
        type: s4
      - id: light_type
        type: s4
      - id: flag
        type: s4
      - id: unk_p1
        type: point
      - id: unk_p2
        type: point
      - id: light_falloff
        type: f4
      - id: light_att1
        type: f4
      - id: light_att2
        type: f4
      - id: light_att3
        type: f4
      - id: light_phi
        type: f4
      - id: light_theta
        type: f4
      - id: rgb
        type: color
      - id: child_blocks
        type: children

  b_point_array:
    instances:
      int1:
        value: 'unk_i1'
    types:
      unk_3fi:
        seq:
          - id: unk_3f
            type: point
          - id: unk_i
            type: s4
    seq:
      - id: bound1
        type: sphere
      - id: unk_i1
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 16

  b_polygon_extended:
    instances:
      int1:
        value: 'vtype'
      int2:
        value: 'texnum'
    seq:
      - id: bound1
        type: sphere
      - id: vtype
        type: s4
      - id: texnum
        type: s4
      - id: poly_count
        type: s4
      - id: vert
        type: polygon_8(_io.pos)
        repeat: expr
        repeat-expr: poly_count

  b_container_env:
    instances:
      int1:
        value: 'color_r'
      float1:
        value: 'unk_f1'
      float2:
        value: 'fog_start'
      float3:
        value: 'fog_end'
      int2:
        value: 'color_id'
    seq:
      - id: bound1
        type: sphere
      - id: color_r
        type: s4
      - id: unk_f1
        type: f4
      - id: fog_start
        type: f4
      - id: fog_end
        type: f4
      - id: color_id
        type: s4
      - id: child_blocks
        type: children

  b_generator:
    instances:
      string1:
        value: 'name1'
      string2:
        value: 'name2'
      int1:
        value: 'unk_i1'
      int2:
        value: 'unk_i2'
    seq:
      - id: bound1
        type: sphere
      - id: name1
        type: str
        encoding: UTF-8
        size: 32
      - id: name2
        type: str
        encoding: UTF-8
        size: 32
      - id: unk_i1
        type: s4
      - id: unk_i2
        type: s4
      - id: unk_count
        type: s4
      - id: unk_floats_raw
        size: unk_count * 4
        
  block:
    params:
      - id: p_group_before
        type: s4
      - id: p_start_pos
        type: s4
    instances:
      start_pos:
        value: p_start_pos
      group_before_count:
        # All elements before the final 333 marker must be 444 delimiters.
        value: group_block_start.size - 1
      group_after_count:
        # All elements before the final 555 marker must be 444 delimiters.
        value: group_block_end.size - 1
      has_group_before:
        value: group_before_count > 0
      has_group_after:
        value: group_after_count > 0
      group_before_pos:
        value: 'has_group_before ? p_start_pos : -1'
      block_group:
        # Group number is local to this block's sibling list.
        value: 'p_group_before + group_before_count'
      next_group:
        # Each trailing delimiter advances the next sibling's group number.
        value: 'block_group + group_after_count'
    seq:
      - id: group_block_start
        type: s4
        repeat: until
        repeat-until: _ == 333

      - id: block_name
        type: str
        encoding: UTF-8
        size: 32
      - id: block_type
        type: s4

      - id: block_data
        type:
          switch-on: block_type
          cases:
            0: b_unused
            1: b_observer
            2: b_render_order
            3: b_container_ordered
            4: b_container_spaced
            5: b_container_simple
            6: b_vertex_simple(true, _io.pos)
            7: b_vertex_simple(false, _io.pos)
            8: b_polygon_simple
            9: b_render_switch_plane
            10: b_render_switch_circle
            11: b_render_switch_cylinder
            12: b_collision_plane
            13: b_trigger_room
            14: b_trigger_circle
            15: b_trigger_circle
            16: b_trigger_cylinder
            17: b_trigger_cylinder
            18: b_connector
            19: b_room
            20: b_collision_wall
            21: b_state_machine
            22: b_render_switch_plane
            23: b_collision
            24: b_space
            25: b_sound
            26: b_render_insphere
            27: b_sprite_simple
            28: b_sprite_polygon
            29: b_render_switch_distance
            30: b_portal
            31: b_sprite_with_lods
            33: b_container_lamp
            34: b_point_array
            35: b_polygon_extended
            36: b_vertex_extended(true, _io.pos)
            37: b_vertex_extended(false, _io.pos)
            39: b_container_env
            40: b_generator

      - id: group_block_end
        type: s4
        repeat: until
        repeat-until: _ == 555

  data_chunks:
    params:
      - id: p_end_pos
        type: s4
    seq:
      - id: data_blocks
        # Number top-level sibling groups from zero.
        type: 'block(_index == 0 ? 0 : data_blocks[_index - 1].next_group, _io.pos)'
        if: _io.pos < p_end_pos
        repeat: until
        repeat-until: _io.pos >= p_end_pos

seq:
  - id: b3d_header
    type: file_header

  - id: b3d_materials
    type: materials_list

  - id: begin_blocks
    type: s4
    enum: identifiers

  - id: data_chunks
    type: data_chunks(_io.pos + (b3d_header.len_nodes - 2) * 4)

  - id: end_blocks
    type: s4
    enum: identifiers
