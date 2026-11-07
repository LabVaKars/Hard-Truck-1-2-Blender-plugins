import bpy
import os
import struct

from ..compatibility import (
    get_context_collection_objects
)

def import_raw(file, context, op, filepath):

    basename1 = os.path.basename(filepath)[:-4]
    basename2 = basename1+"_2"
    basename1 = basename1+"_1"

    vertexes = []
    faces1 = []
    faces2 = []

    counter = 0

    width = 257

    for i in range(width):
        for j in range(width):
            vertexes.append((i*10,j*10,struct.unpack('<B',file.read(1))[0]))
            file.read(1)

    for i in range(width-1):
        for j in range(i,width-1):
            counter = i*width+j
            if i == j:
                faces1.append((counter, counter+1, counter+width+1))
            else:
                faces1.append((counter, counter+1, counter+width+1, counter+width))

    for i in range(width-1):
        for j in range(i,width-1):
            counter = j*width+i
            if i == j:
                faces2.append((counter, counter+width, counter+width+1))
            else:
                faces2.append((counter, counter+1, counter+width+1, counter+width))


    b3d_mesh1 = bpy.data.meshes.new(basename1)
    b3d_mesh2 = bpy.data.meshes.new(basename2)

    b3d_mesh1.from_pydata(vertexes,[],faces1)
    b3d_mesh2.from_pydata(vertexes,[],faces2)

    b3d_obj1 = bpy.data.objects.new(basename1, b3d_mesh1)
    get_context_collection_objects(context).link(b3d_obj1)

    b3d_obj2 = bpy.data.objects.new(basename2, b3d_mesh2)
    get_context_collection_objects(context).link(b3d_obj2)
