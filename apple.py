class Apple:
	price = 5
	apple_number = 0
	def __init__(self, color):
		Apple.apple_number += 1

		if Apple.apple_number == 3:
			self.__color = "purple"
		elif Apple.apple_number == 4:
			self.__color = "brown"
		elif Apple.apple_number % 12 == 0:
			self.__color = "brurple"
		else:
			self.__color = color
		self.__price = Apple.price 

	def __repr__(self):
		return "This is a {} cedi {} Apple".format(int(self.__price), self.__color)

	@classmethod
	def change_price(cls, price):
		cls.price = price

for _ in range(14):
	print(Apple("red"))

second = Apple("blue")
print(second)

Apple.change_price(6.0)

third = Apple("green")
print(third)
