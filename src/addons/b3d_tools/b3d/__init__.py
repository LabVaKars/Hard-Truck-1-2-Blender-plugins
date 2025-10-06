

# To support reload properly, try to access a package var, if it's there,
# reload everything
if "bpy" in locals():
    print("Reimporting modules!!!")
    import importlib

    importlib.reload(common)
    importlib.reload(geom_nodes)
    importlib.reload(data_api_utils)
    importlib.reload(custom_ui_list)
    importlib.reload(class_descr)
    importlib.reload(callbacks)
    importlib.reload(classes)
    importlib.reload(ui_utils)
    importlib.reload(imghelp)
    importlib.reload(import_b3d)
    importlib.reload(import_way)
    importlib.reload(import_res)
    importlib.reload(export_b3d)
    importlib.reload(export_way)
    importlib.reload(export_res)
    importlib.reload(scripts)
    importlib.reload(operators)
    importlib.reload(panels)
    importlib.reload(menus)
    importlib.reload(mytool)
else:
    import bpy
    from . import (
        common,
        geom_nodes,
        data_api_utils,
        custom_ui_list,
        class_descr,
        callbacks,
        classes,
        ui_utils,
        imghelp,
        import_b3d,
        import_way,
        import_res,
        export_b3d,
        export_way,
        export_res,
        scripts,
        operators,
        panels,
        menus,
        mytool
    )

def register():
    print("registering addons")
    custom_ui_list.register()
    class_descr.register()
    classes.register()
    menus.register()
    operators.register()
    panels.register()
    mytool.register()


def unregister():
    print("unregistering addons")
    mytool.unregister()
    panels.unregister()
    operators.unregister()
    menus.unregister()
    classes.unregister()
    class_descr.unregister()
    custom_ui_list.unregister()
