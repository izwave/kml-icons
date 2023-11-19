from xml.etree import ElementTree as et
import re

class Color:
	def to_hex(hex):
		subhex = re.findall('..?', hex)
		return 'ff{}'.format(''.join(subhex[::-1]))

class Style:
	DEFAULT_LINE_COLOR = 'ff000000'
	DEFAULT_LINE_WIDTH = 1.0
	DEFAULT_ICON_ID = 1899
	DEFAULT_ICON_COLOR = '0288D1'

class LineStyle:

	def __init__(self, root, url, color = None, width = None):
		self.__root = root
		self.__sroot = et.SubElement(self.__root, 'LineStyle')
		self._url = url
		self._color = et.SubElement(self.__sroot, 'color')
		self._width = et.SubElement(self.__sroot, 'width')
		self._color.text = Style.DEFAULT_LINE_COLOR
		self._width.text = str(Style.DEFAULT_LINE_WIDTH)

		LineStyle.get_style_url(self)

		if color is not None:
			self.color = color
		if width is not None:
			self.width = width

	''' linestyle.color '''
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, rename):
		if not et.iselement(self._color):
			self._color = et.SubElement(self.__sroot, 'color')
		self._color.text = str(rename)
		LineStyle.get_style_url(self)

	''' linestyle.width '''
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, rename):
		if not et.iselement(self._width):
			self._width = et.SubElement(self.__sroot, 'width')
		self._width.text = str(rename)
		LineStyle.get_style_url(self)

	''' linestyle.get_style_url() '''
	def get_style_url(self):
		forcstr = str(self.width.text)
		styleid = 'line-{}-{}'.format(str(self.color.text), forcstr.replace('.', ''))
		''' update style id '''
		self._url.text = '#' + styleid
		self.__root.attrib['id'] = styleid


class PolyStyle:

	def __init__(self, root, color = '4d000000', fill = None, outline = None):
		self.__root = root
		self.__sroot = et.SubElement(self.__root, 'PolyStyle')
		self._color = color
		self._fill = fill
		self._outline = outline

		if color is not None:
			self.color = color
		if fill is not None:
			self.fill = fill
		if outline is not None:
			self.outline = outline

	''' polystyle.color '''
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, rename):
		if not et.iselement(self._color):
			self._color = et.SubElement(self.__sroot, 'color')
		self._color.text = rename

	''' polystyle.fill '''
	@property
	def fill(self):
		return self._fill

	@fill.setter
	def fill(self, rename):
		if not et.iselement(self._fill):
			self._fill = et.SubElement(self.__sroot, 'fill')
		self._fill.text = rename

	''' polystyle.outline '''
	@property
	def outline(self):
		return self._outline

	@outline.setter
	def outline(self, rename):
		if not et.iselement(self._outline):
			self._outline = et.SubElement(self.__sroot, 'outline')
		self._outline.text = rename

	''' polystyle.get_style_url() '''
	def get_style_url(self):
		forcstr = ''
		if self._fill is not None:
			forcstr = str(self._fill.text)
		if self._outline is not None:
			forcstr = forcstr + str(self._outline.text)
		return 'poly-{}-{}'.format(str(self._color.text), forcstr)


class IconStyle:

	def __init__(self, root, url, color = None, scale = None, heading = None, id = None, iconcolor = None, href = None):
		self.__root = root
		self.__sroot = et.SubElement(self.__root, 'IconStyle')
		self._url = url
		self._color = color
		self._scale = scale
		self._heading = heading
				
		if color is not None:
			self.color = color
		if scale is not None:
			self.scale = scale
		if heading is not None:
			self.heading = heading

		self.icon = IconStyle.icon(self.__root, self._url, et.SubElement(self.__sroot, 'Icon'), id, iconcolor, href)

	''' iconstyle.color '''
	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, rename):
		if not et.iselement(self._color):
			self._color = et.SubElement(self.__sroot, 'color')
		self._color.text = rename

	''' iconstyle.scale '''
	@property
	def scale(self):
		return self._scale

	@scale.setter
	def scale(self, rename):
		if not et.iselement(self._scale):
			self._scale = et.SubElement(self.__sroot, 'scale')
		self._scale.text = rename

	''' iconstyle.heading '''
	@property
	def heading(self):
		return self._heading

	@heading.setter
	def heading(self, rename):
		if not et.iselement(self._heading):
			self._heading = et.SubElement(self.__sroot, 'heading')
		self._heading.text = rename

	''' iconstyle.get_style_url() '''
	def get_style_url(self):
		forcstr = ''
		if self._color is not None:
			forcstr = str(self._color.text)
		if self._scale is not None:
			forcstr = forcstr + str(self._scale.text)
		if self._heading is not None:
			forcstr = forcstr + str(self._heading.text)
		if not forcstr:
			return None
		return 'is-{}'.format(forcstr)

	class icon:

		def __init__(self, root, url, iroot, id=None, color=None, href=None):
			self.__root = root
			self._url = url
			self.__iroot = iroot

			self._id = Style.DEFAULT_ICON_ID
			self._color = Style.DEFAULT_ICON_COLOR
			self._href = href
		
			if color is not None:
				self.color = color
			if id is not None:
				self.id = id
			self.href = href

		''' icon.color '''
		@property
		def color(self):
			return self._color

		@color.setter
		def color(self, rename):
			self._color = rename.upper()
			self.__get_style_url()

		''' icon.id '''
		@property
		def id(self):
			return self._id

		@id.setter
		def id(self, rename):
			self._id = rename
			self.__get_style_url()

		''' iconstyle.href '''
		@property
		def href(self):
			return self._href

		@href.setter
		def href(self, rename):
			if not et.iselement(self._href):
				self._href = et.SubElement(self.__iroot, 'href')
			self._href.text = rename

		''' icon.get_style_url() '''
		def __get_style_url(self):
			styleid = 'icon-{}-{}'.format(str(self.id), self.color)
			''' update style id '''
			self._url.text = '#' + styleid
			self.__root.attrib['id'] = styleid