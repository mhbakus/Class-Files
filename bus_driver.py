class Person:
	def __init__(self, is_alive = True):
		self.is_alive = is_alive

class Driver(Person):
	pass

class Children(Person):
	pass

class Bus:
	def __init__(self, passengers=[], is_on = False):
		self.__is_on = is_on
		self.__passengers = passengers


	def add_passenger(self, passenger):
		self.__passengers.append(passenger)
	
	def drive(self):
		driver = 0
		children = 0
		for passenger in self.__passengers:
			if isinstance(passenger, Driver):
				driver += 1
			elif isinstance(passenger, Children):
				children += 1
			else:
				pass

		if driver >= 1 and children >= 10 :
			self.__is_on = True
			print("you're driving the bus")
		else:
			self.__is_on = False
			print("you can't drive the bus")

	# def get_passenger(self):
	# 	for passenger in self.__passengers:
	# 		print(passenger)

mest_bus = Bus()

for _ in range(9):
	mest_bus.add_passenger(Children())

for _ in range(1):
	mest_bus.add_passenger(Driver())

# mest_bus.get_passenger()
mest_bus.drive()
# mest_bus.get_passenger()
mest_bus.drive()
# mest_bus.get_passenger()
mest_bus.drive()
