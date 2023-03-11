import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import pages.components.weather_cards as weather_cards

dash.register_page(__name__,order=6)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Weather")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([weather_cards.weather_CUR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([weather_cards.weather_TEMP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([weather_cards.weather_VIS],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([weather_cards.weather_W_SPD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([weather_cards.weather_W_DEG],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([weather_cards.weather_W_GUST],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([weather_cards.weather_SUNRISE],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([weather_cards.weather_SUNSET],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)