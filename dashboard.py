import pathlib
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
print(app_path)
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "smarthome.csv")))
elect = pd.read_csv(os.path.join(app_path, os.path.join("data", "electricity.csv")))

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#7FDBFF'
}

new_theme = {
    'background': '#999966',
    'text': '#ebebe0'
}

def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Enegry Consumption'),
                ],
            ),
        ],
    )


def generate_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in elect.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ], style={'color':new_theme['text'], 'marginBottom': 500, 'marginTop': 250}) for i in range(min(len(dataframe), max_rows))
        ]),

    ], style = {
  'table-layout': 'fixed',
  'width': '100%',
  'border-collapse': 'collapse',
  'border': '3px solid purple'})

def build_graph():
    return dcc.Graph(
        id='basic',
        figure={
            'data': [
                {
                    'x': df['Batch'][:50],
                    'y': df['Techniques'][:50],
                    'name': 'Techniques',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Workplace'][:50],
                    'name': 'Workplace',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Garage'][:50],
                    'name': 'Garage',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Kitchen'][:50],
                    'name': 'Kitchen',
                    'marker': {'size': 12}
                },
                {
                    'x': df['Batch'][:50],
                    'y': df['Hall'][:50],
                    'name': 'Hall',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )




def build_graph_elect():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': elect['Current batch'][:50],
                    'y': elect['Voltage in techniques'][:50],
                    'name': 'Techniques',
                    'marker': {'size': 12}
                },
                {
                    'x': elect['Current batch'][:50],
                    'y': elect['Voltage in workplace'][:50],
                    'name': 'Workplace',
                    'marker': {'size': 12}
                },
                {
                    'x': elect['Current batch'][:50],
                    'y': elect['Votage in garage'][:50],
                    'name': 'Garage',
                    'marker': {'size': 12}
                },
                {
                    'x': elect['Current batch'][:50],
                    'y': elect['Voltage in kitchen'][:50],
                    'name': 'Kitchen',
                    'marker': {'size': 12}
                },
                {
                    'x': elect['Current batch'][:50],
                    'y': elect['Voltage in hall'][:50],
                    'name': 'Hall',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'title': 'Electricity outages in the flat',
                'showlegend': 'True',
                'plot_bgcolor': new_theme['background'],
                'paper_bgcolor': new_theme['background'],
                'font': {
                    'color': new_theme['text']
                }
        }

    }
)


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(), build_graph_elect(), generate_table(elect),

            ]
        )
    ]
)
