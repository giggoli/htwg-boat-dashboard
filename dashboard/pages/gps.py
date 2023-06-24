import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json
import os

import pages.components.gps_cards as gps_cards

dash.register_page(__name__, name='GPS',order=4)

layout = html.Div(
    children=[
        dcc.Store(id='store_gps', storage_type='session', data=dict()),
        WebSocket(id="gps_ws", url='ws://127.0.0.1:8123/daq/gps/data'),
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
                        gps_cards.gps_MAP,
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        gps_cards.gps_LAT,
                                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                                dbc.Col(
                                    [
                                        gps_cards.gps_LONG,
                                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                            ]
                        ),
                        gps_cards.gps_VALID,
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),

                dbc.Col(
                    [
                        gps_cards.gps_HEAD,
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        gps_cards.gps_NS,
                                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                                dbc.Col(
                                    [
                                        gps_cards.gps_EW, 
                                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                            ]
                        ),
                        gps_cards.gps_VARIAT_EW,
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),

                dbc.Col(
                    [
                        gps_cards.gps_VARIAT,
                        gps_cards.gps_SPEED,
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
        Output("gps_MAP", "children", allow_duplicate=True),       
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
        State("gps_MAP", "children"), 
        State("store_gps", 'data')
    ],
    prevent_initial_call=True
)
def update_gps(msg, head, valid, lat, ns, long, ew, speed, variant, variant_ew, map, storage):
    is_json, message = validate_message(msg["data"])
    if is_json:
        head = set_gps_head(message["head"])
        valid = set_gps_valid(message["valid"])
        lat = set_gps_lat(message["lat"])
        ns = set_gps_ns(message["ns"])
        long = set_gps_long(message["long"])
        ew = set_gps_ew(message["ew"])
        speed = set_gps_speed(message["speed"])
        variant = set_gps_variant(message["variat"])
        variant_ew = set_gps_variant_ew(message["variat_ew"])
        map = set_gps_map(message["lat"], message["long"])

        storage["gps_HEAD"] = head
        storage["gps_VALID"] = valid
        storage["gps_LAT"] = lat
        storage["gps_NS"] = ns
        storage["gps_LONG"] = long
        storage["gps_EW"] = ew
        storage["gps_SPEED"] = speed 
        storage["gps_VARIAT"] = variant
        storage["gps_VARIAT_EW"] = variant_ew
        storage["gps_MAP"] = map

        return [
            head, valid, lat, ns, long, ew, speed, variant, variant_ew, map, storage
        ]
    else:
        return [
            head, valid, lat, ns, long, ew, speed, variant, variant_ew, map, storage
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
        Output("gps_MAP", "children"),
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
        data.get("gps_VARIAT_EW", "no Value received"),
        data.get("gps_MAP", "no Value to show on Map")
    ]

def validate_message(msg):
    try:
        message = json.loads(msg)
        keys = ["head", "valid", "lat", "ns", "long", "ew",
                "speed", "variat", "variat_ew", "long"]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"
                
    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]
    
def set_gps_head(value):
    fig = go.Figure(
        go.Barpolar(
            hoverinfo="skip",
            r=[1],
            theta=[value],
            width=[6],
            marker_line_color = "black",
            marker_line_width = 1
        ),
    )
    fig.update_layout(
        title = dict(text=f"{value}°",font_size=25),
        polar = dict(
            radialaxis = dict(range=[0,1], showticklabels=False, ticks=''),
            angularaxis = dict(direction="clockwise", rotation=90),
        )
    )
    return dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": 400})

def set_gps_valid(value):
    if value == "A":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "V":
        return dbc.Alert("INVALID", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})
    
def set_gps_lat(value):
    return f"{value}"

def set_gps_ns(value):
    return f"{value}"

def set_gps_long(value):
    return f"{value}"

def set_gps_ew(value):
    return f"{value}"

def set_gps_speed(value):
    fig = go.Figure(
        go.Indicator(
            mode = "gauge+number",
            value = value,
            title = {"text": "knots"},
            gauge={"bar": {"color": "#009a91"}}
        )
    )
    fig.update_traces(
        gauge_axis=dict(range=[0,15])
    )
    fig.update_layout(
        margin=dict(l=50,r=50,b=50,t=50)
    )
    return dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": 230})

def set_gps_variant(value):
    fig = go.Figure(
        go.Barpolar(
            hoverinfo="skip",
            r=[1],
            theta=[value],
            width=[6],
            marker_line_color = "black",
            marker_line_width = 1
        ),
    )
    fig.update_layout(
        title = dict(text=f"{value}°",font_size=25),
        polar = dict(
            radialaxis = dict(range=[0,1], showticklabels=False, ticks=''),
            angularaxis = dict(direction="clockwise", rotation=90),
        )
    )
    return dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": 400})

def set_gps_variant_ew(value):
    return f"{value}"

def set_gps_map(lat, lon):
    mapbox_token = open("dashboard/pages/.mapboxtoken").read()
    latitude = f"{lat}"
    longitude = f"{lon}"

    fig = go.Figure(
        go.Scattermapbox(
            lat=[latitude],
            lon=[longitude],
            mode="markers",
            marker=go.scattermapbox.Marker(
                size=14
            ),
        )
    )
    fig.update_layout(
        mapbox = dict(
            accesstoken = mapbox_token,
            bearing = 0,
            center = go.layout.mapbox.Center(
                lat = lat,
                lon = lon
            ),
            pitch = 0,
            zoom = 15
        ),
        margin=dict(l=5,r=5,b=5,t=5)

    )
    return dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": 430})
