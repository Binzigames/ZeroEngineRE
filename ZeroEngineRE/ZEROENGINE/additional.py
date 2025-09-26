#-------------> importing
from Main import *
#-------------> additional stuff

#small scene manager
class SceneManager:
    def __init__(self):
        self.current_scene = None
        self.scenes = {}

    def add_scene(self, name, scene):
        self.scenes[name] = scene
        if self.current_scene is None:
            self.current_scene = name

    def switch_to(self, name):
        if name in self.scenes:
            self.current_scene = name
        else:
            print(f"{c.Fore.RED}[SceneManager] Does not '{name}' exist!")

    def update(self):
        if self.current_scene is not None:
            self.scenes[self.current_scene].update()

    def draw(self):
        if self.current_scene is not None:
            self.scenes[self.current_scene].draw()


#-------------> scene template
class Scene:
    def __init__(self, update_fn=None, draw_fn=None):
        """
        update_fn - logic
        draw_fn   - draw
        """
        self.update_fn = update_fn if update_fn is not None else lambda: None
        self.draw_fn = draw_fn if draw_fn is not None else lambda: None

    def update(self):
        self.update_fn()

    def draw(self):
        self.draw_fn()
