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

# for line in range(1, 10):
# 	for space in range(9-line):
# 		print(" ", end="")
# 	for stars in range(2*line - 1):
# 		print(" * ", end="")
# 	print("\n")

# 	if line == 9:
# 		new_line = line
# 		while new_line > 0:
# 			for space in range(9-new_line):
# 				print(" ", end="")
# 			for stars in range(2*new_line - 1):
# 				print(" * ", end="")
# 			print("\n")

# 			new_line -= 1





# for line2 in range(1, 5):
# 	for space in range(14):
# 		print(" ", end="")
# 	for stars2 in range(4):
# 		print("*", end="")
# 	print("\n")


# IS_BEAUTIFULL = True
# name = "Andrew"
# if IS_BEAUTIFULL and name == "Andrew":
# 	print("hey, beautifull")
# else:
# 	print("Sorry SA")



# print the number fron 11 to 53 that are even and divisible by 3


# for number in range(11, 54):
# 	if number % 2 == 0 and number % 3 == 0:
# 		print("{} is even and divisible by 3".format(number))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 3, -7, 0.5, 3]

# length = len(nums)

# #my way
# i = 1
# while i < length:
# 	print(nums[i])
# 	i += 2

#eva way
# for i in range(1, length, 2):
# 	print(nums[i])

#samuel way but not good solution
# for i in nums:
# 	if nums.index(i) % 2 == 0:
# 		print("")
# 	else:
# 		print(i)



# str = "learN python THe hArd way"
# strlower = str.lower()
# words = strlower.split(" ")
# newarr = []
# for word in words:
# 	up = word[0].upper()
# 	neword = word.replace(word[0], up)
# 	newarr.append(neword)

# newstr = " ".join(newarr)
# print(newstr)



# for line in range(1, 4):
# 	for space in range(3-line):
# 		print(" ", end="")
# 	for stars in range(2*line - 1):
# 		print("*", end="")
# 	print(" ")
# 	if line == 3:
# 		new_line = line
# 		while new_line > 0:
# 			for space in range(3-new_line):
# 				print(" ", end="")
# 			for stars in range(2*new_line - 1):
# 				print("*", end="")
# 			print(" ")
# 			new_line -= 1


def diamond(ln):

	for line in range(1, ln):
		for space in range((ln-1)-line):
			print(" ", end="")
		for stars in range(2*line - 1):
			print("*", end="")
		print(" ")
		if line == (ln-1):
			new_line = line
			while new_line > 0:
				for space in range((ln)-new_line):
					print(" ", end="")
				for stars in range(2*new_line - 3):
					print("*", end="")
				print(" ")
				new_line -= 1




diamond(20)


















			




