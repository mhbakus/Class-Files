# fav_nums = [2, 6, 3, 18, 11]

# for num in fav_nums:
# 	if num % 2 == 0:
# 		print("{} is even".format(num))
# 	else:
# 		print("{} is odd".format(num))

# i = 2

# while i <= 15:
# 	print(i)
# 	i = i + 3

# i = 14

# while i >= 2:
# 	print(i)
# 	i = i - 3

# i = 14

# while i >= -1:
# 	if i % 2 == 0:
# 		print("{} is even".format(i))
# 	elif i == -1:
# 		print("{} negative".format(i))
# 	else:
# 		print("{} is odd".format(i))			
# 	i = i - 3	




# i = 50
# while i <= 130:
# 	if i % 2 == 0:
#  		print("{} is even and it double is {}".format(i, i*2))
#  	i = i +1



# for i in range(50, 130):
# 	if i % 2 == 0:
#  		print("{} is even and it double is {}".format(i, i*2))
#  	i = i +1


# for num in range(121, 331):
# 	for divisor in range(2, num):
# 		prime = True
# 		res = num % divisor
# 		if res == 0:
# 			prime = False
# 			break
# 	if prime == True:
# 		print(num)
			

# def say_nice_things(name, adjective):
# 	print("{} is {}".format(name, adjective))



# for _ in range(5):
# 	say_nice_things("Francis")


# for noun in ["Francis", "MEST", "a turtle"]:
# 	say_nice_things(noun);

# say_nice_things(adjective = "in charge", name = "Andrew")


# def say_a_lot(*args):
# 	print("i like:  ")

# 	for word in args:
# 		print(str(word) + "_")


# say_a_lot("ours", "MEST", "18")

# def add_all_nums(*args):

# 	total = 0
# 	for num in args:
# 		total = total + num
# 	return total


# print(add_all_nums(15, 25, 12, 36))


# def get_squares(*args):
# 	newArr = []
# 	for num in args:
# 		newArr.append(num**2)
# 	print(newArr)


# get_squares(2, 5, 7)


#triangle

for line in range(1, 10):
	for space in range(9-line):
		print(" ", end="")
	for stars in range(2*line - 1):
		print(" * ", end="")
	print("\n")

	if line == 9:
		new_line = line
		while new_line > 0:
			for space in range(9-new_line):
				print(" ", end="")
			for stars in range(2*new_line - 1):
				print(" * ", end="")
			print("\n")

			new_line -= 1





# for line2 in range(1, 5):
# 	for space in range(14):
# 		print(" ", end="")
# 	for stars2 in range(4):
# 		print("*", end="")
# 	print("\n")




































			




