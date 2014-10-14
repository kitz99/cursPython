def print_5():
	for i in range(1999, 3001):
		if i % 5 == 0 and i % 7 != 0:
			print "{},".format(i),

def is_palindrome(str):
	if str == ''.join(reversed(str)):
		return True 
	else: 
		return False

def comun(l1, l2):
	for i in l1:
		if i in l2:
			return True
	return False

# l1 = [1, 2, 3, 4]
# l2 = [5, 7, 3, 1]

# if comun(l1, l2):
# 	print "am gasit"
# else:
# 	print "Da nu merge!"

def find_longest_word(list):
	maxWord = list[0]
	for word in list:
		if len(word) > len(maxWord):
			maxWord = word
	print maxWord

# find_longest_word(['ana', 'maria', 'anamaria'])

def filter_long_words(list, num):
	for word in list:
		if len(word) > num:
			print word,

# filter_long_words(['ana', 'maria', 'anamaria'], 2)

# functie cu numar variabil de argumente
def suma(*arg):
	print type(arg)
	S = 0
	for i in arg:
		S+=i
	print S

# functia de decriptare
def decript(string):
	out = ''

	for i in range(0, len(string)):
		if ord(string[i]) in range(97, 122):
			if string[i] == 'a':
				out += 'z'
			elif string[i] == 'z':
				out += 'a'
			else:
				out += chr(ord(string[i]) - 1)
		else:
			out += string[i]

	print out












