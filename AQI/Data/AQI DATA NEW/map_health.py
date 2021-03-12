import folium
import os
import json
from folium.features import DivIcon
import pandas as pd
Chedda_Nagar = pd.read_csv("CheddaNagar.csv").dropna(how='all')


Tilak_Nagar = pd.read_csv("TilakNagar.csv").dropna(how='all')


Sindhi_Society = pd.read_csv("SIndhiSociety.csv").dropna(how='all')


Chembur_West = pd.read_csv("Chembur_west.csv").dropna(how='all')

Deonar = pd.read_csv("Deonar.csv").dropna(how='all')


Mahul_E = pd.read_csv("MahulApi.csv").dropna(how='all')


CheddaApi = Chedda_Nagar['AQI'].iloc[-1]


DeonarApi = Deonar['AQI'].iloc[-1]


TilakApi = Tilak_Nagar['AQI'].iloc[-1]

SindhiApi = Sindhi_Society['AQI'].iloc[-1]

ChemburWApi = Chembur_West['AQI'].iloc[-1]

MahulApi = Mahul_E['AQI'].iloc[-1]

Cheeta_camp = pd.read_csv("CheetaCampApi.csv").dropna(how='all')


chembur_east = pd.read_csv("ChemburE.csv").dropna(how='all')


govandi_east = pd.read_csv("GovandiE.csv").dropna(how='all')


shivaji_nagar = pd.read_csv("ShivajiNagar.csv").dropna(how='all')


trombay = pd.read_csv("TrombayApi.csv").dropna(how='all')

Anushakti = pd.read_csv("AnushaktiApi.csv").dropna(how='all')

mankhud_west = pd.read_csv("MankhurdWest.csv").dropna(how='all')

Cheeta_campApi = Cheeta_camp['AQI'].iloc[-1]


chembur_eastApi = chembur_east['AQI'].iloc[-1]


govandi_eastApi = govandi_east['AQI'].iloc[-1]


shivaji_nagarApi = shivaji_nagar['AQI'].iloc[-1]

trombayApi = trombay['AQI'].iloc[-1]

AnushaktiApi = Anushakti['AQI'].iloc[-1]

mankhud_westApi = mankhud_west['AQI'].iloc[-1]

################

with open('M-ward-parts(E).json') as f:
    data = json.load(f)

for item in data['features']:
    if item['properties']['name'] == 'Trombay':
        item['properties']['AQI'] = int(trombayApi)
    if item['properties']['name'] == 'Ansuhakti Nagar':
        item['properties']['AQI'] = int(AnushaktiApi)
    if item['properties']['name'] == 'Mankhurd':
        item['properties']['AQI'] = int(mankhud_westApi)
    if item['properties']['name'] == 'Chembur-east':
        item['properties']['AQI'] = int(chembur_eastApi)
    if item['properties']['name'] == 'Govandi':
        item['properties']['AQI'] = int(govandi_eastApi)
    if item['properties']['name'] == 'Shivaji Nagar':
        item['properties']['AQI'] = int(shivaji_nagarApi)


with open('M-ward-parts(E).json', 'w') as f:
    json.dump(data, f)
f.close()


with open('M-ward-parts(W).json') as f:
    data = json.load(f)

for item in data['features']:
    if item['properties']['name'] == 'Chedda nagar':
        item['properties']['AQI'] = int(CheddaApi)
    if item['properties']['name'] == 'Chembur-west':
        item['properties']['AQI'] = int(ChemburWApi)
    if item['properties']['name'] == 'Mahul':
        item['properties']['AQI'] = int(MahulApi)


with open('M-ward-parts(W).json', 'w') as f:
    json.dump(data, f)
f.close()


with open('partsoverlap.json') as f:
    data = json.load(f)

for item in data['features']:
    if item['properties']['name'] == 'Sindhi Society':
        item['properties']['AQI'] = int(SindhiApi)
    if item['properties']['name'] == 'Tilak Nagar':
        item['properties']['AQI'] = int(TilakApi)
    if item['properties']['name'] == 'Cheetah Camp':
        item['properties']['AQI'] = int(Cheeta_campApi)
    if item['properties']['name'] == 'Deonar':
        item['properties']['AQI'] = int(DeonarApi)


with open('partsoverlap.json', 'w') as f:
    json.dump(data, f)
f.close()

# Create map object
pd.options.mode.chained_assignment = None
m = folium.Map(location=[19.0447, 72.9103], zoom_start=13)


# Geojson Data
overlay = os.path.join('', 'M-ward-parts(W).json')
overlay3 = os.path.join('', 'M-ward-parts(E).json')

overlay2 = os.path.join('', 'partsoverlap.json')

# csv for m ward west population
Chedda_Nagar = pd.read_csv("CheddaNagar.csv").dropna(how='all')


Tilak_Nagar = pd.read_csv("TilakNagar.csv").dropna(how='all')


Sindhi_Society = pd.read_csv("SIndhiSociety.csv").dropna(how='all')


Chembur_West = pd.read_csv("Chembur_west.csv").dropna(how='all')

Deonar = pd.read_csv("Deonar.csv").dropna(how='all')


Mahul_E = pd.read_csv("MahulApi.csv").dropna(how='all')


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
Cheeta_camp = pd.read_csv("CheetaCampApi.csv").dropna(how='all')


chembur_east = pd.read_csv("ChemburE.csv").dropna(how='all')


govandi_east = pd.read_csv("GovandiE.csv").dropna(how='all')


shivaji_nagar = pd.read_csv("ShivajiNagar.csv").dropna(how='all')


trombay = pd.read_csv("TrombayApi.csv").dropna(how='all')

Anushakti = pd.read_csv("AnushaktiApi.csv").dropna(how='all')

mankhud_west = pd.read_csv("MankhurdWest.csv").dropna(how='all')

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

df_row = pd.concat([CheddaApi, ChemburWApi, MahulApi, TilakApi, SindhiApi])
df_row2 = pd.concat([SindhiApi, TilakApi, Cheeta_campApi, DeonarApi])

df_row3 = pd.concat([chembur_eastApi, govandi_eastApi, shivaji_nagarApi,
                     trombayApi, AnushaktiApi, mankhud_westApi, Cheeta_campApi, DeonarApi])

##################

# csv for m ward west
Chedda_Nagar = pd.read_csv("demographic/dchedda.csv").dropna(how='all')


Tilak_Nagar = pd.read_csv("demographic/dtilak.csv").dropna(how='all')


Sindhi_Society = pd.read_csv("demographic/dsindhi.csv").dropna(how='all')


Chembur_West = pd.read_csv("demographic/dche_w.csv").dropna(how='all')

Deonar = pd.read_csv("demographic/ddeonar.csv").dropna(how='all')


Mahul_E = pd.read_csv("demographic/dmahul.csv").dropna(how='all')


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
Cheeta_camp = pd.read_csv("demographic/dcheeta.csv").dropna(how='all')


chembur_east = pd.read_csv("demographic/dchem_e.csv").dropna(how='all')


govandi_east = pd.read_csv("demographic/dgovandi.csv").dropna(how='all')


shivaji_nagar = pd.read_csv("demographic/dshivaji.csv").dropna(how='all')


trombay = pd.read_csv("demographic/dtrombay.csv").dropna(how='all')

Anushakti = pd.read_csv("demographic/danu.csv").dropna(how='all')

mankhud_west = pd.read_csv("demographic/dmankhud.csv").dropna(how='all')

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

#############
df_rowde = pd.concat([CheddaApi, ChemburWApi, MahulApi, TilakApi, SindhiApi])
df_row2de = pd.concat([SindhiApi, TilakApi, Cheeta_campApi, DeonarApi])

df_row3de = pd.concat([chembur_eastApi, govandi_eastApi, shivaji_nagarApi,
                       trombayApi, AnushaktiApi, mankhud_westApi, DeonarApi, Cheeta_campApi])

#########
# colormap = branca.colormap.linear.YlOrRd_09.scale(0, 500)
# colormap = colormap.to_step(index=[0, 50, 100, 150, 200, 300, 400, 500])
# colormap.caption = 'Air Quality Index of M-ward West'
# colormap.add_to(m)

#######
df = pd.read_csv('demographic\health.csv')
df.head()
#######
choropleth = folium.Choropleth(
    geo_data=overlay,
    data=df_row,
    columns=['name', 'AQI'],
    name='MAP AQI-WEST',
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
    name='MAP AQI-EAST',
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
    name='MAP AQI-OVERLAPPING REGIONS',
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

# population
choroplethh = folium.Choropleth(
    geo_data=overlay,
    data=df_rowde,
    columns=['name', 'Population'],
    name='POPULATION M-WARD WEST',
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    show=False,
    fill_opacity=0.7,
    legend_name='Population In M-Ward',
    highlight=False

).add_to(m)

choropleth2i = folium.Choropleth(
    geo_data=overlay3,
    data=df_row3de,
    columns=['name', 'Population'],
    name='POPULATION M-WARD EAST',
    key_on='feature.properties.name',
    fill_color='YlOrRd',

    fill_opacity=0.7,
    show=False,
    highlight=False



)
for key in choropleth2i._children:
    if key.startswith('color_map'):
        del(choropleth2i._children[key])
choropleth2i.add_to(m)


def style_function(x): return {'interactive': False, 'layer': hide}


choropleth3i = folium.Choropleth(
    geo_data=overlay2,
    data=df_row2de,
    columns=['name', 'Population'],
    name='POPULATION M-WARD OVERLAPPING REGIONS',
    key_on='feature.properties.name',
    fill_color='YlOrRd',
    style_function=style_function,
    fill_opacity=0.7,
    show=False,
    highlight=False


)

for key in choropleth3i._children:
    if key.startswith('color_map'):
        del(choropleth3i._children[key])
choropleth3i.add_to(m)
################################################


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


choropleth2i.geojson.add_child(
    folium.features.GeoJsonTooltip(['name', 'Population'], labels=True)
)
choroplethh.geojson.add_child(
    folium.features.GeoJsonTooltip(['name', 'Population'], labels=True)
)
choropleth3i.geojson.add_child(
    folium.features.GeoJsonTooltip(['name', 'Population'], labels=True)
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

m.save('map.html')
