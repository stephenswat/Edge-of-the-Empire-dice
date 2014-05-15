Edge of the Empire dice roller
==============================

A Python utility used for rolling special dice used in the Star Wars: Edge of the Empire roleplaying game (and variants). Also has support for arbitrarily sided dice.

Credits go out to https://github.com/DoWhileGeek for inspiring me to create this.

Usage
-----

This dice roller can either be used as a stand-alone dice rolling application invoked from a command line interface, or it can be imported and used from a different program.

To roll dice from the command line, invoke the Python as follows:

	python main.py [pool]

Here, pool is a string representing the dice you want to roll. Each letter represents one die, as follows:

	a = Ability die
	b = Boost die
	c = Challenge die
	d = Difficulty die
	p = Proficiency die
	s = Setback die
	f = Force die
	D = Standard die

To roll a standard n-sided die, use D followed by a number, like D20 to roll a 20-sided die.

Finally, to roll 2 ability dice, 1 boost die, 1 difficulty die, 1 challenge die and a D12, use the following:

	python main.py aabdcD12

Which might output the following:

	The roll succeeded with 1 success!
	The roll generated 1 threat.
	Your 12-sided die rolled 3.