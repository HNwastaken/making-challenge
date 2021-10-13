#this trust testing not work like minecraft yet but i will try to upgrade it but renimber to install ursina when run
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.white,
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
    for z in range(35):
        for x in range(35):
            voxel = Voxel(position=(x,y,z))

player = FirstPersonController()

app.run()
