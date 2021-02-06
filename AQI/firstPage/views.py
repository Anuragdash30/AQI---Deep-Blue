from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostRegressor 
from sklearn.ensemble import RandomForestRegressor

# Create your views here.
df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')
pd.options.mode.chained_assignment = None


# Geojson Data 


#csv for m ward west
Chedda_Nagar = pd.read_csv("Data\AQI DATA NEW\CheddaNagar.csv")

Chedda_Nagar=Chedda_Nagar.dropna(how = 'all')
Tilak_Nagar = pd.read_csv("Data\AQI DATA NEW\TilakNagar.csv")

Tilak_Nagar=Tilak_Nagar.dropna(how = 'all')
Sindhi_Society = pd.read_csv("Data\AQI DATA NEW\SIndhiSociety.csv")

Sindhi_Society=Sindhi_Society.dropna(how = 'all')
Chembur_West =  pd.read_csv("Data\AQI DATA NEW\Chembur_west.csv")
Chembur_West=Chembur_West.dropna(how = 'all')
Deonar =  pd.read_csv("Data\AQI DATA NEW\Deonar.csv")

Deonar=Deonar.dropna(how = 'all')
Mahul_E = pd.read_csv("Data\AQI DATA NEW\MahulApi.csv")

Mahul_E=Mahul_E.dropna(how = 'all')
CheddaApi = Chedda_Nagar.tail(1)
CheddaApi['name'] = 'Chedda-Nagar'

DeonarApi = Deonar.tail(1)
DeonarApi['name'] = 'Deonar'

TilakApi = Tilak_Nagar.tail(1)
TilakApi['name'] = 'Tilak-Nagar'
SindhiApi = Sindhi_Society.tail(1)
SindhiApi['name'] = 'Sindhi-Society'
ChemburWApi = Chembur_West.tail(1)
ChemburWApi['name'] = 'Chembur-West'
MahulApi = Mahul_E.tail(1)
MahulApi['name'] = 'Mahul'




################# m ward east
Cheeta_camp = pd.read_csv("Data\AQI DATA NEW\CheetaCampApi.csv")
Cheeta_camp=Cheeta_camp.dropna(how = 'all')

chembur_east = pd.read_csv("Data\AQI DATA NEW\ChemburE.csv")

chembur_east=chembur_east.dropna(how = 'all')
govandi_east = pd.read_csv("Data\AQI DATA NEW\GovandiE.csv")

govandi_east=govandi_east.dropna(how = 'all')
shivaji_nagar =  pd.read_csv("Data\AQI DATA NEW\ShivajiNagar.csv")

shivaji_nagar=shivaji_nagar.dropna(how = 'all')
trombay = pd.read_csv("Data\AQI DATA NEW\TrombayApi.csv")
trombay=trombay.dropna(how = 'all')
Anushakti = pd.read_csv("Data\AQI DATA NEW\AnushaktiApi.csv")

Anushakti=Anushakti.dropna(how = 'all')

mankhud_west = pd.read_csv("Data\AQI DATA NEW\MankhurdWest.csv")
mankhud_west=mankhud_west.dropna(how = 'all')
Cheeta_campApi = Cheeta_camp.tail(1)
Cheeta_campApi['name'] = 'Cheeta-Camp'

chembur_eastApi = chembur_east.tail(1)
chembur_eastApi['name'] = 'Chembur-East'

govandi_eastApi = govandi_east.tail(1)
govandi_eastApi['name'] = 'Govandi'

shivaji_nagarApi = shivaji_nagar.tail(1)
shivaji_nagarApi['name'] = 'Shivaji-Nagar'

trombayApi = trombay.tail(1)
trombayApi['name'] = 'Trombay'

AnushaktiApi = Anushakti.tail(1)
AnushaktiApi['name'] = 'Anushakti'

mankhud_westApi = mankhud_west.tail(1)
mankhud_westApi['name'] = 'Mankhurd'

#################

df_row = pd.concat([CheddaApi,SindhiApi,TilakApi,ChemburWApi,DeonarApi,MahulApi]) 

df_row2=pd.concat([chembur_eastApi,Cheeta_campApi,govandi_eastApi,shivaji_nagarApi,trombayApi,AnushaktiApi,mankhud_westApi])

df_total=pd.concat([df_row,df_row2]) 

def index(request):
    # Ml prediction
    train=df_row
    train=train.fillna(0)
    m1 = RandomForestRegressor() 
    train1 = train.drop(['AQI','Date','name'], axis=1) 
    target = train['AQI']
    m1.fit(train1, target) 
    m1.score(train1, target) * 100
    m1.predict([[49,301,205]])
    m2 = AdaBoostRegressor()
    m2.fit(train1, target)
    m2.score(train1, target)*100
    AQIW=m2.predict([[49,301,205]])
    AQIW_W=AQIW[0]
    #ml ends
    mwardwest=df_row
    mwardeast=df_row2
    uniquewest=pd.unique(mwardwest['name'])
    overallCountminwest=df_row['AQI'].min()
    overallCountmineast=df_row2['AQI'].min() 
    maxVal_west=df_row['AQI'].max()
    maxVal_east=df_row2['AQI'].max() 
    
    unique_east=pd.unique(mwardeast['name'])

    wast_west_n,countsVal_west,logVals,dataForMapGraph,wast_east_n,countsVal_east=getBarData(mwardwest,uniquewest)
    #dataForheatMap,dateCat=getHeatMapData(mwardwest,wast_west_n)
    #datasetForLine,axisvalues=getLinebarGroupData(mwardwest,uniquewest)
    context={'AQIW':AQIW_W,'uniquewest':uniquewest,'wast_west_n':wast_west_n,'countsVal_west':countsVal_west,'logVals':logVals,'maxVal_east':maxVal_east,'maxVal_west':maxVal_west,'overallCountminwest':overallCountminwest,'overallCountmineast':overallCountmineast,'wast_east_n':wast_east_n,'countsVal_east':countsVal_east}
    return render(request,'index.html',context)
    

def getBarData(mwardwest,uniquewest):
    df2=df_row[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df3=df_row2[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df2.columns=['AQI','name']
    df2=df2.sort_values(by='AQI',ascending=False)
    wast_west_n=list(df2['name'].values)
    countsVal_west=list(df2['AQI'].values)

    df3.columns=['AQI','name']
    df3=df3.sort_values(by='AQI',ascending=False)
    wast_east_n=list(df3['name'].values)
    countsVal_east=list(df3['AQI'].values)

    
    
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal_west )
    dataForMapGraph=getDataforMap(uniquewest,df2)
    # dictVal=[]
    # for i in range(df2.shape[0]):
    #     dictVal.append(dict(df2.ix[i]))
    return (wast_west_n,countsVal_west,logVals,dataForMapGraph,wast_east_n,countsVal_east)

def getLinebarGroupData(mwardwest,uniquewest):
    colNames=mwardwest.columns[4:-1]
    datasetsForLine=[]
    for i in uniquewest:
        temp={}
        temp['label']=i
        temp['fill']='false'
        temp['data']=mwardwest[mwardwest['Country/Region']==i][colNames].sum().values.tolist()
        datasetsForLine.append(temp)
    return datasetsForLine,list(range(len(colNames)))

def getDataforMap(uniqueName_region,df2):
    dataForMap=[]
    for i in uniqueName_region:
        try:
            tempdf=df3[df3['name']==i]
            temp={}
            temp["code3"]=list(tempdf['code3'].values)[0]
            temp["name"]=i
            temp["value"]=df2[df2['Country/Region']==i]['values'].sum()
            temp["code"]=list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass
    print (len(dataForMap))
    return dataForMap





def drillDownACountry(request):
    print (request.POST.dict())
    Name_region=request.POST.get('Name_region')
    if(Name_region=="Chedda-Nagar"):
        indi = Chedda_Nagar
    if(Name_region=="Tilak-Nagar"):
        indi = Tilak_Nagar
    if(Name_region=="Sindhi-Society"):
        indi = Sindhi_Society
    if(Name_region=="Chembur-West"):
        indi = Chembur_West
    if(Name_region=="Deonar"):
        indi = Deonar
    if(Name_region=="Mahul"):
        indi = Mahul_E
    if(Name_region=="Cheeta-Camp"):
        indi = Cheeta_camp
    if(Name_region=="Chembur-East"):
        indi = chembur_east
    if(Name_region=="Govandi"):
        indi = govandi_east
    if(Name_region=="Shivaji-Nagar"):
        indi = shivaji_nagar
    if(Name_region=="Trombay"):
        indi = trombay
    if(Name_region=="Anushakti"):
        indi = Anushakti
    if(Name_region=="Mankhurd"):
        indi = mankhud_west
   
    indi=indi[list(indi.columns[0:4])+list([indi.columns[-1]])]
    indi.columns=['Date','O3','PM2.5','PM10','AQI']
    indidate=list(indi['Date'].values)
    indidata=list(indi['AQI'].values)
    
    mwardwest=df_row
    mwardeast=df_row2
    uniquewest=pd.unique(mwardwest['name'])
    overallCountminwest=df_row['AQI'].min()
    overallCountmineast=df_row2['AQI'].min() 
    maxVal_west=df_row['AQI'].max()
    maxVal_east=df_row2['AQI'].max() 
    
    unique_east=pd.unique(mwardeast['name'])
    
    df2=df_row[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df3=df_row2[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df2.columns=['AQI','name']
    df2=df2.sort_values(by='AQI',ascending=False)
    wast_west_n=list(df2['name'].values)
    countsVal_west=list(df2['AQI'].values)

    df3.columns=['AQI','name']
    df3=df3.sort_values(by='AQI',ascending=False)
    wast_east_n=list(df3['name'].values)
    countsVal_east=list(df3['AQI'].values)

    
    
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal_west )


    context=context={'Name_region':Name_region,'indidate':indidate,'indidata':indidata,'uniquewest':uniquewest,'wast_west_n':wast_west_n,'countsVal_west':countsVal_west,'maxVal_east':maxVal_east,'maxVal_west':maxVal_west,'overallCountminwest':overallCountminwest,'overallCountmineast':overallCountmineast,'wast_east_n':wast_east_n,'countsVal_east':countsVal_east}

    return render(request,'index2.html',context)

