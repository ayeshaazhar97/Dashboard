#!/usr/bin/env python
# coding: utf-8

# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


## Import Data for visualization
df = pd.read_excel("kabulfinal.xlsx")

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df_monthly = df.resample('1M').mean()
# print(df.head())
# print(df_monthly.head())


trace_daily = go.Scatter(x=list(df.index),
                         y=list(df.Flow),
                         name="Kabul Flow",
                         line=dict(color='firebrick', width=1))

trace_monthly = go.Scatter(x=list(df_monthly.index),
                         y=list(df_monthly.Flow),
                         name="Kabul Flow - Monthly",
                         line=dict(color='royalblue', width=2))

data = [trace_daily]
data2 = [trace_monthly]
layout = dict(title="Water Flow", showlegend=True)
fig = dict(data=data, layout=layout)

fig2 = dict(data=data2, layout=layout)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        html.H2('Rethinking Indus'),
        html.Img(src='/assets/water-icon.svg')
    ], className="banner"),

    html.Div([

        html.Div([

            html.Div(
                dcc.Graph(id="flow-daily",
                    figure=fig)
            ),

        ], className="six columns"),

        html.Div([

            html.Div(
                dcc.Graph(id="flow-monthly",
                    figure=fig2)
            ),

        ], className="six columns"),

    ], className="row")

])

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




