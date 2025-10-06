import bpy

from .. import consts

from ..compatibility import (
    get_ui_region,
    get_active_object,
    layout_split
)

from .custom_ui_list import (
    draw_list_controls
)

from .ui_utils import (
    draw_common,
    draw_fields_by_type
)

from .classes import (
    BlockClassHandler
)

from .class_descr import (
    Pvb008, Pvb035,
    Pfb008, Pfb028, Pfb035
)

from .common import (
    get_current_res_index
)

from ..common import panels_logger
log = panels_logger

# ------------------------------------------------------------------------
# panels
# ------------------------------------------------------------------------

class OBJECT_PT_b3d_info_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_info_panel"
    bl_label = "Block info"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        b3d_obj = get_active_object()

        if b3d_obj is not None:
            draw_common(self, b3d_obj)

class OBJECT_PT_b3d_add_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_add_panel"
    bl_label = "Block add"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool


class OBJECT_PT_b3d_single_add_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_single_add_panel"
    bl_label = "Single block"
    bl_parent_id = "OBJECT_PT_b3d_add_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        
        block_type = int(mytool.add_block_type_enum)

        self.layout.label(text="Block type:")
        layout.prop(mytool, "add_block_type_enum", text="")
        layout.prop(mytool, "block_name_string")

        zclass = BlockClassHandler.get_class_def_by_type(block_type)

        if zclass is not None:
            draw_fields_by_type(self, zclass)

        layout.operator("wm.single_add_operator")

class OBJECT_PT_b3d_hier_add_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_hier_add_panel"
    bl_label = "Block hierarchy"
    bl_parent_id = "OBJECT_PT_b3d_add_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "current_hierarchy_enum")

        layout.prop(mytool, "block_name_string")
        layout.prop(mytool, "lod_level_int")

        current_hier = getattr(mytool, "current_hierarchy_enum")
        lod_level = getattr(mytool, "lod_level_int")

        if current_hier == "LOD_9":
            zclass = BlockClassHandler.get_class_def_by_type(9)
            draw_fields_by_type(self, zclass)
            layout.operator("wm.hierarchy_add_operator")
        elif current_hier == "LOD_10":
            zclass = BlockClassHandler.get_class_def_by_type(10)
            draw_fields_by_type(self, zclass)
            layout.operator("wm.hierarchy_add_operator")
        elif current_hier == "LOD_21":
            zclass = BlockClassHandler.get_class_def_by_type(21)
            draw_fields_by_type(self, zclass)


class OBJECT_PT_b3d_cast_add_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_cast_add_panel"
    bl_label = "Cast to B3D object"
    bl_parent_id = "OBJECT_PT_b3d_add_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        split = layout_split(layout, 0.75)
        c = split.column()
        c.prop(mytool, 'parent_str')
        c = split.column()
        c.operator("wm.set_parent_operator")

        layout.prop(mytool, "cast_type_enum")
        cast_type = mytool.cast_type_enum
        layout.prop(mytool, "cast_copy")
        box = layout.box()
        if cast_type == 'mesh':
            box.prop(mytool, "vertex_block_enum")
            box.prop(mytool, "poly_block_enum")

        box.operator("wm.cast_add_operator")

class OBJECT_PT_b3d_pfb_edit_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_pfb_edit_panel"
    bl_label = "Multiple polygons edit"
    bl_parent_id = "OBJECT_PT_b3d_edit_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        b3d_obj = get_active_object()
        if b3d_obj is not None: 
            if consts.BLOCK_TYPE in b3d_obj:
                block_type = b3d_obj[consts.BLOCK_TYPE]
            else:
                block_type = None

            return (context.object is not None) and block_type in [8, 28, 35]

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        b3d_obj = get_active_object()

        if b3d_obj is not None:

            if consts.BLOCK_TYPE in b3d_obj:
                block_type = b3d_obj[consts.BLOCK_TYPE]
            else:
                block_type = None

            if block_type in [8, 28, 35]:
                layout.operator("wm.get_face_values_operator")
                layout.operator("wm.set_face_values_operator")
                layout.operator("wm.select_similar_faces_operator")

            if block_type == 8:
                draw_fields_by_type(self, Pfb008)
            if block_type == 28:
                draw_fields_by_type(self, Pfb028)
            if block_type == 35:
                draw_fields_by_type(self, Pfb035)

class OBJECT_PT_b3d_pvb_edit_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_pvb_edit_panel"
    bl_label = "Multiple vertexes edit"
    bl_parent_id = "OBJECT_PT_b3d_edit_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        #Disabled for now. More analyze needed.
        return False

        b3d_obj = get_active_object()
        if consts.BLOCK_TYPE in b3d_obj:
            block_type = b3d_obj[consts.BLOCK_TYPE]
        else:
            block_type = None

        return (context.object is not None) and block_type in [8, 28, 35]

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        b3d_obj = get_active_object()

        if b3d_obj is not None:

            if consts.BLOCK_TYPE in b3d_obj:
                block_type = b3d_obj[consts.BLOCK_TYPE]
            else:
                block_type = None

            if block_type == 8:
                draw_fields_by_type(self, Pvb008)
            if block_type == 35:
                draw_fields_by_type(self, Pvb035)

            if block_type in [8, 28, 35]:
                layout.operator("wm.get_vertex_values_operator")
                layout.operator("wm.set_vertex_values_operator")

class OBJECT_PT_b3d_edit_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_edit_panel"
    bl_label = "Block edit"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

class OBJECT_PT_b3d_pob_edit_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_pob_edit_panel"
    bl_label = "Multiple blocks"
    bl_parent_id = "OBJECT_PT_b3d_edit_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        block_type = ''
        #for i in range(len(bpy.context.selected_objects)):

        b3d_obj = get_active_object()

        # if len(bpy.context.selected_objects):
        #     for i in range(1):
        if b3d_obj is not None:

            if consts.BLOCK_TYPE in b3d_obj:
                block_type = b3d_obj[consts.BLOCK_TYPE]
            # else:
            #     block_type = None

                len_str = str(len(b3d_obj.children))

                zclass = BlockClassHandler.get_class_def_by_type(block_type)

                layout.operator("wm.get_block_values_operator")
                layout.operator("wm.set_block_values_operator")
                layout.operator("wm.select_similar_objects_operator")

                if zclass is not None:
                    draw_fields_by_type(self, zclass)


class OBJECT_PT_b3d_pob_single_edit_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_pob_single_edit_panel"
    bl_label = "Single block"
    bl_parent_id = "OBJECT_PT_b3d_edit_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        #for i in range(len(bpy.context.selected_objects)):

        b3d_obj = get_active_object()

        # if len(bpy.context.selected_objects):
        #     for i in range(1):
        if b3d_obj is not None:

            if consts.BLOCK_TYPE in b3d_obj:
                block_type = b3d_obj[consts.BLOCK_TYPE]
            # else:
            #     block_type = None

                len_str = str(len(b3d_obj.children))

                zclass = BlockClassHandler.get_class_def_by_type(block_type)

                if zclass is not None:
                    draw_fields_by_type(self, zclass, False)

            # else:
            #     self.layout.label(text="Выбранный объект не имеет типа.")
            #     self.layout.label(text="Чтобы указать его, нажмите на кнопку сохранения настроек.")

            # layout.operator("wm.del_block_values_operator")
            # layout.operator("wm.fix_uv_operator")
            # layout.operator("wm.fix_verts_operator")

class OBJECT_PT_b3d_hier_edit_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_hier_edit_panel"
    bl_parent_id = "OBJECT_PT_b3d_edit_panel"
    bl_label = "Block hierarchy"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return True

    def draw(self, context):
        layout = self.layout
        mytool = context.scene.my_tool

        layout.prop(mytool, "current_hierarchy_enum")

        current_hier = getattr(mytool, "current_hierarchy_enum")
        
        box = layout.box()
        if current_hier == "LOD_9":
            # draw_enum(box, 'render_tree')
            box.prop(mytool, 'render_tree_enum')
            o = layout.operator('wm.visualise_render_tree_operator')
            o.node_name = getattr(mytool, 'render_tree_enum')
            layout.operator('wm.apply_render_tree_changes_operator')
        elif current_hier == "LOD_10":
            # draw_enum(box, 'LOD')
            box.prop(mytool, 'LOD_enum')
            o = layout.operator('wm.visualise_lod_tree_operator')
            o.node_name = getattr(mytool, 'LOD_enum')
            layout.operator('wm.apply_lod_tree_changes_operator')
        elif current_hier == "LOD_21":
            # draw_enum(box, 'event')
            box.prop(mytool, 'event_enum')

class OBJECT_PT_b3d_func_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_func_panel"
    bl_label = "Additional options"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool


        # layout.prop(mytool, "mirror_type_enum")

        # layout.operator("wm.mirror_objects_operator")
        layout.operator("wm.apply_transforms_operator")
        layout.operator("wm.show_hide_collisions_operator")
        layout.operator("wm.show_hide_2d_collisions_operator")
        layout.operator("wm.show_hide_room_borders_operator")
        layout.operator("wm.show_hide_generator_operator")

        box = layout.box()
        box.operator("wm.show_lod_operator")
        box.operator("wm.hide_lod_operator")

        box = layout.box()
        box.prop(mytool, "condition_group")
        oper = box.operator("wm.show_conditional_operator")
        oper.group = getattr(mytool, 'condition_group')
        oper = box.operator("wm.hide_conditional_operator")
        oper.group = getattr(mytool, 'condition_group')

class OBJECT_PT_b3d_res_module_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_res_module_panel"
    bl_label = "RES resources"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "selected_res_module")

class OBJECT_PT_b3d_palette_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_palette_panel"
    bl_label = "Palette"
    bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        res_ind = get_current_res_index()
        if res_ind != -1:
            cur_res_module = mytool.res_modules[res_ind]

            box = self.layout.box()

            box.prop(cur_res_module, "palette_subpath", text="Subpath")
            box.prop(cur_res_module, "palette_name", text="Path")

            row_indexes = bpy.context.scene.palette_row_indexes
            col_indexes = bpy.context.scene.palette_col_indexes

            rows = 32
            cols = 8
            row1 = layout_split(box.row(), 0.15)
            # row.template_list("CUSTOM_UL_colors", "palette_list", cur_res_module, "palette_colors", scene, "palette_index", type='GRID', columns = 2, rows=rows)
            col1 = row1.column()
            col2 = row1.column()
            col2.template_list("CUSTOM_UL_colors_grid", "indexes_col", col_indexes, "prop_list", scene, "palette_row_index", type='GRID', columns = cols, rows=1)

            row2 = layout_split(box.row(), 0.15)
            col1 = row2.column()
            col1.template_list("CUSTOM_UL_colors_grid", "indexes_row", row_indexes, "prop_list", scene, "palette_col_index", type='GRID', columns = 1, rows=rows)
            col2 = row2.column()
            col2.template_list("CUSTOM_UL_colors", "palette_list", cur_res_module, "palette_colors", scene, "palette_index", type='GRID', columns = cols, rows=rows)

class OBJECT_PT_b3d_maskfiles_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_maskfiles_panel"
    bl_label = "MSK-files"
    bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        res_ind = get_current_res_index()
        if res_ind != -1:
            cur_res_module = mytool.res_modules[res_ind]

            box = self.layout.box()

            rows = 2
            row = box.row()
            row.template_list("CUSTOM_UL_maskfiles", "maskfiles_list", cur_res_module, "maskfiles", scene, "maskfiles_index", rows=rows)

            draw_list_controls(row, "custom.list_action_arrbname", "res_modules", res_ind, "maskfiles", "maskfiles_index")

            maskfiles_index = scene.maskfiles_index
            if len(cur_res_module.maskfiles):
                cur_maskfile = cur_res_module.maskfiles[maskfiles_index]

                box.prop(cur_maskfile, "subpath", text="Subpath")
                box.prop(cur_maskfile, "msk_name", text="Name")

                box.prop(cur_maskfile, "is_noload", text="Noload")

                split = layout_split(box, 0.3)
                split.prop(cur_maskfile, "is_someint", text="?Someint?")
                col = split.column()
                col.prop(cur_maskfile, "someint")

                col.enabled = cur_maskfile.is_someint

class OBJECT_PT_b3d_textures_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_textures_panel"
    bl_label = "Textures"
    bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        res_ind = get_current_res_index()
        if res_ind != -1:
            cur_res_module = mytool.res_modules[res_ind]

            box = self.layout.box()

            rows = 2
            row = box.row()
            row.template_list("CUSTOM_UL_textures", "textures_list", cur_res_module, "textures", scene, "textures_index", rows=rows)

            draw_list_controls(row, "custom.list_action_arrbname", "res_modules", res_ind, "textures", "textures_index")

            texture_index = scene.textures_index
            if (len(cur_res_module.textures)):
                cur_texture = cur_res_module.textures[texture_index]

                box.prop(cur_texture, "subpath", text="Subpath")
                box.prop(cur_texture, "tex_name", text="Name")

                box.prop(cur_texture, "img_type", text="Image type")
                box.prop(cur_texture, "has_mipmap", text="Has mipmap")
                box.prop(cur_texture, "img_format", text="Image format")

                box.prop(cur_texture, "is_memfix", text="Memfix")
                box.prop(cur_texture, "is_noload", text="Noload")
                box.prop(cur_texture, "is_bumpcoord", text="Bympcoord")

                split = layout_split(box, 0.3)
                split.prop(cur_texture, "is_someint", text="?Someint?")
                col = split.column()
                col.prop(cur_texture, "someint")

                col.enabled = cur_texture.is_someint

class OBJECT_PT_b3d_materials_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_materials_panel"
    bl_label = "Materials"
    bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        res_ind = get_current_res_index()
        if res_ind != -1:
            cur_res_module = mytool.res_modules[res_ind]


            # self.layout.template_ID(item, 'id_value')

            box = self.layout.box()

            rows = 2
            row = box.row()
            row.template_list("CUSTOM_UL_materials", "materials_list", cur_res_module, "materials", scene, "materials_index", rows=rows)

            draw_list_controls(row, "custom.list_action_arrbname", "res_modules", res_ind, "materials", "materials_index")

            texture_index = scene.materials_index
            if (len(cur_res_module.materials)):
                cur_material = cur_res_module.materials[texture_index]
                
                box.prop(cur_material, "mat_name", text="Name")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_reflect", text="Reflect")
                col = split.column()
                col.enabled = cur_material.is_reflect
                col.prop(cur_material, "reflect")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_specular", text="Specular")
                col = split.column()
                col.enabled = cur_material.is_specular
                col.prop(cur_material, "specular")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_transp", text="Transparency")
                col = split.column()
                col.enabled = cur_material.is_transp
                col.prop(cur_material, "transp")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_rot", text="Rotation")
                col = split.column()
                col.enabled = cur_material.is_rot
                col.prop(cur_material, "rot")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_col", text="Color")
                col = split.column()
                col.enabled = cur_material.is_col
                col.prop(cur_material, "col_switch")
                if cur_material.col_switch:
                    col.prop(cur_material, "id_col", text="Col num")
                else:
                    col.prop(cur_material, "col", text="Col num")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_tex", text="Texture TEX")
                col = split.column()
                col.enabled = cur_material.is_tex
                col.prop(cur_material, "tex_type")
                col.prop(cur_material, "tex_switch")
                if cur_material.tex_switch:
                    col.prop(cur_material, "id_tex", text="Tex num")
                else:
                    col.prop(cur_material, "tex", text="Tex num")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_att", text="Att")
                col = split.column()
                col.enabled = cur_material.is_att
                col.prop(cur_material, "att_switch")
                if cur_material.att_switch:
                    col.prop(cur_material, "id_att", text="Att num")
                else:
                    col.prop(cur_material, "att", text="Att num")

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_msk", text="Maskfile")
                col = split.column()
                col.enabled = cur_material.is_msk
                col.prop(cur_material, "msk_switch")
                if cur_material.msk_switch:
                    col.prop(cur_material, "id_msk", text="Msk num")
                else:
                    col.prop(cur_material, "msk", text="Msk num")


                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_power", text="Power")
                col = split.column()
                col.prop(cur_material, "power")
                col.enabled = cur_material.is_power

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_coord", text="Coord")
                col = split.column()
                col.prop(cur_material, "coord")
                col.enabled = cur_material.is_coord

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_envId", text="Env")
                col = split.column()
                col.prop(cur_material, "envId")
                col.enabled = cur_material.is_envId

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_env", text="Env")
                col = split.column()
                col.prop(cur_material, "env")
                col.enabled = cur_material.is_env

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_RotPoint", text="Rotation Center")
                col = split.column()
                col.prop(cur_material, "RotPoint")
                col.enabled = cur_material.is_RotPoint

                split = layout_split(box, 0.3)
                split.prop(cur_material, "is_move", text="Movement")
                col = split.column()
                col.prop(cur_material, "move")
                col.enabled = cur_material.is_move

                box.prop(cur_material, "is_noz", text="No Z")
                box.prop(cur_material, "is_nof", text="No F")
                box.prop(cur_material, "is_notile", text="No tiling")
                box.prop(cur_material, "is_notileu", text="No tiling U")
                box.prop(cur_material, "is_notilev", text="No tiling V")
                box.prop(cur_material, "is_alphamirr", text="Alphamirr")
                box.prop(cur_material, "is_bumpcoord", text="Bympcoord")
                box.prop(cur_material, "is_usecol", text="UseCol")
                box.prop(cur_material, "is_wave", text="Wave")

class OBJECT_PT_b3d_misc_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_b3d_misc_panel"
    bl_label = "About add-on"
    bl_space_type = "VIEW_3D"
    bl_region_type = get_ui_region()
    bl_category = "b3d Tools"
    #bl_context = "objectmode"

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        self.layout.label(text="Add-on author: aleko2144, LabVaKars")
        self.layout.label(text="vk.com/rnr_mods")

_classes = [
    # panels
    #Block info
    OBJECT_PT_b3d_info_panel,
    #Block add
    OBJECT_PT_b3d_add_panel,
    OBJECT_PT_b3d_single_add_panel,
    OBJECT_PT_b3d_cast_add_panel,
    OBJECT_PT_b3d_hier_add_panel,
    #Block edit
    OBJECT_PT_b3d_edit_panel,
    OBJECT_PT_b3d_pob_single_edit_panel,
    OBJECT_PT_b3d_pob_edit_panel,
    OBJECT_PT_b3d_pfb_edit_panel,
    OBJECT_PT_b3d_pvb_edit_panel,
    OBJECT_PT_b3d_hier_edit_panel,
    #RES resources
    OBJECT_PT_b3d_res_module_panel,
    OBJECT_PT_b3d_palette_panel,
    OBJECT_PT_b3d_maskfiles_panel,
    OBJECT_PT_b3d_textures_panel,
    OBJECT_PT_b3d_materials_panel,
    #Additional options
    OBJECT_PT_b3d_func_panel,
    #Misc
    OBJECT_PT_b3d_misc_panel
]

def register():
    for cls in _classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in _classes[::-1]:
        bpy.utils.unregister_class(cls)