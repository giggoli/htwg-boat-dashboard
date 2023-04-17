import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import sys,os,time
from multiprocessing import Process
from gevent.pywsgi import WSGIServer

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ws_server import websocket_server
from mqtt import mqtt_receiver

import plotly.io as pio
import htwg_plotly_theme
pio.templates.default = "htwg_color_style"
my_bootstrap = ("/assets/HTWG_theme.css")


dashboard = dash.Dash(__name__, use_pages=True, external_stylesheets=[my_bootstrap])

sidebar = dbc.Nav(
    [
        
        dbc.NavLink(
            [
                html.Div(page["name"])
            ],
            href=page["path"],
            active="exact"
        )
        for page in dash.page_registry.values()
    ],
    vertical = True,
    pills = True,
    id="menu"
)



dashboard.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(children="Dashboard", className="myHeader")
                    ]
                )
            ]
        ),

        html.Hr(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        sidebar
                    ],xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

                dbc.Col(
                    [
                        dash.page_container
                    ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10),
            ]
        )
    ],
    fluid=True
)

if __name__ == "__main__":
    print("......Launching DASHBOARD......")
    time.sleep(2)

    print("start websocket server")
    proc_ws = Process(target=websocket_server.start_ws)
    proc_ws.start()
    time.sleep(2)

    print("start mqtt server")
    proc_mqtt = Process(target=mqtt_receiver.launch_mqtt)
    proc_mqtt.start()
    time.sleep(2)

    dashboard.run_server(debug=False)



