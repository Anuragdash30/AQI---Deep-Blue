import folium
import os
import json
from folium.features import DivIcon

# Create map object
m = folium.Map(location=[19.0611, 72.8993], zoom_start=13)

# Global tooltip
# tooltip = 'Click For More Info'

# Create custom marker icon
# logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

# Vega data
# vis = os.path.join('data', 'vis.json')

# Geojson Data
overlay = os.path.join('', 'M-ward-east.json')

# Create markers
# folium.Marker([42.363600, -71.099500],
#               popup='<strong>Location One</strong>',
#               tooltip=tooltip).add_to(m),
# folium.Marker([42.333600, -71.109500],
#               popup='<strong>Location Two</strong>',
#               tooltip=tooltip,
#               icon=folium.Icon(icon='cloud')).add_to(m),
# folium.Marker([42.377120, -71.062400],
#               popup='<strong>Location Three</strong>',
#               tooltip=tooltip,
#               icon=folium.Icon(color='purple')).add_to(m),
# folium.Marker([42.374150, -71.122410],
#               popup='<strong>Location Four</strong>',
#               tooltip=tooltip,
#               icon=folium.Icon(color='green', icon='leaf')).add_to(m),
# folium.Marker([42.375140, -71.032450],
#               popup='<strong>Location Five</strong>',
#               tooltip=tooltip,
#               icon=logoIcon).add_to(m),
# folium.Marker([42.315140, -71.072450],
#               popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)

# Circle marker
# folium.CircleMarker(
#     location=[42.466470, -70.942110],
#     radius=50,
#     popup='My Birthplace',
#     color='#428bca',
#     fill=True,
#     fill_color='#428bca'
# ).add_to(m)

# Geojson overlay
folium.GeoJson(overlay, name='M-ward-east').add_to(m)

# folium.map.Marker(
#     [19.044310172961623, 72.88300037384032],
#     icon=DivIcon(
#         icon_size=(180, 30),
#         icon_anchor=(0, 0),
#         html='<div style="font-size: 24pt">M-ward(W)</div>',
#     )
# ).add_to(m)

# Generate map
m.save('map_me.html')
