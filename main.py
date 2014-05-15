import random
import sys
import dice
import re

class DicePool(object):
	__value = {
		"success":   0,
		"advantage": 0,
		"triumph":   0,
		"despair":   0,
		"dark":      0,
		"light":     0,
		"custom":    []
	}

	def __init__(self, dicePoolString):
		self.dice = re.findall("([A-Za-z])(\d+)?", dicePoolString)

		for die in self.dice:
			if not (die[0] in dice.dieOptions.keys() + ["D"]):
				raise ValueError("Invalid die type supplied. Valid dice are: " 
					+ ", ".join(dice.dieOptions.keys() + ["D"]))

	def __addResults(self, results):
		for result in results:
			if isinstance(result, dict):
				for key in result.keys():
					self.__value[key] += result[key]
			elif isinstance(result, tuple):
				self.__value['custom'].append(result)
			else:
				raise ValueError("Illegal result type.")

	def roll(self):
		for die in self.dice:
			results = Die(die).roll()
			self.__addResults(results)

		return self.__value

class Die(object):
	def __init__(self, dieType):
		self.dieType = dieType

	def roll(self):
		if self.dieType[0] == "D":
			return ((self.dieType[0] + self.dieType[1], 
				random.choice(range(int(self.dieType[1])))),)
		else:
			return random.choice(dice.dieOptions[self.dieType[0]])

def rollString(string):
	pool = DicePool(string)
	return pool.roll()

def displayResults(results):
	print ("The roll failed with %d failure." % abs(results['success']) 
		if results['success'] <= 0 
		else "The roll succeeded with %d success!" % results['success'])

	print ("The roll gained neither threat nor advantage." 
		if results['advantage'] == 0 
		else (("The roll generated %d threat." % abs(results['advantage'])) 
			if (results['advantage'] <= 0) 
			else ("The roll generated %d advantage!" % results['advantage'])))

	if results['despair'] > 0:
		print "The roll generated %d despair.." % results['despair']
	if results['triumph'] > 0:
		print "The roll generated %d triumph!" % results['triumph']

	if results['light'] > 0 or results['dark'] > 0:
		print ("The roll generated %d light and %d dark force points!" 
			% (results['light'], results['dark']))

	for customRoll in results['custom']:
		print "Your %s-sided die rolled %d." % (customRoll[0][1:], 
			customRoll[1])


if __name__ == "__main__":
	if len(sys.argv) >= 2 and len(sys.argv[1]) > 0:
		try:
			result = rollString(sys.argv[1])
			displayResults(result)
		except Exception as e:
			print("Error: " + str(e))
	else:
		print("Error: Please supply a dice pool as an argument")
