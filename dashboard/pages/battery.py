import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import pages.components.battery_cards as battery_cards

dash.register_page(__name__, order=0)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Battery")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_BSR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_BLVW],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_BHVW],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_BORC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_BORE],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_SoC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_E_NE],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_ST],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_OC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_E_OV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_UV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_D],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_E_OUT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_P],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_C],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_E_H],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_CP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_CM],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_E_CPC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_CD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_E_S],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_W_NE],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_W_ST],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_W_OC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_W_OV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_W_UV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_W_D],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_W_OUT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_W_P],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_W_C],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_E_NID],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_BV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_BC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_B_MSCV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_mSCV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_HS],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_SoH],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_HMT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_CMT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_SWV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_RS],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_RC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_B_TR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_LC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_IM],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([battery_cards.battery_B_PCC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_PDC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([battery_cards.battery_B_AC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)