import pandas as pd
import requests
import zipfile
import re
import os
import glob
import pandas as pd

confirmed = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', stream=True)
deaths = requests.get('https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', stream=True)

def transpose(filename):
    df = pd.read_csv('datasets/' + filename + '.csv')
    df = df.groupby(['Country/Region']).sum()
    df = df.drop(['Lat', 'Long'], axis=1)
    df = df.transpose()
    df.to_csv('datasets/' + filename + '_transposed.csv')

prefix = 'datasets/'
with open(prefix + 'confirmed.csv', 'w', encoding='utf-8') as file:
    file.write(confirmed.text)
with open(prefix + 'deaths.csv', 'w', encoding='utf-8') as file:
    file.write(deaths.text)

transpose('confirmed')
transpose('deaths')