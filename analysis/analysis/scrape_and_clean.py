import pandas as pd
import stats
import json
import plots

def transpose(df):
    df = df.groupby(['Country/Region']).sum()
    df = df.drop(['Lat', 'Long'], axis=1)
    return df.transpose()

confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

deaths = transpose(deaths)
confirmed = transpose(confirmed)

data = {
    'plots': {},
    'stats': {}
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

fig = plots.daily_change(deaths, 3)
data['plots']['daily_change'] = fig.to_json()

fig = plots.daily_change(deaths.loc[pd.to_datetime(deaths.index) >= pd.to_datetime('2020-03-01')], 1)
data['plots']['daily_change2'] = fig.to_json()

data['stats'] = stats.calc_stats(deaths)

with open('frontend/src/data/data.json', 'w') as f:
    json.dump(data, f)