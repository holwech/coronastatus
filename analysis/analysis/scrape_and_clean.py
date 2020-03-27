import pandas as pd
import requests
import zipfile
import re
import os
import glob
import pandas as pd
import stats
import json
import plots

confirmed = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', stream=True)
deaths = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', stream=True)

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

confirmed = pd.read_csv('datasets/confirmed_transposed.csv', index_col=0)
deaths = pd.read_csv('datasets/deaths_transposed.csv', index_col=0)

data = {
    'stats': {},
    'plots': {}
}

fig = plots.confirmed_cases_over_threshold(confirmed)
data['plots']['figure_1'] = fig.to_json()

fig = plots.countries_deaths_over_threshold(deaths)
data['plots']['figure_2'] = fig.to_json()

fig = plots.top_countries_deaths_over_threshold_and_aligned(deaths)
data['plots']['figure_3'] = fig.to_json()

fig = plots.deaths_over_threshold_and_aligned(deaths)
data['plots']['figure_4'] = fig.to_json()

fig = plots.aligned_on_lockdown(deaths)
data['plots']['figure_5'] = fig.to_json()

fig = plots.deaths_area(deaths)
data['plots']['deaths_area'] = fig.to_json()

fig = plots.deaths_pie_chart(deaths)
data['plots']['deaths_pie_chart'] = fig.to_json()

fig = plots.daily_change(deaths)
data['plots']['daily_change'] = fig.to_json()

data['stats'] = stats.calc_stats(deaths)

with open('../../frontend/src/data/data.json', 'w') as f:
    json.dump(data, f)