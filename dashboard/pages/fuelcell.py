import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json

import pages.components.fuelcell_cards as fuelcell_cards
import pages.sidebar as sidebar
from pages.components.fuelcell_helper import *

dash.register_page(__name__, order=2)

page_layout = html.Div(
    children=[
        WebSocket(id="fuelcell_ws", url="ws://127.0.0.1:8123/daq/fuelcell/data"),
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

layout = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                [
                    html.Br(),
                    html.Br(),
                    sidebar.sidebar
                ],xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),
            dbc.Col(
                [
                    page_layout
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10),
        ]
    ),
    fluid=True
)


@callback(
    output = [
        Output("fuelcell_status_e_i", "children", allow_duplicate=True),
        Output("fuelcell_status_e_s", "children", allow_duplicate=True),
        Output("fuelcell_SOC_e_i", "children", allow_duplicate=True),
        Output("fuelcell_SOC_e_s", "children", allow_duplicate=True),
        Output("fuelcell_SOV_e_i", "children", allow_duplicate=True),
        Output("fuelcell_SOV_e_s", "children", allow_duplicate=True),
        Output("fuelcell_SOP_e_i", "children", allow_duplicate=True),
        Output("fuelcell_SOP_e_s", "children", allow_duplicate=True),
        Output("fuelcell_status", "children", allow_duplicate=True),
        Output("fuelcell_SOC", "children", allow_duplicate=True),
        Output("fuelcell_SOV", "children", allow_duplicate=True),
        Output("fuelcell_SOP", "children", allow_duplicate=True),
        Output("store_fuelcell", "data"),
    ],
    inputs = [
        Input("fuelcell_ws", "message"),
    ],
    state = [
        State("fuelcell_status_e_i", "children"),
        State("fuelcell_status_e_s", "children"),
        State("fuelcell_SOC_e_i", "children"),
        State("fuelcell_SOC_e_s", "children"),
        State("fuelcell_SOV_e_i", "children"),
        State("fuelcell_SOV_e_s", "children"),
        State("fuelcell_SOP_e_i", "children"),
        State("fuelcell_SOP_e_s", "children"),
        State("fuelcell_status", "children"),
        State("fuelcell_SOC", "children"),
        State("fuelcell_SOV", "children"),
        State("fuelcell_SOP", "children"),
        State("store_fuelcell", "data"),
    ],
    prevent_initial_call = True,
)
def update_fuelcell(msg, status_e_i, status_e_s, soc_e_i, soc_e_s, sov_e_i,
                    sov_e_s, sop_e_i, sop_e_s, status, soc, sov, sop, storage):
    if msg is None:
        raise PreventUpdate
    is_json, message = validate_fuelcell_message(msg["data"])
    if is_json:
            
        status_e_i = set_fuelcell_status_e_i(message["status_e_i"])
        status_e_s = set_fuelcell_status_e_s(message["status_e_s"])
        soc_e_i = set_fuelcell_soc_e_i(message["SOC_e_i"])
        soc_e_s = set_fuelcell_soc_e_s(message["SOC_e_s"])
        sov_e_i = set_fuelcell_sov_e_i(message["SOV_e_i"])
        sov_e_s = set_fuelcell_sov_e_s(message["SOV_e_s"])
        sop_e_i = set_fuelcell_sop_e_i(message["SOP_e_i"])
        sop_e_s = set_fuelcell_sop_e_s(message["SOP_e_s"])
        status = set_fuelcell_status(message["status"])
        soc = set_fuelcell_soc(message["SOC"])
        sov = set_fuelcell_sov(message["SOV"])
        sop = set_fuelcell_sop(message["SOP"])

        storage["status_e_i"] = status_e_i
        storage["status_e_s"] = status_e_s        
        storage["soc_e_i"] = soc_e_i
        storage["soc_e_s"] = soc_e_s
        storage["sov_e_i"] = sov_e_i
        storage["sov_e_s"] = sov_e_s
        storage["sop_e_i"] = sop_e_i
        storage["sop_e_s"] = sop_e_s
        storage["status"] = status
        storage["soc"] = soc
        storage["sov"] = sov        
        storage["sop"] = sop

        return [
            status_e_i, status_e_s, soc_e_i, soc_e_s, sov_e_i,
            sov_e_s, sop_e_i, sop_e_s, status, soc, sov, sop, storage
        ]
    else:
        return [
            status_e_i, status_e_s, soc_e_i, soc_e_s, sov_e_i,
            sov_e_s, sop_e_i, sop_e_s, status, soc, sov, sop, storage
        ]
    
@callback(
    output = [
        Output("fuelcell_status_e_i", "children"),
        Output("fuelcell_status_e_s", "children"),
        Output("fuelcell_SOC_e_i", "children"),
        Output("fuelcell_SOC_e_s", "children"),
        Output("fuelcell_SOV_e_i", "children"),
        Output("fuelcell_SOV_e_s", "children"),
        Output("fuelcell_SOP_e_i", "children"),
        Output("fuelcell_SOP_e_s", "children"),
        Output("fuelcell_status", "children"),
        Output("fuelcell_SOC", "children"),
        Output("fuelcell_SOV", "children"),
        Output("fuelcell_SOP", "children")
    ],
    inputs = [Input("store_fuelcell", "modified_timestamp")],
    state = [State("store_fuelcell", "data")]        
)
def get_fuelcell_storage(ts, data):
    if ts is None:
        raise PreventUpdate
    
    return[
        data.get("status_e_i", "no Value received"),
        data.get("status_e_s", "no Value received"),
        data.get("soc_e_i", "no Value received"),
        data.get("soc_e_s", "no Value received"),
        data.get("sov_e_i", "no Value received"),
        data.get("sov_e_s", "no Value received"),
        data.get("sop_e_i", "no Value received"),
        data.get("sop_e_s", "no Value received"),
        data.get("status", "no Value received"),
        data.get("soc", "no Value received"),
        data.get("sov", "no Value received"),
        data.get("sop", "no Value received")
    ]


