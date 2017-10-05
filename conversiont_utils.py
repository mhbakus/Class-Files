class ConversionUtils:


	@staticmethod
	def weight(value, unit):
		if unit == 'gm':
			libs = value * 0.00220462
			return "{} grams = {} libs".format(value, libs)
		elif unit == 'libs':
			gm = value * 453.592
			return "{} libs = {} grams".format(value, gm)
		else:
			return "unknow unit"

	@staticmethod
	def distance(value, unit):
		if unit == 'mi':
			km = value * 1.60934
			return "{} miles = {} km".format(value, km)
		elif unit == 'km':
			mi = value * 0.621371
			return "{} km = {} miles".format(value, mi)
		else:
			return "unknow unit"

	@staticmethod
	def fluide(value, unit):
		if unit == 'l':
			fl = value * 33.814
			return "{} Liter = {} US fluide".format(value, fl)
		elif unit == 'fl':
			L = value * 0.0295735
			return "{} US fluide = {} Liter".format(value, L)
		else:
			return "unknow unit"

	@staticmethod
	def temperature(value, unit):
		if unit == 'fh':
			c = (value-32) * 0.5556
			return "{} fahrent = {} celsuis".format(value, c)
		elif unit == 'c':
			fh = value * 1.8+32
			return "{} celsuis = {} fahrent".format(value, fh)
		else:
			return "unknow unit"

	@staticmethod
	def inchCent(value, unit):
		if unit == 'inch':
			cm = value * 2.54
			return "{} inch = {} centimeter".format(value, cm)
		elif unit == 'cm':
			inch = value * 0.393701
			return "{} centimeter = {} inch".format(value, inch)
		else:
			return "unknow unit"

	# @staticmethod
	# def gram_to_libs(gm):
	# 	libs = gm * 0.00220462
	# 	return "{} grams = {} libs".format(gm, libs)


	# @staticmethod
	# def libs_to_gram(lbs):
	# 	gm = libs * 453.592
	# 	return "{} grams = {} libs".format(gm, libs)

	# @staticmethod
	# def distance(mi, km):


	# @staticmethod
	# def f

print(ConversionUtils.weight(1, 'gm'))
print(ConversionUtils.distance(1, 'km'))
print(ConversionUtils.fluide(1, 'l'))
print(ConversionUtils.temperature(120, 'fh'))
print(ConversionUtils.inchCent(1, 'inch'))


# 1 gm = 0.00220462
# 1 liters = 33.814 us fluid 
# 1 fahrent = -17.2222 celsuis
# 1 inch = 2.54 centimeters