import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json

import pages.components.weather_cards as weather_cards
import pages.sidebar as sidebar
dash.register_page(__name__,order=6)

page_layout = html.Div(
    children=[
        WebSocket(id="weather_ws", url='ws://127.0.0.1:8123/daq/weather/data'),
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Weather")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        weather_cards.weather_CUR,
                        weather_cards.weather_TEMP,
                        weather_cards.weather_VIS
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        weather_cards.weather_SUNRISE,
                                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                                dbc.Col(
                                    [
                                        weather_cards.weather_SUNSET,
                                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                            ]
                        ),
                        weather_cards.weather_W_SPD,
                        weather_cards.weather_W_GUST
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                
                dbc.Col(
                    [
                        weather_cards.weather_W_DEG,
                    ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
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
    output=[
        Output("weather_CUR", "children", allow_duplicate=True),
        Output("weather_TEMP", "children", allow_duplicate=True),
        Output("weather_VIS", "children", allow_duplicate=True),
        Output("weather_W_SPD", "children", allow_duplicate=True),
        Output("weather_W_DEG", "children", allow_duplicate=True),
        Output("weather_W_GUST", "children", allow_duplicate=True),
        Output("weather_SUNRISE", "children", allow_duplicate=True),
        Output("weather_SUNSET", "children", allow_duplicate=True),
        Output("store_weather", "data")
    ],
    inputs=[
        Input("weather_ws", "message"),
    ],
    state=[
        State("weather_CUR", "children"),
        State("weather_TEMP", "children"),
        State("weather_VIS", "children"),
        State("weather_W_SPD", "children"),
        State("weather_W_DEG", "children"),
        State("weather_W_GUST", "children"),
        State("weather_SUNRISE", "children"),
        State("weather_SUNSET", "children"),
        State("store_weather", "data")
    ],
    prevent_initial_call=True
)
def update_weather(msg, cur, temp, vis, w_spd, w_deg, w_gust, sunrise, sunset, storage):
    if msg is None:
        raise PreventUpdate
    is_json, message = validate_message(msg["data"])
    if is_json:
        cur = set_weather_cur(message["cur"])
        temp = set_weather_temp(message["temp"])
        vis = set_weather_vis(message["vis"])
        w_spd = set_weather_w_spd(message["w_spd"])
        w_deg = set_weather_w_deg(message["w_deg"])
        w_gust = set_weather_w_gust(message["w_gust"])
        sunrise = set_weather_sunrise(message["sunrise"])
        sunset = set_weather_sunset(message["sunset"])

        storage["cur"] = cur
        storage["temp"] = temp
        storage["vis"] = vis
        storage["w_spd"] = w_spd
        storage["w_deg"] = w_deg
        storage["w_gust"] = w_gust
        storage["sunrise"] = sunrise
        storage["sunset"] = sunset

        return[
            cur, temp, vis, w_spd, w_deg, w_gust, sunrise, sunset, storage
        ]
    
    else:
        return[
            cur, temp, vis, w_spd, w_deg, w_gust, sunrise, sunset, storage
        ]

@callback(
    output=[
        Output("weather_CUR", "children"),
        Output("weather_TEMP", "children"),
        Output("weather_VIS", "children"),
        Output("weather_W_SPD", "children"),
        Output("weather_W_DEG", "children"),
        Output("weather_W_GUST", "children"),
        Output("weather_SUNRISE", "children"),
        Output("weather_SUNSET", "children"),
    ],
    inputs=[Input("store_weather", "modified_timestamp")],
    state=[State("store_weather", "data")], 
)
def get_weather_storage(ts, data):
    if ts is None:
        raise PreventUpdate
    
    return[
        data.get("cur", "no Value received"),
        data.get("temp", "no Value received"),
        data.get("vis", "no Value received"),
        data.get("w_spd", "no Value received"),
        data.get("w_deg", "no Value received"),
        data.get("w_gust", "no Value received"),
        data.get("sunrise", "no Value received"),
        data.get("sunset", "no Value received")
    ]


def validate_message(msg):
    try:
        message = json.loads(msg)
        keys = ["cur", "temp", "vis", "w_spd", "w_deg", "w_gust", "sunrise", "sunset"]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"

    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]
    

def set_weather_cur(value):
    image = html.Img(style={"width": "100%", "height": "100%", "objectFit": "scale-down"})
    match value:
        case "sonnig":
            image.src="/assets/sonnig.png"
        case "bewoelkt":
            image.src="/assets/bewoelkt.png"
        case "regen":
            image.src="/assets/regen.png"
        case "gewitter":
            image.src="/assets/gewitter.png"
        case "schnee":
            image.src="/assets/schnee.png"
        case _:
            image.src="/assets/unbekannt.png"

    content = html.Div(
        children=[
            html.Div(children=f"{value}", style={"textAlign": "center",  "fontSize": "24px"}),
            html.Div(children=image, style={"height": 100})
        ]
    )
    return content

def set_weather_temp(value):
    fig = go.Figure(
        go.Bar(
            hoverinfo="skip",
            x=[value],
            y=["C"],
            orientation="h"
        )
    )
    fig.update_layout(
        xaxis=dict(range=[-25, 50]),
        yaxis=dict(
            showticklabels=False,
            showline=False
        ),
        margin=dict(l=20,r=20,b=20,t=20),
        annotations=[
            dict(
                x=value/2,
                y="C",
                text=f"{value} °C",
                showarrow=False,
                font=dict(
                    size=14
                )
            )
        ]
    )
    return dcc.Graph(figure=fig, config={"displayModeBar": False}, style={"height": 100})


def set_weather_vis(value):
    return dbc.Progress(label=f"{value} %", value=value, style={"fontSize": "1em"})

def set_weather_w_spd(value):
    return f"{value} m/s"

def set_weather_w_deg(value):
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

def set_weather_w_gust(value):
    return f"{value} m/s"

def set_weather_sunrise(value):
    return f"{value}"

def set_weather_sunset(value):
    return f"{value}"