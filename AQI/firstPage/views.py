from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import datetime
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import RandomForestRegressor
import emoji
from statsmodels.tsa.stattools import adfuller
from pmdarima import auto_arima
from statsmodels.tsa.arima_model import ARIMA

pd.options.mode.chained_assignment = None


# Geojson Data


# csv for m ward west
Chedda_Nagar = pd.read_csv("Data\AQI DATA NEW\CheddaNagar.csv")

Chedda_Nagar = Chedda_Nagar.dropna(how='all')
Tilak_Nagar = pd.read_csv("Data\AQI DATA NEW\TilakNagar.csv")

Tilak_Nagar = Tilak_Nagar.dropna(how='all')
Sindhi_Society = pd.read_csv("Data\AQI DATA NEW\SIndhiSociety.csv")

Sindhi_Society = Sindhi_Society.dropna(how='all')
Chembur_West = pd.read_csv("Data\AQI DATA NEW\Chembur_west.csv")
Chembur_West = Chembur_West.dropna(how='all')
Deonar = pd.read_csv("Data\AQI DATA NEW\Deonar.csv")

Deonar = Deonar.dropna(how='all')
Mahul_E = pd.read_csv("Data\AQI DATA NEW\MahulApi.csv")

Mahul_E = Mahul_E.dropna(how='all')
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


# m ward east
Cheeta_camp = pd.read_csv("Data\AQI DATA NEW\CheetaCampApi.csv")
Cheeta_camp = Cheeta_camp.dropna(how='all')

chembur_east = pd.read_csv("Data\AQI DATA NEW\ChemburE.csv")

chembur_east = chembur_east.dropna(how='all')
govandi_east = pd.read_csv("Data\AQI DATA NEW\GovandiE.csv")

govandi_east = govandi_east.dropna(how='all')
shivaji_nagar = pd.read_csv("Data\AQI DATA NEW\ShivajiNagar.csv")

shivaji_nagar = shivaji_nagar.dropna(how='all')
trombay = pd.read_csv("Data\AQI DATA NEW\TrombayApi.csv")
trombay = trombay.dropna(how='all')
Anushakti = pd.read_csv("Data\AQI DATA NEW\AnushaktiApi.csv")

Anushakti = Anushakti.dropna(how='all')

mankhud_west = pd.read_csv("Data\AQI DATA NEW\MankhurdWest.csv")
mankhud_west = mankhud_west.dropna(how='all')
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

df_row = pd.concat([CheddaApi, SindhiApi, TilakApi,
                    ChemburWApi, DeonarApi, MahulApi])

df_row2 = pd.concat([chembur_eastApi, Cheeta_campApi, govandi_eastApi,
                     shivaji_nagarApi, trombayApi, AnushaktiApi, mankhud_westApi])

df_total = pd.concat([df_row, df_row2])


def index(request):
    # Ml prediction
    # mwest
    train = df_row
    train = train.fillna(0)
    m1 = RandomForestRegressor()
    train1 = train.drop(['AQI', 'Date', 'name'], axis=1)
    # print(train1)
    v1 = train1["O3"].mean()
    v2 = train1["PM2.5"].mean()
    v3 = train1["PM10"].mean()
    target = train['AQI']
    m1.fit(train1, target)
    m1.score(train1, target) * 100
    m1.predict([[v1, v2, v3]])
    m2 = AdaBoostRegressor()
    m2.fit(train1, target)
    m2.score(train1, target)*100
    AQIW = m2.predict([[v1, v2, v3]])
    AQIW_W = round(AQIW[0], 2)
    # ml ends

    message_west = gettext(AQIW_W)
    # East pred
    # meast
    train = df_row2
    train = train.fillna(0)
    m1 = RandomForestRegressor()
    train1 = train.drop(['AQI', 'Date', 'name'], axis=1)
    # print(train1)
    v1 = train1["O3"].mean()
    v2 = train1["PM2.5"].mean()
    v3 = train1["PM10"].mean()
    target = train['AQI']
    m1.fit(train1, target)
    m1.score(train1, target) * 100
    m1.predict([[v1, v2, v3]])
    m2 = AdaBoostRegressor()
    m2.fit(train1, target)
    m2.score(train1, target)*100
    AQIW = m2.predict([[v1, v2, v3]])
    AQIW_E = round(AQIW[0], 2)

    # meast ends
    message_east = gettext(AQIW_E)
    mwardwest = df_row
    mwardeast = df_row2
    uniquewest = pd.unique(mwardwest['name'])
    overallCountminwest = df_row['AQI'].min()
    overallCountmineast = df_row2['AQI'].min()
    maxVal_west = df_row['AQI'].max()
    maxVal_east = df_row2['AQI'].max()

    unique_east = pd.unique(mwardeast['name'])

    # getcolor
    color_west = getcolor(AQIW_W)
    color_east = getcolor(AQIW_E)

    # getemoji
    emoji_west = getemoji(AQIW_W)
    emoji_east = getemoji(AQIW_E)

    # gettext2
    text2_W = gettext2(AQIW_W)
    text2_E = gettext2(AQIW_E)

    # getimg
    img_W = getimg(AQIW_W)
    img_E = getimg(AQIW_E)

    wast_west_n, countsVal_west, logVals, dataForMapGraph, wast_east_n, countsVal_east = getBarData(
        mwardwest, uniquewest)
    # dataForheatMap,dateCat=getHeatMapData(mwardwest,wast_west_n)
    # datasetForLine,axisvalues=getLinebarGroupData(mwardwest,uniquewest)
    context = {'img_W': img_W, 'img_E': img_E, 'text2_W': text2_W, 'text2_E': text2_E, 'emoji_west': emoji_west, 'emoji_east': emoji_east, 'color_west': color_west, 'color_east': color_east, 'message_east': message_east, 'message_west': message_west, 'AQIW': AQIW_W, 'AQIE': AQIW_E, 'uniquewest': uniquewest, 'wast_west_n': wast_west_n, 'countsVal_west': countsVal_west, 'logVals': logVals, 'maxVal_east': maxVal_east,
               'maxVal_west': maxVal_west, 'overallCountminwest': overallCountminwest, 'overallCountmineast': overallCountmineast, 'wast_east_n': wast_east_n, 'countsVal_east': countsVal_east}
    return render(request, 'index.html', context)


def getBarData(mwardwest, uniquewest):
    df2 = df_row[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df3 = df_row2[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df2.columns = ['AQI', 'name']
    df2 = df2.sort_values(by='AQI', ascending=False)
    wast_west_n = list(df2['name'].values)
    countsVal_west = list(df2['AQI'].values)

    df3.columns = ['AQI', 'name']
    df3 = df3.sort_values(by='AQI', ascending=False)
    wast_east_n = list(df3['name'].values)
    countsVal_east = list(df3['AQI'].values)

    logVals = list(np.log(ind) if ind != 0 else 0 for ind in countsVal_west)
    dataForMapGraph = getDataforMap(uniquewest, df2)
    # dictVal=[]
    # for i in range(df2.shape[0]):
    #     dictVal.append(dict(df2.ix[i]))
    return (wast_west_n, countsVal_west, logVals, dataForMapGraph, wast_east_n, countsVal_east)


def getLinebarGroupData(mwardwest, uniquewest):
    colNames = mwardwest.columns[4:-1]
    datasetsForLine = []
    for i in uniquewest:
        temp = {}
        temp['label'] = i
        temp['fill'] = 'false'
        temp['data'] = mwardwest[mwardwest['Country/Region']
                                 == i][colNames].sum().values.tolist()
        datasetsForLine.append(temp)
    return datasetsForLine, list(range(len(colNames)))


def getDataforMap(uniqueName_region, df2):
    dataForMap = []
    for i in uniqueName_region:
        try:
            tempdf = df3[df3['name'] == i]
            temp = {}
            temp["code3"] = list(tempdf['code3'].values)[0]
            temp["name"] = i
            temp["value"] = df2[df2['Country/Region'] == i]['values'].sum()
            temp["code"] = list(tempdf['code'].values)[0]
            dataForMap.append(temp)
        except:
            pass
    print(len(dataForMap))
    return dataForMap


def drillDownACountry(request):
    print(request.POST.dict())
    Name_region = request.POST.get('Name_region')
    if(Name_region == "Chedda-Nagar"):
        indi = Chedda_Nagar
    if(Name_region == "Tilak-Nagar"):
        indi = Tilak_Nagar
    if(Name_region == "Sindhi-Society"):
        indi = Sindhi_Society
    if(Name_region == "Chembur-West"):
        indi = Chembur_West
    if(Name_region == "Deonar"):
        indi = Deonar
    if(Name_region == "Mahul"):
        indi = Mahul_E
    if(Name_region == "Cheeta-Camp"):
        indi = Cheeta_camp
    if(Name_region == "Chembur-East"):
        indi = chembur_east
    if(Name_region == "Govandi"):
        indi = govandi_east
    if(Name_region == "Shivaji-Nagar"):
        indi = shivaji_nagar
    if(Name_region == "Trombay"):
        indi = trombay
    if(Name_region == "Anushakti"):
        indi = Anushakti
    if(Name_region == "Mankhurd"):
        indi = mankhud_west
    train = indi
    train = train.dropna()
    train.set_index('Date', inplace=True)
    train.index = pd.DatetimeIndex(train.index).to_period('D')

    model = ARIMA(train['AQI'], order=(1, 0, 0))
    model = model.fit()
    start = len(train)
    end = len(train)+6
    pred = model.predict(start=start, end=end,
                         typ='levels').rename('ARIMA Predictions')

    daypredict = pred.index.to_series().astype(str)
    aqipredict = pred.values
    aqipredict = aqipredict.astype(int)
    aqipredict = list(aqipredict)
    predcol = getpredcolor(aqipredict)
    predemj = getpredemoj(aqipredict)

    # day predict
    newdates = []
    for date in daypredict:
        newdates.append(datetime.datetime.strptime(
            date, '%Y-%m-%d').strftime('%d/%m/%y'))
    daypredicts = []
    for day in daypredict:
        daypredicts.append(datetime.datetime.strptime(
            day, '%Y-%m-%d').strftime('%A'))

    indi = indi[list(indi.columns[0:4])+list([indi.columns[-1]])]
    indi.columns = ['Date', 'O3', 'PM2.5', 'PM10', 'AQI']
    indidate = list(indi['Date'].values)
    indidata = list(indi['AQI'].values)

    mwardwest = df_row
    mwardeast = df_row2
    uniquewest = pd.unique(mwardwest['name'])
    overallCountminwest = df_row['AQI'].min()
    overallCountmineast = df_row2['AQI'].min()
    maxVal_west = df_row['AQI'].max()
    maxVal_east = df_row2['AQI'].max()

    unique_east = pd.unique(mwardeast['name'])

    df2 = df_row[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df3 = df_row2[list(df_row.columns[4:5])+list([df_row.columns[-1]])]
    df2.columns = ['AQI', 'name']
    df2 = df2.sort_values(by='AQI', ascending=False)
    wast_west_n = list(df2['name'].values)
    countsVal_west = list(df2['AQI'].values)

    df3.columns = ['AQI', 'name']
    df3 = df3.sort_values(by='AQI', ascending=False)
    wast_east_n = list(df3['name'].values)
    countsVal_east = list(df3['AQI'].values)

    logVals = list(np.log(ind) if ind != 0 else 0 for ind in countsVal_west)

    context = context = {'predemj': predemj, 'predcol': predcol, 'newdates': newdates, 'daypredicts': daypredicts, 'aqipredict': aqipredict, 'Name_region': Name_region, 'indidate': indidate, 'indidata': indidata, 'uniquewest': uniquewest, 'wast_west_n': wast_west_n, 'countsVal_west': countsVal_west,
                         'maxVal_east': maxVal_east, 'maxVal_west': maxVal_west, 'overallCountminwest': overallCountminwest, 'overallCountmineast': overallCountmineast, 'wast_east_n': wast_east_n, 'countsVal_east': countsVal_east}

    return render(request, 'index2.html', context)


def gettext(AQIW):
    if AQIW >= 300:
        pool = "AQI exceeding 300 is highly unacceptable to human- can lead to premature death."
    elif AQIW >= 201 and AQIW < 300:
        pool = "Breathing polluted AQI may lead to chronic health issues."
    elif (AQIW >= 151 and AQIW < 201):
        pool = "Toxic air can provoke health difficulties expecially to the young kids and elderly people"
    elif (AQIW >= 101 and AQIW < 151):
        pool = "Poor air quality can affect health issues such as difficulty in breathing."
    elif (AQIW >= 51 and AQIW < 101):
        pool = "Acceptable air quality for a healthy adults but still pose threat to sensitive individual."
    else:
        pool = "People are no longer exposed to any health risk."
    return pool


def getcolor(AQIW):
    if AQIW >= 300:
        pool = "#800000"
    elif AQIW >= 201 and AQIW < 300:
        pool = "#9C27B0"
    elif (AQIW >= 151 and AQIW < 201):
        pool = "#f44336"
    elif (AQIW >= 101 and AQIW < 151):
        pool = "#FF9100"
    elif (AQIW >= 51 and AQIW < 101):
        pool = "#FFEA00"
    else:
        pool = "#00C853"
    return pool


def getemoji(AQIW):
    if AQIW >= 300:
        emoj = emoji.emojize(':skull:', use_aliases=True)

    elif AQIW >= 201 and AQIW < 300:
        emoj = emoji.emojize(':fearful_face:', use_aliases=True)

    elif (AQIW >= 151 and AQIW < 201):
        emoj = emoji.emojize(':face_with_medical_mask:', use_aliases=True)

    elif (AQIW >= 101 and AQIW < 151):
        emoj = emoji.emojize(':frowning_face:', use_aliases=True)

    elif (AQIW >= 51 and AQIW < 101):
        emoj = emoji.emojize(
            ':grinning_face_with_smiling_eyes:', use_aliases=True)

    else:
        emoj = emoji.emojize(':thumbsup:', use_aliases=True)

    return emoj


def getpredcolor(aqipredic):
    pool = []
    for x in aqipredic:
        if x >= 300:
            pool.append("radial-gradient(#cc0000, #800000)")

        elif x >= 201 and x < 300:
            pool.append("radial-gradient(#cc00cc, #660066)")

        elif (x >= 151 and x < 201):
            pool.append("radial-gradient(#ff6600, #cc0000)")

        elif (x >= 101 and x < 151):
            pool.append("radial-gradient(#ffcc66, #ff6600)")

        elif (x >= 51 and x < 101):
            pool.append("radial-gradient(#ffff66, #ffcc00)")

        else:
            pool.append("radial-gradient(#00ff99, #66ff33)")
    return pool


def getpredemoj(aqipredic):
    emo = []
    for x in aqipredic:
        if x >= 300:
            emoj = emoji.emojize(':skull:', use_aliases=True)
            emo.append(emoj)
        elif x >= 201 and x < 300:
            emoj = emoji.emojize(':fearful_face:', use_aliases=True)
            emo.append(emoj)

        elif (x >= 151 and x < 201):
            emoj = emoji.emojize(':face_with_medical_mask:', use_aliases=True)
            emo.append(emoj)

        elif (x >= 101 and x < 151):
            emoj = emoji.emojize(':frowning_face:', use_aliases=True)
            emo.append(emoj)

        elif (x >= 51 and x < 101):
            emoj = emoji.emojize(
                ':grinning_face_with_smiling_eyes:', use_aliases=True)
            emo.append(emoj)
        else:
            emoj = emoji.emojize(':thumbsup:', use_aliases=True)
            emo.append(emoj)
    return emo


def gettext2(AQIW):
    if AQIW >= 300:
        pool = "Hazardous"
    elif AQIW >= 201 and AQIW < 300:
        pool = "Severe"
    elif (AQIW >= 151 and AQIW < 201):
        pool = "Unhealthy"
    elif (AQIW >= 101 and AQIW < 151):
        pool = "Poor"
    elif (AQIW >= 51 and AQIW < 101):
        pool = "Moderate"
    else:
        pool = "Good"
    return pool


def getimg(AQIW):
    if AQIW >= 300:
        pool = "aqi-6.png"
    elif AQIW >= 201 and AQIW < 300:
        pool = "aqi-5.png"
    elif (AQIW >= 151 and AQIW < 201):
        pool = "aqi-4.png"
    elif (AQIW >= 101 and AQIW < 151):
        pool = "aqi-3.png"
    elif (AQIW >= 51 and AQIW < 101):
        pool = "aqi-2.png"
    else:
        pool = "aqi-1.png"
    return pool
