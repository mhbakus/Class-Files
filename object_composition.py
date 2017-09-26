class Egg:
	def __init__(self, color, is_broken = False):
		self.color = color
		self.is_broken = is_broken

	def drop(self):
		self.is_broken = True


class EggCarton:
	def __init__(self):
		self.eggs = list()

	def add_egg(self, egg):
		self.eggs.append(egg)

	def drop_egg(self):
		last_egg = self.eggs.pop()
		last_egg.drop()
		return last_egg

mycarton = EggCarton()

for _ in range(3):
	mycarton.add_egg(Egg('blue'))

for _ in range(4):
	mycarton.add_egg(Egg('yellow'))

print(mycarton.drop_egg().color)

