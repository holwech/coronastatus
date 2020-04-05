import numpy as np
import pandas as pd
import utils
from datetime import date

def calc_stats(deaths, confirmed):
  stats = {}
  over_5_deaths = utils.over_threshold(deaths, 5)
  change = utils.sort_columns_on_row(over_5_deaths.diff())
  stats['deaths'] = over_5_deaths.iloc[-1].to_dict()
  stats['change_deaths'] = change.iloc[-1].to_dict()
  stats['num_countries_over_5_deaths'] = len(utils.over_threshold(deaths, 5).columns)
  stats['num_countries_over_5_deaths_change'] = len(utils.over_threshold(deaths, 5, -1).columns) - len(utils.over_threshold(deaths, 5, -2).columns)
  stats['num_countries_over_limit_confirmed'] = len(utils.over_threshold(confirmed, 500).columns)
  stats['num_countries_over_limit_confirmed_change'] = len(utils.over_threshold(confirmed, 500, -1).columns) - len(utils.over_threshold(confirmed, 500, -2).columns)
  stats['total_deaths'] = int(deaths.iloc[-1].sum())
  stats['total_deaths_change'] = int(deaths.iloc[-1].sum()) - int(deaths.iloc[-2].sum())
  stats['total_confirmed'] = int(confirmed.iloc[-1].sum())
  stats['total_confirmed_change'] = int(confirmed.iloc[-1].sum()) - int(confirmed.iloc[-2].sum())
  stats['last_updated'] = date.today().strftime('%Y-%m-%d')
  return stats