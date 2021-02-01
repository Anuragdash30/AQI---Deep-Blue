import folium
import os
import json
from folium.features import DivIcon
import pandas as pd
# Create map object
pd.options.mode.chained_assignment = None
m = folium.Map(location=[19.0611, 72.8993], zoom_start=13)


# Geojson Data
overlay = os.path.join('', 'M-ward-parts(W).json')
overlay3 = os.path.join('', 'M-ward-parts(E).json')

overlay2 = os.path.join('', 'partsoverlap.json')

# csv for m ward west
Chedda_Nagar = pd.read_csv("AQI DATA NEW\CheddaNagar.csv")


Tilak_Nagar = pd.read_csv("AQI DATA NEW\TilakNagar.csv")


Sindhi_Society = pd.read_csv("AQI DATA NEW\SIndhiSociety.csv")


Chembur_West = pd.read_csv("AQI DATA NEW\Chembur_west.csv")

Deonar = pd.read_csv("AQI DATA NEW\Deonar.csv")


Mahul_E = pd.read_csv("AQI DATA NEW\MahulApi.csv")


CheddaApi = Chedda_Nagar.tail(1)
CheddaApi['name'] = 'Chedda nagar'

DeonarApi = Deonar.tail(1)
DeonarApi['name'] = 'Deonar'

TilakApi = Tilak_Nagar.tail(1)
TilakApi['name'] = 'Tilak Nagar'
SindhiApi = Sindhi_Society.tail(1)
SindhiApi['name'] = 'Sindhi Society'
ChemburWApi = Chembur_West.tail(1)
ChemburWApi['name'] = 'Chembur-west'
MahulApi = Mahul_E.tail(1)
MahulApi['name'] = 'Mahul'


# m ward east
Cheeta_camp = pd.read_csv("AQI DATA NEW\CheetaCampApi.csv")


chembur_east = pd.read_csv("AQI DATA NEW\ChemburE.csv")


govandi_east = pd.read_csv("AQI DATA NEW\GovandiE.csv")


shivaji_nagar = pd.read_csv("AQI DATA NEW\ShivajiNagar.csv")


trombay = pd.read_csv("AQI DATA NEW\TrombayApi.csv")

Anushakti = pd.read_csv("AQI DATA NEW\AnushaktiApi.csv")

mankhud_west = pd.read_csv("AQI DATA NEW\MankhurdWest.csv")

Cheeta_campApi = Cheeta_camp.tail(1)
Cheeta_campApi['name'] = 'Cheetah Camp'

chembur_eastApi = chembur_east.tail(1)
chembur_eastApi['name'] = 'Chembur-east'

govandi_eastApi = govandi_east.tail(1)
govandi_eastApi['name'] = 'Govandi'

shivaji_nagarApi = shivaji_nagar.tail(1)
shivaji_nagarApi['name'] = 'Shivaji Nagar'

trombayApi = trombay.tail(1)
trombayApi['name'] = 'Trombay'

AnushaktiApi = Anushakti.tail(1)
AnushaktiApi['name'] = 'Ansuhakti Nagar'

mankhud_westApi = mankhud_west.tail(1)
mankhud_westApi['name'] = 'Mankhurd'

#################

df_row = pd.concat([CheddaApi, ChemburWApi, MahulApi])
df_row2 = pd.concat([SindhiApi, TilakApi, Cheeta_campApi, DeonarApi])

df_row3 = pd.concat([chembur_eastApi, govandi_eastApi,
                     shivaji_nagarApi, trombayApi, AnushaktiApi, mankhud_westApi])


#############

folium.GeoJson(overlay, name='M-ward-parts(W)').add_to(m)
folium.GeoJson(overlay3, name='M-ward-parts(E)').add_to(m)
folium.GeoJson(overlay2, name='partsoverlap').add_to(m)

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
    threshold_scale=[0, 100, 150, 200, 280, 300, 310, 340, 400, 500],
    fill_opacity=0.7,
    legend_name='Air Quality Index of M-ward West',
    highlight=True


).add_to(m)

choropleth2 = folium.Choropleth(
    geo_data=overlay3,
    data=df_row3,
    columns=['name', 'AQI'],
    name='choropleth',
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    threshold_scale=[0, 100, 150, 200, 280, 300, 310, 340, 400, 500],
    fill_opacity=0.7,

    highlight=True


)
for key in choropleth2._children:
    if key.startswith('color_map'):
        del(choropleth2._children[key])
choropleth2.add_to(m)

choropleth3 = folium.Choropleth(
    geo_data=overlay2,
    data=df_row2,
    columns=['name', 'AQI'],
    name='choropleth',
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    threshold_scale=[0, 100, 150, 200, 280, 300, 310, 340, 400, 500],
    fill_opacity=0.7,

    highlight=True


)
for key in choropleth3._children:
    if key.startswith('color_map'):
        del(choropleth3._children[key])
choropleth3.add_to(m)


folium.LayerControl().add_to(m)
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['name', 'AQI'], labels=True)
)
choropleth2.geojson.add_child(
    folium.features.GeoJsonTooltip(['name', 'AQI'], labels=True)
)
choropleth3.geojson.add_child(
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
m.save('map_all.html')
