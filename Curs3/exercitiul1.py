class BankAccount(object):
	"""Class describe a bank account"""
	def __init__(self, nume, sold = 0):
		self.nume = nume
		self.sold = sold

	def depune(self, suma):
		self.sold += suma
		print "Operatiune reusita\n" + "Sold curent: " + str(self.sold)

	def retrage(self, suma):
		if suma > self.sold:
			return "Fonduri insuficiente"
		self.sold -= suma
		return "Operatiune reusita\n" + "Sold curent: " + str(self.sold)



class Person(object):
	def __init__(self, name, cont, salary = 0):
		self.name = name
		self.cont = cont
		self.__salary = salary

	def get_salary(self):
		return "Salariul confidential!!"

	def set_salary(self, salary):
		self.__salary = salary

	salary = property(get_salary, set_salary)

	def receive_salary(self):
		self.cont.depune(self.__salary)




