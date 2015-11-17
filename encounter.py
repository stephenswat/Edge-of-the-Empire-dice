"""
This program aims to provide a simple and efficient way to run encounters in
the Edge of the Empire roleplaying game. Doing this from paper can be confusing
and even frustrating at times, because there is a lot to keep track of such as
distances, critical hits, temporary modifiers, initiative slots and more.

Star Wars: Edge of the Empire is a roleplaying game by Fantasy Flight Games.
Credits go to them for developing the dice system. Apart from that, I don't
know anything about copyrighting, so please FFG, don't sue me.
"""

__author__     = "Stephen Swatman"
__credits__    = ["Fantasy Flight Games"]
__license__    = "Unlicense"
__version__    = "0.0.1"
__email__      = "stephenswat@gmail.com"

import json
import dice

class Modifier(object):
    pass


class Weapon(object):
    pass


class Actor(object):
    def __init__(self, data, player=False):
        self.player = player

    def take_damage(self, damage):
        pass

    def move(self, target, distance):
        pass

    def attack(self, target):
        pass

    def kill(self):
        pass

    def save(self, file_name):
        pass

    def add_modifier(self, modifier):
        pass

    def roll_initiative(self):
        self.set_initiative(0, 0)

    def set_initiative(self, success, advantage):
        self.initiative = (success, advantage)


class Vehicle(Actor):
    pass


class Infantry(Actor):
    pass


class Encounter(object):
    def __init__(self):
        self.actors = []

    def add_actor(self, actor):
        if type(actor) == Actor:
            self.actors.append(actor)
        elif type(actor) == list:
            assert(all(type(x) == Actor for x in actor))
            self.actors += actor
        else:
            raise ValueError("add_actor takes either an Actor or a list.")


class EncounterInterface(object):
    def __init__(self, data, **kwargs):
        self.encounter = kwargs.get('encounter', Encounter(**kwargs))

        assert(type(data) == dict), "type of encounter data must be a dict."
        self.encounter.add_actor([Actor(x) for x in data['npcs']])
        self.encounter.add_actor([Actor([], player=True) for _ in range(int(data['players']))])

        self.determine_initiative()

    def determine_initiative(self):
        for actor in self.encounter.actors:
            if actor.player:
                actor.set_initiative(*self.query_initiative())
            else:
                actor.roll_initiative()

    @staticmethod
    def query_initiative():
        return (int(x) for x in raw_input("Enter initiative as <success>,<advantage>\n > ").split(','))


if __name__ == "__main__":
    with open('encounters/test.json') as f:
        e = EncounterInterface(json.load(f))

    for x in e.encounter.actors:
        print x
        print x.initiative
