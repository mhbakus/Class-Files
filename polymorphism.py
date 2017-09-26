class Person:
	def __init__(self, complaint="no water, too much PHP"):
		self.__complaint = complaint

	def complain(self):
		print(self.__complaint)
class EIT(Person):
	pass

class Fellow(Person):
	pass

class Cat:
	pass

People = list()

People.append(Fellow())

for _ in range(27):
	People.append(EIT())

People.append(Cat())

for person in People:
	if(isinstance(person, Person)):
		person.complain()
	else:
		print("Not a person")

