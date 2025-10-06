import bpy
import time

from ..consts import (
    BLOCK_TYPE,
    CACHE_TIME
)

from .common import (
    get_root_obj,
    get_col_property_by_name,
    is_root_obj,
    get_room_obj,
    get_parent

)

from ..common import callbacks_logger
log = callbacks_logger

callback_cache = {}
callback_cache_last_used = {}

def get_cached(cache_key):
    global callback_cache
    global callback_cache_last_used
    if callback_cache_last_used.get(cache_key) is not None \
        and time.perf_counter() - callback_cache_last_used.get(cache_key) < CACHE_TIME:
        return callback_cache.get(cache_key)
    return None
    
def save_cache(cache_key, values):
    global callback_cache
    global callback_cache_last_used
    
    callback_cache[cache_key] = values
    callback_cache_last_used[cache_key] = time.perf_counter()


def referenceables_callback(self, context):
    
    cache_key = 'referenceables'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties
    
    mytool = context.scene.my_tool
    root_obj = get_root_obj(context.object)

    referenceables = [cn for cn in root_obj.children if cn.get(BLOCK_TYPE) != 24]

    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(referenceables)])

    save_cache(cache_key, enum_properties)

    return enum_properties

def spaces_callback(self, context):
    
    cache_key = 'spaces'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    mytool = context.scene.my_tool
    root_obj = get_root_obj(context.object)

    spaces = [cn for cn in bpy.data.objects if cn.get(BLOCK_TYPE) == 24 and get_root_obj(cn) == root_obj]

    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(spaces)])

    save_cache(cache_key, enum_properties)

    return enum_properties

def res_materials_callback(self, context):
    
    cache_key = 'res_materials'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    mytool = context.scene.my_tool
    root_obj = get_root_obj(context.object)
    module_name = root_obj.name[:-4]

    res_modules = mytool.res_modules
    cur_module = get_col_property_by_name(res_modules, module_name)

    enum_properties = [("-1", "None", "")]
    if(cur_module is not None):
        enum_properties.extend([(str(i), cn.mat_name, "") for i, cn in enumerate(cur_module.materials)])

    save_cache(cache_key, enum_properties)

    return enum_properties

def rooms_callback(bname, pname):
    def callback_func(self, context):
        
        cache_key = 'rooms'

        enum_properties = get_cached(cache_key)
        if enum_properties:
            return enum_properties
    
        enum_properties = []

        mytool = context.scene.my_tool
        res_module = context.object.path_resolve('["{}"]'.format(pname))

        root_obj = bpy.data.objects.get('{}.b3d'.format(res_module))
        if root_obj:
            rooms = [cn for cn in root_obj.children if cn.get(BLOCK_TYPE) == 19]

            enum_properties = [("?", "None", "")]
            enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(rooms)])

            save_cache(cache_key, enum_properties)

        return enum_properties
    return callback_func


def modules_callback(self, context):
    
    cache_key = 'modules'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties
    
    modules = [cn for cn in bpy.data.objects if is_root_obj(cn)]
    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name[:-4], cn.name[:-4], "") for i, cn in enumerate(modules)])

    save_cache(cache_key, enum_properties)

    return enum_properties

def rooms_callback_mytool(self, context):

    cache_key = 'rooms_mytool'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    enum_properties = []

    mytool = context.scene.my_tool

    selected_module = getattr(mytool, 'active_module')
    if selected_module not in ['?', '']:
        root_obj = bpy.data.objects.get('{}.b3d'.format(selected_module))
        if root_obj:
            rooms = [cn for cn in root_obj.children if cn.get(BLOCK_TYPE) == 19]
    else:
        rooms = [cn for cn in bpy.data.objects if cn.get(BLOCK_TYPE) == 19]

    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(rooms)])

    save_cache(cache_key, enum_properties)

    return enum_properties


def res_modules_callback(self, context):

    cache_key = 'res_modules'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties
    
    mytool = bpy.context.scene.my_tool
    modules = [cn for cn in mytool.res_modules if cn.value != "-1"]
    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.value, cn.value, "") for i, cn in enumerate(modules)])
    
    save_cache(cache_key, enum_properties)

    return enum_properties


def render_tree_callback(self, context):

    cache_key = 'render_tree'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    enum_properties = []

    mytool = context.scene.my_tool

    selected_module = getattr(mytool, 'active_module')
    selected_room = getattr(mytool, 'active_room')
    block_9 = []
    if selected_room not in ['?', '']:
        room_obj = bpy.data.objects.get(selected_room)
        if room_obj:
            block_9 = [cn for cn in bpy.data.objects if get_room_obj(cn) == room_obj and cn.get(BLOCK_TYPE) == 9 and get_parent(cn).get(BLOCK_TYPE) != 9]
    elif selected_module not in ['?', '']:
        root_obj = bpy.data.objects.get('{}.b3d'.format(selected_module))
        if root_obj:
            block_9 = [cn for cn in bpy.data.objects if get_root_obj(cn) == root_obj and cn.get(BLOCK_TYPE) == 9 and get_parent(cn).get(BLOCK_TYPE) != 9]

    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(block_9)])

    save_cache(cache_key, enum_properties)

    return enum_properties

def LOD_callback(self, context):

    cache_key = 'LOD'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    enum_properties = []

    mytool = context.scene.my_tool

    selected_module = getattr(mytool, 'active_module')
    selected_room = getattr(mytool, 'active_room')
    if selected_room not in ['?', '']:
        room_obj = bpy.data.objects.get(selected_room)
        if room_obj:
            block_10 = [cn for cn in bpy.data.objects if get_room_obj(cn) == room_obj and cn.get(BLOCK_TYPE) == 10 and get_parent(cn).get(BLOCK_TYPE) != 10]
    elif selected_module not in ['?', '']:
        root_obj = bpy.data.objects.get('{}.b3d'.format(selected_module))
        if root_obj:
            block_10 = [cn for cn in bpy.data.objects if get_root_obj(cn) == root_obj and cn.get(BLOCK_TYPE) == 10 and get_parent(cn).get(BLOCK_TYPE) != 10]

    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(block_10)])

    save_cache(cache_key, enum_properties)

    return enum_properties

def event_callback(self, context):

    cache_key = 'event'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    enum_properties = []

    mytool = context.scene.my_tool

    selected_module = getattr(mytool, 'active_module')
    selected_room = getattr(mytool, 'active_room')
    if selected_room not in ['?', '']:
        room_obj = bpy.data.objects.get(selected_room)
        if room_obj:
            block_21 = [cn for cn in bpy.data.objects if get_room_obj(cn) == room_obj and cn.get(BLOCK_TYPE) == 21 and get_parent(cn).get(BLOCK_TYPE) != 21]
    elif selected_module not in ['?', '']:
        root_obj = bpy.data.objects.get('{}.b3d'.format(selected_module))
        if root_obj:
            block_21 = [cn for cn in bpy.data.objects if get_root_obj(cn) == root_obj and cn.get(BLOCK_TYPE) == 21 and get_parent(cn).get(BLOCK_TYPE) != 21]

    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.name, cn.name, "") for i, cn in enumerate(block_21)])

    save_cache(cache_key, enum_properties)

    return enum_properties