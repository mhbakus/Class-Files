import random

class StringHelper:

	@staticmethod
	def randomCase(string):
		tempstr = ""
		for char in string:
			tempstr += char.upper() if random.randint(0, 1) else char.lower()

		return tempstr

	@staticmethod
	def abbreviate(string, num):
		tempstr = ""
		if num >= len(string):
			return string
		else:
			for i in range(num):
				tempstr += string[i]
		tempstr += "..."

		return tempstr


text = "Hello this is a test"
print(StringHelper.randomCase(text))


print(StringHelper.abbreviate("hello my name is", 5))
print(StringHelper.abbreviate("Eyram", 5))
print(StringHelper.abbreviate("I am late for class because i hate programming", 9))