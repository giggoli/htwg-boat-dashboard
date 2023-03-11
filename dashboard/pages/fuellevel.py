import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import pages.components.fuellevel_cards as fuellevel_cards

dash.register_page(__name__, order=2)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Fuellevel")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([fuellevel_cards.fuellevel_ID],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuellevel_cards.fuellevel_FL],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuellevel_cards.fuellevel_FA],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([fuellevel_cards.fuellevel_TEMP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuellevel_cards.fuellevel_ERROR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)