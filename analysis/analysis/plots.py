import pandas as pd
import numpy as np
import plotly.graph_objects as go
import utils

hubei_lockdown = '2020-01-23'
lombardy_lockdown = '2020-03-08'
spain_lockdown = '2020-03-14'
uk_lockdown = '2020-03-20'
norway_lockdown = '2020-03-12'
france_lockdown = '2020-03-17'

def confirmed_cases_over_threshold(confirmed):
  threshold = 500
  confirmed_over_threshold = utils.over_threshold(confirmed, threshold)
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries with over {threshold} confirmed cases due to COVID-19'),
      plot_bgcolor='rgb(255,255,255)',
      yaxis=go.layout.YAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(200,200,200)'
      ),
      xaxis=go.layout.XAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(200,200,200)',
        dtick=4
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
      marker_color=color,
      line=dict(width=1, dash='solid' if show else 'dot')
    ))
  return fig


def countries_deaths_over_threshold(deaths):
  threshold = 5
  confirmed_over_threshold = utils.over_threshold(deaths, threshold)
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries with over {threshold} confirmed cases due to COVID-19'),
      plot_bgcolor='rgb(255,255,255)',
      yaxis=go.layout.YAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(200,200,200)'
      ),
      xaxis=go.layout.XAxis(
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(200,200,200)',
        dtick=4
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
      marker_color=color,
      line=dict(width=1, dash='solid' if show else 'dot')
    ))
  return fig

def top_countries_deaths_over_threshold_and_aligned(deaths):
  threshold = 5
  deaths_over_threshold = utils.over_threshold(deaths, threshold)
  deaths_china = deaths_over_threshold['China']
  deaths_over_threshold = deaths_over_threshold.drop(['China'], axis=1)

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Top 6 countries with over {threshold} deaths, aligned with second registered death'),
      plot_bgcolor='rgb(255,255,255)',
      yaxis=go.layout.YAxis(
        type='log', showgrid=True, gridwidth=1, gridcolor='rgb(200,200,200)'
      ),
      xaxis=go.layout.XAxis(showgrid=True, gridwidth=1, gridcolor='rgb(200,200,200)', dtick=4),
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
        pad={"r": 0, "t": 0},
        showactive=True,
        x=0,
        xanchor="left",
        y=-0.1,
        yanchor="top"
      )
    ]
  )

  max_count = 0
  for i, column in enumerate(deaths_over_threshold):
    x, y = utils.get_from_first_occurrence(deaths_over_threshold, column, 1)
    if len(x) > max_count:
      max_count = len(x)
    color, show = utils.get_color(column, i, 6)
    fig.add_trace(go.Scatter(
      x=x, 
      y=y,
      name=column,
      mode='lines',
      marker_color=color,
      line=dict(width=1, dash='solid' if show else 'dot'),
      visible=True if show else 'legendonly'
    ))

  color, show = utils.get_color('China')
  fig.add_trace(go.Scatter(
    x=np.arange(0, max_count), 
    y=np.array([2, 2, 4, 7, 11] + deaths_china.values.tolist())[:max_count],
    name='China',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
  ))

  return fig


def deaths_over_threshold_and_aligned(deaths):
  threshold = 5
  deaths_over_threshold = utils.over_threshold(deaths, threshold)
  deaths_china = deaths_over_threshold['China']
  deaths_over_threshold = deaths_over_threshold.drop(['China'], axis=1)

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries with over {threshold} deaths, aligned with second registered death'),
      plot_bgcolor='rgb(255,255,255)',
      yaxis=go.layout.YAxis(
        type='log', showgrid=True, gridwidth=1, gridcolor='rgb(200,200,200)'
      ),
      xaxis=go.layout.XAxis(showgrid=True, gridwidth=1, gridcolor='rgb(200,200,200)', dtick=4),
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
        pad={"r": 0, "t": 0},
        showactive=True,
        x=0,
        xanchor="left",
        y=-0.1,
        yanchor="top"
      )
    ]
  )

  color, show = utils.get_color('China')
  fig.add_trace(go.Scatter(
    x=np.arange(0, len(deaths_china)), 
    y=np.array([2, 2, 4, 7, 11] + deaths_china.values.tolist()),
    name='China',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
  ))

  for i, column in enumerate(deaths_over_threshold):
    x, y = utils.get_from_first_occurrence(deaths_over_threshold, column, 1)
    color, show = utils.get_color(column, i, 8)
    fig.add_trace(go.Scatter(
      x=x, 
      y=y,
      name=column,
      mode='lines',
      marker_color=color,
      line=dict(width=1, dash='solid' if show else 'dot')
    ))
  return fig


def aligned_on_lockdown(deaths):
  latest_lockdown = uk_lockdown
  lockdown_index = np.where(pd.to_datetime(deaths.index).values == np.datetime64(pd.to_datetime(latest_lockdown)))[0][0]
  cutoff = 40
  current_max = max(deaths.iloc[-1])

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Number of deaths due to COVID-19 when countries initiated lockdown'),
      plot_bgcolor='rgb(255,255,255)',
      yaxis=go.layout.YAxis(
        showgrid=True, gridwidth=1, gridcolor='rgb(200,200,200)', range=[0, 500]
      ),
      xaxis=go.layout.XAxis(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgb(200,200,200)', 
        dtick=4,
        range = [cutoff, 60]
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
            args=[{"xaxis.range": [cutoff, 60], "yaxis.range": [0, 550]}]
          ),
          dict(
            label="Zoom out",
            method="relayout",
            args=[{"xaxis.range": [cutoff, len(x)], "yaxis.range": [0, current_max]}]
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
    x=x[cutoff:], 
    y=y[cutoff:],
    name='China',
    mode='lines',
    marker_color='rgb(255,0,150)',
    line=dict(width=1)
  ))

  x, y = utils.align_series(deaths['Italy'], lombardy_lockdown,latest_lockdown)
  color, show = utils.get_color('Italy')
  fig.add_trace(go.Scatter(
    x=x[cutoff:], 
    y=y[cutoff:],
    name='Italy',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
  ))

  x, y = utils.align_series(deaths['Spain'], spain_lockdown, latest_lockdown)
  color, show = utils.get_color('Spain')
  fig.add_trace(go.Scatter(
    x=x[cutoff:], 
    y=y[cutoff:],
    name='Spain',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
  ))

  x, y = utils.align_series(deaths['United Kingdom'], uk_lockdown, latest_lockdown)
  color, show = utils.get_color('United Kingdom')
  fig.add_trace(go.Scatter(
    x=x[cutoff:], 
    y=y[cutoff:],
    name='United Kingdom',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
  ))

  x, y = utils.align_series(deaths['France'], france_lockdown, latest_lockdown)
  color, show = utils.get_color('France')
  fig.add_trace(go.Scatter(
    x=x[cutoff:], 
    y=y[cutoff:],
    name='France',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
  ))

  x, y = utils.align_series(deaths['Norway'], norway_lockdown, latest_lockdown)
  color, show = utils.get_color('Norway')
  fig.add_trace(go.Scatter(
    x=x[cutoff:], 
    y=y[cutoff:],
    name='Norway',
    mode='lines',
    marker_color=color,
    line=dict(width=1)
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