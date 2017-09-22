"""
This code is to test private and protected attributes of objects in Python
"""

class cup:
	def __init__(self):
		self.__color = None
		self._content = None

	def set_color(self, color):
		self.__color = color

	def get_color(self):
		return (self.__color)

	def fill(self, drink):
		self._content = drink

	def get_content(self):
		return (self._content)

	def empty(self):
		slef._content = None


a = cup()
a.set_color('red')
a.fill('Tea')
#print a
print a.get_color()

a.set_color('green')
a.fill('Tea')
a._cup__color = 'blue'
#print a
print a.get_color()
print a.get_content()
