class Point(object):
	"""docstring for Point"""
	x = 0
	y = 0
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, B):
		try:
			isinstance(B, Point)
		except ValueError:
			print "invalid operation"
		x = self.x + B.x
		y = self.y + B.y
		return Point(x, y)

	def __sub__(self, B):
		try:
			isinstance(B, Point)
		except ValueError:
			print "invalid operation"
		x = self.x - B.x
		y = self.y - B.y
		return Point(x, y)




class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		

		