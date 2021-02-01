import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# import data csv here
<<<<<<< HEAD
Trombay = pd.read_csv("SIndhiSociety.csv")
Anushakti = pd.read_csv("Chembur_west.csv")
CheetaCamp = pd.read_csv("Deonar.csv")
=======
Trombay = pd.read_csv(
    r'AQI DATA NEW\TrombayApi.csv')
Anushakti = pd.read_csv(
    r'AQI DATA NEW\AnushaktiApi.csv')
CheetaCamp = pd.read_csv(
    r'AQI DATA NEW\CheetaCampApi.csv')
>>>>>>> 3b5776208d6ced166a2e6baff4c78630ad50356f

# Aqi column selected from all csv and date selected from any one of them
Api_date = Trombay['Date']
Trombay_Aqi = Trombay['AQI']
Anushakti_Aqi = Anushakti['AQI']
Cheeta_Aqi = CheetaCamp['AQI']

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 1.6, 1.6])
ax.plot(Api_date, Trombay_Aqi, 'r', lw=3, label='Trombay')
ax.plot(Api_date, Anushakti_Aqi, 'b', lw=3, label='Anushakti')
ax.plot(Api_date, Cheeta_Aqi, 'g', lw=3, label='CheetaCamp')
ax.legend()
ax.set_xlabel('Dates')
ax.set_ylabel('AQI')
ax.set_title('M-Ward AQI')
plt.show()
