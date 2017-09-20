#creating a headphone object
class HeadPhone():
	def __init__(self, color, size, connectivity, cable):
		self.color = color
		self.size = size
		self.connectivity = connectivity
		self.cable = cable

#creating the setter
	def set_color(self, color):
		self.color = color

	def set_size(self, size):
		self.size = size

	def set_connectivity(self, connectivity):
		self.connectivity = connectivity

	def set_cable(self, cable):
		self.cable = cable


beatAudio = HeadPhone('red', '12m', 'bluetooth', 'type-c')
beatAudio.set_color('blue')
print(beatAudio.color)