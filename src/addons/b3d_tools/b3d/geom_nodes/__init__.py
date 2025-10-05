if "bpy" in locals():
    print("Reimporting modules!!!")
    import importlib
    importlib.reload(get_tangent_point_xy)
    importlib.reload(pie_segment)
    importlib.reload(circle_visualize)
    importlib.reload(render_branch_visualize)
    importlib.reload(lod_branch_visualize)
    importlib.reload(portal_visualize)
else:
    import bpy
    from . import (
        get_tangent_point_xy,
        pie_segment,
        circle_visualize,
        render_branch_visualize,
        lod_branch_visualize,
        portal_visualize
    )
