import os
import bpy
import math
import datetime

# TODO: `bpy.context.active_object` vs `bpy.context.object` vs `bpy.context.scene.objects.active`?

today = datetime.date.today()
texts = [
    today.strftime('%b %d'),
    today.strftime('%Y'),
    today.strftime('%A')
]

for line in range(0, 3):
    for index, letter in enumerate(texts[line]):
        if letter == ' ':
            continue

        # Add the card plane
        bpy.ops.mesh.primitive_plane_add(
            location=(.125 + line * .0075, -.4 + index * .15, 0.505 + line * -.2))
        bpy.context.active_object.rotation_euler = (
            math.radians(0), math.radians(87), math.radians(0))
        bpy.context.active_object.scale = (.1, .07, 1)
        # TODO: Associate the correct material as per `light-box.blend`
        # `bpy.context.active_object.data.materials.append(TODO)`

        # Add the card text
        bpy.ops.object.text_add(
            location=(.13 + line * .0075, -.47 + index * .15, .44 + line * -.2))
        bpy.context.active_object.rotation_euler = (
            math.radians(87), math.radians(0), math.radians(90))
        bpy.context.active_object.scale = (.2, .2, .2)

        black = bpy.data.materials.new("Black")
        black.diffuse_color = (0, 0, 0, 0)  # RGB?
        bpy.context.active_object.data.materials.append(black)
        bpy.context.active_object.data.body = letter
