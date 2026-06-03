from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

window.borderless = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# Block types
block_textures = {
    1: 'grass.png',
    2: 'stone.png',
    3: 'brick.png'
}
current_block = 1

# Sky
Sky()

# Ground generation
for z in range(20):
    for x in range(20):
        voxel = Button(
            parent=scene,
            model='cube',
            origin_y=0.5,
            texture=block_textures[1],
            color=color.white,
            position=(x, 0, z),
            collider='box'
        )

# Player
player = FirstPersonController()
player.gravity = 0.5
player.jump_height = 1.2
player.cursor.visible = False  # Hide pink diamond

# Sounds
punch_sound = Audio('assets/punch.wav', autoplay=False)
place_sound = Audio('assets/place.wav', autoplay=False)

# 🎯 Ultra-micro white crosshair (lines touching center, razor-thin)
crosshair_thickness = 0.00015   # extremely thin
crosshair_length = 0.00075      # extremely short

Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=(crosshair_thickness, crosshair_length),
    position=(0, crosshair_length / 2)
)
Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=(crosshair_thickness, crosshair_length),
    position=(0, -crosshair_length / 2)
)
Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=(crosshair_length, crosshair_thickness),
    position=(-crosshair_length / 2, 0)
)
Entity(
    parent=camera.ui,
    model='quad',
    color=color.white,
    scale=(crosshair_length, crosshair_thickness),
    position=(crosshair_length / 2, 0)
)

# Input handling
def input(key):
    global current_block

    if key == 'left mouse down':
        hit_info = mouse.hovered_entity
        if hit_info and hit_info != player:
            destroy(hit_info)
            punch_sound.play()

    if key == 'right mouse down' and mouse.hovered_entity:
        hit_pos = mouse.hovered_entity.position + mouse.normal
        block = Button(
            parent=scene,
            model='cube',
            origin_y=0.5,
            texture=block_textures[current_block],
            color=color.white,
            position=hit_pos,
            collider='box'
        )
        place_sound.play()

    if key in ['1', '2', '3']:
        current_block = int(key)
        print(f"Selected block: {current_block} ({block_textures[current_block]})")

app.run()
 