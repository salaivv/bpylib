# bpylib – An intuitive API for Blender

The idea is to create an API that is intuitive to use. By intuitive, I mean, anyone who has an understanding of Blender should be able to write scripts easily to automate or build their own tools. 

Often times, when you try the Blender API for the first time, you will realize there is a lot of conventions that you need to know to use it properly. And, the conventions are very different or not straightforward compared to how you use Blender through the GUI.

```python
from bpylib import EditMode
from bpylib import Bool

# Create an Edit Mode context to perform mesh operations
with EditMode(mesh_object) as obj:
    obj.select_all()
    obj.face_mode_set()
    obj.merge_by_distance(0.01)
    obj.deselect_all()

# Create a Bool context to do boolean operations
with Bool(mesh_obj) as obj:
    obj += data.objects['Cube']
```

Also, just like how I select an object, go to the material tab, click on a material and edit material properties, I need to be able to do the same using the API. 

Something like:

```python
import bpylib

obj = bpylib.objects['Cube']

# Change Base Color of a material
# (assuming there's a Principled BSDF and only one)
obj.materials['Wood'].base_color = (0.1, 0.2, 0.2, 0)

# Local transforms
obj.translate_local(0, 0, -1)  # Move 1 unit back in local Z axis
obj.rotate_local(0, 0, 90)  # Rotate 90 degrees in local Z axis

context = bpylib.context
context.objects_mesh  # Get all mesh objects
context.objects_curve
context.selected
```

Node tree operations:

```python
# Connect two nodes
node_image_tex.Image >> node_principled.basecolor  # connect sockets
node_image_tex.Image | node_principled.basecolor  # cut sockets

# Alternative interface
node_image_tex.Image.connect(node_principled.basecolor)
node_image_tex.Image.cut(node_principled.basecolor)
```