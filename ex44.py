class Parent(object):
	"""docstring for Parent"""
	def __init__(self, arg):
		super(Parent, self).__init__()
		self.arg = arg
		
	def implicit(self):
		print "Parent implicit."

class Child(Parent):
	def implicit():
		super(Child, self).implicit()

