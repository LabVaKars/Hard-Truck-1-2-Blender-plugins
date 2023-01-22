

if "bpy" in locals():
    print("Reimporting modules!!!")
    import importlib
    importlib.reload(scripts)
else:
    import bpy
    from . import (
        scripts
    )

from ..common import (
	getRegion
)

from .. import consts

from .common import (
	isRootObj
)
from .scripts import (
	applyRemoveTransforms,
	applyTransforms,
	hideConditionals,
	showConditionals,
	hideLOD,
	showLOD,
	showConditionals,
	hideConditionals,
	showHideObjByType,
	showHideObjTreeByType,
	prop,
	drawCommon,
	drawAllFieldsByType,
	drawFieldByType,
	getAllObjsByType,
	setAllObjsByType,
	getPerFaceByType,
	setPerFaceByType,
	getPerVertexByType,
	setPerVertexByType,
	showSphere,

)


from .classes import (
	block_1,block_2,block_3,block_4,block_5,block_6,block_7,block_8,block_9,block_10,\
	block_11,block_12,block_13,block_14,block_15,block_16,block_17,block_18,block_20,\
	block_21,block_22,block_23,block_24,block_25,block_26,block_27,block_28,block_29,block_30,\
	block_31,block_33,block_34,block_35,block_36,block_37,block_39,block_40,block_common,\
	perFaceBlock_8, perFaceBlock_28, perFaceBlock_35, perVertBlock_8, perVertBlock_35
)
from .class_descr import (
	getClassDefByType,
	b_1,b_2,b_3,b_4,b_5,b_6,b_7,b_8,b_9,b_10,\
	b_11,b_12,b_13,b_14,b_15,b_16,b_17,b_18,b_20,\
	b_21,b_22,b_23,b_24,b_25,b_26,b_27,b_28,b_29,b_30,\
	b_31,b_33,b_34,b_35,b_36,b_37,b_39,b_40,b_common, \
	pfb_8, pfb_28, pfb_35, pvb_8, pvb_35,
	ResBlock
)


from bpy.props import (StringProperty,
						BoolProperty,
						IntProperty,
						FloatProperty,
						EnumProperty,
						PointerProperty,
						FloatVectorProperty,
						CollectionProperty
						)

from bpy.types import (Panel,
						Operator,
						PropertyGroup,
						)




# ------------------------------------------------------------------------
#	store properties in the active scene
# ------------------------------------------------------------------------

def resModuleCallback(scene, context):

	mytool = context.scene.my_tool
	resModules = mytool.resModules

	enumProperties = [(str(i), cn.value, "") for i, cn in enumerate(resModules)]

	return enumProperties



class PanelSettings(bpy.types.PropertyGroup):

	block1: PointerProperty(type=block_1)
	block2: PointerProperty(type=block_2)
	block3: PointerProperty(type=block_3)
	block4: PointerProperty(type=block_4)
	block5: PointerProperty(type=block_5)
	block6: PointerProperty(type=block_6)
	block7: PointerProperty(type=block_7)
	block8: PointerProperty(type=block_8)
	block9: PointerProperty(type=block_9)
	block10: PointerProperty(type=block_10)
	block11: PointerProperty(type=block_11)
	block12: PointerProperty(type=block_12)
	block13: PointerProperty(type=block_13)
	block14: PointerProperty(type=block_14)
	block15: PointerProperty(type=block_15)
	block16: PointerProperty(type=block_16)
	block17: PointerProperty(type=block_17)
	block18: PointerProperty(type=block_18)
	block20: PointerProperty(type=block_20)
	block21: PointerProperty(type=block_21)
	block22: PointerProperty(type=block_22)
	block23: PointerProperty(type=block_23)
	block24: PointerProperty(type=block_24)
	block25: PointerProperty(type=block_25)
	block26: PointerProperty(type=block_26)
	block27: PointerProperty(type=block_27)
	block28: PointerProperty(type=block_28)
	block29: PointerProperty(type=block_29)
	block30: PointerProperty(type=block_30)
	block31: PointerProperty(type=block_31)
	block33: PointerProperty(type=block_33)
	block34: PointerProperty(type=block_34)
	block35: PointerProperty(type=block_35)
	block36: PointerProperty(type=block_36)
	block37: PointerProperty(type=block_37)
	block39: PointerProperty(type=block_39)
	block40: PointerProperty(type=block_40)
	blockcommon: PointerProperty(type=block_common)

	perFaceBlock8: PointerProperty(type=perFaceBlock_8)
	perFaceBlock28: PointerProperty(type=perFaceBlock_28)
	perFaceBlock35: PointerProperty(type=perFaceBlock_35)
	perVertBlock8: PointerProperty(type=perVertBlock_8)
	perVertBlock35: PointerProperty(type=perVertBlock_35)

	resModules: CollectionProperty(type=ResBlock)

	selectedResModule: EnumProperty(
        name="RES модуль",
        description="Выбранный RES модуль",
        items=resModuleCallback
	)

	conditionGroup : bpy.props.IntProperty(
		name='Номер условия',
		description='Номер условия(группа обьекта), который надо скрыть/отобразить. Если -1, то берутся все доступные номера. При слишком большом числе берётся ближайшее подходящее.',
		default=-1,
		min=-1
	)

	coordinates : bpy.props.FloatVectorProperty(
		name='Координаты блока',
		description='',
		default=(0.0, 0.0, 0.0)
	)

	BlockName_string : bpy.props.StringProperty(
		name="Имя блока",
		default="",
		maxlen=30,
		)

	addBlockType_enum : bpy.props.EnumProperty(
		name="Тип блока",
		items= consts.blockTypeList
		)


	CollisionType_enum : bpy.props.EnumProperty(
		name="Тип коллизии",
		items=consts.collisionTypeList,
		)

	Radius : bpy.props.FloatProperty(
		name = "Радиус блока",
		description = "Дальность прорисовки блока",
		default = 1.0,
		)

	Radius1 : bpy.props.FloatProperty(
		name = "Радиус блока",
		description = "Дальность прорисовки блока",
		default = 1.0,
		)

	LOD_Distance : bpy.props.FloatProperty(
		name = "Дальность отображения LOD",
		description = "Маскимальная дальность отображения LOD",
		default = 10.0,
		)

	LOD_Distance1 : bpy.props.FloatProperty(
		name = "Дальность отображения LOD",
		description = "Маскимальная дальность отображения LOD",
		default = 10.0,
		)

	Intensity : bpy.props.FloatProperty(
		name = "Интенсивность освещения",
		description = "Яркость источника света",
		default = 1.0,
		min = 0.0,
		)

	Intensity1 : bpy.props.FloatProperty(
		name = "Интенсивность освещения",
		description = "Яркость источника света",
		default = 1.0,
		min = 0.0,
		)

	R : bpy.props.FloatProperty(
		name = "R",
		description = "",
		default = 255,
		min = 0.0,
		max = 255,
		)

	G : bpy.props.FloatProperty(
		name = "G",
		description = "",
		default = 255,
		min = 0.0,
		max = 255,
		)

	B : bpy.props.FloatProperty(
		name = "B",
		description = "",
		default = 255,
		min = 0.0,
		max = 255,
		)

	R1 : bpy.props.FloatProperty(
		name = "R",
		description = "",
		default = 255,
		min = 0.0,
		max = 255,
		)

	G1 : bpy.props.FloatProperty(
		name = "G",
		description = "",
		default = 255,
		min = 0.0,
		max = 255,
		)

	B1 : bpy.props.FloatProperty(
		name = "B",
		description = "",
		default = 255,
		min = 0.0,
		max = 255,
		)

	RadiusLight : bpy.props.FloatProperty(
		name = "Радиус освещения",
		description = "",
		default = 1,
		min = 0.0,
		)

	RadiusLight1 : bpy.props.FloatProperty(
		name = "Радиус освещения",
		description = "",
		default = 1,
		min = 0.0,
		)

	LType_enum : bpy.props.EnumProperty(
		name= "Тип источника света",
		items = consts.lTypeList,
		)

	SType_enum : bpy.props.EnumProperty(
		name= "Тип записи вершин",
		items = consts.sTypeList,
		)

	MType_enum : bpy.props.EnumProperty(
		name="Тип записи полигонов (35)",
		items=consts.mTypeList,
		)

	texNum_int : bpy.props.IntProperty(
		name = "Номер текстуры",
		description="Номер используемой текстуры.",
		)

	addBlockName_string : bpy.props.StringProperty(
		name="Присоединённый блок",
		description="Имя блока, который будет приписан к текущему блоку, например: hit_BmwM5 приписан к BmwM5 (05)",
		default="",
		maxlen=30,
		)

	addBlockName1_string : bpy.props.StringProperty(
		name="Присоединённый блок",
		description="Имя блока, который будет приписан к текущему блоку, например: hit_BmwM5 приписан к BmwM5 (05)",
		default="",
		maxlen=30,
		)

	addSpaceName_string : bpy.props.StringProperty(
		name="Используемый локатор",
		description="Имя блока, который будет использоваться в качестве локатора для привязанного блока, например: AirportSpace и Airport",
		default="",
		maxlen=30,
		)

	addSpaceName1_string : bpy.props.StringProperty(
		name="Используемый локатор",
		description="Имя блока, который будет использоваться в качестве локатора для привязанного блока, например: AirportSpace и Airport",
		default="",
		maxlen=30,
		)

	add24Flag_enum : bpy.props.EnumProperty(
		name="Флаг",
		items=[ ('0', "0", "Присоединённый объект не будет отображаться"),
				('1', "1", "Присоединённый объект будет отображаться"),
				]
		)

	add24Flag_enum1 : bpy.props.EnumProperty(
		name="Флаг",
		items=[ ('0', "0", "Присоединённый объект не будет отображаться"),
				('1', "1", "Присоединённый объект будет отображаться"),
				]
		)

	TGType_int : bpy.props.IntProperty(
		name = "Тип модели дерева",
		description="",
		)

	Scale : bpy.props.FloatProperty(
		name = "Масштаб генератора",
		description="",
		min=0.0,
		default=9.5,
		)

	generatorType_enum : bpy.props.EnumProperty(
		name="Тип генератора",
		items=consts.generatorTypeList,
		)

	groupsNum_int : bpy.props.IntProperty(
		name = "Кол-во групп",
		description="Кол-во переключаемых групп.",
		)

	groupsNum1_int : bpy.props.IntProperty(
		name = "Кол-во групп",
		description="Кол-во переключаемых групп.",
		)

	Refer_bool = bpy.props.BoolProperty(
		name="refer",
		description="",
		default = False
		)

	Type21_enum : bpy.props.EnumProperty(
		name="Имя 21 блока",
		items=consts.conditionBlockTypeList,
		)

	addGroupName_string : bpy.props.StringProperty(
		name="Имя группы",
		description="Имя переключаемой группы",
		default="",
		maxlen=30,
		)

	T14_enum : bpy.props.EnumProperty(
		name="Преднастройки",
		items=[ ('car', "Для транспорта", ""),
				('trl', "Для полуприцепа", ""),
				('trl_cyc', "Для полуприцепа-цистерны", ""),
				('clk', "Для коллизии", ""),
				]
		)

	T28_radius : bpy.props.FloatProperty(
		name = "Радиус спрайта",
		description = "Радиус плоскости спрайта",
		default = 1.0,
		min = 0.01,
		)

	T28_radius1 : bpy.props.FloatProperty(
		name = "Радиус спрайта",
		description = "Радиус плоскости спрайта",
		default = 1.0,
		min = 0.01,
		)

	CH : bpy.props.FloatProperty(
		name = "Высота коллизии",
		description = "Высота плоскости коллизии",
		)

	CH1 : bpy.props.FloatProperty(
		name = "Высота коллизии",
		description = "Высота плоскости коллизии",
		)

	RSound : bpy.props.FloatProperty(
		name = "Радиус звука",
		description = "Радиус звука",
		default = 10.0,
		min = 0.0,
		)

	RSound1 : bpy.props.FloatProperty(
		name = "Радиус звука",
		description = "Радиус звука",
		default = 10.0,
		min = 0.0,
		)

	addSoundName_string : bpy.props.StringProperty(
		name="Присоединённый звуковой файл",
		description="Имя звукового файла, который будет использоваться данным блоком",
		default="",
		maxlen=30,
		)

	addSoundName1_string : bpy.props.StringProperty(
		name="Присоединённый звуковой файл",
		description="Имя звукового файла, который будет использоваться данным блоком",
		default="",
		maxlen=30,
		)

	SLevel : bpy.props.FloatProperty(
		name = "Уровень громкости звука",
		description = "Уровень громкости звука",
		default = 1.0,
		min = 0.0,
		max = 1.0,
		)

	SLevel1 : bpy.props.FloatProperty(
		name = "Уровень громкости звука",
		description = "Уровень громкости звука",
		default = 1.0,
		min = 0.0,
		max = 1.0,
		)

	addRoomName_string : bpy.props.StringProperty(
		name="Присоединённая комната",
		description="Имя комнаты, которая будет загружена",
		default="",
		maxlen=30,
		)

	FType_enum : bpy.props.EnumProperty(
		name="Тип записи полигонов (08)",
		items=(('0', "Тип 0", "С нормалями"),
			   ('1', "Тип 1", "Без нормалей"),
			   ('2', "Тип 2", "С нормалями, UV разрывная"),
			   ('128', "Тип 128", ""),
			   ('144', "Тип 144", ""),
			   ),
		)

	Faces_enum : bpy.props.EnumProperty(
		name="Тип блока полигонов",
		items=(('8', "8", ""),
			   ('35', "35", ""),
			   ),
		)

	addBlockMeshType_enum : bpy.props.EnumProperty(
		name="Тип записи модели",
		items=[ ('auto', "Автоматический", "Экспортер сам определит, какой блок использовать (8, 35 или оба)"),
				('manual', "Ручной", "Будет записан блок, который выбран в настройках"),
			   ]
		)

	addMeshType_enum : bpy.props.EnumProperty(
		name="Тип записи полигонов",
		items=[ ('uv0', "Обычный", ""),
				('uv1', "С разрывной UV", ""),
			   ]
		)

	materialName_string : bpy.props.StringProperty(
		name="Имя материала",
		description="Имя материала, который будет использоваться генератором",
		default="",
		maxlen=10,
		)

	routeName_string : bpy.props.StringProperty(
		name="Имя участка карты",
		description="Имя участка карты, который будет загружен",
		default="",
		maxlen=2,
		)

	triggerType_enum : bpy.props.EnumProperty(
		name="Тип триггера",
		items=(('loader', "Загрузчик", "Загрузчик участков карты"),
			   ('radar0', "Радар 0", "Event 0"),
			   ('radar1', "Радар 1", "Event 1"),
			   ),
		)

	addBlockName4_string : bpy.props.StringProperty(
		name="Родительский блок",
		description="",
		default="",
		maxlen=30,
		)

	speed_limit : bpy.props.FloatProperty(
		name = "Ограничение скорости",
		description = "",
		default = 60.0,
		min = 0.0,
		)

	addBlocks_enum : bpy.props.EnumProperty(
		name="Тип сборки",
		items=[ ('room', "Комната", "Комната с коллизией"),
				#('07', "07", "Меш (ДБ1)"),
				#('10', "10", "LOD"),
				#('12', "12", "Плоскость коллизии"),
				#('14', "14", "Блок, связанный с автомобилями"),
				#('18', "18", "Связка локатора и 3D-модели, например: FiatWheel0Space и Single0Wheel14"),
				#('19', "19", "Контейнер, в отличие от блока типа 05, не имеет возможности привязки"),
				#('20', "20", "Плоская коллизия"),
				#('21', "21", "Контейнер с обработкой событий"),
				#('23', "23", "Объёмная коллизия"),
				#('24', "24", "Локатор"),
				#('28', "28", "3D-спрайт"),
				#('33', "33", "Источник света"),
				#('37', "37", "Меш"),
				#('40', "40", "Генератор объектов"),
			   ]
		)

	addRoomNameIndex_string : bpy.props.StringProperty(
		name="Имя комнаты",
		description="",
		default="aa_000",
		maxlen=30,
		)

	mirrorType_enum : bpy.props.EnumProperty(
		name="Тип блока",
		items=[ ('x', "x", ""),
				('y', "y", ""),
				('z', "z", ""),
			   ]
		)

# ------------------------------------------------------------------------
#	menus
# ------------------------------------------------------------------------

# class BasicMenu(bpy.types.Menu):
# 	bl_idname = "OBJECT_MT_select_test"
# 	bl_label = "Select"

# 	def draw(self, context):
# 		layout = self.layout

# 		# built-in example operators
# 		layout.operator("object.select_all", text="Select/Deselect All").action = 'TOGGLE'
# 		layout.operator("object.select_all", text="Inverse").action = 'INVERT'
# 		layout.operator("object.select_random", text="Random")

# ------------------------------------------------------------------------
#	operators / buttons
# ------------------------------------------------------------------------

class AddOperator(bpy.types.Operator):
	bl_idname = "wm.add_operator"
	bl_label = "Добавить блок на сцену"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		global block_type

		block_type = int(mytool.addBlockType_enum)

		global cursor_pos
		cursor_pos = bpy.context.scene.cursor_location

		object_name = mytool.BlockName_string

		if block_type == 6566754:
			object_name = "b3d"
			object = bpy.data.objects.new(object_name, None)
			object.location=(0.0,0.0,0.0)
			bpy.context.scene.objects.link(object)

		elif block_type == 0:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			bpy.context.scene.objects.link(object)

		elif block_type == 1:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_1)
			bpy.context.scene.objects.link(object)

		elif block_type == 2:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_2)
			bpy.context.scene.objects.link(object)

		elif block_type == 3:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_3)
			bpy.context.scene.objects.link(object)

		elif block_type == 4:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos #(0.0,0.0,0.0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_4)
			bpy.context.scene.objects.link(object)

		elif block_type == 5:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos #(0.0,0.0,0.0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_5)
			bpy.context.scene.objects.link(object)

		elif block_type == 6:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos #(0.0,0.0,0.0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_6)
			bpy.context.scene.objects.link(object)

		elif block_type == 7:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos #(0.0,0.0,0.0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_7)
			bpy.context.scene.objects.link(object)

		elif block_type == 8:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos #(0.0,0.0,0.0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_8)
			bpy.context.scene.objects.link(object)

		elif block_type == 9:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos #(0.0,0.0,0.0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_9)
			bpy.context.scene.objects.link(object)

		elif block_type == 10:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_10)
			bpy.context.scene.objects.link(object)

		elif block_type == 11:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_11)
			bpy.context.scene.objects.link(object)

		elif block_type == 12:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_12)
			bpy.context.scene.objects.link(object)

		elif block_type == 13:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_13)
			bpy.context.scene.objects.link(object)

		elif block_type == 14:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_14)

		elif block_type == 15:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_15)
			bpy.context.scene.objects.link(object)

		elif block_type == 16:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_16)
			bpy.context.scene.objects.link(object)

		elif block_type == 17:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_17)
			bpy.context.scene.objects.link(object)

		elif block_type == 18:
			object = bpy.data.objects.new(object_name, None)
			object['block_type'] = block_type
			object.location=cursor_pos
			setAllObjsByType(context, object, b_18)
			bpy.context.scene.objects.link(object)

		elif block_type == 19:
			object = bpy.data.objects.new(object_name, None)
			object['block_type'] = block_type
			object.location=cursor_pos
			bpy.context.scene.objects.link(object)

		elif block_type == 20:
			points = [(0,0,0), (0,1,0)]
			curveData = bpy.data.curves.new('curve', type='CURVE')

			curveData.dimensions = '3D'
			curveData.resolution_u = 2

			polyline = curveData.splines.new('POLY')
			polyline.points.add(len(points)-1)
			for i, coord in enumerate(points):
				x,y,z = coord
				polyline.points[i].co = (x, y, z, 1)

			curveData.bevel_depth = 0.01
			object = bpy.data.objects.new(object_name, curveData)
			object.location = (0,0,0)
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_20)
			context.scene.objects.link(object)

		elif block_type == 21:
			object['block_type'] = block_type
			object.location=cursor_pos
			setAllObjsByType(context, object, b_20)
			bpy.context.scene.objects.link(object)

		elif block_type == 22:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_22)
			bpy.context.scene.objects.link(object)

		elif block_type == 23:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_23)
			bpy.context.scene.objects.link(object)

		elif block_type == 24:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_24)
			bpy.context.scene.objects.link(object)

		elif block_type == 25:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_25)
			bpy.context.scene.objects.link(object)

		elif block_type == 26:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_26)
			bpy.context.scene.objects.link(object)

		elif block_type == 27:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_27)
			bpy.context.scene.objects.link(object)

		elif block_type == 28:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_28)
			bpy.context.scene.objects.link(object)

		elif block_type == 29:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_29)
			bpy.context.scene.objects.link(object)

		elif block_type == 30:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_30)
			bpy.context.scene.objects.link(object)

		elif block_type == 31:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_31)
			bpy.context.scene.objects.link(object)


		elif block_type == 33:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			setAllObjsByType(context, object, b_33)
			bpy.context.scene.objects.link(object)

		elif block_type == 34:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_34)
			bpy.context.scene.objects.link(object)

		elif block_type == 35:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_35)
			bpy.context.scene.objects.link(object)

		elif block_type == 36:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_36)
			bpy.context.scene.objects.link(object)

		elif block_type == 37:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_37)
			bpy.context.scene.objects.link(object)

		elif block_type == 39:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_39)
			bpy.context.scene.objects.link(object)

		elif block_type == 40:
			object = bpy.data.objects.new(object_name, None)
			object.location=cursor_pos
			object['block_type'] = block_type
			setAllObjsByType(context, object, b_40)
			bpy.context.scene.objects.link(object)
		return {'FINISHED'}

class GetVertexValuesOperator(bpy.types.Operator):
	bl_idname = "wm.get_vertex_values_operator"
	bl_label = "Получить настройки блока"

	def execute(self, context):
		object = bpy.context.selected_objects[0]
		block_type = object['block_type']

		if block_type == 8:
			getPerVertexByType(context, object, pvb_8)
		elif block_type == 35:
			getPerVertexByType(context, object, pvb_35)

		return {'FINISHED'}

class GetFaceValuesOperator(bpy.types.Operator):
	bl_idname = "wm.get_face_values_operator"
	bl_label = "Получить настройки блока"

	def execute(self, context):
		object = bpy.context.selected_objects[0]
		block_type = object['block_type']

		if block_type == 8:
			getPerFaceByType(context, object, pfb_8)
		elif block_type == 28:
			getPerFaceByType(context, object, pfb_28)
		elif block_type == 35:
			getPerFaceByType(context, object, pfb_35)

		return {'FINISHED'}

class GetValuesOperator(bpy.types.Operator):
	bl_idname = "wm.get_block_values_operator"
	bl_label = "Получить настройки блока"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		global block_type
		global lenStr
		object = bpy.context.object
		block_type = object['block_type']

		zclass = getClassDefByType(block_type)

		if zclass is not None:
			getAllObjsByType(context, object, zclass)

		return {'FINISHED'}

class SetFaceValuesOperator(bpy.types.Operator):
	bl_idname = "wm.set_face_values_operator"
	bl_label = "Сохранить настройки блока"

	def execute(self, context):
		curtype = bpy.context.object['block_type']
		objects = [cn for cn in bpy.context.selected_objects if cn['block_type'] is not None and cn['block_type'] == curtype]

		for i in range(len(objects)):

			object = objects[i]
			block_type = object['block_type']

			if block_type == 8:
				setPerFaceByType(context, object, pfb_8)
			elif block_type == 28:
				setPerFaceByType(context, object, pfb_28)
			elif block_type == 35:
				setPerFaceByType(context, object, pfb_35)

		return {'FINISHED'}

class SetVertexValuesOperator(bpy.types.Operator):
	bl_idname = "wm.set_vertex_values_operator"
	bl_label = "Сохранить настройки блока"

	def execute(self, context):
		curtype = bpy.context.object['block_type']
		objects = [cn for cn in bpy.context.selected_objects if cn['block_type'] is not None and cn['block_type'] == curtype]

		for i in range(len(objects)):

			object = objects[i]
			block_type = object['block_type']

			if block_type == 8:
				setPerVertexByType(context, object, pvb_8)
			elif block_type == 35:
				setPerVertexByType(context, object, pvb_35)

		return {'FINISHED'}

class SetValuesOperator(bpy.types.Operator):
	bl_idname = "wm.set_block_values_operator"
	bl_label = "Сохранить настройки блока"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		global block_type
		global lenStr
		#object = bpy.context.selected_objects[0]

		active_obj = bpy.context.object

		curtype = active_obj['block_type']

		objects = [cn for cn in bpy.context.selected_objects if cn['block_type'] is not None and cn['block_type'] == curtype]

		for i in range(len(objects)):

			object = objects[i]

			if 'block_type' in object:
				block_type = object['block_type']
			else:
				block_type = 0

			object['block_type'] = block_type

			zclass = getClassDefByType(block_type)

			if zclass is not None:
				setAllObjsByType(context, object, zclass)

		return {'FINISHED'}

class DelValuesOperator(bpy.types.Operator):
	bl_idname = "wm.del_block_values_operator"
	bl_label = "Удалить настройки блока"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		global block_type
		global lenStr
		#object = bpy.context.selected_objects[0]

		for i in range(len(bpy.context.selected_objects)):

			object = bpy.context.selected_objects[i]

			if 'block_type' in object:
				del object['block_type']

		return {'FINISHED'}

class FixUVOperator(bpy.types.Operator):
	bl_idname = "wm.fix_uv_operator"
	bl_label = "Исправить UV для экспорта"

	def execute(self, context):

		for i in range(len(bpy.context.selected_objects)):

			object = bpy.context.selected_objects[i]

			bpy.ops.object.mode_set(mode = 'EDIT')

			context = bpy.context
			obj = context.edit_object
			me = obj.data
			bm = bmesh.from_edit_mesh(me)
			# old seams
			old_seams = [e for e in bm.edges if e.seam]
			# unmark
			for e in old_seams:
				e.seam = False
			# mark seams from uv islands
			bpy.ops.uv.seams_from_islands()
			seams = [e for e in bm.edges if e.seam]
			# split on seams
			print(seams)
			print("salo 111")
			bmesh.ops.split_edges(bm, edges=seams)
			# re instate old seams.. could clear new seams.
			for e in old_seams:
				e.seam = True
			bmesh.update_edit_mesh(me)

			boundary_seams = [e for e in bm.edges if e.seam and e.is_boundary]

			bpy.ops.object.mode_set(mode = 'OBJECT')

		return {'FINISHED'}

class FixVertsOperator(bpy.types.Operator):
	bl_idname = "wm.fix_verts_operator"
	bl_label = "Исправить меш для экспорта"

	def execute(self, context):

		for i in range(len(bpy.context.selected_objects)):

			object = bpy.context.selected_objects[i]

			bpy.ops.object.mode_set(mode = 'EDIT')
			bpy.ops.mesh.select_mode(type="FACE")
			bpy.ops.mesh.select_all(action='DESELECT')
			bpy.ops.mesh.select_all(action='INVERT')
			bpy.ops.mesh.select_mode(type="VERT")
			bpy.ops.mesh.select_all(action='INVERT')
			bpy.ops.mesh.delete(type='VERT')

			bpy.ops.object.mode_set(mode = 'OBJECT')

		return {'FINISHED'}

class MirrorAndFlipObjectsOperator(bpy.types.Operator):
	bl_idname = "wm.mirror_objects_operator"
	bl_label = "Отзеркалить объекты"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		x = False
		y = False
		z = False

		if (mytool.mirrorType_enum) == "x":
			x = True
		else:
			x = False

		if (mytool.mirrorType_enum) == "y":
			y = True
		else:
			y = False

		if (mytool.mirrorType_enum) == "z":
			z = True
		else:
			z = False

		for object in context.selected_objects:
			if object.type == 'MESH':
				#object = bpy.context.selected_objects[i]
				bpy.ops.transform.mirror(constraint_axis=(x, y, z), constraint_orientation='GLOBAL')
				bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

				#if object.type == 'MESH':
				bpy.ops.object.mode_set(mode = 'EDIT')
				bpy.ops.mesh.select_mode(type="FACE")
				bpy.ops.mesh.select_all(action='DESELECT')
				bpy.ops.mesh.select_all(action='INVERT')
				bpy.ops.mesh.flip_normals()
				bpy.ops.mesh.select_all(action='DESELECT')
				bpy.ops.object.mode_set(mode = 'OBJECT')




		#bpy.ops.object.mode_set(mode = 'OBJECT')

		return {'FINISHED'}

class ApplyTransformsOperator(bpy.types.Operator):
	bl_idname = "wm.apply_transforms_operator"
	bl_label = "Расположить/Убрать обьекты"
	bl_description = "Создаёт копии обьектов и располагает по местам(блок 24) указанным в блоке 18"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		applyRemoveTransforms(self)

		return {'FINISHED'}

class ShowHideCollisionsOperator(bpy.types.Operator):
	bl_idname = "wm.show_hide_collisions_operator"
	bl_label = "Отобразить/Скрыть коллизии"
	bl_description = "Если скрыты все коллизии(23), показывает их. Иначе - скрывает."

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		showHideObjByType(self, 23)

		return {'FINISHED'}

class ShowHideRoomBordersOperator(bpy.types.Operator):
	bl_idname = "wm.show_hide_room_borders_operator"
	bl_label = "Отобразить/Скрыть границы комнат"
	bl_description = "Если скрыты все границы комнат(30), показывает их. Иначе - скрывает."

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		showHideObjByType(self, 30)

		return {'FINISHED'}

class ShowHideGeneratorsOperator(bpy.types.Operator):
	bl_idname = "wm.show_hide_generator_operator"
	bl_label = "Отобразить/Скрыть генераторы обьектов"
	bl_description = "Если скрыты все генераторы обьектов(40), показывает их. Иначе - скрывает."

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		showHideObjByType(self, 40)

		return {'FINISHED'}

class ShowLODOperator(bpy.types.Operator):
	bl_idname = "wm.show_lod_operator"
	bl_label = "Отобразить LOD модели"
	bl_description = "Показывает LOD(10) выделенного обьекта. " + \
					"Если нет активного обьекта показывает LOD у всех обьектов сцены"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		objs = context.selected_objects
		if not len(objs):
			objs = [cn for cn in bpy.data.objects if isRootObj(cn)]

		for obj in objs:
			showLOD(obj)
		self.report({'INFO'}, "{} LOD objects(block 10) are shown".format(len(objs)))

		return {'FINISHED'}

class HideLODOperator(bpy.types.Operator):
	bl_idname = "wm.hide_lod_operator"
	bl_label = "Скрыть LOD модели"
	bl_description = "Скрывает LOD(10) выделенного обьекта. " + \
					"Если нет активного обьекта скрывает LOD у всех обьектов сцены"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		objs = context.selected_objects
		if not len(objs):
			objs = [cn for cn in bpy.data.objects if isRootObj(cn)]

		for obj in objs:
			hideLOD(obj)
		self.report({'INFO'}, "{} LOD objects(block 10) are hidden".format(len(objs)))

		return {'FINISHED'}

class ShowConditionalsOperator(bpy.types.Operator):
	bl_idname = "wm.show_conditional_operator"
	bl_label = "Отобразить обьекты с условием"
	bl_description = "Показывает выбранное условие блока 21 выделенного обьекта. " + \
					"Если нет активного обьекта показывает выбранное условие блока 21 у всех обьектов сцены"

	group : bpy.props.IntProperty()

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		objs = context.selected_objects
		if not len(objs):
			objs = [cn for cn in bpy.data.objects if isRootObj(cn)]

		for obj in objs:
			showConditionals(obj, self.group)
		self.report({'INFO'}, "{} Conditional objects(block 21) are shown".format(len(objs)))


		return {'FINISHED'}

class HideConditionalsOperator(bpy.types.Operator):
	bl_idname = "wm.hide_conditional_operator"
	bl_label = "Скрыть обьекты с условием"
	bl_description = "Скрывает выбранное условие блока 21 выделенного обьекта. " + \
					"Если нет активного обьекта скрывает выбранное условие блока 21 у всех обьектов сцены"

	group : bpy.props.IntProperty()

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		objs = context.selected_objects
		if not len(objs):
			objs = [cn for cn in bpy.data.objects if isRootObj(cn)]

		for obj in objs:
			hideConditionals(obj, self.group)
		self.report({'INFO'}, "{} Conditional objects(block 21) are hidden".format(len(objs)))

		return {'FINISHED'}

class AddBlocksOperator(bpy.types.Operator):
	bl_idname = "wm.add1_operator"
	bl_label = "Добавить сборку блоков на сцену"

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		global type

		type = mytool.addBlocks_enum

		global cursor_pos
		cursor_pos = bpy.context.scene.cursor_location

		def type05(name, radius, add_name):
			object_name = name
			object = bpy.data.objects.new(object_name, None)
			object['block_type'] = 5
			object.location=cursor_pos
			object['node_radius'] = radius
			object['add_name'] = add_name
			bpy.context.scene.objects.link(object)
			object.select = True

		def type19(name):
			object_name = name
			object = bpy.data.objects.new(object_name, None)
			object['block_type'] = 19
			object.location=cursor_pos
			bpy.context.scene.objects.link(object)
			object.select = True

		if type == "room":
			type19("room_" + mytool.addRoomNameIndex_string)
			room = bpy.context.selected_objects[0]

			type05(("road_" + mytool.addRoomNameIndex_string), mytool.Radius, ("hit_road_" + mytool.addRoomNameIndex_string))
			road = bpy.context.selected_objects[0]

			type05(("obj_" + mytool.addRoomNameIndex_string), mytool.Radius, ("hit_obj_" + mytool.addRoomNameIndex_string))
			obj = bpy.context.selected_objects[0]

			hit_road = type05(("hit_road_" + mytool.addRoomNameIndex_string), 0, "")
			hit_obj = type05(("hit_obj_" + mytool.addRoomNameIndex_string), 0, "")

			bpy.ops.object.select_all(action='DESELECT')

			room.select = True
			road.select = True
			obj.select = True

			bpy.context.scene.objects.active = room

			bpy.ops.object.parent_set()

			bpy.ops.object.select_all(action='DESELECT')

		return {'FINISHED'}

class ShowSphereOperator(bpy.types.Operator):
	bl_idname = "b3d.show_sphere_operator"
	bl_label = "Показать/Скрыть сферу"
	bl_description = "Показывает/скрывает сферу"

	pname: bpy.props.StringProperty()

	def execute(self, context):
		scene = context.scene
		mytool = scene.my_tool

		obj = context.object

		showSphere(context, obj, self.pname)

		self.report({'INFO'}, "Sphere shown")

		return {'FINISHED'}


# ------------------------------------------------------------------------
# panels
# ------------------------------------------------------------------------

class OBJECT_PT_b3d_add_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_add_panel"
	bl_label = "Добавление блоков"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool
		# print(type(mytool))
		# print(bpy.types.Scene.my_tool)
		# print(dir(bpy.types.Scene.my_tool))
		# print(dir(context.scene.my_tool))
		global block_type
		block_type = int(mytool.addBlockType_enum)

		self.layout.label(text="Тип блока:")
		layout.prop(mytool, "addBlockType_enum", text="")
		layout.prop(mytool, "BlockName_string")

		zclass = getClassDefByType(block_type)

		if zclass is not None:
			drawAllFieldsByType(self, context, zclass)

		layout.operator("wm.add_operator")

class OBJECT_PT_b3d_pfb_edit_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_pfb_edit_panel"
	bl_label = "Параметры полигона"
	bl_parent_id = "OBJECT_PT_b3d_edit_panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		mytool = context.scene.my_tool

		object = bpy.context.object

		if object is not None:

			if 'block_type' in object:
				block_type = object['block_type']
			else:
				block_type = None

			if block_type == 8:
				drawAllFieldsByType(self, context, pfb_8)
			if block_type == 28:
				drawAllFieldsByType(self, context, pfb_28)
			if block_type == 35:
				drawAllFieldsByType(self, context, pfb_35)


		layout.operator("wm.get_face_values_operator")
		layout.operator("wm.set_face_values_operator")

class OBJECT_PT_b3d_pvb_edit_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_pvb_edit_panel"
	bl_label = "Параметры вершины"
	bl_parent_id = "OBJECT_PT_b3d_edit_panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		mytool = context.scene.my_tool

		object = bpy.context.object

		if object is not None:

			if 'block_type' in object:
				block_type = object['block_type']
			else:
				block_type = None

			if block_type == 8:
				drawAllFieldsByType(self, context, pvb_8)
			if block_type == 35:
				drawAllFieldsByType(self, context, pvb_35)


		layout.operator("wm.get_vertex_values_operator")
		layout.operator("wm.set_vertex_values_operator")

class OBJECT_PT_b3d_edit_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_edit_panel"
	bl_label = "Редактирование блоков"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		mytool = context.scene.my_tool

		object = bpy.context.object
		if object is not None:
			drawCommon(self, object)

class OBJECT_PT_b3d_pob_edit_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_pob_edit_panel"
	bl_label = "Параметры обьекта"
	bl_parent_id = "OBJECT_PT_b3d_edit_panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		mytool = context.scene.my_tool

		type(context)
		#for i in range(len(bpy.context.selected_objects)):

		object = bpy.context.object

		# if len(bpy.context.selected_objects):
		# 	for i in range(1):
		if object is not None:

			level_group = None

			if 'block_type' in object:
				block_type = object['block_type']
			else:
				block_type = None

			if 'level_group' in object:
				level_group = object['level_group']
			else:
				level_group = None

			lenStr = str(len(object.children))

			zclass = getClassDefByType(block_type)

			layout.operator("wm.get_block_values_operator")
			layout.operator("wm.set_block_values_operator")

			if zclass is not None:
				drawAllFieldsByType(self, context, zclass)

			# else:
			# 	self.layout.label(text="Выбранный объект не имеет типа.")
			# 	self.layout.label(text="Чтобы указать его, нажмите на кнопку сохранения настроек.")

			layout.operator("wm.del_block_values_operator")
			layout.operator("wm.fix_uv_operator")
			layout.operator("wm.fix_verts_operator")

class OBJECT_PT_b3d_blocks_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_blocks_panel"
	bl_label = "Сборки блоков"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		mytool = context.scene.my_tool

		type = mytool.addBlocks_enum

		layout.prop(mytool, "addBlocks_enum")

		if type == "room":
			layout.prop(mytool, "addRoomNameIndex_string")
			layout.prop(mytool, "Radius")

		layout.operator("wm.add1_operator")

class OBJECT_PT_b3d_func_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_func_panel"
	bl_label = "Дополнительные функции"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool


		layout.prop(mytool, "mirrorType_enum")

		layout.operator("wm.mirror_objects_operator")
		layout.operator("wm.apply_transforms_operator")
		layout.operator("wm.show_hide_collisions_operator")
		layout.operator("wm.show_hide_room_borders_operator")
		layout.operator("wm.show_hide_generator_operator")

		box = layout.box()
		box.operator("wm.show_lod_operator")
		box.operator("wm.hide_lod_operator")

		box = layout.box()
		box.prop(mytool, "conditionGroup")
		oper = box.operator("wm.show_conditional_operator")
		oper.group = getattr(mytool, 'conditionGroup')
		oper = box.operator("wm.hide_conditional_operator")
		oper.group = getattr(mytool, 'conditionGroup')

class OBJECT_PT_b3d_res_module_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_res_module_panel"
	bl_label = "Игровые ресурсы"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool

		layout.prop(mytool, "selectedResModule")

class OBJECT_PT_b3d_maskfiles_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_maskfiles_panel"
	bl_label = "MSK-файлы"
	bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool

		currentRes = int(mytool.selectedResModule)
		curResModule = mytool.resModules[currentRes]

		box = self.layout.box()

		rows = 2
		row = box.row()
		row.template_list("CUSTOM_UL_items", "maskfiles_list", curResModule, "maskfiles", scene, "maskfiles_index", rows=rows)

		col = row.column(align=True)

		props = col.operator("custom.list_action_arrbname", icon='ADD', text="")
		props.action = 'ADD'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "maskfiles"
		props.customindex = "maskfiles_index"

		props = col.operator("custom.list_action_arrbname", icon='REMOVE', text="")
		props.action = 'REMOVE'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "maskfiles"
		props.customindex = "maskfiles_index"

		col.separator()

		props = col.operator("custom.list_action_arrbname", icon='TRIA_UP', text="")
		props.action = 'UP'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "maskfiles"
		props.customindex = "maskfiles_index"

		props = col.operator("custom.list_action_arrbname", icon='TRIA_DOWN', text="")
		props.action = 'DOWN'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "maskfiles"
		props.customindex = "maskfiles_index"

		#Maskfile edit
		box = self.layout.box()

		maskfiles_index = scene.maskfiles_index
		if len(curResModule.maskfiles):
			curMaskfile = curResModule.maskfiles[maskfiles_index]

			box.prop(curMaskfile, "is_noload", text="Noload")

			split = box.split(factor=0.3)
			split.prop(curMaskfile, "is_someint", text="?Someint?")
			col = split.column()
			col.prop(curMaskfile, "someint")

			col.enabled = curMaskfile.is_someint

class OBJECT_PT_b3d_textures_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_textures_panel"
	bl_label = "Текстуры"
	bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool

		currentRes = int(mytool.selectedResModule)
		curResModule = mytool.resModules[currentRes]

		box = self.layout.box()

		rows = 2
		row = box.row()
		row.template_list("CUSTOM_UL_items", "textures_list", curResModule, "textures", scene, "textures_index", rows=rows)

		col = row.column(align=True)

		props = col.operator("custom.list_action_arrbname", icon='ADD', text="")
		props.action = 'ADD'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "textures"
		props.customindex = "textures_index"

		props = col.operator("custom.list_action_arrbname", icon='REMOVE', text="")
		props.action = 'REMOVE'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "textures"
		props.customindex = "textures_index"

		col.separator()

		props = col.operator("custom.list_action_arrbname", icon='TRIA_UP', text="")
		props.action = 'UP'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "textures"
		props.customindex = "textures_index"

		props = col.operator("custom.list_action_arrbname", icon='TRIA_DOWN', text="")
		props.action = 'DOWN'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "textures"
		props.customindex = "textures_index"

		#Texture edit
		box = self.layout.box()

		textureIndex = scene.textures_index
		if (len(curResModule.textures)):
			curTexture = curResModule.textures[textureIndex]

			box.prop(curTexture, "is_memfix", text="Memfix")
			box.prop(curTexture, "is_noload", text="Noload")
			box.prop(curTexture, "is_bumpcoord", text="Bympcoord")

			split = box.split(factor=0.3)
			split.prop(curTexture, "is_someint", text="?Someint?")
			col = split.column()
			col.prop(curTexture, "someint")

			col.enabled = curTexture.is_someint

class OBJECT_PT_b3d_materials_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_materials_panel"
	bl_label = "Материалы"
	bl_parent_id = "OBJECT_PT_b3d_res_module_panel"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool

		currentRes = int(mytool.selectedResModule)
		curResModule = mytool.resModules[currentRes]

		box = self.layout.box()

		rows = 2
		row = box.row()
		row.template_list("CUSTOM_UL_items", "materials_list", curResModule, "materials", scene, "materials_index", rows=rows)

		col = row.column(align=True)

		props = col.operator("custom.list_action_arrbname", icon='ADD', text="")
		props.action = 'ADD'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "materials"
		props.customindex = "materials_index"

		props = col.operator("custom.list_action_arrbname", icon='REMOVE', text="")
		props.action = 'REMOVE'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "materials"
		props.customindex = "materials_index"

		col.separator()

		props = col.operator("custom.list_action_arrbname", icon='TRIA_UP', text="")
		props.action = 'UP'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "materials"
		props.customindex = "materials_index"

		props = col.operator("custom.list_action_arrbname", icon='TRIA_DOWN', text="")
		props.action = 'DOWN'
		props.bname = "resModules"
		props.bindex = currentRes
		props.pname = "materials"
		props.customindex = "materials_index"

		#Material edit
		box = self.layout.box()

		textureIndex = scene.materials_index
		if (len(curResModule.materials)):
			curMaterial = curResModule.materials[textureIndex]

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_reflect", text="Reflect")
			col = split.column()
			col.prop(curMaterial, "reflect")
			col.enabled = curMaterial.is_reflect

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_specular", text="Specular")
			col = split.column()
			col.prop(curMaterial, "specular")
			col.enabled = curMaterial.is_specular

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_transp", text="Transparency")
			col = split.column()
			col.prop(curMaterial, "transp")
			col.enabled = curMaterial.is_transp

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_rot", text="Rotation")
			col = split.column()
			col.prop(curMaterial, "rot")
			col.enabled = curMaterial.is_rot

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_col", text="Color")
			col = split.column()
			col.prop(curMaterial, "col")
			col.enabled = curMaterial.is_col

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_tex", text="Texture TEX")
			col = split.column()
			col.prop(curMaterial, "tex")
			col.enabled = curMaterial.is_tex

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_ttx", text="Texture TTX")
			col = split.column()
			col.prop(curMaterial, "ttx")
			col.enabled = curMaterial.is_ttx

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_itx", text="Texture ITX")
			col = split.column()
			col.prop(curMaterial, "itx")
			col.enabled = curMaterial.is_itx

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_att", text="Att")
			col = split.column()
			col.prop(curMaterial, "att")
			col.enabled = curMaterial.is_att

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_msk", text="Maskfile")
			col = split.column()
			col.prop(curMaterial, "msk")
			col.enabled = curMaterial.is_msk

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_power", text="Power")
			col = split.column()
			col.prop(curMaterial, "power")
			col.enabled = curMaterial.is_power

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_coord", text="Coord")
			col = split.column()
			col.prop(curMaterial, "coord")
			col.enabled = curMaterial.is_coord

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_env", text="Env")
			col = split.column()
			col.prop(curMaterial, "envId")
			col.prop(curMaterial, "env")
			col.enabled = curMaterial.is_env

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_rotPoint", text="Rotation Center")
			col = split.column()
			col.prop(curMaterial, "rotPoint")
			col.enabled = curMaterial.is_rotPoint

			split = box.split(factor=0.3)
			split.prop(curMaterial, "is_move", text="Movement")
			col = split.column()
			col.prop(curMaterial, "move")
			col.enabled = curMaterial.is_move

			box.prop(curMaterial, "is_noz", text="No Z")
			box.prop(curMaterial, "is_nof", text="No F")
			box.prop(curMaterial, "is_notile", text="No tiling")
			box.prop(curMaterial, "is_notileu", text="No tiling U")
			box.prop(curMaterial, "is_notilev", text="No tiling V")
			box.prop(curMaterial, "is_alphamirr", text="Alphamirr")
			box.prop(curMaterial, "is_bumpcoord", text="Bympcoord")
			box.prop(curMaterial, "is_usecol", text="UseCol")
			box.prop(curMaterial, "is_wave", text="Wave")

class OBJECT_PT_b3d_misc_panel(bpy.types.Panel):
	bl_idname = "OBJECT_PT_b3d_misc_panel"
	bl_label = "О плагине"
	bl_space_type = "VIEW_3D"
	bl_region_type = getRegion()
	bl_category = "b3d Tools"
	#bl_context = "objectmode"

	@classmethod
	def poll(self,context):
		return context.object is not None

	def draw(self, context):
		layout = self.layout
		scene = context.scene
		mytool = scene.my_tool

		self.layout.label(text="Автор плагина: aleko2144")
		self.layout.label(text="vk.com/rnr_mods")
# ------------------------------------------------------------------------
# register and unregister
# ------------------------------------------------------------------------

_classes = (
	PanelSettings,
	AddOperator,
	# getters
	GetValuesOperator,
	GetFaceValuesOperator,
	GetVertexValuesOperator,
	# setters
	SetValuesOperator,
	SetFaceValuesOperator,
	SetVertexValuesOperator,
	DelValuesOperator,
	FixUVOperator,
	FixVertsOperator,
	MirrorAndFlipObjectsOperator,
	ApplyTransformsOperator,
	ShowHideCollisionsOperator,
	ShowHideRoomBordersOperator,
	ShowLODOperator,
	HideLODOperator,
	ShowHideGeneratorsOperator,
	ShowConditionalsOperator,
	HideConditionalsOperator,
	AddBlocksOperator,
	ShowSphereOperator,

	OBJECT_PT_b3d_add_panel,
	OBJECT_PT_b3d_edit_panel,
	OBJECT_PT_b3d_pob_edit_panel,
	OBJECT_PT_b3d_pfb_edit_panel,
	OBJECT_PT_b3d_pvb_edit_panel,
	OBJECT_PT_b3d_res_module_panel,
	OBJECT_PT_b3d_maskfiles_panel,
	OBJECT_PT_b3d_textures_panel,
	OBJECT_PT_b3d_materials_panel,
	OBJECT_PT_b3d_blocks_panel,
	OBJECT_PT_b3d_func_panel,
	OBJECT_PT_b3d_misc_panel,
)

def register():
	for cls in _classes:
		bpy.utils.register_class(cls)
	bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=PanelSettings)

def unregister():
	del bpy.types.Scene.my_tool
	for cls in _classes[::-1]:
		bpy.utils.unregister_class(cls)

