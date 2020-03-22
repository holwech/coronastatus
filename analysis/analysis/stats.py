import numpy as np
import pandas as pd
import utils
from datetime import date

def calc_stats(deaths):
  stats = {}
  over_5_deaths = utils.over_threshold(deaths, 5)
  change = over_5_deaths.iloc[-1] - over_5_deaths.iloc[-2]
  stats['change_deaths'] = change.to_json()
  stats['num_countries_over_5_deaths'] = len(change)
  stats['total_deaths'] = int(deaths.iloc[-1].sum())
  stats['total_deaths_change'] = int(deaths.iloc[-1].sum()) - int(deaths.iloc[-2].sum())
  stats['last_updated'] = date.today().strftime('%Y-%m-%d')
  return stats