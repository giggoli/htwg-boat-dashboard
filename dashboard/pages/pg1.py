import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", order=0)

layout = html.Div(
    dbc.Row(
        [
            dbc.Col(
                [
                   html.Div(
                    children=[
                        html.H1(children="MQTT Examplel"),
                        html.P(children="Get values from an other python script sending over websocket")
                    ])
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
            )
        ]
    )
)