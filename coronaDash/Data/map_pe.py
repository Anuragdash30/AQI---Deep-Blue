import folium
import os
import json
from folium.features import DivIcon
import pandas as pd
# Create map object
m = folium.Map(location=[19.0611, 72.8993], zoom_start=13)

# Global tooltip
# tooltip = 'Click For More Info'

# Create custom marker icon
# logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

# Vega data
# vis = os.path.join('data', 'vis.json')

# Geojson Data
overlay = os.path.join('', 'M-ward-parts(E).json')

Anushakti = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\AnushaktiApi.csv'
Anushakti_Nagar = pd.read_csv(Anushakti)

Trombay = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\TrombayApi.csv'
Trombay_Api = pd.read_csv(Trombay)

Cheeta = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\CheetaCampApi.csv'
CheetaCamp = pd.read_csv(Cheeta)

ShivajiNagar = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\ShivajiNagar.csv'
ShivajiNagar_Api = pd.read_csv(ShivajiNagar)

Mankhurd = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\MankhurdWest.csv'
Mankhurd_Api = pd.read_csv(Mankhurd)

Govandi = r'C: \Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\GovandiE.csv'
Govandi_Api = pd.read_csv(Govandi)

ChemburEast = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\ChemburE.csv'
ChemburEast_Api = pd.read_csv(ChemburEast)

Deonar = r'C:\Users\Nagesh\Desktop\nn_python\AQV-DeepBlue\Folium_maps\AQI DATA NEW\Deonar.csv'
Deonar_Api = pd.read_csv(Deonar)

AnushaktiApi = Anushakti_Nagar['AQI'].iloc[-1]
print(AnushaktiApi)
TrombayApi = Trombay_Api['AQI'].iloc[-1]
print(TrombayApi)
CheetaApi = CheetaCamp['AQI'].iloc[-1]
print(CheetaApi)
ShivajiNagarApi = ShivajiNagar_Api['AQI'].iloc[-1]
print(ShivajiNagarApi)
GovandiApi = Govandi_Api['AQI'].iloc[-1]
print(GovandiApi)
ChemburEastApi = ChemburEast_Api['AQI'].iloc[-1]
print(ChemburEastApi)
MankhurdApi = Mankhurd_Api['AQI'].iloc[-1]
print(MankhurdApi)
DeonarApi = Deonar_Api['AQI'].iloc[-1]
print(DeonarApi)

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
folium.GeoJson(overlay, name='M-ward-parts(E)').add_to(m)

# folium.map.Marker(
#     [19.044310172961623, 72.88300037384032],
#     icon=DivIcon(
#         icon_size=(180, 30),
#         icon_anchor=(0, 0),
#         html='<div style="font-size: 24pt">M-ward(W)</div>',
#     )
# ).add_to(m)

# Generate map
m.save('map_pe.html')
