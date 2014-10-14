def Fizzbuzz(x):
 	if x % 3 == 0 and x % 5 == 0:
 		print 'fizz buzz'
 		return
 	elif x % 3 == 0:
 		print 'fizz'
 		return
 	elif x % 5 == 0:
 		print 'buzz'
 		return
 	else:
 		print x
 		return

for i in range(0, 101):
	Fizzbuzz(i)
