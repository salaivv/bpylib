import bpy

class Cursor:
    def __init__(self):
        self._context = bpy.context
        self._data = bpy.data
        self._ops = bpy.ops
    
    @property
    def object(self):
        return Object(self._context.object)
    
    @property
    def objects(self):
        for obj in self._data.objects:
            yield Object(obj)

    @property
    def objects_selected(self):
        for obj in self._data.objects:
            if obj.select_get():
                yield Object(obj)

    @property
    def objects_mesh(self):
        for obj in self._data.objects:
            if obj.type == 'MESH':
                yield Object(obj)


class Object:
    def __init__(self, obj):
        self._object = obj
    
    @property
    def materials(self):
        return self._object.data.materials
    
    def __repr__(self):
        return repr(self._object)