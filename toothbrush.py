import time
class ToothBrush:

	def __init__(self, color, toothpaste=None):
		self.color = color

	def add_toothpaste(self, toothpaste):
		self.toothpaste = toothpaste

	def brush(self, teeth, seconds):
		time.sleep(seconds)
		print("finished brushing " + teeth)

class ElectricBrush(ToothBrush):
	"""docstring for ElectricBrush"""
	def __init__(self, color):
		super().__init__(self, color)
		self.__is_on = False

	def turn_on(self):
		self.__is_on = True

	def turn_off(self):
		self.__is_on = False

	def brush(self, teeth, time):
		if not self.__is_on:
			raise MemoryError("Forgot to turn ToothBrush on")
		super().brush(teeth, time)

	def add_toothpaste(self, toothpaste):
		if self.__is_on:
			raise MemoryError("you have to turn off the ToothBrush before to add toothpaste")
		super().add_toothpaste(toothpaste)




yellow_electric = ElectricBrush('yellow')

eyram_brush = ElectricBrush('purple')
eyram_brush.add_toothpaste('signal')
eyram_brush.turn_on()
eyram_brush.brush('eyram teeth', 7)
		