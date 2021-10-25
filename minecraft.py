# it have a new update is void update (minecraft v1.0.1)
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

def update():
    if player.y <= -100:
        player.position = (0, 50, 0)

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0.2,0,random.uniform(0.9,1)),
            highlight_color = color.lime)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=(self.position + mouse.normal))
            if key == 'right mouse down':
                destroy(self)

app = Ursina()

window.fps_counter.enabled = False
window.exit_button.visible = False

for y in range(1):
    for z in range(36):
        for x in range(36):
            voxel = Voxel(position=(x-18,y,z-18))

player = FirstPersonController()

app.run()
