from xml.etree import ElementTree as et

class altitudeMode:
	clampToGround = 'clampToGround'
	relativeToGround = 'relativeToGround'
	absolute = 'absolute'

class gxaltitudeMode:
	clampToSeaFloor = 'clampToSeaFloor'
	relativeToSeaFloor = 'relativeToSeaFloor'


class AltitudeProperty:
	def __init__(self, root, extrude = None, altitudemode = None, gxaltitudemode = None):
		self.__root = root
		self._extrude = extrude
		self._altitudeMode = altitudemode
		self._gxaltitudeMode = gxaltitudemode

		if extrude is not None:
				self.extrude = extrude
	
	''' geometry.extrude '''
	@property
	def extrude(self):
		return self._extrude

	@extrude.setter
	def extrude(self, rename):
		if not et.iselement(self._extrude):
			self._extrude = et.SubElement(self.__root,'extrude')
		self._extrude.text = rename

	''' geometry.altitudeMode '''
	@property
	def altitudeMode(self):
		return self._extrude

	@altitudeMode.setter
	def altitudeMode(self, rename):
		if not et.iselement(self._altitudeMode):
			self._altitudeMode = et.SubElement(self.__root,'altitudeMode')
		self._altitudeMode.text = rename

	@property
	def gxaltitudeMode(self):
		return self._extrude

	''' geometry.gxaltitudeMode '''
	@gxaltitudeMode.setter
	def gxaltitudeMode(self, rename):
		if not et.iselement(self._gxaltitudeMode):
			self._gxaltitudeMode = et.SubElement(self.__root,'gx:altitudeMode')
		self._gxaltitudeMode.text = rename

class AltitudeSpace(AltitudeProperty):

	def __init__(self, root, extrude = None, altitudeMode = None, gxaltitudeMode =  None, tessellate = None):
		super().__init__(root, extrude, altitudeMode, gxaltitudeMode)
		self.__root = root
		self._tessellate = tessellate

	@property
	def tessellate(self):
		return self._tessellate

	@tessellate.setter
	def tessellate(self, rename):
		if not et.iselement(self._tessellate):
			self._tessellate = et.SubElement(self.__root,'tessellate')
		self._tessellate.text = rename


class AltitudeString(AltitudeSpace):

	def __init__(self, root, extrude = None, altitudeMode = None, gxaltitudeMode =  None, tessellate = None, gxaltitudeoffset = None):
		super().__init__(root, extrude, altitudeMode, gxaltitudeMode, tessellate)
		self.__root = root
		self._gxaltitudeoffset = gxaltitudeoffset

	@property
	def gxaltitudeoffset(self):
		return self._gxaltitudeoffset

	@gxaltitudeoffset.setter
	def gxaltitudeoffset(self, rename):
		if not et.iselement(self._gxaltitudeoffset):
			self._gxaltitudeoffset = et.SubElement(self.__root,'gx:altitudeOffset')
		self._gxaltitudeoffset.text = rename

