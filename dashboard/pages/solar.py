import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pages.components.solar_cards as solar_cards
import pages.components.solar_sys_cards as solar_sys_cards

dash.register_page(__name__, order=1)

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Solar")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_BV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_BC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_BT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_CH],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_CHM],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_PVV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_PVC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_EQP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_EQTR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_ROCH],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_SYSALRM],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_SYSAL],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_SYSAH],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_YTD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_MPTD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_YYD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_MPYD],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_ERROR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_cards.solar_YPVP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_UYPWR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_cards.solar_MPPT],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        #### System ####
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="System")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_sys_cards.system_SolSerial],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_AIS],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_SYSBV],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_sys_cards.system_SYSBC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_SYSBP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_SYSSOC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_sys_cards.system_SYSSTATE],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_SYSCAH],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_SYST2G],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_sys_cards.system_PVCP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_PVCC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_SYSCP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col([solar_sys_cards.system_SYSPWR],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_BUSCC],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([solar_sys_cards.system_BUSCP],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)
