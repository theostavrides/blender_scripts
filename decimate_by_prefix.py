import bpy

#CHANGE THESE INPUTS
PREFIX = "PREFIX"
VERTEX_THRESHHOLD = 10
DECIMATE_ITERATIONS = 1
DECIMATE_TYPE = 'UNSUBDIV'


#SCRIPT
objs = [obj for obj in bpy.context.scene.objects if obj.name.startswith(PREFIX)]

bpy.ops.object.select_all(action='DESELECT')
for obj in objs:
    verts = len(obj.data.vertices)
    if (verts > VERTEX_THRESHHOLD):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[obj.name].select_set(True)
        bpy.context.view_layer.objects.active = obj
        
        bpy.ops.object.modifier_add(type='DECIMATE')
        bpy.context.object.modifiers["Decimate"].decimate_type = DECIMATE_TYPE
        bpy.context.object.modifiers["Decimate"].iterations = DECIMATE_ITERATIONS
        bpy.ops.object.modifier_apply(modifier="Decimate")
