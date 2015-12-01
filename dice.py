"""
Very simple Python script to roll special dice for the Star Wars: Edge of the
Empire game. Rolls a given dice pool and is capable of printing the results in
a human-readable fashion.

Star Wars: Edge of the Empire is a roleplaying game by Fantasy Flight Games.
Credits go to them for developing the dice system. Apart from that, I don't
know anything about copyrighting, so please FFG, don't sue me.
"""

__author__ = "Stephen Swatman"
__credits__ = ["Fantasy Flight Games"]
__license__ = "Unlicense"
__version__ = "0.0.1"
__email__ = "stephenswat@gmail.com"

import random
import sys
import dice_values
import re

class DicePool(object):
    """
    Class representing a pool of dice to be rolled by the script. Stores a dict
    representing the current roll. Has a roll() function which (re)rolls all
    dice in the pool and an internal function __add_results(results) which adds
    a set of results to the value of the current pool.
    """

    __value = {}

    def __init__(self, dice_pool):
        self.dice = re.findall(r"([A-Za-z])(\d+)?", dice_pool)

        for die in self.dice:
            if not die[0] in list(dice_values.DIE_OPTIONS.keys()) + ["D"]:
                raise ValueError("Invalid die type supplied. Valid dice are: "
                                 + ", ".join(list(dice_values.DIE_OPTIONS.keys()) + ["D"]))

    def __add_results(self, results):
        """
        Takes a set of results as a dictionary (or tuple for custom dice) and
        adds then to the current value of the dice pool.

        input: A dictionary of results.
        output: None, but __value is updated.
        """
        for res in results:
            if isinstance(res, dict):
                for key in res.keys():
                    if key in self.__value.keys():
                        self.__value[key] += res[key]
                    else:
                        self.__value['custom'].append((key, res[key]))
            else:
                raise ValueError("Illegal result type.")

    def reset_results(self):
        """
        Resets the value of __value to all zero.

        input: None.
        output: None, but resets __value.
        """

        self.__value = {
            "success":   0,
            "advantage": 0,
            "triumph":   0,
            "despair":   0,
            "dark":      0,
            "light":     0,
            "custom":    []
        }

    def roll(self):
        """
        Rolls all dice in this pool and adds the results to the value of the
        dice pool.

        input: None.
        output: None.
        """

        self.reset_results()

        for die in self.dice:
            results = Die(die).roll()
            self.__add_results(results)

    def get_values(self):
        """
        Returns a complete list of dice pool values, including failure and
        threat.

        input: None.
        output: The value of the dice pool after (re)rolling all dice.
        """
        values = self.__value.copy()

        values['failure'] = -values['success']
        values['threat'] = -values['advantage']

        return values

class Die(object):
    """
    Shortlived class that respresents a rollable die. Has a type of die which
    is represented as a tuple.
    """

    def __init__(self, die_type):
        self.die_type = die_type

    def roll(self):
        """
        Rolls this die and retuns the value of the roll as a tuple.

        input: None.
        output: The result of the roll as a dictionary.
        """
        if self.die_type[0] == "D":
            return ({self.die_type[0] + self.die_type[1]:
                     random.randint(1, int(self.die_type[1]))},)
        else:
            return random.choice(dice_values.DIE_OPTIONS[self.die_type[0]])

def roll_string(string):
    """
    Creates a dice pool from an input string, rolls it and returns the result.

    input: A string representing a dice pool.
    output: The result of the dice pool when rolled.
    """

    pool = DicePool(string)
    pool.roll()
    return pool.get_values()

def display_results(results):
    """
    Prints some human-readable information about the results of a dice roll,
    like if it succeeded, if it generated threat, advantage, triumph, despair,
    dark or light force points. Also prints the values of any custom dice.

    input: A dictionary of results.
    output: Some printed information about the roll.
    """

    if results['success'] < 1:
        print("The roll failed with {failure} failure.".format(**results))
    else:
        print("The roll succeeded with {success} success!".format(**results))

    if results['advantage'] > 0:
        print("The roll generated {advantage} advantage!".format(**results))
    elif results['advantage'] < 0:
        print("The roll generated {threat} threat!".format(**results))

    if results['despair'] > 0:
        print("The roll generated {despair} despair..".format(**results))
    if results['triumph'] > 0:
        print("The roll generated {triumph} triumph!".format(**results))

    if results['light'] > 0 or results['dark'] > 0:
        print("The roll generated {light} light and {dark} dark force points!"
              .format(**results))

    for custom_roll in results['custom']:
        print("Your %s-sided die rolled %d." % (custom_roll[0][1:],
                                                custom_roll[1]))


if __name__ == "__main__":
    if len(sys.argv) >= 2 and len(sys.argv[1]) > 0:
        display_results(roll_string(sys.argv[1]))
    else:
        print("Error: Please supply a dice pool as an argument")
