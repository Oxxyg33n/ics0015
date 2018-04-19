'''
Using Singleton pattern we can achieve the result,
if new instance created it will overwrite or replace the existing one
'''

class ParentClass:
	SharedState = {}
	def __init__(self):
		self.__dict__ = self.SharedState

class MainClass(ParentClass):
	def __init__(self, arg):
		ParentClass.__init__(self)
		self.name = arg

	def __str__(self):
		return self.name

# Test example

inst1 = MainClass('Python')
print(inst1) # will print "python"

inst_2 = MainClass('Ruby')
print(inst2) # will print "Ruby"
print(inst1) # will print "Ruby" because first instance is replaced with the new one, which is "Ruby"

