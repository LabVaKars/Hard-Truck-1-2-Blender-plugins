# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import ReadWriteKaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ht2B3d(ReadWriteKaitaiStruct):
    """Models, game logic objects (Optimized for Python: mesh and numeric arrays stored as raw byte buffers for on-demand decoding.)."""

    class Identifiers(IntEnum):
        nodes_section_start = 111
        nodes_section_end = 222
        nodes_end = 333
        nodes_group = 444
        nodes_start = 555
    def __init__(self, _io=None, _parent=None, _root=None):
        super(Ht2B3d, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self

    def _read(self):
        self.b3d_header = Ht2B3d.FileHeader(self._io, self, self._root)
        self.b3d_header._read()
        self.b3d_materials = Ht2B3d.MaterialsList(self._io, self, self._root)
        self.b3d_materials._read()
        self.begin_blocks = KaitaiStream.resolve_enum(Ht2B3d.Identifiers, self._io.read_s4le())
        self.data_chunks = Ht2B3d.DataChunks(self._io.pos() + (self.b3d_header.len_nodes - 2) * 4, self._io, self, self._root)
        self.data_chunks._read()
        self.end_blocks = KaitaiStream.resolve_enum(Ht2B3d.Identifiers, self._io.read_s4le())
        self._dirty = False


    def _fetch_instances(self):
        pass
        self.b3d_header._fetch_instances()
        self.b3d_materials._fetch_instances()
        self.data_chunks._fetch_instances()


    def _write__seq(self, io=None):
        super(Ht2B3d, self)._write__seq(io)
        self.b3d_header._write__seq(self._io)
        self.b3d_materials._write__seq(self._io)
        self._io.write_s4le(int(self.begin_blocks))
        if self.data_chunks.p_end_pos != self._io.pos() + (self.b3d_header.len_nodes - 2) * 4:
            raise kaitaistruct.ConsistencyError(u"data_chunks", self._io.pos() + (self.b3d_header.len_nodes - 2) * 4, self.data_chunks.p_end_pos)
        self.data_chunks._write__seq(self._io)
        self._io.write_s4le(int(self.end_blocks))


    def _check(self):
        if self.b3d_header._root != self._root:
            raise kaitaistruct.ConsistencyError(u"b3d_header", self._root, self.b3d_header._root)
        if self.b3d_header._parent != self:
            raise kaitaistruct.ConsistencyError(u"b3d_header", self, self.b3d_header._parent)
        if self.b3d_materials._root != self._root:
            raise kaitaistruct.ConsistencyError(u"b3d_materials", self._root, self.b3d_materials._root)
        if self.b3d_materials._parent != self:
            raise kaitaistruct.ConsistencyError(u"b3d_materials", self, self.b3d_materials._parent)
        if self.data_chunks._root != self._root:
            raise kaitaistruct.ConsistencyError(u"data_chunks", self._root, self.data_chunks._root)
        if self.data_chunks._parent != self:
            raise kaitaistruct.ConsistencyError(u"data_chunks", self, self.data_chunks._parent)
        self._dirty = False

    class BCollision(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BCollision, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unk_i1 = self._io.read_s4le()
            self.surface = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self.verts_count = self._io.read_s4le()
            self.verts = []
            for i in range(self.verts_count):
                _t_verts = Ht2B3d.BCollision.Vert23(self._io, self, self._root)
                try:
                    _t_verts._read()
                finally:
                    self.verts.append(_t_verts)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.verts)):
                pass
                self.verts[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Ht2B3d.BCollision, self)._write__seq(io)
            self._io.write_s4le(self.unk_i1)
            self._io.write_s4le(self.surface)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)
            self._io.write_s4le(self.verts_count)
            for i in range(len(self.verts)):
                pass
                self.verts[i]._write__seq(self._io)



        def _check(self):
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            if len(self.verts) != self.verts_count:
                raise kaitaistruct.ConsistencyError(u"verts", self.verts_count, len(self.verts))
            for i in range(len(self.verts)):
                pass
                if self.verts[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"verts", self._root, self.verts[i]._root)
                if self.verts[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"verts", self, self.verts[i]._parent)

            self._dirty = False

        class Vert23(ReadWriteKaitaiStruct):
            def __init__(self, _io=None, _parent=None, _root=None):
                super(Ht2B3d.BCollision.Vert23, self).__init__(_io)
                self._parent = _parent
                self._root = _root

            def _read(self):
                self.vert_count = self._io.read_s4le()
                self.verts_raw = self._io.read_bytes(self.vert_count * 12)
                self._dirty = False


            def _fetch_instances(self):
                pass


            def _write__seq(self, io=None):
                super(Ht2B3d.BCollision.Vert23, self)._write__seq(io)
                self._io.write_s4le(self.vert_count)
                self._io.write_bytes(self.verts_raw)


            def _check(self):
                if len(self.verts_raw) != self.vert_count * 12:
                    raise kaitaistruct.ConsistencyError(u"verts_raw", self.vert_count * 12, len(self.verts_raw))
                self._dirty = False


        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.unk_i1
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.surface
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2

    class BCollisionPlane(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BCollisionPlane, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.length = self._io.read_f4le()
            self.trigger_type = self._io.read_s4le()
            self.trigger_id = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BCollisionPlane, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self._io.write_f4le(self.length)
            self._io.write_s4le(self.trigger_type)
            self._io.write_s4le(self.trigger_id)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.length
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.trigger_type
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.trigger_id
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BCollisionWall(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BCollisionWall, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.coords_count = self._io.read_s4le()
            self.trigger_type = self._io.read_s4le()
            self.trigger_id = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self.coords_raw = self._io.read_bytes(self.coords_count * 12)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BCollisionWall, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.coords_count)
            self._io.write_s4le(self.trigger_type)
            self._io.write_s4le(self.trigger_id)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)
            self._io.write_bytes(self.coords_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            if len(self.coords_raw) != self.coords_count * 12:
                raise kaitaistruct.ConsistencyError(u"coords_raw", self.coords_count * 12, len(self.coords_raw))
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.trigger_type
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.trigger_id
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2

    class BConnector(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BConnector, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.space_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.add_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BConnector, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_bytes((self.space_name).encode(u"UTF-8"))
            self._io.write_bytes((self.add_name).encode(u"UTF-8"))


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len((self.space_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"space_name", 32, len((self.space_name).encode(u"UTF-8")))
            if len((self.add_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"add_name", 32, len((self.add_name).encode(u"UTF-8")))
            self._dirty = False

        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.space_name
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.add_name
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2

    class BContainerEnv(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BContainerEnv, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.color_r = self._io.read_s4le()
            self.unk_f1 = self._io.read_f4le()
            self.fog_start = self._io.read_f4le()
            self.fog_end = self._io.read_f4le()
            self.color_id = self._io.read_s4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BContainerEnv, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.color_r)
            self._io.write_f4le(self.unk_f1)
            self._io.write_f4le(self.fog_start)
            self._io.write_f4le(self.fog_end)
            self._io.write_s4le(self.color_id)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.unk_f1
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def float2(self):
            if hasattr(self, '_m_float2'):
                return self._m_float2

            self._m_float2 = self.fog_start
            return getattr(self, '_m_float2', None)

        def _invalidate_float2(self):
            del self._m_float2
        @property
        def float3(self):
            if hasattr(self, '_m_float3'):
                return self._m_float3

            self._m_float3 = self.fog_end
            return getattr(self, '_m_float3', None)

        def _invalidate_float3(self):
            del self._m_float3
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.color_r
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.color_id
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2

    class BContainerLamp(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BContainerLamp, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.use_lights = self._io.read_s4le()
            self.light_type = self._io.read_s4le()
            self.flag = self._io.read_s4le()
            self.unk_p1 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p1._read()
            self.unk_p2 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p2._read()
            self.light_falloff = self._io.read_f4le()
            self.light_att1 = self._io.read_f4le()
            self.light_att2 = self._io.read_f4le()
            self.light_att3 = self._io.read_f4le()
            self.light_phi = self._io.read_f4le()
            self.light_theta = self._io.read_f4le()
            self.rgb = Ht2B3d.Color(self._io, self, self._root)
            self.rgb._read()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.unk_p1._fetch_instances()
            self.unk_p2._fetch_instances()
            self.rgb._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BContainerLamp, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.use_lights)
            self._io.write_s4le(self.light_type)
            self._io.write_s4le(self.flag)
            self.unk_p1._write__seq(self._io)
            self.unk_p2._write__seq(self._io)
            self._io.write_f4le(self.light_falloff)
            self._io.write_f4le(self.light_att1)
            self._io.write_f4le(self.light_att2)
            self._io.write_f4le(self.light_att3)
            self._io.write_f4le(self.light_phi)
            self._io.write_f4le(self.light_theta)
            self.rgb._write__seq(self._io)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.unk_p1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self._root, self.unk_p1._root)
            if self.unk_p1._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self, self.unk_p1._parent)
            if self.unk_p2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self._root, self.unk_p2._root)
            if self.unk_p2._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self, self.unk_p2._parent)
            if self.rgb._root != self._root:
                raise kaitaistruct.ConsistencyError(u"rgb", self._root, self.rgb._root)
            if self.rgb._parent != self:
                raise kaitaistruct.ConsistencyError(u"rgb", self, self.rgb._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.light_falloff
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def float2(self):
            if hasattr(self, '_m_float2'):
                return self._m_float2

            self._m_float2 = self.light_att1
            return getattr(self, '_m_float2', None)

        def _invalidate_float2(self):
            del self._m_float2
        @property
        def float3(self):
            if hasattr(self, '_m_float3'):
                return self._m_float3

            self._m_float3 = self.light_att2
            return getattr(self, '_m_float3', None)

        def _invalidate_float3(self):
            del self._m_float3
        @property
        def float4(self):
            if hasattr(self, '_m_float4'):
                return self._m_float4

            self._m_float4 = self.light_att3
            return getattr(self, '_m_float4', None)

        def _invalidate_float4(self):
            del self._m_float4
        @property
        def float5(self):
            if hasattr(self, '_m_float5'):
                return self._m_float5

            self._m_float5 = self.light_phi
            return getattr(self, '_m_float5', None)

        def _invalidate_float5(self):
            del self._m_float5
        @property
        def float6(self):
            if hasattr(self, '_m_float6'):
                return self._m_float6

            self._m_float6 = self.light_theta
            return getattr(self, '_m_float6', None)

        def _invalidate_float6(self):
            del self._m_float6
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.use_lights
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.light_type
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def int3(self):
            if hasattr(self, '_m_int3'):
                return self._m_int3

            self._m_int3 = self.flag
            return getattr(self, '_m_int3', None)

        def _invalidate_int3(self):
            del self._m_int3
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.unk_p1
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1
        @property
        def vector2(self):
            if hasattr(self, '_m_vector2'):
                return self._m_vector2

            self._m_vector2 = self.unk_p2
            return getattr(self, '_m_vector2', None)

        def _invalidate_vector2(self):
            del self._m_vector2
        @property
        def vector3(self):
            if hasattr(self, '_m_vector3'):
                return self._m_vector3

            self._m_vector3 = self.rgb
            return getattr(self, '_m_vector3', None)

        def _invalidate_vector3(self):
            del self._m_vector3

    class BContainerOrdered(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BContainerOrdered, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BContainerOrdered, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False


    class BContainerSimple(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BContainerSimple, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.collision_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BContainerSimple, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_bytes((self.collision_name).encode(u"UTF-8"))
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len((self.collision_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"collision_name", 32, len((self.collision_name).encode(u"UTF-8")))
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.collision_name
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2

    class BContainerSpaced(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BContainerSpaced, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.space_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.collision_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BContainerSpaced, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_bytes((self.space_name).encode(u"UTF-8"))
            self._io.write_bytes((self.collision_name).encode(u"UTF-8"))
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len((self.space_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"space_name", 32, len((self.space_name).encode(u"UTF-8")))
            if len((self.collision_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"collision_name", 32, len((self.collision_name).encode(u"UTF-8")))
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.space_name
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.collision_name
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2

    class BGenerator(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BGenerator, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.name1 = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.name2 = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.unk_i1 = self._io.read_s4le()
            self.unk_i2 = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BGenerator, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_bytes((self.name1).encode(u"UTF-8"))
            self._io.write_bytes((self.name2).encode(u"UTF-8"))
            self._io.write_s4le(self.unk_i1)
            self._io.write_s4le(self.unk_i2)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len((self.name1).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"name1", 32, len((self.name1).encode(u"UTF-8")))
            if len((self.name2).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"name2", 32, len((self.name2).encode(u"UTF-8")))
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.unk_i1
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.unk_i2
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.name1
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.name2
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2

    class BObserver(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BObserver, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.name1 = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.name2 = (self._io.read_bytes(32)).decode(u"UTF-8")
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Ht2B3d.BObserver, self)._write__seq(io)
            self._io.write_bytes((self.name1).encode(u"UTF-8"))
            self._io.write_bytes((self.name2).encode(u"UTF-8"))


        def _check(self):
            if len((self.name1).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"name1", 32, len((self.name1).encode(u"UTF-8")))
            if len((self.name2).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"name2", 32, len((self.name2).encode(u"UTF-8")))
            self._dirty = False

        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.name1
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.name2
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2

    class BPointArray(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BPointArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.unk_i1 = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 16)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BPointArray, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.unk_i1)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len(self.unk_floats_raw) != self.unk_count * 16:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 16, len(self.unk_floats_raw))
            self._dirty = False

        class Unk3fi(ReadWriteKaitaiStruct):
            def __init__(self, _io=None, _parent=None, _root=None):
                super(Ht2B3d.BPointArray.Unk3fi, self).__init__(_io)
                self._parent = _parent
                self._root = _root

            def _read(self):
                self.unk_3f = Ht2B3d.Point(self._io, self, self._root)
                self.unk_3f._read()
                self.unk_i = self._io.read_s4le()
                self._dirty = False


            def _fetch_instances(self):
                pass
                self.unk_3f._fetch_instances()


            def _write__seq(self, io=None):
                super(Ht2B3d.BPointArray.Unk3fi, self)._write__seq(io)
                self.unk_3f._write__seq(self._io)
                self._io.write_s4le(self.unk_i)


            def _check(self):
                if self.unk_3f._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"unk_3f", self._root, self.unk_3f._root)
                if self.unk_3f._parent != self:
                    raise kaitaistruct.ConsistencyError(u"unk_3f", self, self.unk_3f._parent)
                self._dirty = False


        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.unk_i1
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1

    class BPolygonExtended(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BPolygonExtended, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.vtype = self._io.read_s4le()
            self.texnum = self._io.read_s4le()
            self.poly_count = self._io.read_s4le()
            self.vert = []
            for i in range(self.poly_count):
                _t_vert = Ht2B3d.Polygon8(self._io.pos(), self._io, self, self._root)
                try:
                    _t_vert._read()
                finally:
                    self.vert.append(_t_vert)

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            for i in range(len(self.vert)):
                pass
                self.vert[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Ht2B3d.BPolygonExtended, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.vtype)
            self._io.write_s4le(self.texnum)
            self._io.write_s4le(self.poly_count)
            for i in range(len(self.vert)):
                pass
                if self.vert[i].p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"vert", self._io.pos(), self.vert[i].p_start_pos)
                self.vert[i]._write__seq(self._io)



        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len(self.vert) != self.poly_count:
                raise kaitaistruct.ConsistencyError(u"vert", self.poly_count, len(self.vert))
            for i in range(len(self.vert)):
                pass
                if self.vert[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"vert", self._root, self.vert[i]._root)
                if self.vert[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"vert", self, self.vert[i]._parent)

            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.vtype
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.texnum
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2

    class BPolygonSimple(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BPolygonSimple, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.poly_count = self._io.read_s4le()
            self.poly = []
            for i in range(self.poly_count):
                _t_poly = Ht2B3d.Polygon8(self._io.pos(), self._io, self, self._root)
                try:
                    _t_poly._read()
                finally:
                    self.poly.append(_t_poly)

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            for i in range(len(self.poly)):
                pass
                self.poly[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Ht2B3d.BPolygonSimple, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.poly_count)
            for i in range(len(self.poly)):
                pass
                if self.poly[i].p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"poly", self._io.pos(), self.poly[i].p_start_pos)
                self.poly[i]._write__seq(self._io)



        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len(self.poly) != self.poly_count:
                raise kaitaistruct.ConsistencyError(u"poly", self.poly_count, len(self.poly))
            for i in range(len(self.poly)):
                pass
                if self.poly[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"poly", self._root, self.poly[i]._root)
                if self.poly[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"poly", self, self.poly[i]._parent)

            self._dirty = False


    class BPortal(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BPortal, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.room_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.point1 = Ht2B3d.Point(self._io, self, self._root)
            self.point1._read()
            self.point2 = Ht2B3d.Point(self._io, self, self._root)
            self.point2._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.point1._fetch_instances()
            self.point2._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BPortal, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_bytes((self.room_name).encode(u"UTF-8"))
            self.point1._write__seq(self._io)
            self.point2._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len((self.room_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"room_name", 32, len((self.room_name).encode(u"UTF-8")))
            if self.point1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"point1", self._root, self.point1._root)
            if self.point1._parent != self:
                raise kaitaistruct.ConsistencyError(u"point1", self, self.point1._parent)
            if self.point2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"point2", self._root, self.point2._root)
            if self.point2._parent != self:
                raise kaitaistruct.ConsistencyError(u"point2", self, self.point2._parent)
            self._dirty = False


    class BRenderInsphere(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRenderInsphere, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.unk_p1 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p1._read()
            self.unk_p2 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p2._read()
            self.unk_p3 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p3._read()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.unk_p1._fetch_instances()
            self.unk_p2._fetch_instances()
            self.unk_p3._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRenderInsphere, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.unk_p1._write__seq(self._io)
            self.unk_p2._write__seq(self._io)
            self.unk_p3._write__seq(self._io)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.unk_p1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self._root, self.unk_p1._root)
            if self.unk_p1._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self, self.unk_p1._parent)
            if self.unk_p2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self._root, self.unk_p2._root)
            if self.unk_p2._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self, self.unk_p2._parent)
            if self.unk_p3._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p3", self._root, self.unk_p3._root)
            if self.unk_p3._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p3", self, self.unk_p3._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.unk_p1
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1
        @property
        def vector2(self):
            if hasattr(self, '_m_vector2'):
                return self._m_vector2

            self._m_vector2 = self.unk_p2
            return getattr(self, '_m_vector2', None)

        def _invalidate_vector2(self):
            del self._m_vector2
        @property
        def vector3(self):
            if hasattr(self, '_m_vector3'):
                return self._m_vector3

            self._m_vector3 = self.unk_p3
            return getattr(self, '_m_vector3', None)

        def _invalidate_vector3(self):
            del self._m_vector3

    class BRenderOrder(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRenderOrder, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.length = self._io.read_f4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRenderOrder, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self._io.write_f4le(self.length)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.length
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BRenderSwitchCircle(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRenderSwitchCircle, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.length = self._io.read_f4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRenderSwitchCircle, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self._io.write_f4le(self.length)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.length
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BRenderSwitchCylinder(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRenderSwitchCylinder, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.center2 = Ht2B3d.Point(self._io, self, self._root)
            self.center2._read()
            self.length = self._io.read_f4le()
            self.length2 = self._io.read_f4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()
            self.center2._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRenderSwitchCylinder, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self.center2._write__seq(self._io)
            self._io.write_f4le(self.length)
            self._io.write_f4le(self.length2)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if self.center2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center2", self._root, self.center2._root)
            if self.center2._parent != self:
                raise kaitaistruct.ConsistencyError(u"center2", self, self.center2._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.length
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def float2(self):
            if hasattr(self, '_m_float2'):
                return self._m_float2

            self._m_float2 = self.length2
            return getattr(self, '_m_float2', None)

        def _invalidate_float2(self):
            del self._m_float2
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1
        @property
        def vector2(self):
            if hasattr(self, '_m_vector2'):
                return self._m_vector2

            self._m_vector2 = self.center2
            return getattr(self, '_m_vector2', None)

        def _invalidate_vector2(self):
            del self._m_vector2

    class BRenderSwitchDistance(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRenderSwitchDistance, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.unk_i1 = self._io.read_s4le()
            self.unk_i2 = self._io.read_s4le()
            self.unk_p1 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p1._read()
            self.unk_f1 = self._io.read_f4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.unk_p1._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRenderSwitchDistance, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.unk_i1)
            self._io.write_s4le(self.unk_i2)
            self.unk_p1._write__seq(self._io)
            self._io.write_f4le(self.unk_f1)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.unk_p1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self._root, self.unk_p1._root)
            if self.unk_p1._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self, self.unk_p1._parent)
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.unk_f1
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.unk_i1
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.unk_i2
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.unk_p1
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BRenderSwitchPlane(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRenderSwitchPlane, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.length = self._io.read_f4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRenderSwitchPlane, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self._io.write_f4le(self.length)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.length
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BRoom(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BRoom, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BRoom, self)._write__seq(io)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False


    class BSound(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BSound, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.unk_i1 = self._io.read_s4le()
            self.unk_i2 = self._io.read_s4le()
            self.unk_i3 = self._io.read_s4le()
            self.name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.unk_p1 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p1._read()
            self.unk_p2 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p2._read()
            self.unk_f11 = self._io.read_f4le()
            self.unk_f12 = self._io.read_f4le()
            self.unk_f13 = self._io.read_f4le()
            self.unk_f14 = self._io.read_f4le()
            self.unk_f15 = self._io.read_f4le()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.unk_p1._fetch_instances()
            self.unk_p2._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BSound, self)._write__seq(io)
            self._io.write_s4le(self.unk_i1)
            self._io.write_s4le(self.unk_i2)
            self._io.write_s4le(self.unk_i3)
            self._io.write_bytes((self.name).encode(u"UTF-8"))
            self.unk_p1._write__seq(self._io)
            self.unk_p2._write__seq(self._io)
            self._io.write_f4le(self.unk_f11)
            self._io.write_f4le(self.unk_f12)
            self._io.write_f4le(self.unk_f13)
            self._io.write_f4le(self.unk_f14)
            self._io.write_f4le(self.unk_f15)


        def _check(self):
            if len((self.name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"name", 32, len((self.name).encode(u"UTF-8")))
            if self.unk_p1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self._root, self.unk_p1._root)
            if self.unk_p1._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self, self.unk_p1._parent)
            if self.unk_p2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self._root, self.unk_p2._root)
            if self.unk_p2._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self, self.unk_p2._parent)
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.unk_f11
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def float2(self):
            if hasattr(self, '_m_float2'):
                return self._m_float2

            self._m_float2 = self.unk_f12
            return getattr(self, '_m_float2', None)

        def _invalidate_float2(self):
            del self._m_float2
        @property
        def float3(self):
            if hasattr(self, '_m_float3'):
                return self._m_float3

            self._m_float3 = self.unk_f13
            return getattr(self, '_m_float3', None)

        def _invalidate_float3(self):
            del self._m_float3
        @property
        def float4(self):
            if hasattr(self, '_m_float4'):
                return self._m_float4

            self._m_float4 = self.unk_f14
            return getattr(self, '_m_float4', None)

        def _invalidate_float4(self):
            del self._m_float4
        @property
        def float5(self):
            if hasattr(self, '_m_float5'):
                return self._m_float5

            self._m_float5 = self.unk_f15
            return getattr(self, '_m_float5', None)

        def _invalidate_float5(self):
            del self._m_float5
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.unk_i1
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.unk_i2
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def int3(self):
            if hasattr(self, '_m_int3'):
                return self._m_int3

            self._m_int3 = self.unk_i3
            return getattr(self, '_m_int3', None)

        def _invalidate_int3(self):
            del self._m_int3
        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.name
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.unk_p1
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1
        @property
        def vector2(self):
            if hasattr(self, '_m_vector2'):
                return self._m_vector2

            self._m_vector2 = self.unk_p2
            return getattr(self, '_m_vector2', None)

        def _invalidate_vector2(self):
            del self._m_vector2

    class BSpace(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BSpace, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.coord1 = Ht2B3d.Point(self._io, self, self._root)
            self.coord1._read()
            self.coord2 = Ht2B3d.Point(self._io, self, self._root)
            self.coord2._read()
            self.coord3 = Ht2B3d.Point(self._io, self, self._root)
            self.coord3._read()
            self.pos = Ht2B3d.Point(self._io, self, self._root)
            self.pos._read()
            self.flag = self._io.read_s4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.coord1._fetch_instances()
            self.coord2._fetch_instances()
            self.coord3._fetch_instances()
            self.pos._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BSpace, self)._write__seq(io)
            self.coord1._write__seq(self._io)
            self.coord2._write__seq(self._io)
            self.coord3._write__seq(self._io)
            self.pos._write__seq(self._io)
            self._io.write_s4le(self.flag)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.coord1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"coord1", self._root, self.coord1._root)
            if self.coord1._parent != self:
                raise kaitaistruct.ConsistencyError(u"coord1", self, self.coord1._parent)
            if self.coord2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"coord2", self._root, self.coord2._root)
            if self.coord2._parent != self:
                raise kaitaistruct.ConsistencyError(u"coord2", self, self.coord2._parent)
            if self.coord3._root != self._root:
                raise kaitaistruct.ConsistencyError(u"coord3", self._root, self.coord3._root)
            if self.coord3._parent != self:
                raise kaitaistruct.ConsistencyError(u"coord3", self, self.coord3._parent)
            if self.pos._root != self._root:
                raise kaitaistruct.ConsistencyError(u"pos", self._root, self.pos._root)
            if self.pos._parent != self:
                raise kaitaistruct.ConsistencyError(u"pos", self, self.pos._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.flag
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1

    class BSpritePolygon(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BSpritePolygon, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.sprite_center = Ht2B3d.Point(self._io, self, self._root)
            self.sprite_center._read()
            self.poly_count = self._io.read_s4le()
            self.vert = []
            for i in range(self.poly_count):
                _t_vert = Ht2B3d.Polygon28(self._io.pos(), self._io, self, self._root)
                try:
                    _t_vert._read()
                finally:
                    self.vert.append(_t_vert)

            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.sprite_center._fetch_instances()
            for i in range(len(self.vert)):
                pass
                self.vert[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Ht2B3d.BSpritePolygon, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.sprite_center._write__seq(self._io)
            self._io.write_s4le(self.poly_count)
            for i in range(len(self.vert)):
                pass
                if self.vert[i].p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"vert", self._io.pos(), self.vert[i].p_start_pos)
                self.vert[i]._write__seq(self._io)



        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.sprite_center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"sprite_center", self._root, self.sprite_center._root)
            if self.sprite_center._parent != self:
                raise kaitaistruct.ConsistencyError(u"sprite_center", self, self.sprite_center._parent)
            if len(self.vert) != self.poly_count:
                raise kaitaistruct.ConsistencyError(u"vert", self.poly_count, len(self.vert))
            for i in range(len(self.vert)):
                pass
                if self.vert[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"vert", self._root, self.vert[i]._root)
                if self.vert[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"vert", self, self.vert[i]._parent)

            self._dirty = False

        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.sprite_center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BSpriteSimple(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BSpriteSimple, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.flag = self._io.read_s4le()
            self.unk_p1 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p1._read()
            self.material = self._io.read_s4le()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.unk_p1._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BSpriteSimple, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.flag)
            self.unk_p1._write__seq(self._io)
            self._io.write_s4le(self.material)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.unk_p1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self._root, self.unk_p1._root)
            if self.unk_p1._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self, self.unk_p1._parent)
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.flag
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.material
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.unk_p1
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BSpriteWithLods(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BSpriteWithLods, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.unk_count = self._io.read_s4le()
            self.unk_p1 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p1._read()
            self.unk_f1 = self._io.read_f4le()
            self.unk_i2 = self._io.read_s4le()
            self.unk_p2 = Ht2B3d.Point(self._io, self, self._root)
            self.unk_p2._read()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 8)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.unk_p1._fetch_instances()
            self.unk_p2._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BSpriteWithLods, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.unk_count)
            self.unk_p1._write__seq(self._io)
            self._io.write_f4le(self.unk_f1)
            self._io.write_s4le(self.unk_i2)
            self.unk_p2._write__seq(self._io)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.unk_p1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self._root, self.unk_p1._root)
            if self.unk_p1._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p1", self, self.unk_p1._parent)
            if self.unk_p2._root != self._root:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self._root, self.unk_p2._root)
            if self.unk_p2._parent != self:
                raise kaitaistruct.ConsistencyError(u"unk_p2", self, self.unk_p2._parent)
            if len(self.unk_floats_raw) != self.unk_count * 8:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 8, len(self.unk_floats_raw))
            self._dirty = False

        class UnkFi(ReadWriteKaitaiStruct):
            def __init__(self, _io=None, _parent=None, _root=None):
                super(Ht2B3d.BSpriteWithLods.UnkFi, self).__init__(_io)
                self._parent = _parent
                self._root = _root

            def _read(self):
                self.unkf = self._io.read_f4le()
                self.unki = self._io.read_s4le()
                self._dirty = False


            def _fetch_instances(self):
                pass


            def _write__seq(self, io=None):
                super(Ht2B3d.BSpriteWithLods.UnkFi, self)._write__seq(io)
                self._io.write_f4le(self.unkf)
                self._io.write_s4le(self.unki)


            def _check(self):
                self._dirty = False


        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.unk_f1
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.unk_count
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.unk_i2
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.unk_p1
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1
        @property
        def vector2(self):
            if hasattr(self, '_m_vector2'):
                return self._m_vector2

            self._m_vector2 = self.unk_p2
            return getattr(self, '_m_vector2', None)

        def _invalidate_vector2(self):
            del self._m_vector2

    class BStateMachine(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BStateMachine, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.group_cnt = self._io.read_s4le()
            self.unk_i1 = self._io.read_s4le()
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BStateMachine, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.group_cnt)
            self._io.write_s4le(self.unk_i1)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.group_cnt
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.unk_i1
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2

    class BTriggerCircle(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BTriggerCircle, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.length = self._io.read_f4le()
            self.trigger_type = self._io.read_s4le()
            self.trigger_id = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BTriggerCircle, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self._io.write_f4le(self.length)
            self._io.write_s4le(self.trigger_type)
            self._io.write_s4le(self.trigger_id)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            self._dirty = False

        @property
        def float1(self):
            if hasattr(self, '_m_float1'):
                return self._m_float1

            self._m_float1 = self.length
            return getattr(self, '_m_float1', None)

        def _invalidate_float1(self):
            del self._m_float1
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.trigger_type
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.trigger_id
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1

    class BTriggerCylinder(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BTriggerCylinder, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.center = Ht2B3d.Point(self._io, self, self._root)
            self.center._read()
            self.axis = Ht2B3d.Point(self._io, self, self._root)
            self.axis._read()
            self.half_length = self._io.read_f4le()
            self.radius = self._io.read_f4le()
            self.trigger_type = self._io.read_s4le()
            self.trigger_id = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            self.center._fetch_instances()
            self.axis._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BTriggerCylinder, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self.center._write__seq(self._io)
            self.axis._write__seq(self._io)
            self._io.write_f4le(self.half_length)
            self._io.write_f4le(self.radius)
            self._io.write_s4le(self.trigger_type)
            self._io.write_s4le(self.trigger_id)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.center._root != self._root:
                raise kaitaistruct.ConsistencyError(u"center", self._root, self.center._root)
            if self.center._parent != self:
                raise kaitaistruct.ConsistencyError(u"center", self, self.center._parent)
            if self.axis._root != self._root:
                raise kaitaistruct.ConsistencyError(u"axis", self._root, self.axis._root)
            if self.axis._parent != self:
                raise kaitaistruct.ConsistencyError(u"axis", self, self.axis._parent)
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.half_length
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.radius
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2
        @property
        def int3(self):
            if hasattr(self, '_m_int3'):
                return self._m_int3

            self._m_int3 = self.trigger_type
            return getattr(self, '_m_int3', None)

        def _invalidate_int3(self):
            del self._m_int3
        @property
        def int4(self):
            if hasattr(self, '_m_int4'):
                return self._m_int4

            self._m_int4 = self.trigger_id
            return getattr(self, '_m_int4', None)

        def _invalidate_int4(self):
            del self._m_int4
        @property
        def vector1(self):
            if hasattr(self, '_m_vector1'):
                return self._m_vector1

            self._m_vector1 = self.center
            return getattr(self, '_m_vector1', None)

        def _invalidate_vector1(self):
            del self._m_vector1
        @property
        def vector2(self):
            if hasattr(self, '_m_vector2'):
                return self._m_vector2

            self._m_vector2 = self.axis
            return getattr(self, '_m_vector2', None)

        def _invalidate_vector2(self):
            del self._m_vector2

    class BTriggerRoom(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BTriggerRoom, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            self.trigger_type = self._io.read_s4le()
            self.trigger_id = self._io.read_s4le()
            self.unk_count = self._io.read_s4le()
            self.unk_floats_raw = self._io.read_bytes(self.unk_count * 4)
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BTriggerRoom, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            self._io.write_s4le(self.trigger_type)
            self._io.write_s4le(self.trigger_id)
            self._io.write_s4le(self.unk_count)
            self._io.write_bytes(self.unk_floats_raw)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if len(self.unk_floats_raw) != self.unk_count * 4:
                raise kaitaistruct.ConsistencyError(u"unk_floats_raw", self.unk_count * 4, len(self.unk_floats_raw))
            self._dirty = False

        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.trigger_type
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def int2(self):
            if hasattr(self, '_m_int2'):
                return self._m_int2

            self._m_int2 = self.trigger_id
            return getattr(self, '_m_int2', None)

        def _invalidate_int2(self):
            del self._m_int2

    class BUnused(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BUnused, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.content = []
            for i in range(11):
                self.content.append(self._io.read_f4le())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.content)):
                pass



        def _write__seq(self, io=None):
            super(Ht2B3d.BUnused, self)._write__seq(io)
            for i in range(len(self.content)):
                pass
                self._io.write_f4le(self.content[i])



        def _check(self):
            if len(self.content) != 11:
                raise kaitaistruct.ConsistencyError(u"content", 11, len(self.content))
            for i in range(len(self.content)):
                pass

            self._dirty = False


    class BVertexExtended(ReadWriteKaitaiStruct):
        def __init__(self, p_is_spaced, p_start_pos, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BVertexExtended, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.p_is_spaced = p_is_spaced
            self.p_start_pos = p_start_pos

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            if self.p_is_spaced:
                pass
                self.space_name = (self._io.read_bytes(32)).decode(u"UTF-8")

            self.collision_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.format_raw = self._io.read_s4le()
            self.poly_count = self._io.read_s4le()
            self.poly_raw = self._io.read_bytes(self.poly_count * ((12 + 8 * (self.uv_count + 1)) + (12 if self.normal_switch == 0 else 4)))
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            if self.p_is_spaced:
                pass

            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BVertexExtended, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            if self.p_is_spaced:
                pass
                self._io.write_bytes((self.space_name).encode(u"UTF-8"))

            self._io.write_bytes((self.collision_name).encode(u"UTF-8"))
            self._io.write_s4le(self.format_raw)
            self._io.write_s4le(self.poly_count)
            self._io.write_bytes(self.poly_raw)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.p_is_spaced:
                pass
                if len((self.space_name).encode(u"UTF-8")) != 32:
                    raise kaitaistruct.ConsistencyError(u"space_name", 32, len((self.space_name).encode(u"UTF-8")))

            if len((self.collision_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"collision_name", 32, len((self.collision_name).encode(u"UTF-8")))
            if len(self.poly_raw) != self.poly_count * ((12 + 8 * (self.uv_count + 1)) + (12 if self.normal_switch == 0 else 4)):
                raise kaitaistruct.ConsistencyError(u"poly_raw", self.poly_count * ((12 + 8 * (self.uv_count + 1)) + (12 if self.normal_switch == 0 else 4)), len(self.poly_raw))
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def format(self):
            if hasattr(self, '_m_format'):
                return self._m_format

            self._m_format = self.format_raw & 255
            return getattr(self, '_m_format', None)

        def _invalidate_format(self):
            del self._m_format
        @property
        def int1(self):
            if hasattr(self, '_m_int1'):
                return self._m_int1

            self._m_int1 = self.format_raw
            return getattr(self, '_m_int1', None)

        def _invalidate_int1(self):
            del self._m_int1
        @property
        def normal_switch(self):
            if hasattr(self, '_m_normal_switch'):
                return self._m_normal_switch

            self._m_normal_switch = (0 if  ((self.format == 1) or (self.format == 2))  else 1)
            return getattr(self, '_m_normal_switch', None)

        def _invalidate_normal_switch(self):
            del self._m_normal_switch
        @property
        def start_pos(self):
            if hasattr(self, '_m_start_pos'):
                return self._m_start_pos

            self._m_start_pos = self.p_start_pos
            return getattr(self, '_m_start_pos', None)

        def _invalidate_start_pos(self):
            del self._m_start_pos
        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.space_name
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.collision_name
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2
        @property
        def uv_count(self):
            if hasattr(self, '_m_uv_count'):
                return self._m_uv_count

            self._m_uv_count = self.format_raw >> 8
            return getattr(self, '_m_uv_count', None)

        def _invalidate_uv_count(self):
            del self._m_uv_count
        @property
        def verts_pos(self):
            if hasattr(self, '_m_verts_pos'):
                return self._m_verts_pos

            self._m_verts_pos = (self.p_start_pos + 56) + (32 if self.p_is_spaced else 0)
            return getattr(self, '_m_verts_pos', None)

        def _invalidate_verts_pos(self):
            del self._m_verts_pos

    class BVertexSimple(ReadWriteKaitaiStruct):
        def __init__(self, p_is_spaced, p_start_pos, _io=None, _parent=None, _root=None):
            super(Ht2B3d.BVertexSimple, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.p_is_spaced = p_is_spaced
            self.p_start_pos = p_start_pos

        def _read(self):
            self.bound1 = Ht2B3d.Sphere(self._io, self, self._root)
            self.bound1._read()
            if self.p_is_spaced:
                pass
                self.space_name = (self._io.read_bytes(32)).decode(u"UTF-8")

            self.collision_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.vert_count = self._io.read_s4le()
            self.vert_raw = self._io.read_bytes(self.vert_count * 20)
            self.child_blocks = Ht2B3d.Children(self._io, self, self._root)
            self.child_blocks._read()
            self._dirty = False


        def _fetch_instances(self):
            pass
            self.bound1._fetch_instances()
            if self.p_is_spaced:
                pass

            self.child_blocks._fetch_instances()


        def _write__seq(self, io=None):
            super(Ht2B3d.BVertexSimple, self)._write__seq(io)
            self.bound1._write__seq(self._io)
            if self.p_is_spaced:
                pass
                self._io.write_bytes((self.space_name).encode(u"UTF-8"))

            self._io.write_bytes((self.collision_name).encode(u"UTF-8"))
            self._io.write_s4le(self.vert_count)
            self._io.write_bytes(self.vert_raw)
            self.child_blocks._write__seq(self._io)


        def _check(self):
            if self.bound1._root != self._root:
                raise kaitaistruct.ConsistencyError(u"bound1", self._root, self.bound1._root)
            if self.bound1._parent != self:
                raise kaitaistruct.ConsistencyError(u"bound1", self, self.bound1._parent)
            if self.p_is_spaced:
                pass
                if len((self.space_name).encode(u"UTF-8")) != 32:
                    raise kaitaistruct.ConsistencyError(u"space_name", 32, len((self.space_name).encode(u"UTF-8")))

            if len((self.collision_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"collision_name", 32, len((self.collision_name).encode(u"UTF-8")))
            if len(self.vert_raw) != self.vert_count * 20:
                raise kaitaistruct.ConsistencyError(u"vert_raw", self.vert_count * 20, len(self.vert_raw))
            if self.child_blocks._root != self._root:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self._root, self.child_blocks._root)
            if self.child_blocks._parent != self:
                raise kaitaistruct.ConsistencyError(u"child_blocks", self, self.child_blocks._parent)
            self._dirty = False

        @property
        def start_pos(self):
            if hasattr(self, '_m_start_pos'):
                return self._m_start_pos

            self._m_start_pos = self.p_start_pos
            return getattr(self, '_m_start_pos', None)

        def _invalidate_start_pos(self):
            del self._m_start_pos
        @property
        def string1(self):
            if hasattr(self, '_m_string1'):
                return self._m_string1

            self._m_string1 = self.space_name
            return getattr(self, '_m_string1', None)

        def _invalidate_string1(self):
            del self._m_string1
        @property
        def string2(self):
            if hasattr(self, '_m_string2'):
                return self._m_string2

            self._m_string2 = self.collision_name
            return getattr(self, '_m_string2', None)

        def _invalidate_string2(self):
            del self._m_string2
        @property
        def verts_pos(self):
            if hasattr(self, '_m_verts_pos'):
                return self._m_verts_pos

            self._m_verts_pos = (self.p_start_pos + 52) + (32 if self.p_is_spaced else 0)
            return getattr(self, '_m_verts_pos', None)

        def _invalidate_verts_pos(self):
            del self._m_verts_pos

    class Block(ReadWriteKaitaiStruct):
        def __init__(self, p_group_before, p_start_pos, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.p_group_before = p_group_before
            self.p_start_pos = p_start_pos

        def _read(self):
            self.group_block_start = []
            i = 0
            while True:
                _ = self._io.read_s4le()
                self.group_block_start.append(_)
                if _ == 333:
                    break
                i += 1
            self.block_name = (self._io.read_bytes(32)).decode(u"UTF-8")
            self.block_type = self._io.read_s4le()
            _on = self.block_type
            if _on == 0:
                pass
                self.block_data = Ht2B3d.BUnused(self._io, self, self._root)
                self.block_data._read()
            elif _on == 1:
                pass
                self.block_data = Ht2B3d.BObserver(self._io, self, self._root)
                self.block_data._read()
            elif _on == 10:
                pass
                self.block_data = Ht2B3d.BRenderSwitchCircle(self._io, self, self._root)
                self.block_data._read()
            elif _on == 11:
                pass
                self.block_data = Ht2B3d.BRenderSwitchCylinder(self._io, self, self._root)
                self.block_data._read()
            elif _on == 12:
                pass
                self.block_data = Ht2B3d.BCollisionPlane(self._io, self, self._root)
                self.block_data._read()
            elif _on == 13:
                pass
                self.block_data = Ht2B3d.BTriggerRoom(self._io, self, self._root)
                self.block_data._read()
            elif _on == 14:
                pass
                self.block_data = Ht2B3d.BTriggerCircle(self._io, self, self._root)
                self.block_data._read()
            elif _on == 15:
                pass
                self.block_data = Ht2B3d.BTriggerCircle(self._io, self, self._root)
                self.block_data._read()
            elif _on == 16:
                pass
                self.block_data = Ht2B3d.BTriggerCylinder(self._io, self, self._root)
                self.block_data._read()
            elif _on == 17:
                pass
                self.block_data = Ht2B3d.BTriggerCylinder(self._io, self, self._root)
                self.block_data._read()
            elif _on == 18:
                pass
                self.block_data = Ht2B3d.BConnector(self._io, self, self._root)
                self.block_data._read()
            elif _on == 19:
                pass
                self.block_data = Ht2B3d.BRoom(self._io, self, self._root)
                self.block_data._read()
            elif _on == 2:
                pass
                self.block_data = Ht2B3d.BRenderOrder(self._io, self, self._root)
                self.block_data._read()
            elif _on == 20:
                pass
                self.block_data = Ht2B3d.BCollisionWall(self._io, self, self._root)
                self.block_data._read()
            elif _on == 21:
                pass
                self.block_data = Ht2B3d.BStateMachine(self._io, self, self._root)
                self.block_data._read()
            elif _on == 22:
                pass
                self.block_data = Ht2B3d.BRenderSwitchPlane(self._io, self, self._root)
                self.block_data._read()
            elif _on == 23:
                pass
                self.block_data = Ht2B3d.BCollision(self._io, self, self._root)
                self.block_data._read()
            elif _on == 24:
                pass
                self.block_data = Ht2B3d.BSpace(self._io, self, self._root)
                self.block_data._read()
            elif _on == 25:
                pass
                self.block_data = Ht2B3d.BSound(self._io, self, self._root)
                self.block_data._read()
            elif _on == 26:
                pass
                self.block_data = Ht2B3d.BRenderInsphere(self._io, self, self._root)
                self.block_data._read()
            elif _on == 27:
                pass
                self.block_data = Ht2B3d.BSpriteSimple(self._io, self, self._root)
                self.block_data._read()
            elif _on == 28:
                pass
                self.block_data = Ht2B3d.BSpritePolygon(self._io, self, self._root)
                self.block_data._read()
            elif _on == 29:
                pass
                self.block_data = Ht2B3d.BRenderSwitchDistance(self._io, self, self._root)
                self.block_data._read()
            elif _on == 3:
                pass
                self.block_data = Ht2B3d.BContainerOrdered(self._io, self, self._root)
                self.block_data._read()
            elif _on == 30:
                pass
                self.block_data = Ht2B3d.BPortal(self._io, self, self._root)
                self.block_data._read()
            elif _on == 31:
                pass
                self.block_data = Ht2B3d.BSpriteWithLods(self._io, self, self._root)
                self.block_data._read()
            elif _on == 33:
                pass
                self.block_data = Ht2B3d.BContainerLamp(self._io, self, self._root)
                self.block_data._read()
            elif _on == 34:
                pass
                self.block_data = Ht2B3d.BPointArray(self._io, self, self._root)
                self.block_data._read()
            elif _on == 35:
                pass
                self.block_data = Ht2B3d.BPolygonExtended(self._io, self, self._root)
                self.block_data._read()
            elif _on == 36:
                pass
                self.block_data = Ht2B3d.BVertexExtended(True, self._io.pos(), self._io, self, self._root)
                self.block_data._read()
            elif _on == 37:
                pass
                self.block_data = Ht2B3d.BVertexExtended(False, self._io.pos(), self._io, self, self._root)
                self.block_data._read()
            elif _on == 39:
                pass
                self.block_data = Ht2B3d.BContainerEnv(self._io, self, self._root)
                self.block_data._read()
            elif _on == 4:
                pass
                self.block_data = Ht2B3d.BContainerSpaced(self._io, self, self._root)
                self.block_data._read()
            elif _on == 40:
                pass
                self.block_data = Ht2B3d.BGenerator(self._io, self, self._root)
                self.block_data._read()
            elif _on == 5:
                pass
                self.block_data = Ht2B3d.BContainerSimple(self._io, self, self._root)
                self.block_data._read()
            elif _on == 6:
                pass
                self.block_data = Ht2B3d.BVertexSimple(True, self._io.pos(), self._io, self, self._root)
                self.block_data._read()
            elif _on == 7:
                pass
                self.block_data = Ht2B3d.BVertexSimple(False, self._io.pos(), self._io, self, self._root)
                self.block_data._read()
            elif _on == 8:
                pass
                self.block_data = Ht2B3d.BPolygonSimple(self._io, self, self._root)
                self.block_data._read()
            elif _on == 9:
                pass
                self.block_data = Ht2B3d.BRenderSwitchPlane(self._io, self, self._root)
                self.block_data._read()
            self.group_block_end = []
            i = 0
            while True:
                _ = self._io.read_s4le()
                self.group_block_end.append(_)
                if _ == 555:
                    break
                i += 1
            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.group_block_start)):
                pass

            _on = self.block_type
            if _on == 0:
                pass
                self.block_data._fetch_instances()
            elif _on == 1:
                pass
                self.block_data._fetch_instances()
            elif _on == 10:
                pass
                self.block_data._fetch_instances()
            elif _on == 11:
                pass
                self.block_data._fetch_instances()
            elif _on == 12:
                pass
                self.block_data._fetch_instances()
            elif _on == 13:
                pass
                self.block_data._fetch_instances()
            elif _on == 14:
                pass
                self.block_data._fetch_instances()
            elif _on == 15:
                pass
                self.block_data._fetch_instances()
            elif _on == 16:
                pass
                self.block_data._fetch_instances()
            elif _on == 17:
                pass
                self.block_data._fetch_instances()
            elif _on == 18:
                pass
                self.block_data._fetch_instances()
            elif _on == 19:
                pass
                self.block_data._fetch_instances()
            elif _on == 2:
                pass
                self.block_data._fetch_instances()
            elif _on == 20:
                pass
                self.block_data._fetch_instances()
            elif _on == 21:
                pass
                self.block_data._fetch_instances()
            elif _on == 22:
                pass
                self.block_data._fetch_instances()
            elif _on == 23:
                pass
                self.block_data._fetch_instances()
            elif _on == 24:
                pass
                self.block_data._fetch_instances()
            elif _on == 25:
                pass
                self.block_data._fetch_instances()
            elif _on == 26:
                pass
                self.block_data._fetch_instances()
            elif _on == 27:
                pass
                self.block_data._fetch_instances()
            elif _on == 28:
                pass
                self.block_data._fetch_instances()
            elif _on == 29:
                pass
                self.block_data._fetch_instances()
            elif _on == 3:
                pass
                self.block_data._fetch_instances()
            elif _on == 30:
                pass
                self.block_data._fetch_instances()
            elif _on == 31:
                pass
                self.block_data._fetch_instances()
            elif _on == 33:
                pass
                self.block_data._fetch_instances()
            elif _on == 34:
                pass
                self.block_data._fetch_instances()
            elif _on == 35:
                pass
                self.block_data._fetch_instances()
            elif _on == 36:
                pass
                self.block_data._fetch_instances()
            elif _on == 37:
                pass
                self.block_data._fetch_instances()
            elif _on == 39:
                pass
                self.block_data._fetch_instances()
            elif _on == 4:
                pass
                self.block_data._fetch_instances()
            elif _on == 40:
                pass
                self.block_data._fetch_instances()
            elif _on == 5:
                pass
                self.block_data._fetch_instances()
            elif _on == 6:
                pass
                self.block_data._fetch_instances()
            elif _on == 7:
                pass
                self.block_data._fetch_instances()
            elif _on == 8:
                pass
                self.block_data._fetch_instances()
            elif _on == 9:
                pass
                self.block_data._fetch_instances()
            for i in range(len(self.group_block_end)):
                pass



        def _write__seq(self, io=None):
            super(Ht2B3d.Block, self)._write__seq(io)
            for i in range(len(self.group_block_start)):
                pass
                self._io.write_s4le(self.group_block_start[i])

            self._io.write_bytes((self.block_name).encode(u"UTF-8"))
            self._io.write_s4le(self.block_type)
            _on = self.block_type
            if _on == 0:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 1:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 10:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 11:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 12:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 13:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 14:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 15:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 16:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 17:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 18:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 19:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 2:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 20:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 21:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 22:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 23:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 24:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 25:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 26:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 27:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 28:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 29:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 3:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 30:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 31:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 33:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 34:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 35:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 36:
                pass
                if self.block_data.p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"block_data", self._io.pos(), self.block_data.p_start_pos)
                self.block_data._write__seq(self._io)
            elif _on == 37:
                pass
                if self.block_data.p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"block_data", self._io.pos(), self.block_data.p_start_pos)
                self.block_data._write__seq(self._io)
            elif _on == 39:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 4:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 40:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 5:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 6:
                pass
                if self.block_data.p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"block_data", self._io.pos(), self.block_data.p_start_pos)
                self.block_data._write__seq(self._io)
            elif _on == 7:
                pass
                if self.block_data.p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"block_data", self._io.pos(), self.block_data.p_start_pos)
                self.block_data._write__seq(self._io)
            elif _on == 8:
                pass
                self.block_data._write__seq(self._io)
            elif _on == 9:
                pass
                self.block_data._write__seq(self._io)
            for i in range(len(self.group_block_end)):
                pass
                self._io.write_s4le(self.group_block_end[i])



        def _check(self):
            if len(self.group_block_start) == 0:
                raise kaitaistruct.ConsistencyError(u"group_block_start", 0, len(self.group_block_start))
            for i in range(len(self.group_block_start)):
                pass
                _ = self.group_block_start[i]
                if (_ == 333) != (i == len(self.group_block_start) - 1):
                    raise kaitaistruct.ConsistencyError(u"group_block_start", i == len(self.group_block_start) - 1, _ == 333)

            if len((self.block_name).encode(u"UTF-8")) != 32:
                raise kaitaistruct.ConsistencyError(u"block_name", 32, len((self.block_name).encode(u"UTF-8")))
            _on = self.block_type
            if _on == 0:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 1:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 10:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 11:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 12:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 13:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 14:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 15:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 16:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 17:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 18:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 19:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 2:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 20:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 21:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 22:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 23:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 24:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 25:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 26:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 27:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 28:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 29:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 3:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 30:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 31:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 33:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 34:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 35:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 36:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
                if self.block_data.p_is_spaced != True:
                    raise kaitaistruct.ConsistencyError(u"block_data", True, self.block_data.p_is_spaced)
            elif _on == 37:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
                if self.block_data.p_is_spaced != False:
                    raise kaitaistruct.ConsistencyError(u"block_data", False, self.block_data.p_is_spaced)
            elif _on == 39:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 4:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 40:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 5:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 6:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
                if self.block_data.p_is_spaced != True:
                    raise kaitaistruct.ConsistencyError(u"block_data", True, self.block_data.p_is_spaced)
            elif _on == 7:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
                if self.block_data.p_is_spaced != False:
                    raise kaitaistruct.ConsistencyError(u"block_data", False, self.block_data.p_is_spaced)
            elif _on == 8:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            elif _on == 9:
                pass
                if self.block_data._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"block_data", self._root, self.block_data._root)
                if self.block_data._parent != self:
                    raise kaitaistruct.ConsistencyError(u"block_data", self, self.block_data._parent)
            if len(self.group_block_end) == 0:
                raise kaitaistruct.ConsistencyError(u"group_block_end", 0, len(self.group_block_end))
            for i in range(len(self.group_block_end)):
                pass
                _ = self.group_block_end[i]
                if (_ == 555) != (i == len(self.group_block_end) - 1):
                    raise kaitaistruct.ConsistencyError(u"group_block_end", i == len(self.group_block_end) - 1, _ == 555)

            self._dirty = False

        @property
        def block_group(self):
            if hasattr(self, '_m_block_group'):
                return self._m_block_group

            self._m_block_group = self.p_group_before + self.group_before_count
            return getattr(self, '_m_block_group', None)

        def _invalidate_block_group(self):
            del self._m_block_group
        @property
        def group_after_count(self):
            if hasattr(self, '_m_group_after_count'):
                return self._m_group_after_count

            self._m_group_after_count = len(self.group_block_end) - 1
            return getattr(self, '_m_group_after_count', None)

        def _invalidate_group_after_count(self):
            del self._m_group_after_count
        @property
        def group_before_count(self):
            if hasattr(self, '_m_group_before_count'):
                return self._m_group_before_count

            self._m_group_before_count = len(self.group_block_start) - 1
            return getattr(self, '_m_group_before_count', None)

        def _invalidate_group_before_count(self):
            del self._m_group_before_count
        @property
        def group_before_pos(self):
            if hasattr(self, '_m_group_before_pos'):
                return self._m_group_before_pos

            self._m_group_before_pos = (self.p_start_pos if self.has_group_before else -1)
            return getattr(self, '_m_group_before_pos', None)

        def _invalidate_group_before_pos(self):
            del self._m_group_before_pos
        @property
        def has_group_after(self):
            if hasattr(self, '_m_has_group_after'):
                return self._m_has_group_after

            self._m_has_group_after = self.group_after_count > 0
            return getattr(self, '_m_has_group_after', None)

        def _invalidate_has_group_after(self):
            del self._m_has_group_after
        @property
        def has_group_before(self):
            if hasattr(self, '_m_has_group_before'):
                return self._m_has_group_before

            self._m_has_group_before = self.group_before_count > 0
            return getattr(self, '_m_has_group_before', None)

        def _invalidate_has_group_before(self):
            del self._m_has_group_before
        @property
        def next_group(self):
            if hasattr(self, '_m_next_group'):
                return self._m_next_group

            self._m_next_group = self.block_group + self.group_after_count
            return getattr(self, '_m_next_group', None)

        def _invalidate_next_group(self):
            del self._m_next_group
        @property
        def start_pos(self):
            if hasattr(self, '_m_start_pos'):
                return self._m_start_pos

            self._m_start_pos = self.p_start_pos
            return getattr(self, '_m_start_pos', None)

        def _invalidate_start_pos(self):
            del self._m_start_pos

    class Children(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Children, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.child_cnt = self._io.read_s4le()
            self.child_block = []
            for i in range(self.child_cnt):
                _t_child_block = Ht2B3d.Block((0 if i == 0 else self.child_block[i - 1].next_group), self._io.pos(), self._io, self, self._root)
                try:
                    _t_child_block._read()
                finally:
                    self.child_block.append(_t_child_block)

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.child_block)):
                pass
                self.child_block[i]._fetch_instances()



        def _write__seq(self, io=None):
            super(Ht2B3d.Children, self)._write__seq(io)
            self._io.write_s4le(self.child_cnt)
            for i in range(len(self.child_block)):
                pass
                if self.child_block[i].p_start_pos != self._io.pos():
                    raise kaitaistruct.ConsistencyError(u"child_block", self._io.pos(), self.child_block[i].p_start_pos)
                self.child_block[i]._write__seq(self._io)



        def _check(self):
            if len(self.child_block) != self.child_cnt:
                raise kaitaistruct.ConsistencyError(u"child_block", self.child_cnt, len(self.child_block))
            for i in range(len(self.child_block)):
                pass
                if self.child_block[i]._root != self._root:
                    raise kaitaistruct.ConsistencyError(u"child_block", self._root, self.child_block[i]._root)
                if self.child_block[i]._parent != self:
                    raise kaitaistruct.ConsistencyError(u"child_block", self, self.child_block[i]._parent)
                if self.child_block[i].p_group_before != (0 if i == 0 else self.child_block[i - 1].next_group):
                    raise kaitaistruct.ConsistencyError(u"child_block", (0 if i == 0 else self.child_block[i - 1].next_group), self.child_block[i].p_group_before)

            self._dirty = False


    class Color(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Color, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = []
            for i in range(3):
                self.value.append(self._io.read_f4le())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.value)):
                pass



        def _write__seq(self, io=None):
            super(Ht2B3d.Color, self)._write__seq(io)
            for i in range(len(self.value)):
                pass
                self._io.write_f4le(self.value[i])



        def _check(self):
            if len(self.value) != 3:
                raise kaitaistruct.ConsistencyError(u"value", 3, len(self.value))
            for i in range(len(self.value)):
                pass

            self._dirty = False


    class DataChunks(ReadWriteKaitaiStruct):
        def __init__(self, p_end_pos, _io=None, _parent=None, _root=None):
            super(Ht2B3d.DataChunks, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.p_end_pos = p_end_pos

        def _read(self):
            if self._io.pos() < self.p_end_pos:
                pass
                self.data_blocks = []
                i = 0
                while True:
                    _t_data_blocks = Ht2B3d.Block((0 if i == 0 else self.data_blocks[i - 1].next_group), self._io.pos(), self._io, self, self._root)
                    try:
                        _t_data_blocks._read()
                    finally:
                        _ = _t_data_blocks
                        self.data_blocks.append(_)
                    if self._io.pos() >= self.p_end_pos:
                        break
                    i += 1

            self._dirty = False


        def _fetch_instances(self):
            pass
            if self._io.pos() < self.p_end_pos:
                pass
                for i in range(len(self.data_blocks)):
                    pass
                    self.data_blocks[i]._fetch_instances()




        def _write__seq(self, io=None):
            super(Ht2B3d.DataChunks, self)._write__seq(io)
            if self._io.pos() < self.p_end_pos:
                pass
                if len(self.data_blocks) == 0:
                    raise kaitaistruct.ConsistencyError(u"data_blocks", 0, len(self.data_blocks))
                for i in range(len(self.data_blocks)):
                    pass
                    if self.data_blocks[i]._root != self._root:
                        raise kaitaistruct.ConsistencyError(u"data_blocks", self._root, self.data_blocks[i]._root)
                    if self.data_blocks[i]._parent != self:
                        raise kaitaistruct.ConsistencyError(u"data_blocks", self, self.data_blocks[i]._parent)
                    if self.data_blocks[i].p_group_before != (0 if i == 0 else self.data_blocks[i - 1].next_group):
                        raise kaitaistruct.ConsistencyError(u"data_blocks", (0 if i == 0 else self.data_blocks[i - 1].next_group), self.data_blocks[i].p_group_before)
                    if self.data_blocks[i].p_start_pos != self._io.pos():
                        raise kaitaistruct.ConsistencyError(u"data_blocks", self._io.pos(), self.data_blocks[i].p_start_pos)
                    self.data_blocks[i]._write__seq(self._io)
                    _ = self.data_blocks[i]
                    if (self._io.pos() >= self.p_end_pos) != (i == len(self.data_blocks) - 1):
                        raise kaitaistruct.ConsistencyError(u"data_blocks", i == len(self.data_blocks) - 1, self._io.pos() >= self.p_end_pos)




        def _check(self):
            self._dirty = False


    class FileHeader(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.FileHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.magic = self._io.read_bytes(4)
            if not self.magic == b"\x62\x33\x64\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x62\x33\x64\x00", self.magic, self._io, u"/types/file_header/seq/0")
            self.len_file = self._io.read_s4le()
            self.ofc_materials = self._io.read_s4le()
            self.len_materials_section = self._io.read_s4le()
            self.ofc_nodes = self._io.read_s4le()
            self.len_nodes = self._io.read_s4le()
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Ht2B3d.FileHeader, self)._write__seq(io)
            self._io.write_bytes(self.magic)
            self._io.write_s4le(self.len_file)
            self._io.write_s4le(self.ofc_materials)
            self._io.write_s4le(self.len_materials_section)
            self._io.write_s4le(self.ofc_nodes)
            self._io.write_s4le(self.len_nodes)


        def _check(self):
            if len(self.magic) != 4:
                raise kaitaistruct.ConsistencyError(u"magic", 4, len(self.magic))
            if not self.magic == b"\x62\x33\x64\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x62\x33\x64\x00", self.magic, None, u"/types/file_header/seq/0")
            self._dirty = False


    class MaterialsList(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.MaterialsList, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.mat_count = self._io.read_s4le()
            self.mat_names = []
            for i in range(self.mat_count):
                self.mat_names.append((self._io.read_bytes(32)).decode(u"UTF-8"))

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.mat_names)):
                pass



        def _write__seq(self, io=None):
            super(Ht2B3d.MaterialsList, self)._write__seq(io)
            self._io.write_s4le(self.mat_count)
            for i in range(len(self.mat_names)):
                pass
                self._io.write_bytes((self.mat_names[i]).encode(u"UTF-8"))



        def _check(self):
            if len(self.mat_names) != self.mat_count:
                raise kaitaistruct.ConsistencyError(u"mat_names", self.mat_count, len(self.mat_names))
            for i in range(len(self.mat_names)):
                pass
                if len((self.mat_names[i]).encode(u"UTF-8")) != 32:
                    raise kaitaistruct.ConsistencyError(u"mat_names", 32, len((self.mat_names[i]).encode(u"UTF-8")))

            self._dirty = False


    class Point(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Point, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = []
            for i in range(3):
                self.value.append(self._io.read_f4le())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.value)):
                pass



        def _write__seq(self, io=None):
            super(Ht2B3d.Point, self)._write__seq(io)
            for i in range(len(self.value)):
                pass
                self._io.write_f4le(self.value[i])



        def _check(self):
            if len(self.value) != 3:
                raise kaitaistruct.ConsistencyError(u"value", 3, len(self.value))
            for i in range(len(self.value)):
                pass

            self._dirty = False


    class Polygon28(ReadWriteKaitaiStruct):
        def __init__(self, p_start_pos, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Polygon28, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.p_start_pos = p_start_pos

        def _read(self):
            self.format_raw = self._io.read_s4le()
            self.unk_f = self._io.read_f4le()
            self.unk_i = self._io.read_s4le()
            self.texnum = self._io.read_s4le()
            self.vert_count = self._io.read_s4le()
            self.verts_raw = self._io.read_bytes(self.vert_count * (8 + (self.uv_count * 8 if self.use_uv else 0)))
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Ht2B3d.Polygon28, self)._write__seq(io)
            self._io.write_s4le(self.format_raw)
            self._io.write_f4le(self.unk_f)
            self._io.write_s4le(self.unk_i)
            self._io.write_s4le(self.texnum)
            self._io.write_s4le(self.vert_count)
            self._io.write_bytes(self.verts_raw)


        def _check(self):
            if len(self.verts_raw) != self.vert_count * (8 + (self.uv_count * 8 if self.use_uv else 0)):
                raise kaitaistruct.ConsistencyError(u"verts_raw", self.vert_count * (8 + (self.uv_count * 8 if self.use_uv else 0)), len(self.verts_raw))
            self._dirty = False

        @property
        def format(self):
            if hasattr(self, '_m_format'):
                return self._m_format

            self._m_format = self.format_raw
            return getattr(self, '_m_format', None)

        def _invalidate_format(self):
            del self._m_format
        @property
        def normal_switch(self):
            if hasattr(self, '_m_normal_switch'):
                return self._m_normal_switch

            self._m_normal_switch = (-1 if (not (self.use_normal)) else (0 if self.format & 1 > 0 else 1))
            return getattr(self, '_m_normal_switch', None)

        def _invalidate_normal_switch(self):
            del self._m_normal_switch
        @property
        def start_pos(self):
            if hasattr(self, '_m_start_pos'):
                return self._m_start_pos

            self._m_start_pos = self.p_start_pos
            return getattr(self, '_m_start_pos', None)

        def _invalidate_start_pos(self):
            del self._m_start_pos
        @property
        def use_normal(self):
            if hasattr(self, '_m_use_normal'):
                return self._m_use_normal

            self._m_use_normal =  ((self.format & 32 > 0) and (self.format & 16 > 0)) 
            return getattr(self, '_m_use_normal', None)

        def _invalidate_use_normal(self):
            del self._m_use_normal
        @property
        def use_uv(self):
            if hasattr(self, '_m_use_uv'):
                return self._m_use_uv

            self._m_use_uv = self.format & 2 > 0
            return getattr(self, '_m_use_uv', None)

        def _invalidate_use_uv(self):
            del self._m_use_uv
        @property
        def uv_count(self):
            if hasattr(self, '_m_uv_count'):
                return self._m_uv_count

            self._m_uv_count = ((self.format & 65280) >> 8) + 1
            return getattr(self, '_m_uv_count', None)

        def _invalidate_uv_count(self):
            del self._m_uv_count
        @property
        def verts_pos(self):
            if hasattr(self, '_m_verts_pos'):
                return self._m_verts_pos

            self._m_verts_pos = self.p_start_pos + 20
            return getattr(self, '_m_verts_pos', None)

        def _invalidate_verts_pos(self):
            del self._m_verts_pos

    class Polygon8(ReadWriteKaitaiStruct):
        def __init__(self, p_start_pos, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Polygon8, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.p_start_pos = p_start_pos

        def _read(self):
            self.format_raw = self._io.read_s4le()
            self.unk_f = self._io.read_f4le()
            self.unk_i = self._io.read_s4le()
            self.texnum = self._io.read_s4le()
            self.vert_count = self._io.read_s4le()
            self.verts_raw = self._io.read_bytes(self.vert_count * ((4 + (self.uv_count * 8 if self.use_uv else 0)) + ((12 if self.normal_switch == 0 else 4) if self.use_normal else 0)))
            self._dirty = False


        def _fetch_instances(self):
            pass


        def _write__seq(self, io=None):
            super(Ht2B3d.Polygon8, self)._write__seq(io)
            self._io.write_s4le(self.format_raw)
            self._io.write_f4le(self.unk_f)
            self._io.write_s4le(self.unk_i)
            self._io.write_s4le(self.texnum)
            self._io.write_s4le(self.vert_count)
            self._io.write_bytes(self.verts_raw)


        def _check(self):
            if len(self.verts_raw) != self.vert_count * ((4 + (self.uv_count * 8 if self.use_uv else 0)) + ((12 if self.normal_switch == 0 else 4) if self.use_normal else 0)):
                raise kaitaistruct.ConsistencyError(u"verts_raw", self.vert_count * ((4 + (self.uv_count * 8 if self.use_uv else 0)) + ((12 if self.normal_switch == 0 else 4) if self.use_normal else 0)), len(self.verts_raw))
            self._dirty = False

        @property
        def format(self):
            if hasattr(self, '_m_format'):
                return self._m_format

            self._m_format = self.format_raw ^ 1
            return getattr(self, '_m_format', None)

        def _invalidate_format(self):
            del self._m_format
        @property
        def normal_switch(self):
            if hasattr(self, '_m_normal_switch'):
                return self._m_normal_switch

            self._m_normal_switch = (-1 if (not (self.use_normal)) else (0 if self.format & 1 > 0 else 1))
            return getattr(self, '_m_normal_switch', None)

        def _invalidate_normal_switch(self):
            del self._m_normal_switch
        @property
        def start_pos(self):
            if hasattr(self, '_m_start_pos'):
                return self._m_start_pos

            self._m_start_pos = self.p_start_pos
            return getattr(self, '_m_start_pos', None)

        def _invalidate_start_pos(self):
            del self._m_start_pos
        @property
        def texnum_pos1(self):
            if hasattr(self, '_m_texnum_pos1'):
                return self._m_texnum_pos1

            self._m_texnum_pos1 = self.p_start_pos + 12
            return getattr(self, '_m_texnum_pos1', None)

        def _invalidate_texnum_pos1(self):
            del self._m_texnum_pos1
        @property
        def use_normal(self):
            if hasattr(self, '_m_use_normal'):
                return self._m_use_normal

            self._m_use_normal =  ((self.format & 32 > 0) and (self.format & 16 > 0)) 
            return getattr(self, '_m_use_normal', None)

        def _invalidate_use_normal(self):
            del self._m_use_normal
        @property
        def use_uv(self):
            if hasattr(self, '_m_use_uv'):
                return self._m_use_uv

            self._m_use_uv = self.format & 2 > 0
            return getattr(self, '_m_use_uv', None)

        def _invalidate_use_uv(self):
            del self._m_use_uv
        @property
        def uv_count(self):
            if hasattr(self, '_m_uv_count'):
                return self._m_uv_count

            self._m_uv_count = ((self.format & 65280) >> 8) + (1 if self.use_uv else 0)
            return getattr(self, '_m_uv_count', None)

        def _invalidate_uv_count(self):
            del self._m_uv_count
        @property
        def verts_pos(self):
            if hasattr(self, '_m_verts_pos'):
                return self._m_verts_pos

            self._m_verts_pos = self.p_start_pos + 20
            return getattr(self, '_m_verts_pos', None)

        def _invalidate_verts_pos(self):
            del self._m_verts_pos

    class Sphere(ReadWriteKaitaiStruct):
        def __init__(self, _io=None, _parent=None, _root=None):
            super(Ht2B3d.Sphere, self).__init__(_io)
            self._parent = _parent
            self._root = _root

        def _read(self):
            self.value = []
            for i in range(4):
                self.value.append(self._io.read_f4le())

            self._dirty = False


        def _fetch_instances(self):
            pass
            for i in range(len(self.value)):
                pass



        def _write__seq(self, io=None):
            super(Ht2B3d.Sphere, self)._write__seq(io)
            for i in range(len(self.value)):
                pass
                self._io.write_f4le(self.value[i])



        def _check(self):
            if len(self.value) != 4:
                raise kaitaistruct.ConsistencyError(u"value", 4, len(self.value))
            for i in range(len(self.value)):
                pass

            self._dirty = False



