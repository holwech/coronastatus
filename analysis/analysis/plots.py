import pandas as pd
import numpy as np
import plotly.graph_objects as go
import utils

hubei_lockdown = '2020-01-23'
lombardy_lockdown = '2020-03-08'
spain_lockdown = '2020-03-14'
uk_lockdown = '2020-03-23'
norway_lockdown = '2020-03-12'
france_lockdown = '2020-03-17'

paper_bgcolor = 'rgba(0,0,0,0)'
plot_bgcolor='rgba(0,0,0,0)'

def confirmed_cases_over_threshold(confirmed):
  threshold = 500
  confirmed_over_threshold = utils.over_threshold(confirmed, threshold)
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries with over {threshold} confirmed cases due to COVID-19'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
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
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  return fig


def countries_deaths_over_threshold(deaths):
  threshold = 5
  confirmed_over_threshold = utils.over_threshold(deaths, threshold)
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries with over {threshold} confirmed cases due to COVID-19'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
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
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  return fig

def top_countries_deaths_over_threshold_and_aligned(deaths):
  align_on = 50
  deaths_over_threshold = utils.over_threshold(deaths, align_on)

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries aligned on the {align_on}th registered death'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
      yaxis=go.layout.YAxis(
        type='log',
        showgrid=True,
        automargin=True,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
        exponentformat='power'
      ),
      xaxis=go.layout.XAxis(
        showgrid=False,
        automargin=True,
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

  for i, column in enumerate(deaths_over_threshold):
    x, y = utils.get_from_first_occurrence(deaths_over_threshold, column, 25)
    color, show = utils.get_color(column, i, 6)
    if not show:
      break
    fig.add_trace(go.Scatter(
      x=x, 
      y=y,
      name=column,
      mode='lines',
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot'),
    ))

  return fig


def deaths_over_threshold_and_aligned(deaths):
  threshold = 5
  align_on = 5
  deaths_over_threshold = utils.over_threshold(deaths, threshold)

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Countries with over {threshold} deaths, aligned on {align_on}th registered death'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      xaxis=go.layout.XAxis(
        showgrid=False,
        gridwidth=1,
        gridcolor='rgb(220,220,220)',
      ),
      yaxis=go.layout.YAxis(
        exponentformat='power',
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
        pad={"r": 0, "t": 0},
        showactive=True,
        x=0,
        xanchor="left",
        y=-0.1,
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
      marker_color=color,
      line=dict(width=1.5, dash='solid' if show else 'dot')
    ))
  return fig


def aligned_on_lockdown(deaths):
  latest_lockdown = uk_lockdown
  lockdown_index = np.where(pd.to_datetime(deaths.index).values == np.datetime64(pd.to_datetime(latest_lockdown)))[0][0]
  cutoff_begin = 40
  cutoff_end = 70
  y_zoom_in_range = [0, 800]
  current_max = max(deaths.iloc[-1])

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Number of deaths due to COVID-19 when countries initiated lockdown'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
      yaxis=go.layout.YAxis(
        showgrid=True,
        gridwidth=1, 
        gridcolor='rgb(220,220,220)',
        range=y_zoom_in_range
      ),
      xaxis=go.layout.XAxis(
        showgrid=True, 
        gridwidth=1, 
        gridcolor='rgb(220,220,220)',
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
  threshold = 10
  deaths_sorted = utils.sort_columns_on_row(deaths)
  deaths_upper = deaths_sorted[deaths_sorted.columns[0:threshold]]
  deaths_lower = deaths_sorted[deaths_sorted.columns[threshold:]].sum(axis=1)

  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'Total deaths due to COVID-19'),
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)',
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
    hoverinfo='x+y',
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

def daily_change(df):
  interval = 3
  df_diff = utils.sort_columns_on_row(df).diff().iloc[1:]
  df_diff = df_diff[df_diff.columns[0:8]]
  df_diff['Other'] = df_diff[df_diff.columns[8:]].sum(axis=1)
  df_buckets = pd.DataFrame([], columns=df_diff.columns)
  for i in range(len(df_diff), 0, -interval):
      series = df_diff.iloc[(i - interval):i].sum()
      series.name = df_diff.iloc[i - interval].name
      df_buckets = df_buckets.append(series)
  df_buckets = df_buckets.iloc[::-1]
  fig = go.Figure(
    layout=go.Layout(
      title=go.layout.Title(text=f'New deaths in the last {interval} days due to COVID-19'),
      paper_bgcolor=paper_bgcolor,
      plot_bgcolor=plot_bgcolor,
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
    color, show = utils.get_color(column)
    fig.add_trace(go.Bar(
      x=df_buckets[column].index, 
      y=df_buckets[column].values,
      name=column,
      marker_color=color,
    ))
  return fig