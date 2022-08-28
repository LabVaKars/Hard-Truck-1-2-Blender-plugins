# Blender-VWI
Плагины для форматов файлов игрового движка Virtual World Inventor.
##### Текущие планы
* Доработка экспорта b3d.

## Поддерживаемые игры
| Название игры | Название игры (международное) | Год выхода |
|-----------|-----------------------|:----------:|
| Дальнобойщики: Путь к победе | Hard Truck: Road to Victory | 1998 |
| Дальнобойщики - 2 | Hard Truck 2 (King of the Road) | 2000 (2003)

## Поддерживаемые форматы файлов
| Расширение | Описание           | Импорт | Экспорт |
|-----------|-----------------------|:----------:|:----------:|
| .b3d + .res  | Модели, логика, различные объекты   | Да   | Нет  |
| .way  | Пути транспорта для ИИ   | Да   | Нет  |
| .tch/.tech  | Параметры транспорта и динамических объектов   |      | Да  |

## Файлы в проекте

#### Папка **src/2.79**

Плагины для версии 2.79.

#### Папка **src/2.80**

Плагины для версии 2.80+.
#### Папка **scenes**

Готовые сцены для экспорта в игру: **ht2-way.blend** - пути транспорта, **ht2-vehicle-export.blend** - транспорт, **ht2-env-module.blend** - карта

## Как установить плагины
1. Распаковать архив.
2. Поместить содержимое в папку Blender/2.79/scripts/addons/.
3. Открыть настройки в Blender (нажать LCtrl + Alt + U ), перейти во вкладку Addons.
4. Найти аддоны (b3d) и активировать их (галка на названии).

## Авторы
Юрий Гладышенко и Андрей Прожога.
Обновление: Иван Карцев


## Ссылки
[Сообщество VK](https://vk.com/rnr_mods)

***

# About

Hard Truck classic games (VWI engine) import/export plugins for Blender.

#### Roadmap
* Export support

## Supported games and formats

1. Hard Truck: Road to Victory (1998)

| Расширение | Описание           | Import |
|-----------|-----------------------|:----------:|
| .b3d  | Models, game logic, various objects    | Yes  |

2. Hard Truck: King Of The Road (2003)

| Расширение | Описание           | Import | Export |
|-----------|-----------------------|:----------:|:----------:|
| .b3d  | Models, game logic, various objects   | Yes   | No  |
| .way  | AI paths   | Yes  | No  |
| .tch/.tech  | Transport parameters |      | Yes |