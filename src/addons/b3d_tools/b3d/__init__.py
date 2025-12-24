

# To support reload properly, try to access a package var, if it's there,
# reload everything
if "bpy" in locals():
    print("Reimporting modules!!!")
    import importlib

    importlib.reload(common)
    importlib.reload(common_classes)
    importlib.reload(geom_nodes)
    importlib.reload(data_api_utils)
    importlib.reload(custom_ui_list)
    importlib.reload(restool)
    importlib.reload(blocktool_defs)
    importlib.reload(callbacks)
    importlib.reload(blocktool)
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
    importlib.reload(paneltool)
else:
    import bpy
    from . import (
        common,
        common_classes,
        geom_nodes,
        data_api_utils,
        custom_ui_list,
        restool,
        blocktool_defs,
        callbacks,
        blocktool,
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
        paneltool
    )

def register():
    print("registering addons")
    common_classes.register()
    custom_ui_list.register()
    restool.register()
    blocktool.register()
    paneltool.register()
    menus.register()
    operators.register()
    panels.register()


def unregister():
    print("unregistering addons")
    panels.unregister()
    operators.unregister()
    menus.unregister()
    paneltool.unregister()
    blocktool.unregister()
    restool.unregister()
    custom_ui_list.unregister()
    common_classes.unregister()
