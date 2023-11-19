from xml.etree import ElementTree as et

from kmli.feature import Feature
from kmli.style import Style, IconStyle, LineStyle, PolyStyle
from kmli.altitude import altitudeMode, gxaltitudeMode, AltitudeProperty, AltitudeSpace, AltitudeString


class Coordinates:
	def __init__(self, root, coordinates):
		self._coordinates = et.SubElement(root, 'coordinates')
		self.coordinates = coordinates

	''' geometry.coordinates '''
	@property
	def coordinates(self):
		return self._coordinates

	@coordinates.setter
	def coordinates(self, rename):
		x = len(rename[0])
		textFormat = ''
		if x == 3:
			textFormat = '%s,%s,%s' % rename[0][::-1]
		elif x == 2:
			textFormat = '%s,%s,%s' % (rename[0][::-1] + (0,))
		else:
			textFormat = '0.0,0.0,0.0'
		self._coordinates.text = textFormat

class multiCoordinates:
	def __init__(self, root, lat, long, alt):
		self.__root = et.SubElement(root, 'coordinates')
		self._lat = lat
		self._long = long
		self._alt = alt

		self.__root.text = '{},{},{}'.format(self._lat, self._long, self._alt)
	
	def add(self, coords):
		x = len(coords[0])
		coordsFormat = []
		if x == 2:
			coordsFormat = [('{},{},0.0'.format(k[1], k[0])) for k in coords ]
		self.__root.text = ', '.join(coordsFormat)

class MultiGeometry(Feature):

	def __init__(self, root, sroot, name = None, visibility = None, open = None, description = None):
		self.__root = et.SubElement(root, 'Placemark')
		self.__sroot = et.SubElement(sroot, None)
		super().__init__(self.__root, name, visibility, open, description)

	def addpoint(self, **kwargs):
		return Point(self.__root, self.__sroot, **kwargs)
	def addlinestring(self, **kwargs):
		return LineString(self.__root, self.__sroot, **kwargs)
	def addpolygon(self, **kwargs):
		return Polygon(self.__root, self.__sroot, **kwargs)

class Geometry:

	def __init__(self, root, sroot):
		self.__root = root
		self.__sroot = sroot

	def addpoint(self, **kwargs):
		return Point(self.__root, self.__sroot, **kwargs)
	def addlinestring(self, **kwargs):
		return LineString(self.__root, self.__sroot, **kwargs)
	def addpolygon(self, **kwargs):
		return Polygon(self.__root, self.__sroot, **kwargs)
	def multigeometry(self, **kwargs):
		return MultiGeometry(self.__root, self.__sroot, **kwargs)


class Point(AltitudeProperty, Feature, Coordinates):
	def __init__(self, root, sroot,
		name=None,
		visibility=None,
		open=None,
		description=None,
		iconid=Style.DEFAULT_ICON_ID,
		iconcolor=Style.DEFAULT_ICON_COLOR,
		href=None,
		color=None,
		scale=None,
		heading=None,
		extrude=None,
		altitudemode=None,
		gxaltitudemode=None,
		coordinates=[(0,0,0)]):

		self.__root = root
		self.__sroot = sroot
		self.__surl = None

		
		if root.tag != 'Placemark':
			self.__root = et.SubElement(root, 'Placemark')
			self.__sroot = et.SubElement(sroot, None)
			Feature.__init__(self, self.__root, name, visibility, open, description)
			#self.__surl = Feature.self.__styleurl

		self.__root = et.SubElement(self.__root, 'Point')
		
		''' Composition '''
		AltitudeProperty.__init__(self, self.__root, extrude, altitudemode, gxaltitudemode)
		Coordinates.__init__(self, self.__root, coordinates)
		self.style = IconStyle(et.SubElement(self.__sroot, 'Style'), self.styleurl, color, scale, heading, iconid, iconcolor, href)


class LineString(AltitudeString, Feature):
	def __init__(self, root, sroot,
		name=None,
		visibility=None,
		open=None,
		description=None,
		color=None,
		width=None,
		extrude=None,
		altitudemode=None,
		gxaltitudemode=None,
		tessellate=None,
		gxaltitudeoffset=None,
		gxdraworder=None,
		lat=None,long=None,alt=None):

		self.__root = root
		self.__sroot = sroot

		if root.tag != 'Placemark':
			self.__root = et.SubElement(root, 'Placemark')
			self.__sroot = et.SubElement(sroot, None)
			Feature.__init__(self, self.__root, name, visibility, open, description)

		self.__root = et.SubElement(self.__root, 'LineString')
		AltitudeString.__init__(self, self.__root, extrude, altitudemode, gxaltitudemode, tessellate, gxaltitudeoffset)

		''' Composition '''
		self.coordinates = multiCoordinates(self.__root, lat, long, alt)
		self.style = LineStyle(et.SubElement(self.__sroot, 'Style'), self.styleurl, color, width)
		self._gxdraworder = gxdraworder

	''' geometry.gxdraworder '''
	@property
	def gxdraworder(self):
		return self._gxdraworder

	@gxdraworder.setter
	def gxdraworder(self, rename):
		if not et.iselement(self._gxdraworder):
			self._gxdraworder = et.SubElement(self.__root,'gx:drawOrder')
		self._gxdraworder.text = rename

class Polygon:
	def __init__(self, root, sroot,
		name=None,
		visibility=None,
		open=None,
		description=None,
		color=None,
		fill=None,
		outline=None,
		linecolor=None,
		width=None,
		extrude=None,
		altitudemode=None,
		gxaltitudemode=None,
		tessellate=None,
		lat=None,long=None,alt=None):

		self.__root = root
		self.__sroot = sroot

		if root.tag != 'Placemark':
			self.__root = et.SubElement(root, 'Placemark')
			self.__sroot = et.SubElement(sroot, None)
			Feature.__init__(self, self.__root, name, visibility, open, description)

		self.__root = et.SubElement(self.__root, 'Polygon')
		
		AltitudeSpace.__init__(self.__root, extrude , altitudeMode, gxaltitudemode, tessellate)

		''' Composition '''
		self.coordinates = Coordinates(self.__root, lat, long, alt)
		self.__sroot = et.SubElement(self.__sroot, 'Style')
		self.polystyle = PolyStyle(self.__sroot, color, fill, outline)
		self.linestyle = LineStyle(self.__sroot, linecolor, width)