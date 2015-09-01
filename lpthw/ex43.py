# File Imports

from sys import exit
from random import randint

class Scene(object):
    """docstring for Scene"""

    def enter(self):
        print "This class does nothing because it is not yet configured."
        print "It can however be configured from the Sub-Classes."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        pass

class Death(Scene):
    """DocString for Death"""

    def __init__(self, name):
        super(Death, self).__init__()
        self.name = name

    def enter(self):
        pass

class CentralCorridor(Scene):
    """DocString for CentralCorridor"""

    def __init__(self, name):
        super(CentralCorridor, self).__init__()
        self.name = name

    def enter(self):
        pass

class LaserWeaponArmory(Scene):
    """DocString for LaserWeaponArmory"""

    def __init__(self, Arg(s)):
        super(LaserWeaponArmory, self).__init__()
        self.Arg(s) = Arg(s)

class TheBridge(Scene):
    """DocString for TheBridge"""

    def __init__(self, name):
        super(TheBridge, self).__init__()
        self.name = name

class EscapePod(Scene):
    """DocString for EscapePod"""

    def __init__(self, name):
        super(EscapePod, self).__init__()
        self.name = name

class Map(object):
    """docstring for Map"""
    def __init__(self, start_scene):
        super(Map, self).__init__()
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
