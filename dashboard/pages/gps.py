import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import pages.components.gps_cards as gps_cards

dash.register_page(__name__, name='GPS',order=4)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="GPS")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([gps_cards.gps_HEAD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([gps_cards.gps_VALID],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([gps_cards.gps_SPEED],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([gps_cards.gps_LAT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([gps_cards.gps_NS],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([gps_cards.gps_VARIAT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([gps_cards.gps_LONG],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([gps_cards.gps_EW],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([gps_cards.gps_VARIAT_EW],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)