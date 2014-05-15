"""
This file stores all possible rolls on all dice, for easy reference in main.py.
"""

SUCCESS = {
    "success": 1
}

ADVANTAGE = {
    "advantage": 1
}

TRIUMPH = {
    "success": 1,
    "triumph": 1
}

FAILURE = {
    "success": -1
}

THREAT = {
    "advantage": -1
}

DESPAIR = {
    "success": -1,
    "despair": 1
}

DARK = {
    "dark": 1
}

LIGHT = {
    "light": 1
}

BLANK = {
}

DIE_OPTIONS = {
    "b": (
        (BLANK,),
        (BLANK,),
        (SUCCESS,),
        (ADVANTAGE,),
        (ADVANTAGE, ADVANTAGE,),
        (ADVANTAGE, SUCCESS,)
    ),
    "a": (
        (BLANK,),
        (ADVANTAGE, ADVANTAGE,),
        (SUCCESS,),
        (ADVANTAGE,),
        (SUCCESS, SUCCESS,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE,),
        (SUCCESS,)
    ),
    "p": (
        (BLANK,),
        (SUCCESS,),
        (SUCCESS,),
        (SUCCESS, SUCCESS,),
        (SUCCESS, SUCCESS,),
        (ADVANTAGE,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE, SUCCESS,),
        (ADVANTAGE, ADVANTAGE,),
        (ADVANTAGE, ADVANTAGE,),
        (TRIUMPH,)
    ),
    "s": (
        (BLANK,),
        (BLANK,),
        (FAILURE,),
        (FAILURE,),
        (THREAT,),
        (THREAT,)
    ),
    "d": (
        (BLANK,),
        (THREAT,),
        (THREAT, THREAT,),
        (THREAT,),
        (THREAT,),
        (THREAT,),
        (THREAT, THREAT,),
        (FAILURE, THREAT,)
    ),
    "c": (
        (BLANK,),
        (FAILURE,),
        (FAILURE,),
        (FAILURE, FAILURE,),
        (FAILURE, FAILURE,),
        (THREAT,),
        (THREAT,),
        (FAILURE, THREAT,),
        (FAILURE, THREAT,),
        (THREAT, THREAT,),
        (THREAT, THREAT,),
        (DESPAIR,)
    ),
    "f": (
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK,),
        (DARK, DARK,),
        (LIGHT,),
        (LIGHT,),
        (LIGHT, LIGHT,),
        (LIGHT, LIGHT,),
        (LIGHT, LIGHT,))
}