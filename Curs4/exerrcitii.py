#!/usr/bin/python
def ex1():
    return [(j, i) for i in range(1, 7) for j in range(1, 7)]
def ex2(l):
    return list({x for x in l })

def ex3(lista):
    return {x[1]: x[0] for x in lista}

def ex4(dictionar):
    return [dictionar[i] if i in dictionar.keys() else None for i in range(0, 11)]

def ex5(string):
    
if __name__ == '__main__':
    print "Problema 1"
    print ex1()
    print "\nProblema 2"
    print ex2([1, 1, 1, 2, 2, 2])
    print "\nProblema 3"
    companies = [
    ("Pixar", 2),
    ("Disney", 4),
    ("Warner Bros.", 9),
    ("Universal", 5),
    ("Reception", 0),
    ("Studio Ghibli", 8),
    ("DreamWorks", 6),
]
    print ex3(companies)
    print "\nProblema 4"
    print ex4(ex3(companies))
    zen =  "Beautiful is better than ugly.\
            Explicit is better than implicit.\
            Simple is better than complex.\
            Complex is better than complicated.\
            Flat is better than nested.\
            Sparse is better than dense.\
            Readability counts.\
            Special cases aren't special enough to break the rules.\
            Although practicality beats purity.\
            Errors should never pass silently.\
            Unless explicitly silenced.\
            In the face of ambiguity, refuse the temptation to guess.\
            There should be one-- and preferably only one --obvious way to do it.\
            Although that way may not be obvious at first unless you're Dutch.\
            Now is better than never.\
            Although never is often better than *right* now.\
            If the implementation is hard to explain, it's a bad idea.\
            If the implementation is easy to explain, it may be a good idea.\
            Namespaces are one honking great idea -- let's do more of those!"
    print "\nProblema 5"
    print ex5(zen)