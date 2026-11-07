if "bpy" in locals():
    print("Reimporting modules!!!")
    import importlib
    importlib.reload(kaitaistruct)
    importlib.reload(b3d_geometry_decode)
    importlib.reload(ht2_b3d)
else:
    import bpy
    import sys
    from . import kaitaistruct
    sys.modules.setdefault("kaitaistruct", kaitaistruct)
    from . import (
        b3d_geometry_decode,
        ht2_b3d
    )
