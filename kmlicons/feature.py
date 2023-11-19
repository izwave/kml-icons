from xml.etree import ElementTree as et

class Base:

	def __init__(self, root, name = None, visibility = None, open = None):
		self.__root = root
		self._name = name
		self._visibility = visibility
		self._open = open

		if name is not None:
			self.name = name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, rename):
		if not et.iselement(self._name):
			self._name = et.SubElement(self.__root,'name')
		self._name.text = rename

class Feature(Base):

	def __init__(self, root, name = None, visibility = None, open = None, description = None):
		Base.__init__(self, root, name, visibility, open)
		self.__root = root
		self._description = description
		self._styleurl = et.SubElement(root, 'styleUrl')


	@property
	def description(self):
		return self._description
	
	@description.setter
	def description(self, rename):
		if not et.iselement(self._description):
			self._description = et.SubElement(self.__root,'description')
		self._description.text = rename
	
	@property
	def styleurl(self):
		return self._styleurl

	@styleurl.setter
	def styleurl(self, rename):
		if not et.iselement(self._styleurl):
			self._styleurl = et.SubElement(self.__root,'styleUrl')
		self._styleurl.text = '#' + str(rename)

		