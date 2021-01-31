from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
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
Cheeta_campApi['name'] = 'Cheetah-Camp'

chembur_eastApi = chembur_east.tail(1)
chembur_eastApi['name'] = 'Chembur-East'

govandi_eastApi = govandi_east.tail(1)
govandi_eastApi['name'] = 'Govandi'

shivaji_nagarApi = shivaji_nagar.tail(1)
shivaji_nagarApi['name'] = 'Shivaji-Nagar'

trombayApi = trombay.tail(1)
trombayApi['name'] = 'Trombay'

AnushaktiApi = Anushakti.tail(1)
AnushaktiApi['name'] = 'Ansuhakti'

mankhud_westApi = mankhud_west.tail(1)
mankhud_westApi['name'] = 'Mankhurd'

#################

df_row = pd.concat([CheddaApi,SindhiApi,TilakApi,ChemburWApi,DeonarApi,MahulApi]) 

df_row2=pd.concat([chembur_eastApi,Cheeta_campApi,govandi_eastApi,shivaji_nagarApi,trombayApi,AnushaktiApi,mankhud_westApi])

df_total=pd.concat([df_row,df_row2]) 

def index(request):
    mwardwest=df_row
    mwardeast=df_row2
    # deathGLobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    # recoverGlobal=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    uniquewest=pd.unique(mwardwest['name'])
    overallCountminwest=df_row['AQI'].min()
    overallCountmineast=df_row2['AQI'].min() 
    maxVal_west=df_row['AQI'].max()
    maxVal_east=df_row2['AQI'].max() 
    
    unique_east=pd.unique(mwardeast['name'])

    wast_west_n,countsVal_west,logVals,dataForMapGraph,wast_east_n,countsVal_east=getBarData(mwardwest,uniquewest)
    #dataForheatMap,dateCat=getHeatMapData(mwardwest,wast_west_n)
    #datasetForLine,axisvalues=getLinebarGroupData(mwardwest,uniquewest)
    context={'uniquewest':uniquewest,'wast_west_n':wast_west_n,'countsVal_west':countsVal_west,'logVals':logVals,'maxVal_east':maxVal_east,'maxVal_west':maxVal_west,'overallCountminwest':overallCountminwest,'overallCountmineast':overallCountmineast,'wast_east_n':wast_east_n,'countsVal_east':countsVal_east}
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

def getDataforMap(uniqueCOuntryName,df2):
    dataForMap=[]
    for i in uniqueCOuntryName:
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
    countryName=request.POST.get('countryName')
    mwardwest=pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    countryDataSpe=pd.DataFrame(mwardwest[mwardwest['Country/Region']==countryName][mwardwest.columns[4:-1]].sum()).reset_index()
    countryDataSpe.columns=['country','values']
    countryDataSpe['lagVal']=countryDataSpe['values'].shift(1).fillna(0)
    countryDataSpe['incrementVal']=countryDataSpe['values']-countryDataSpe['lagVal']
    countryDataSpe['rollingMean']=countryDataSpe['incrementVal'].rolling(window=4).mean()
    countryDataSpe=countryDataSpe.fillna(0)
    datasetsForLine=[{'yAxisID': 'y-axis-1','label':'Daily Cumulated Data','data':countryDataSpe['values'].values.tolist(),'borderColor':'#03a9fc','backgroundColor':'#03a9fc','fill':'false'},
                    {'yAxisID': 'y-axis-2','label':'Rolling Mean 4 days','data':countryDataSpe['rollingMean'].values.tolist(),'borderColor':'#fc5203','backgroundColor':'#fc5203','fill':'false'}]
    axisvalues=countryDataSpe.index.tolist()
    uniquewest=pd.unique(mwardwest['Country/Region'])
    wast_west_n,countsVal_west,logVals,overallCount,dataForMapGraph,maxVal=getBarData(mwardwest,uniquewest)
    dataForheatMap,dateCat=getHeatMapData(mwardwest,wast_west_n)
    context=context={"countryName":countryName,'axisvalues':axisvalues,'datasetsForLine':datasetsForLine,'dateCat':dateCat,'dataForheatMap':dataForheatMap,'maxVal':maxVal,'dataForMapGraph':dataForMapGraph,'uniquewest':uniquewest,'wast_west_n':wast_west_n,'countsVal_west':countsVal_west,'logVals':logVals,'overallCount':overallCount}

    return render(request,'index2.html',context)

