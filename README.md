# kml-icons
Kml document icons for importing maps into Google My Maps

Example to create a simple icon

```python
import kmlicons as kmli
from kmlicons import icons

doc = kmli.Kml()

icon = doc.addpoint(name = 'Car point')
icon.style.icon.id = icons.transport.car
icon.style.icon.color = 'D9730D'
icon.description = 'My orange car'
doc.export('map.kml')
```

export
```xml
<?xml version="1.0" ?>
<kml xmlns="http://www.opengis.net/kml/2.2">
	<Document>
		<Style id="icon-1538-D9730D">
			<IconStyle>
				<Icon>
					<href/>
				</Icon>
			</IconStyle>
		</Style>
		<Placemark>
			<name>Car point</name>
			<styleUrl>#icon-1538-D9730D</styleUrl>
			<Point>
				<coordinates>0,0,0</coordinates>
			</Point>
			<description>My orange car</description>
		</Placemark>
	</Document>
</kml>
```

Create a linestring

```python
import kmlicons as kmli

doc = kmli.Kml()

line = doc.addlinestring(name = 'Line string')

coords = [
    (-23.4567,-46.35,0.0),
    (-23.456,-47.456,0.0),
    (-23.543,-43.35,0.0)
]

line.coordinates.add(coords)
line.style.width = 3.2
line.style.color = kmli.Color.to_hex('D9730D')
line.description = "My orange line"
doc.export('map.kml')
```

export

```xml
<?xml version="1.0" ?>
<kml xmlns="http://www.opengis.net/kml/2.2">
	<Document>
		<Style id="line-ff0D73D9-32">
			<LineStyle>
				<color>ff0D73D9</color>
				<width>3.2</width>
			</LineStyle>
		</Style>
		<Placemark>
			<name>Line string</name>
			<styleUrl>#line-ff0D73D9-32</styleUrl>
			<LineString>
				<coordinates>-46.35,-23.4567,0.0, -47.456,-23.456,0.0, -43.35,-23.543,0.0</coordinates>
			</LineString>
			<description>My orange line</description>
		</Placemark>
	</Document>
</kml>
```


[KML Reference](https://developers.google.com/kml/documentation/kmlreference)

![Texto alternativo](https://developers.google.com/static/kml/documentation/images/classTree52.gif)
