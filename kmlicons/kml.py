from xml.etree import ElementTree as et
import xml.dom.minidom
from kmlicons.feature import Base, Feature
from kmlicons.geometry import Geometry, MultiGeometry, Point, LineString, Polygon, altitudeMode, gxaltitudeMode


class Kml(Base, Geometry):

	def __init__(self, name = None, visibility = None, open = None):
		self._groot = et.Element('kml', xmlns='http://www.opengis.net/kml/2.2')
		self._gdoc = et.SubElement(self._groot,'Document')
		
		#self.document = Base(self._gdoc, name)

		self.__colorstyle = et.Element(None)
		self.__geometry = et.Element(None)

		Base.__init__(self, self._gdoc, name, visibility, open)
		Geometry.__init__(self, self.__geometry, self.__colorstyle)
	
	def addfolder(self, name = None):
		return Geometry(et.SubElement(self.__geometry,'Folder'), self.__colorstyle)

	def export(self, filename):
		
		# style
		self._gdoc.append(self.__colorstyle)
		# geometry
		self._gdoc.append(self.__geometry)
		
		# Gets a string from XML
		xml_string = et.tostring(self._groot, encoding='utf-8').decode('utf-8')
		
		# Parse the XML to add indentation
		dom = xml.dom.minidom.parseString(xml_string)
		indented_xml_string = dom.toprettyxml(indent="\t")
		
		# Write to file
		with open(filename, 'w', encoding='utf-8') as f:
			f.write(indented_xml_string)

if __name__ == '__main__':
	file = Kml()
	'''
	pnt = file.addpoint(name='oi',lat=0.9,long=5.4,alt=3.5)
	pnt.extrude = '1'
	pnt.altitudeMode = altitudeMode.clampToGround
	pnt.gxaltitudeMode = gxaltitudeMode.clampToSeaFloor
	pnt.tessellate = '1'
	file.name = 'oxe'
	'''
	
	coords = [(-23.4567,-46.35),(-23.456,-47.456,0.0), (-23.543,-43.35,0.0)]
	'''
	ponto = file.addpoint(name = 'POnto', lat=5.9,long=5.4,alt=5.5)
	#ponto.style.color = 'FAED4F'
	ponto.style.icon.id = '1849'
	ponto.style.icon.color = 'A87D4D'
	ponto.description = 'eaeaae'
	'''

	ls = file.addlinestring(name = 'linha 1')
	ls.coordinates.add(coords)
	ls.style.width = 10.2
	ls.style.color = '3456AAFF'
	ls.description = "minha reta"

	file.generate('bora.kml')
	
