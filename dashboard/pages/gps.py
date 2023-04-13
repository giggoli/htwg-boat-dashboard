import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json

import pages.components.gps_cards as gps_cards

dash.register_page(__name__, name='GPS',order=4)

layout = html.Div(
    children=[
        dcc.Store(id='store_gps', storage_type='session', data=dict()),
        WebSocket(id="gps_ws", url='ws://127.0.0.1:8123/gps'),
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="GPS")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        gps_cards.gps_HEAD,
                        gps_cards.gps_LAT,
                        gps_cards.gps_LONG
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col(
                    [
                        gps_cards.gps_VALID,
                        gps_cards.gps_NS,
                        gps_cards.gps_EW
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col(
                    [
                        gps_cards.gps_SPEED,
                        gps_cards.gps_VARIAT,
                        gps_cards.gps_VARIAT_EW
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)

@callback(
    output = [
        Output("gps_HEAD", "children", allow_duplicate=True),
        Output("gps_VALID", "children", allow_duplicate=True),
        Output("gps_LAT", "children", allow_duplicate=True),
        Output("gps_NS", "children", allow_duplicate=True),
        Output("gps_LONG", "children", allow_duplicate=True),
        Output("gps_EW", "children", allow_duplicate=True),
        Output("gps_SPEED", "children", allow_duplicate=True),
        Output("gps_VARIAT", "children", allow_duplicate=True),
        Output("gps_VARIAT_EW", "children", allow_duplicate=True),      
        Output("store_gps", 'data')
    ],
    inputs = [
        Input("gps_ws", "message"),
    ],
    state = [
        State("gps_HEAD", "children"),
        State("gps_VALID", "children"),
        State("gps_LAT", "children"),
        State("gps_NS", "children"),
        State("gps_LONG", "children"),
        State("gps_EW", "children"),
        State("gps_SPEED", "children"),
        State("gps_VARIAT", "children"),
        State("gps_VARIAT_EW", "children"), 
        State("store_gps", 'data')
    ],
    prevent_initial_call=True
)
def update_gps(msg, head, valid, lat, ns, long, ew, speed, variant, variant_ew, storage):
    is_json, message = validate_message(msg["data"])
    if is_json:
        head = set_gps_head(message["head"])
        valid = set_gps_valid(message["valid"])
        lat = set_gps_lat(message["lat"])
        ns = set_gps_ns(message["ns"])
        long = set_gps_long(message["long"])
        ew = set_gps_ew(message["ew"])
        speed = set_gps_speed(message["speed"] )
        variant = set_gps_variant(message["variat"])
        variant_ew = set_gps_variant_ew(message["variat_ew"])

        storage["gps_HEAD"] = head
        storage["gps_VALID"] = valid
        storage["gps_LAT"] = lat
        storage["gps_NS"] = ns
        storage["gps_LONG"] = long
        storage["gps_EW"] = ew
        storage["gps_SPEED"] = speed 
        storage["gps_VARIAT"] = variant
        storage["gps_VARIAT_EW"] = variant_ew

        return [
            head, valid, lat, ns, long, ew, speed, variant, variant_ew, storage
        ]
    else:
        return [
            head, valid, lat, ns, long, ew, speed, variant, variant_ew, storage
        ]

@callback(
    output = [
        Output("gps_HEAD", "children"),
        Output("gps_VALID", "children"),
        Output("gps_LAT", "children"),
        Output("gps_NS", "children"),
        Output("gps_LONG", "children"),
        Output("gps_EW", "children"),
        Output("gps_SPEED", "children"),
        Output("gps_VARIAT", "children"),
        Output("gps_VARIAT_EW", "children"),
    ],
    inputs = [Input("store_gps", "modified_timestamp")],
    state = [State("store_gps", 'data')],
)
def get_gps_storage(ts, data):
    if ts is None:
        raise PreventUpdate
    
    return [
        data.get("gps_HEAD", "no Value received"),
        data.get("gps_VALID", "no Value received"),
        data.get("gps_LAT", "no Value received"),
        data.get("gps_NS", "no Value received"),
        data.get("gps_LONG", "no Value received"),
        data.get("gps_EW", "no Value received"),
        data.get("gps_SPEED", "no Value received"),
        data.get("gps_VARIAT", "no Value received"),
        data.get("gps_VARIAT_EW", "no Value received")
    ]

def validate_message(msg):
    try:
        message = json.loads(msg)
    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]
    
def set_gps_head(value):
    return f"{value}"

def set_gps_valid(value):
    return f"{value}"

def set_gps_lat(value):
    return f"{value}"

def set_gps_ns(value):
    return f"{value}"

def set_gps_long(value):
    return f"{value}"

def set_gps_ew(value):
    return f"{value}"

def set_gps_speed(value):
    return f"{value}"

def set_gps_variant(value):
    return f"{value}"

def set_gps_variant_ew(value):
    return f"{value}"