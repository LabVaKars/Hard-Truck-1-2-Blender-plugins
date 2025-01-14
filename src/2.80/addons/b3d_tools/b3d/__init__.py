

# To support reload properly, try to access a package var, if it's there,
# reload everything
if "bpy" in locals():
    print("Reimporting modules!!!")
    import importlib

    importlib.reload(common)
    importlib.reload(custom_UIList)
    importlib.reload(class_descr)
    importlib.reload(classes)
    importlib.reload(imghelp)
    importlib.reload(import_b3d)
    importlib.reload(import_way)
    importlib.reload(export_b3d)
    importlib.reload(export_way)
    importlib.reload(panel)
    importlib.reload(menus)
else:
    import bpy
    from . import (
        common,
        custom_UIList,
        class_descr,
        classes,
        imghelp,
        import_b3d,
        import_way,
        export_b3d,
        export_way,
        panel,
        menus
    )

def register():
    print("registering addon")
    custom_UIList.register()
    class_descr.register()
    classes.register()
    menus.register()
    panel.register()


def unregister():
    print("unregistering addon")
    panel.unregister()
    menus.unregister()
    classes.unregister()
    class_descr.unregister()
    custom_UIList.unregister()
