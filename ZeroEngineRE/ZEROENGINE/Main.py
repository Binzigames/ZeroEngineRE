#-------------> importing
#befor using zeroehine, be sure that you have installed :
#raylib
#colorama
import pyray as pr
import colorama as c
import sys
import os

# -----------------> bools
#W -WindowProperties
Wx , Wy = 900 , 900
Wname = "ZEROENGINE"
# G - Game Properties
Gfps = 30

#D - debug
Dcorelog = f" {c.Fore.RED}[CORE] / {c.Fore.WHITE}"
# -----------------> class
#Gameobjects used to simplify management of project
#Types used to draw and optimase of project:
#empty = nothing
#scriptible = updated empty + any function
# text = draws simple ui text

#there is a few functions for that one :
#draw (symply draws object that was created)
#destroy (deletes this object from game loop)

class GameObject:
    def __init__(self, type="empty", X=0, Y=0, property=None, additionalColor=pr.WHITE):
        self.activated = True
        self.type = type
        self.property = property
        self.x, self.y = X, Y
        self.color = additionalColor
        self._handle = None

    def draw(self):
        if not self.activated:
            return

        if self.type == "text":
            if isinstance(self.property, str):
                pr.draw_text(self.property, self.x, self.y, 20, self.color)

        elif self.type == "scriptable":
            if callable(self.property):
                self.property(self)

        elif self.type == "empty":
            pass

    def destroy(self):
        self.activated = False
        if self._handle and self in self._handle.objects:
            self._handle.objects.remove(self)

#simpled game setuper
#start_game (used to start game , create a base window)
#add_object (adds a object to scene)
#game_loop (Handle a game loop)
#shutdown  (game exit)

class GameHandle:
    def __init__(self):
        self.Wx, self.Wy = Wx, Wy
        self.Wname = Wname
        self.objects = []

    def clear_console(self):
        os.system("cls" if os.name == "nt" else "clear")

    def debug_log(self , type , text= None):
        if type == None:
            pass
        if type == "core":
            print(Dcorelog + text)
        elif type == "separate":
            print(c.Fore.RED +"================" + c.Fore.WHITE)
        elif type == "logo":
            print(c.Fore.RED + "ZERO ENGINE REUNION")
            print(c.Fore.WHITE + "developed by our comunity!")
            print("{0}link : https://github.com/Binzigames/ZeroEngineRE".format(c.Fore.WHITE))





    def start_game(self):
        pr.init_window(self.Wx, self.Wy, self.Wname)
        pr.set_target_fps(Gfps)
        self.clear_console()
        self.debug_log("logo")
        self.debug_log("separate")
        self.debug_log("core" , "pyray init : success")

    def add_object(self, obj):
        obj._handle = self
        self.objects.append(obj)

    def game_loop(self):
        while not pr.window_should_close():
            pr.begin_drawing()
            pr.clear_background(pr.BLACK)

            for obj in list(self.objects):
                obj.draw()

            pr.end_drawing()

        self.shutdown()

    def shutdown(self):
        pr.close_window()
        self.clear_console()
        print(c.Fore.RED + "ZERO ENGINE IS CLOSING WINDOW" + c.Fore.WHITE)
        sys.exit(0)



