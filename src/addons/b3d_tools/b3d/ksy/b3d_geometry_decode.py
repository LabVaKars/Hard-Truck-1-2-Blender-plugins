"""On-demand, pure-Python decoders for hard_truck_2_b3d_optimized.ksy.

All the mesh buffers are little-endian. `struct.iter_unpack` reads each record
from the existing bytes without creating Kaitai objects per vertex.

The `extract_*` helpers return Python lists, so call them only when needed.
Use `iter_vec3`, `iter_floats` for large, optional numeric arrays.
"""
import struct


def _records(raw: bytes, fmt: str, count: int):
    """Validate exactly the expected buffer size; return a lazy iterator."""
    st = struct.Struct(fmt)
    if len(raw) != count * st.size:
        raise ValueError(
            f"Expected {count * st.size} bytes for {count} records; "
            f"got {len(raw)} bytes"
        )
    return st.iter_unpack(raw)


def extract_simple_vertices(block):
    """b_vertex_simple -> (positions, uv0), each a list of tuples."""
    positions, uv = [], []
    for x, y, z, u, v in _records(block.vert_raw, '<5f', block.vert_count):
        positions.append((x, y, z))
        uv.append((u, v))
    return positions, uv


def extract_complex_vertices(block):
    """b_vertex_extended -> (positions, uv_layers, normals, intensities).

    UV layer layout is uv_layers[layer][vertex_index].
    When the binary stores three normal floats, intensity defaults to 1.0.
    When it stores one intensity float, normal defaults to (0, 0, 0).
    """
    channels = block.uv_count + 1
    normal_dims = 3 if block.normal_switch == 0 else 1
    floats_per_vertex = 3 + channels * 2 + normal_dims
    rows = _records(block.poly_raw, f'<{floats_per_vertex}f', block.poly_count)
    positions, uv_layers, normals, intensities = [], [[] for _ in range(channels)], [], []
    for values in rows:
        positions.append(values[:3])
        for channel in range(channels):
            i = 3 + 2 * channel
            uv_layers[channel].append(values[i:i + 2])
        i = 3 + channels * 2
        if normal_dims == 3:
            normals.append(values[i:i + 3])
            intensities.append(1.0)
        else:
            normals.append((0.0, 0.0, 0.0))
            intensities.append(values[i])
    return positions, uv_layers, normals, intensities


def extract_polygon_8(polygon):
    """polygon_8 -> (indices, uv_layers, normals, intensities).

    If the polygon lacks normal data, normals and intensities are None.
    """
    channels = polygon.uv_count if polygon.use_uv else 0
    normal_dims = (3 if polygon.normal_switch == 0 else 1) if polygon.use_normal else 0
    rows = _records(polygon.verts_raw, '<I' + 'f' * (2 * channels + normal_dims), polygon.vert_count)
    indices, uv_layers = [], [[] for _ in range(channels)]
    normals = [] if polygon.use_normal else None
    intensities = [] if polygon.use_normal else None
    for values in rows:
        indices.append(values[0])
        for channel in range(channels):
            i = 1 + 2 * channel
            uv_layers[channel].append(values[i:i + 2])
        i = 1 + 2 * channels
        if polygon.use_normal:
            if normal_dims == 3:
                normals.append(values[i:i + 3])
                intensities.append(1.0)
            else:
                normals.append((0.0, 0.0, 0.0))
                intensities.append(values[i])
    return indices, uv_layers, normals, intensities


def extract_polygon_28(polygon):
    """polygon_28 -> (scale_u, scale_v, uv_layers)."""
    channels = polygon.uv_count if polygon.use_uv else 0
    rows = _records(polygon.verts_raw, '<ff' + 'f' * (2 * channels), polygon.vert_count)
    scale_u, scale_v = [], []
    uv_layers = [[] for _ in range(channels)]
    for values in rows:
        scale_u.append(values[0])
        scale_v.append(values[1])
        for channel in range(channels):
            i = 2 + 2 * channel
            uv_layers[channel].append(values[i:i + 2])
    return scale_u, scale_v, uv_layers


def iter_vec3(raw: bytes):
    """Iterate float XYZ triples (b_collision_wall.coords_raw, vert_23.verts_raw)."""
    if len(raw) % 12:
        raise ValueError('Expected a multiple of 12 bytes')
    return struct.iter_unpack('<3f', raw)


def iter_floats(raw: bytes):
    """Iterate one float per record (the unk_floats_raw arrays)."""
    if len(raw) % 4:
        raise ValueError('Expected a multiple of 4 bytes')
    return (rec[0] for rec in struct.iter_unpack('<f', raw))


def iter_sprite_lods(raw: bytes):
    """Iterate (float, unsigned int) pairs for b_sprite_with_lods."""
    if len(raw) % 8:
        raise ValueError('Expected a multiple of 8 bytes')
    return struct.iter_unpack('<fI', raw)


def iter_point_array(raw: bytes):
    """Iterate (float x,y,z, uint32) for b_point_array."""
    if len(raw) % 16:
        raise ValueError('Expected a multiple of 16 bytes')
    return struct.iter_unpack('<3fI', raw)
