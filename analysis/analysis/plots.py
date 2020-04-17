import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import utils
from math import log

hubei_lockdown = '2020-01-23'
lombardy_lockdown = '2020-03-08'
spain_lockdown = '2020-03-14'
uk_lockdown = '2020-03-23'
norway_lockdown = '2020-03-12'
denmark_lockdown = '2020-03-14'
france_lockdown = '2020-03-17'

paper_bgcolor = 'rgba(0,0,0,0)'
plot_bgcolor='rgba(0,0,0,0)'

def confirmed_cases_over_threshold(confirmed):
  limit = 25
  confirmed = confirmed.assign(EU=confirmed[['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
    'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
    'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']].sum(axis=1))
  confirmed_over_threshold = utils.sort_columns_on_row(confirmed).iloc[:, :limit]
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Positive cases of COVID-19 - Top {limit} countries'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        nticks=5,
        gridcolor='rgb(220,220,220)'
      ),
      xaxis=go.layout.XAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        nticks=5,
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )

  for i, column in enumerate(confirmed_over_threshold):
    color, show = utils.get_color(column, i, 8)
    fig.add_trace(go.Scatter(
      x=confirmed_over_threshold[column].index, 
      y=confirmed_over_threshold[column].values,
      name=column,
      hoverinfo='none',
      hovertemplate = 'Positive cases: %{y}<br>Date: %{x}',
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  return fig


def countries_deaths_over_threshold(deaths):
  limit = 25
  confirmed_over_threshold = utils.sort_columns_on_row(deaths).iloc[:, :limit]
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Deaths due to COVID-19 - Top {limit} countries'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)'
      ),
      xaxis=go.layout.XAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        nticks=5
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )

  for i, column in enumerate(confirmed_over_threshold):
    color, show = utils.get_color(column, i, 8)
    fig.add_trace(go.Scatter(
      x=confirmed_over_threshold[column].index, 
      y=confirmed_over_threshold[column].values,
      name=column,
      hoverinfo='none',
      hovertemplate = 'Total deaths: %{y}<br>Date: %{x}',
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  return fig

def top_countries_deaths_over_threshold_and_aligned(deaths):
  align_on = 50
  limit = 10
  deaths = deaths.assign(EU=deaths[['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']].sum(axis=1))
  deaths_over_threshold = utils.sort_columns_on_row(deaths).iloc[:, :limit]

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Number of deaths aligned on the {align_on}th registered death - Top {limit} countries'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        exponentformat='none',
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
      ),
      xaxis=go.layout.XAxis(
        showgrid=False,
        automargin=True,
        title_text=f'Number of days since {align_on}th death',
        range=[0, len(deaths) - 30]
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )


  fig.update_layout(
    updatemenus=[
      dict(
        type="buttons",
        direction='left',
        buttons=[
          dict(
            label="Linear",
            method="relayout",
            args=["yaxis.type", 'lin']
          ),
          dict(
            label="Logarithmic",
            method="relayout",
            args=["yaxis.type", 'log']
          ),
        ],
        pad={"r": 0, "t": 0, "b": 20},
        showactive=True,
        x=0,
        xanchor="left",
        y=-0.2,
        yanchor="top"
      )
    ]
  )

  for i, column in enumerate(deaths_over_threshold):
    x, y = utils.get_from_first_occurrence(deaths_over_threshold, column, 25)
    color, show = utils.get_color(column, i, limit)
    if not show:
      break
    fig.add_trace(go.Scatter(
      x=x, 
      y=y,
      name=column,
      mode='lines',
      hoverinfo='none',
      hovertemplate = 'Deaths: %{y}<br>Day: %{x}',
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot'),
    ))

  return fig


def deaths_over_threshold_and_aligned(deaths):
  threshold = 5
  align_on = 5
  limit = 40
  deaths = deaths.assign(EU=deaths[['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg',
 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']].sum(axis=1))
  deaths_over_threshold = utils.sort_columns_on_row(deaths).iloc[:, :limit]

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Number of deaths aligned on the {align_on}th registered death - Top {limit} countries'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      xaxis=go.layout.XAxis(
        showgrid=False,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        title_text=f'Number of days since {align_on}th death',
        range=[0, len(deaths) - 25]
      ),
      yaxis=go.layout.YAxis(
        exponentformat='none',
        type='log',
        showgrid=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        nticks=5
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )


  fig.update_layout(
    updatemenus=[
      dict(
        type="buttons",
        direction='left',
        buttons=[
          dict(
            label="Logarithmic",
            method="relayout",
            args=["yaxis.type", 'log']
          ),
          dict(
            label="Linear",
            method="relayout",
            args=["yaxis.type", 'lin']
          ),
        ],
        pad={"r": 0, "t": 0, "b": 20},
        showactive=True,
        x=0,
        xanchor="left",
        y=-0.2,
        yanchor="top"
      )
    ]
  )

  for i, column in enumerate(deaths_over_threshold):
    x, y = utils.get_from_first_occurrence(deaths_over_threshold, column, align_on)
    color, show = utils.get_color(column, i, 8)
    fig.add_trace(go.Scatter(
      x=x, 
      y=y,
      name=column,
      mode='lines',
      hoverinfo='none',
      hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  return fig


def aligned_on_lockdown(deaths):
  latest_lockdown = uk_lockdown
  lockdown_index = np.where(pd.to_datetime(deaths.index).values == np.datetime64(pd.to_datetime(latest_lockdown)))[0][0]
  cutoff_begin = 50
  cutoff_end = 70
  y_zoom_in_range = [0, 1000]
  current_max = max(deaths.iloc[-1])

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Number of deaths aligned on date of lock down for selected countries'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        showgrid=True,
        gridwidth=1, 
        gridcolor='rgb(220,220,220)',
        range=y_zoom_in_range
      ),
      xaxis=go.layout.XAxis(
        showticklabels=False,
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgb(220,220,220)',
        nticks=5,
        range = [cutoff_begin, cutoff_end],
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )

  x, y = utils.align_series(deaths['China'], hubei_lockdown, spain_lockdown)

  fig.update_layout(
    updatemenus=[
      dict(
        type="buttons",
        direction='left',
        buttons=[
          dict(
            label="Zoom in",
            method="relayout",
            args=[{"xaxis.range": [cutoff_begin, cutoff_end], "yaxis.range": y_zoom_in_range }]
          ),
          dict(
            label="Zoom out",
            method="relayout",
            args=[{"xaxis.range": [cutoff_begin, len(x)], "yaxis.range": [0, current_max]}]
          ),
        ],
        pad={"r": 0, "t": 0},
        showactive=True,
        x=0,
        xanchor="left",
        y=-0.1,
        yanchor="top"
      )
    ]
  )


  x, y = utils.align_series(deaths['China'], hubei_lockdown, latest_lockdown)
  color, show = utils.get_color('China')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='China',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  x, y = utils.align_series(deaths['Italy'], lombardy_lockdown,latest_lockdown)
  color, show = utils.get_color('Italy')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='Italy',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  x, y = utils.align_series(deaths['Spain'], spain_lockdown, latest_lockdown)
  color, show = utils.get_color('Spain')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='Spain',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  x, y = utils.align_series(deaths['United Kingdom'], uk_lockdown, latest_lockdown)
  color, show = utils.get_color('United Kingdom')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='United Kingdom',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  x, y = utils.align_series(deaths['France'], france_lockdown, latest_lockdown)
  color, show = utils.get_color('France')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='France',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  x, y = utils.align_series(deaths['Norway'], norway_lockdown, latest_lockdown)
  color, show = utils.get_color('Norway')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='Norway',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  x, y = utils.align_series(deaths['Denmark'], denmark_lockdown, latest_lockdown)
  color, show = utils.get_color('Denmark')
  fig.add_trace(go.Scatter(
    x=x, 
    y=y,
    name='Denmark',
    mode='lines',
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    marker_color=color,
    line=dict(width=1.5)
  ))

  fig.add_trace(go.Scatter(
    x=[lockdown_index, lockdown_index],
    y=[0, current_max],
    name='Time of lockdown',
    mode="lines",
    marker_color="rgb(100,100,100)",
    line=dict(dash="dot")
  ))
  return fig

def deaths_area(deaths):
  threshold = 15
  deaths_sorted = utils.sort_columns_on_row(deaths)
  deaths_upper = deaths_sorted[deaths_sorted.columns[0:threshold]]
  deaths_lower = deaths_sorted[deaths_sorted.columns[threshold:]].sum(axis=1)

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Total deaths due to COVID-19'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
      ),
      xaxis=go.layout.XAxis(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        nticks=5
      ),
      legend_orientation="h",
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )

  color, show = utils.get_color('Other', 1000, 1)
  fig.add_trace(go.Scatter(
    x=deaths_lower.index,
    y=deaths_lower.values,
    hoverinfo='none',
    hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
    mode='lines',
    name='Other',
    line=dict(width=0, color=color),
    stackgroup='one' # define stack group
  ))

  for i, column in enumerate(deaths_upper.columns):
    color, show = utils.get_color(column)
    fig.add_trace(go.Scatter(
      x=deaths_upper[column].index,
      y=deaths_upper[column].values,
      mode='lines',
      name=column,
      hoverinfo='none',
      hovertemplate = 'Total deaths: %{y}<br>Day: %{x}',
      line=dict(width=0, color=color),
      stackgroup='one' # define stack group
    ))
  return fig


def deaths_pie_chart(deaths):
  threshold = 10
  deaths_sorted = utils.sort_columns_on_row(deaths)
  deaths_merged = deaths_sorted[deaths_sorted.columns[0:threshold]]
  deaths_merged['Other'] = deaths_sorted[deaths_sorted.columns[threshold:]].sum(axis=1)
  deaths_merged = deaths_merged.iloc[-1].transpose()
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Distribution of deaths by country'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      legend_orientation="h",
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    ),
    data=[
        go.Pie(
            labels=deaths_merged.index,
            values=deaths_merged.values,
            hole=0.5,
            marker=dict(
                colors=[utils.get_color(c)[0] for c in deaths_merged.index]
            )
        )
    ]
  )
  return fig

def current_distribution(deaths):
  threshold = 15
  deaths_sorted = utils.sort_columns_on_row(deaths)
  deaths_merged = deaths_sorted[deaths_sorted.columns[0:threshold]]
  deaths_merged['Other'] = deaths_sorted[deaths_sorted.columns[threshold:]].sum(axis=1)
  deaths_merged = deaths_merged.iloc[-1].sort_values()
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Distribution of deaths by country'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      legend_orientation="h",
      yaxis=go.layout.YAxis(
        showgrid=False,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        side='right'
      ),
      xaxis=go.layout.XAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        tickformat=',.0%',
        range=[0, deaths_merged.max() / deaths_merged.sum()]
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    ),
  )
  fig.add_trace(go.Bar(
    y=deaths_merged.index, 
    x=deaths_merged / deaths_merged.sum(),
    text=[str(x) + '%' for x in round(deaths_merged / deaths_merged.sum() * 1000) / 10],
    textposition='auto',
    marker=dict(
        color=[utils.get_color(c)[0] for c in deaths_merged.index]
    ),
    orientation='h'
  ))
  return fig

def daily_change(df, interval=1):
  limit = 10
  df_diff = utils.sort_columns_on_row(df).diff().iloc[1:]
  df_buckets = utils.bucket_values(df_diff, limit=limit, interval=interval)
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Sum of new deaths every {interval} day due to COVID-19'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        nticks=5
      ),
      xaxis=go.layout.XAxis(
        showgrid=False,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        nticks=5,
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      },
      barmode='stack'
    )
  )

  for i, column in enumerate(df_buckets):
    hovertemplate = 'New deaths: %{y}<br>Date: %{x}'
    if (interval > 1):
      hovertemplate = 'New deaths: %{y}<br>Date: %{x}+' + str(interval - 1)
    color, show = utils.get_color(column)
    fig.add_trace(go.Bar(
      x=df_buckets[column].index, 
      y=df_buckets[column].values,
      name=column,
      hoverinfo='none',
      hovertemplate = hovertemplate,
      marker_color=color,
    ))
  return fig


def animated_map(df, iso_alpha_path):
  iso_alpha = pd.read_csv(iso_alpha_path, delimiter='\t')
  limit = 25
  df_flat = utils.sort_columns_on_row(df).iloc[:, :limit].diff().iloc[1:]
  df_flat = df_flat.iloc[1:].transpose().reset_index().melt(id_vars=['Country/Region'], var_name='Date', value_name='Count')
  df_flat['Count'] = df_flat['Count'].clip(lower=0)
  df_flat = df_flat.merge(iso_alpha, on='Country/Region', how='left')
  fig = px.scatter_geo(df_flat, 
    locations="iso3",
    hover_name="Country/Region", size="Count",
    animation_frame="Date",
    color='Country/Region',
    projection="natural earth"
  )
  return fig

def rate_vs_total(df, x_lower, y_lower, type_name, limit=35, window=7):
  df = utils.sort_columns_on_row(df)
  df_diff = df.diff().iloc[1:]
  df = df.iloc[1:]
  confirmed = utils.bucket_values(df, limit=limit, include_other=False, interval=window)
  confirmed_diff = utils.bucket_values(df_diff, limit=limit, include_other=False, interval=window)
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Weekly {type_name} rate vs. total {type_name}s - Top {limit} countries'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
      font=dict(
        family="Lato, Helvetica",
        color="#333447"
      ),
      yaxis=go.layout.YAxis(
        type='log',
        showgrid=True,
        automargin=True,
        title='New deaths',
        gridwidth=1,
        range=[log(y_lower)/log(10), log(confirmed_diff.max().max())/log(10)],
        gridcolor='rgb(220,220,220)'
      ),
      xaxis=go.layout.XAxis(
        type='log',
        title='Total deaths',
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        range=[log(x_lower)/log(10), log(confirmed.max().max())/log(10)],
        nticks=5
      ),
      margin={
        'l': 0, 'r': 0, 'pad': 0
      }
    )
  )

  for i, column in enumerate(confirmed):
    confirmed_single = confirmed[confirmed_diff[column] > 0][column]
    confirmed_diff_single = confirmed_diff[confirmed_diff[column] > 0][column]
    color, show = utils.get_color(column, i, 8)
    fig.add_trace(go.Scatter(
      x=confirmed_single.values, 
      y=confirmed_diff_single.values,
      name=column,
      hoverinfo='none',
      mode='lines',
      hovertemplate = 'New deaths: %{y}<br>Total deaths: %{x}',
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  fig.add_trace(go.Scatter(
    x=[2, 1000000],
    y=[1, 100000],
    name='Time of lockdown',
    mode="lines",
    marker_color="red",
    line=dict(dash="dot", width=4)
  ))
  return fig