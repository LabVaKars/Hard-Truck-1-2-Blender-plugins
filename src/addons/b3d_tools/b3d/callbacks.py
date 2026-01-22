import bpy
import time

from ..consts import (
    BLOCK_TYPE,
    CACHE_TIME,
    b40PresetList
)

from .common import (
    get_root_obj,
    get_col_property_by_name,
    is_root_obj,
    get_room_obj,
    get_parent
)

from ..common import (
    get_res_tool,
    get_res_modules,
    get_panel_tool,
    callbacks_logger
)
log = callbacks_logger

callback_cache = {}
callback_cache_last_used = {}
callback_cache_never_expire = set()

def clear_cache(cache_key):
    global callback_cache
    global callback_cache_last_used
    global callback_cache_never_expire

    if cache_key in callback_cache:
        callback_cache[cache_key] = None
        callback_cache_last_used[cache_key] = None
        callback_cache_never_expire.discard(cache_key)

def get_cached(cache_key):
    global callback_cache
    global callback_cache_last_used
    global callback_cache_never_expire

    if cache_key in callback_cache_never_expire:
        return callback_cache.get(cache_key)

    last_used = callback_cache_last_used.get(cache_key)
    if last_used is None:
        return None

    if time.perf_counter() - last_used < CACHE_TIME:
        return callback_cache.get(cache_key)

    # TTL expired → remove entry
    clear_cache(cache_key)
    return None
    
def save_cache(cache_key, values, never_expire = False):
    global callback_cache
    global callback_cache_last_used
    global callback_cache_never_expire
    
    if get_cached(cache_key) is None:
        callback_cache[cache_key] = values
        if never_expire:
            callback_cache_never_expire.add(cache_key)
            callback_cache_last_used.pop(cache_key, None)
        else:
            callback_cache_last_used[cache_key] = time.perf_counter()

def presets_callback(bnum):
    def callback_func(self, context):
        
        cache_key = 'presets'
        
        enum_properties = get_cached(cache_key)
        
        if enum_properties:
            return enum_properties
        
        enum_properties = [("?", "None", "")]
        presets = None
        if bnum == 40:
            presets = b40PresetList

        if presets is not None:
            enum_properties.extend(presets)

        save_cache(cache_key, enum_properties, True)

        return enum_properties
    return callback_func


def referenceables_callback(self, context):
    
    cache_key = 'referenceables'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties
    
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

    root_obj = get_root_obj(context.object)
    module_name = root_obj.name[:-4]

    res_modules = get_res_modules(context)
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
    
        enum_properties = [("?", "None", "")]

        res_module = context.object.path_resolve('["{}{}"]'.format(pname[:-1], int(pname[-1])-1))

        root_obj = bpy.data.objects.get('{}.b3d'.format(res_module))
        if root_obj:
            rooms = [cn for cn in root_obj.children if cn.get(BLOCK_TYPE) == 19]

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

    mytool = get_panel_tool(context)

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


def b3d_modules_callback(self, context):

    cache_key = 'b3d_modules'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties
    
    res_modules = get_res_modules(context)
    modules = [cn for cn in res_modules if cn.value != "-1"]
    enum_properties = [("?", "None", "")]
    enum_properties.extend([(cn.value, cn.value, "") for i, cn in enumerate(modules)])
    
    save_cache(cache_key, enum_properties)

    return enum_properties


def res_modules_callback(self, context):

    res_modules = get_res_modules(context)

    enum_properties = [("-1", "None", "")]

    enum_properties.extend([(str(i), cn.value, "") for i, cn in enumerate(res_modules)])

    return enum_properties


def render_tree_callback(self, context):

    cache_key = 'render_tree'

    enum_properties = get_cached(cache_key)
    if enum_properties:
        return enum_properties

    enum_properties = []

    mytool = get_panel_tool(context)

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

    mytool = get_panel_tool(context)

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

    mytool = get_panel_tool(context)

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