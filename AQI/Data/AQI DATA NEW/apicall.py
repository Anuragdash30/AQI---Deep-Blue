import requests
from datetime import date 
from csv import writer 
from csv import DictWriter 
import json
import pandas as pd
today = date.today()
#chemburwest
r_Chembur_west = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0673&lon=72.9018&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_cw = ['Date','PM10','O3', 
               'PM2.5','AQI'] 
chembur_w = {}
chembur_w['Date']=today


for eachw in r_Chembur_west['data']['aqiParams']:
    if(eachw['name']=='O3'):
        chembur_w['O3']=eachw['aqi']
    if(eachw['name']=='PM2.5'):
        chembur_w['PM2.5']=eachw['aqi']
    if(eachw['name']=='PM10'):
        chembur_w['PM10']=eachw['aqi']
chembur_w['AQI'] = r_Chembur_west['data']['value']


with open('Chembur_west.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_cw) 
  
    
    dictwriter_object.writerow(chembur_w) 
  
   
    f_object.close()

#deonar    
r_Deonar = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0447&lon=72.9103&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_deo = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

Deonar = {}
Deonar['Date']=today


for eachd in r_Deonar['data']['aqiParams']:
    if(eachd['name']=='O3'):
        Deonar['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        Deonar['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        Deonar['PM10']=eachd['aqi']
Deonar['AQI'] = r_Deonar['data']['value']


with open('Deonar.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_deo) 
  
    
    dictwriter_object.writerow(Deonar) 
    f_object.close()

#tilaknagar
r_tilak = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0683&lon=72.8973&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_tilak = ['Date','O3', 
               'PM2.5','PM10','AQI'] 
print
tilak = {}
tilak['Date']=today


for eachd in r_tilak['data']['aqiParams']:
    if(eachd['name']=='O3'):
        tilak['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        tilak['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        tilak['PM10']=eachd['aqi']
tilak['AQI'] = r_tilak['data']['value']


with open('TilakNagar.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_tilak) 
  
    
    dictwriter_object.writerow(tilak) 
  
   
    f_object.close()
    

#govandi
r_govandi = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0535&lon=72.9239&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_govandi = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

govandi = {}
govandi['Date']=today


for eachd in r_govandi['data']['aqiParams']:
    if(eachd['name']=='O3'):
        govandi['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        govandi['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        govandi['PM10']=eachd['aqi']
govandi['AQI'] = r_govandi['data']['value']


with open('GovandiE.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_govandi) 
  
    
    dictwriter_object.writerow(govandi) 
  
   
    f_object.close()

#shivajinagar
r_ShivajiNagar = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.06432699351229&lon=72.9253193501495&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_ShivajiNagar = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

ShivajiNagar = {}
ShivajiNagar['Date']=today


for eachd in r_ShivajiNagar['data']['aqiParams']:
    if(eachd['name']=='O3'):
        ShivajiNagar['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        ShivajiNagar['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        ShivajiNagar['PM10']=eachd['aqi']
ShivajiNagar['AQI'] = r_ShivajiNagar['data']['value']


with open('ShivajiNagar.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_ShivajiNagar) 
  
    
    dictwriter_object.writerow(ShivajiNagar) 
  
   
    f_object.close()
#chembur east
r_ChemburE = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0522&lon=72.9005&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_ChemburE = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

ChemburE = {}
ChemburE['Date']=today


for eachd in r_ChemburE['data']['aqiParams']:
    if(eachd['name']=='O3'):
        ChemburE['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        ChemburE['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        ChemburE['PM10']=eachd['aqi']
ChemburE['AQI'] = r_ChemburE['data']['value']


with open('ChemburE.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_ChemburE) 
  
    
    dictwriter_object.writerow(ChemburE) 
  
   
    f_object.close()

#chedda nagar
r_CheddaNagar = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.069200569679644&lon=72.9056944243479&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_CheddaNagar = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

CheddaNagar = {}
CheddaNagar['Date']=today


for eachd in r_CheddaNagar['data']['aqiParams']:
    if(eachd['name']=='O3'):
        CheddaNagar['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        CheddaNagar['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        CheddaNagar['PM10']=eachd['aqi']
CheddaNagar['AQI'] = r_CheddaNagar['data']['value']


with open('CheddaNagar.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_CheddaNagar) 
  
    
    dictwriter_object.writerow(CheddaNagar) 
  
   
    f_object.close()

#SIndhiSociety
r_SIndhiSociety = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0511&lon=72.8907&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_SIndhiSociety = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

SIndhiSociety = {}
SIndhiSociety['Date']=today


for eachd in r_SIndhiSociety['data']['aqiParams']:
    if(eachd['name']=='O3'):
        SIndhiSociety['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        SIndhiSociety['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        SIndhiSociety['PM10']=eachd['aqi']
SIndhiSociety['AQI'] = r_SIndhiSociety['data']['value']


with open('SIndhiSociety.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_SIndhiSociety) 
  
    
    dictwriter_object.writerow(SIndhiSociety) 
  
   
    f_object.close()

#trombay
r_TrombayApi = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0093&lon=72.8984&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_TrombayApi = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

TrombayApi = {}
TrombayApi['Date']=today


for eachd in r_TrombayApi['data']['aqiParams']:
    if(eachd['name']=='O3'):
        TrombayApi['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        TrombayApi['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        TrombayApi['PM10']=eachd['aqi']
TrombayApi['AQI'] = r_TrombayApi['data']['value']


with open('TrombayApi.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_TrombayApi) 
  
    
    dictwriter_object.writerow(TrombayApi) 
  
   
    f_object.close()

#cheetahcamp
r_CheetaCampApi = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0511&lon=72.9486&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_CheetaCampApi = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

CheetaCampApi = {}
CheetaCampApi['Date']=today


for eachd in r_CheetaCampApi['data']['aqiParams']:
    if(eachd['name']=='O3'):
        CheetaCampApi['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        CheetaCampApi['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        CheetaCampApi['PM10']=eachd['aqi']
CheetaCampApi['AQI'] = r_CheetaCampApi['data']['value']


with open('CheetaCampApi.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_CheetaCampApi) 
  
    
    dictwriter_object.writerow(CheetaCampApi) 
  
   
    f_object.close()
#anushakti nagar
r_AnushaktiApi = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.0385&lon=72.9232&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_AnushaktiApi = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

AnushaktiApi = {}
AnushaktiApi['Date']=today


for eachd in r_AnushaktiApi['data']['aqiParams']:
    if(eachd['name']=='O3'):
        AnushaktiApi['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        AnushaktiApi['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        AnushaktiApi['PM10']=eachd['aqi']
AnushaktiApi['AQI'] = r_AnushaktiApi['data']['value']


with open('AnushaktiApi.csv', 'a') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_AnushaktiApi) 
  
    
    dictwriter_object.writerow(AnushaktiApi) 
  
   
    f_object.close()

#mahul 
r_MahulApi = requests.get('http://api.airpollutionapi.com/1.0/aqi?lat=19.033708690103797&lon=72.89618102619643&APPID=up223na4hk0hug72bk2fd8fdr3' ).json()
field_names_MahulApi = ['Date','O3', 
               'PM2.5','PM10','AQI'] 

MahulApi = {}
MahulApi['Date']=today


for eachd in r_MahulApi['data']['aqiParams']:
    if(eachd['name']=='O3'):
        MahulApi['O3']=eachd['aqi']
    if(eachd['name']=='PM2.5'):
        MahulApi['PM2.5']=eachd['aqi']
    if(eachd['name']=='PM10'):
        MahulApi['PM10']=eachd['aqi']
MahulApi['AQI'] = r_MahulApi['data']['value']


with open('MahulApi.csv', 'a',newline='') as f_object: 
      
   
    dictwriter_object = DictWriter(f_object, fieldnames=field_names_MahulApi) 
  
    
    dictwriter_object.writerow(MahulApi) 
  
   
    f_object.close()

##############################
Chedda_Nagar = pd.read_csv("CheddaNagar.csv")


Tilak_Nagar = pd.read_csv("TilakNagar.csv")


Sindhi_Society = pd.read_csv("SIndhiSociety.csv")


Chembur_West =  pd.read_csv("Chembur_west.csv")

Deonar =  pd.read_csv("Deonar.csv")


Mahul_E = pd.read_csv("MahulApi.csv")


CheddaApi = Chedda_Nagar['AQI'].iloc[-1]


DeonarApi = Deonar['AQI'].iloc[-1]


TilakApi = Tilak_Nagar['AQI'].iloc[-1]

SindhiApi = Sindhi_Society['AQI'].iloc[-1]

ChemburWApi = Chembur_West['AQI'].iloc[-1]

MahulApi = Mahul_E['AQI'].iloc[-1]





################# m ward east
Cheeta_camp = pd.read_csv("CheetaCampApi.csv")


chembur_east = pd.read_csv("ChemburE.csv")


govandi_east = pd.read_csv("GovandiE.csv")


shivaji_nagar =  pd.read_csv("ShivajiNagar.csv")


trombay = pd.read_csv("TrombayApi.csv")

Anushakti = pd.read_csv("AnushaktiApi.csv")

mankhud_west = pd.read_csv("MankhurdWest.csv")

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
    if item['properties']['name']== 'Trombay':
        item['properties']['AQI'] = int(trombayApi)
    if item['properties']['name']== 'Ansuhakti Nagar':
        item['properties']['AQI'] = int(AnushaktiApi)
    if item['properties']['name']== 'Mankhurd':
        item['properties']['AQI'] = int(mankhud_westApi)
    if item['properties']['name']== 'Chembur-east':
        item['properties']['AQI'] = int(chembur_eastApi)
    if item['properties']['name']== 'Govandi':
        item['properties']['AQI'] = int(govandi_eastApi)
    if item['properties']['name']== 'Shivaji Nagar':
        item['properties']['AQI'] = int(shivaji_nagarApi)
    

with open('M-ward-parts(E).json', 'w') as f:
    json.dump(data, f)
f.close()


with open('M-ward-parts(W).json') as f:
    data = json.load(f)

for item in data['features']:
    if item['properties']['name']== 'Chedda nagar':
        item['properties']['AQI'] = int(CheddaApi)
    if item['properties']['name']== 'Chembur-west':
        item['properties']['AQI'] = int(ChemburWApi)
    if item['properties']['name']== 'Mahul':
        item['properties']['AQI'] = int(MahulApi)
   
    

with open('M-ward-parts(W).json', 'w') as f:
    json.dump(data, f)
f.close()



with open('partsoverlap.json') as f:
    data = json.load(f)

for item in data['features']:
    if item['properties']['name']== 'Sindhi Society':
        item['properties']['AQI'] = int(SindhiApi)
    if item['properties']['name']== 'Tilak Nagar':
        item['properties']['AQI'] = int(TilakApi)
    if item['properties']['name']== 'Cheetah Camp':
        item['properties']['AQI'] = int(Cheeta_campApi)
    if item['properties']['name']== 'Deonar':
        item['properties']['AQI'] = int(DeonarApi)
   
    

with open('partsoverlap.json', 'w') as f:
    json.dump(data, f)
f.close()
