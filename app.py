import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd
import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import os
from dash.dependencies import Input, Output
import dash_table as dt
import pandas as pd

df_albon = pd.read_excel('https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.xlsx')

app = dash.Dash(__name__)
server = app.server

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div(children=[
    html.Br(),
    dt.DataTable(style_table={'overflowX':'scroll'},
               style_cell={'minWidth':'45px'},
               style_header={'backgroundColor':'#f8f8f8','fontWeight':'bold'},
               style_data_conditional=[{'if':{'row_index':'odd'},
                                        'backgroundColor':'#f8f8f8'}],
               columns=[{"name": i, "id": i} for i in df_albon.columns],
               style_as_list_view=True,
               data=df_albon.to_dict('records')),
    html.Br()
])

if __name__ == '__main__':
    app.run_server(debug=True)
