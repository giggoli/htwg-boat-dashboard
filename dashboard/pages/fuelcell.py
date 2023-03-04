import dash
from dash import dcc, html, Output, Input
import dash_bootstrap_components as dbc

import pages.components.fuelcell_cards as fuelcell_cards

dash.register_page(__name__, order=2)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Fuelcell")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([fuelcell_cards.fuelcell_SOC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_SOC_e_s],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_SOC_e_i],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([fuelcell_cards.fuelcell_SOV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_SOV_e_s],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_SOV_e_i],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([fuelcell_cards.fuelcell_SOP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_SOP_e_s],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_SOP_e_i],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([fuelcell_cards.fuelcell_status],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_status_e_s],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([fuelcell_cards.fuelcell_status_e_i],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)
