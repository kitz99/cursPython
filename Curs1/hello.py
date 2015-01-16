print "hello world"

# afisati 100 de mesaje hello world
for i in range(1, 101):
	print "hello world"

# exercitiul 2
s = "mesajul meu "
for i in range(1, 101):
	s += " hello "
print s

#exercitiul 3

for i in a:
	if i % 3 == 0:
		print "{} este divizibil cu 3".format(i)


# exercitiul 4
ll = []
for i in range(1, len(a), 2):
	ll.append(a[i])

#ex 5
d = {'tastatura' : 70, 'mouse' : 50, 'casti' : 100}
s = 0

for key, value in d.iteritems():
	pret = d[key]
	cuTVA = pret + 24.0/100.0 * pret
	s += cuTVA

print s

def fact(x):
	if x == 0 or x == 1:
		return 1
	return x * fact(x - 1)

