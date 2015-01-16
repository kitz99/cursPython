class Pet(object):
	"""class that describe a pet"""

	def __init__(self, name, weight = 5):
		self.__name = name
		self.weight = weight

	def __str__(self):
		return "I am " + self.__name

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	name = property(get_name, set_name)


class Cat(Pet):
	def __init__(self, name, nr_lives):
		super(Cat, self).__init__(name)
		self.nr_lives = nr_lives


		