Edge of the Empire dice roller
==============================

A Python utility used for rolling special dice used in the Star Wars: Edge of the Empire roleplaying game (and variants). Also has support for arbitrarily sided dice.

Credits go out to https://github.com/DoWhileGeek for inspiring me to create this.

Usage
-----

This dice roller can either be used as a stand-alone dice rolling application invoked from a command line interface, or it can be imported and used from a different program.

To roll dice from the command line, invoke the Python as follows:

	python dice.py [pool]

Here, pool is a string representing the dice you want to roll. Each letter represents one die, as follows:

	a = Ability die
	b = Boost die
	c = Challenge die
	d = Difficulty die
	p = Proficiency die
	s = Setback die
	f = Force die
	D = Standard die

As well, when rolling, you can select a difficulty level (a predetermined number of difficulty dice) as well as upgrading X number difficulty dice to Challenge dice (or adding additional difficulty dice, should there not be enough)

	Simple = -
    Easy = d
    Average = dd
    Hard = ddd
    Daunting = dddd
    Formidable = ddddd

To roll a standard n-sided die, use D followed by a number, like D20 to roll a 20-sided die.

Finally, to roll 2 ability dice, 1 boost die, and a D12 at Easy difficulty upgraded twice, you could use either of the following:

	python dice.py aabdcD12
	python dice.py aabD12 easy 2

Which might output the following:

	The roll succeeded with 1 success!
	The roll generated 1 threat.
	Your 12-sided die rolled 3.