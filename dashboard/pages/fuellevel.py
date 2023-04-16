import dash
import json
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate

import pages.components.fuellevel_cards as fuellevel_cards

dash.register_page(__name__, order=3)

layout = html.Div(
    children=[
        dcc.Store(id='store_fuellevel', storage_type='session', data=dict()),
        WebSocket(id="fuellevel_ws", url='ws://127.0.0.1:8123/fuellevel'),
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Fuellevel"),
                    
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        fuellevel_cards.fuellevel_ID,
                        fuellevel_cards.fuellevel_TEMP
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col(
                    [
                        fuellevel_cards.fuellevel_FL,
                        fuellevel_cards.fuellevel_ERROR
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col(
                    [
                        fuellevel_cards.fuellevel_FA
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)


@callback(
    output = [
        Output("fuellevel_ID", "children", allow_duplicate=True),
        Output("fuellevel_FL", "children", allow_duplicate=True),
        Output("fuellevel_FA", "children", allow_duplicate=True),
        Output("fuellevel_TEMP", "children", allow_duplicate=True),
        Output("fuellevel_ERROR", "children", allow_duplicate=True),
        Output("store_fuellevel", 'data')
    ],
    inputs = [
        Input("fuellevel_ws", "message"),
    ],
    state = [
        State("fuellevel_ID", "children"),
        State("fuellevel_FL", "children"),
        State("fuellevel_FA", "children"),
        State("fuellevel_TEMP", "children"),
        State("fuellevel_ERROR", "children"),
        State("store_fuellevel", 'data')
    ],
    prevent_initial_call=True
)
def update_fuellevel(msg, id, fl, fa, temp, error, storage):
    is_json, message = validate_message(msg["data"])
    if is_json:
        id = set_fuellevel_ID(message["ID"])
        fl = set_fuellevel_FL(message["FL"])
        fa = set_fuellevel_FA(message["FA"])
        temp = set_fuellevel_TEMP(message["TEMP"])
        error = set_fuellevel_ERROR(message["ERROR"])

        storage["ID"] = id
        storage["FL"] = fl
        storage["FA"] = fa
        storage["TEMP"] = temp
        storage["ERROR"] = error

        return [
            id, fl, fa, temp, error, storage
        ]
    else:
        return [
            id, fl, fa, temp, error, storage
        ]


@callback(
     output = [
        Output("fuellevel_ID", "children"),
        Output("fuellevel_FL", "children"),
        Output("fuellevel_FA", "children"),
        Output("fuellevel_TEMP", "children"),
        Output("fuellevel_ERROR", "children"),
    ],
    inputs = [Input("store_fuellevel", 'modified_timestamp')],
    state = [State("store_fuellevel", 'data')],
)
def get_fuellevel_storage(ts, data):
        if ts is None:
            raise PreventUpdate

        return [
            data.get('ID', "no Value received"),
            data.get('FL', "no Value received"),
            data.get('FA', "no Value received"),
            data.get('TEMP', "no Value received"),
            data.get('ERROR', "no Value received")
        ]


def validate_message(msg):
    try:
        message = json.loads(msg)
    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]


def set_fuellevel_ID(value):
    return f"{value}"

def set_fuellevel_FL(value):
    return dbc.Progress(label=f"{value}%", value=value, style={"fontSize": "1em"})

def set_fuellevel_FA(value):
    return dbc.Alert(f"{value} ml", color="primary", style={"textAlign": "center"})

def set_fuellevel_TEMP(value):
    return f"{value}"

def set_fuellevel_ERROR(value):
    if value == 0:
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == 1:
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="light", style={"textAlign": "center"})