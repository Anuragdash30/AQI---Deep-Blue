import folium
import os
import json
from folium.features import DivIcon
import pandas as pd
import branca.colormap as cm
# Create map object
m = folium.Map(location=[19.0611, 72.8993], zoom_start=13)

# Global tooltip
# tooltip = 'Click For More Info'

# Create custom marker icon
# logoIcon = folium.features.CustomIcon('logo.png', icon_size=(50, 50))

# Vega data
# vis = os.path.join('data', 'vis.json')

# Geojson Data
overlay = os.path.join('', 'M-ward-parts(W).json')

Chedda = r'AQI DATA NEW\CheddaNagar.csv'
Chedda_Nagar = pd.read_csv(Chedda)

Tilak = r'AQI DATA NEW\TilakNagar.csv'
Tilak_Nagar = pd.read_csv(Tilak)

Sindhi = r'AQI DATA NEW\SIndhiSociety.csv'
Sindhi_Society = pd.read_csv(Sindhi)

ChemburW = r'AQI DATA NEW\Chembur_west.csv'
Chembur_West = pd.read_csv(ChemburW)

Mahul = r'AQI DATA NEW\MahulApi.csv'
Mahul_E = pd.read_csv(Mahul)

CheddaApi = Chedda_Nagar.tail(1)
CheddaApi['name'] = 'Chedda nagar'
TilakApi = Tilak_Nagar.tail(1)

TilakApi['name'] = 'Tilak Nagar'
SindhiApi = Sindhi_Society.tail(1)
SindhiApi['name'] = 'Sindhi Society'
ChemburWApi = Chembur_West.tail(1)
ChemburWApi['name'] = 'Chembur-west'
MahulApi = Mahul_E.tail(1)
MahulApi['name'] = 'Mahul'

df_row = pd.concat([CheddaApi, TilakApi, SindhiApi, ChemburWApi, MahulApi])
print(df_row)
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
folium.GeoJson(overlay, name='M-ward-parts(W)').add_to(m)

# colormap = branca.colormap.linear.YlOrRd_09.scale(0, 500)
# colormap = colormap.to_step(index=[0, 50, 100, 150, 200, 300, 400, 500])
# colormap.caption = 'Air Quality Index of M-ward West'
# colormap.add_to(m)

choropleth = folium.Choropleth(
    geo_data=overlay,
    data=df_row,
    columns=['name', 'AQI'],
    name='choropleth',
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    threshold_scale=[0, 50, 100, 150, 200, 250, 300, 400, 500],
    fill_opacity=0.7,
    legend_name='Air Quality Index of M-ward West',
    highlight=True


).add_to(m)
folium.LayerControl().add_to(m)
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name', 'AQI'], labels=True)
)
# folium.map.Marker(
#     [19.044310172961623, 72.88300037384032],
#     icon=DivIcon(
#         icon_size=(180, 30),
#         icon_anchor=(0, 0),
#         html='<div style="font-size: 24pt">M-ward(W)</div>',
#     )
# ).add_to(m)

# Generate map
m.save('map_pw.html')
