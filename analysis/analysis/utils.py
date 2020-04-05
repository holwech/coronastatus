import string
import random
import numpy as np
import pandas as pd

alphabets = [
    ['t', 'w', 'c', 'd', 'v', 'n', 's', 'l', 'x', 'f', 'j', 'k', 'b', 'g', 'r', 'h', 'z', 'p', 'y', 'm', 'a', 'i', 'o', 'e', 'u', 'q'],
    ['j', 'z', 'r', 's', 'c', 'm', 'p', 'q', 'w', 'u', 'v', 'd', 'l', 'e', 'h', 't', 'n', 'b', 'y', 'a', 'o', 'i', 'k', 'x', 'g', 'f'],
    ['d', 'p', 'x', 'm', 'r', 'b', 'n', 'u', 't', 'o', 'q', 'j', 's', 'a', 'w', 'g', 'e', 'i', 'y', 'v', 'l', 'h', 'c', 'z', 'k', 'f']
]

def get_color(column, i=0, limit=2000, shift=0):
  if (i > limit or column is 'Other'):
    return 'rgb(150,150,150)', False
  r = min(round(alphabets[0].index(column.lower()[0]) / 25 * 255) + shift, 255)
  g = min(round(alphabets[1].index(column.lower()[1]) / 25 * 255) + shift, 255)
  b = 150
  if (len(column) > 2 and column[3] != ' '):
    b = min(round(alphabets[2].index(column.lower()[3]) / 25 * 255) + shift, 255)
  return f'rgb({r},{g},{b})', True

def sort_columns_on_row(df, index=-1):
  sorted_indicies = (-df.loc[df.index[index]]).argsort()
  return df[df.columns[sorted_indicies]]

def over_threshold(df, threshold, index=-1):
  mask = (df.iloc[index] > threshold).index[df.iloc[index] > threshold]
  over_threshold = df[mask]
  return sort_columns_on_row(over_threshold, index)

def shuffled_alphabet():
  alphabets = [list(string.ascii_lowercase), list(string.ascii_lowercase), list(string.ascii_lowercase)]
  for alphabet in alphabets:
    random.shuffle(alphabet)
  return alphabets

def get_from_first_occurrence(df, country, above_value):
  above = df[country][df[country] > above_value]
  return np.arange(0, len(above)), above.values

def align_series(series, lockdown, latest_lockdown):
  delta = np.timedelta64(pd.to_datetime(latest_lockdown) - pd.to_datetime(lockdown), 'D')
  x = np.arange(0, delta + len(series)).astype(int)
  y = np.append(np.full((delta / np.timedelta64(1, 'D')).astype(int), None), series.values)
  return x, y

def bucket_values(df, limit=10, interval=1, include_other=True):
  if limit is None:
    limit = len(df.columns)
  df_out = df.iloc[:, :limit]
  if include_other and limit is not None:
    columns = np.append(np.array(['Other']), df_out.columns.values)
    df_out['Other'] = df.iloc[:, limit:].sum(axis=1)
    df_out = df_out[columns]
  df_buckets = pd.DataFrame([], columns=df_out.columns)
  date_ranges = []
  for i in range(len(df_out), 0, -interval):
      date_ranges.append([df_out.iloc[i - interval].name, df_out.iloc[i - 1].name])
      series = df_out.iloc[(i - interval):i].sum()
      series.name = df_out.iloc[i - interval].name
      df_buckets = df_buckets.append(series)
  return df_buckets.iloc[::-1]