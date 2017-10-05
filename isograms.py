def is_isograms(words):
	# dictword = dict()
	# for word in words.lower():
	# 	if word in dictword.keys():
	# 		return False
	# 	dictword[word] = 1
	# return True

	return sorted(set(words.lower())) == sorted(list(words.lower())) if words.isalpha() else False

	 


print(is_isograms('heldfcspno'))