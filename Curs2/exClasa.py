def nr_lines():
	with open('input.txt', 'r') as f:
		lines = f.readlines()

	g = open('output.txt', 'w')
	g.write('In input.txt sunt: ' + str(len(lines)) + ' linii')
	g.close()


def fnc2():
	import random
	f = open('output2.txt', 'w')
	num_lines = random.randrange(1,10,2)
	for i in range(0, num_lines):
		line = random.randrange(100, 1000, 2)
		f.write(str(line) + '\n')
	f.close()


def fnc3():
	f = open('born.txt', 'r')
	import datetime
	cont = f.read()
	date_list = cont.split()
	print datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))