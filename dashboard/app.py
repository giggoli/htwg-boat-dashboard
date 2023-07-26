import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import sys,os,time
from multiprocessing import Process


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ws_server import websocket_server
from mqtt import mqtt_receiver

import plotly.io as pio
import htwg_plotly_theme
pio.templates.default = "htwg_color_style"
my_bootstrap = ("/assets/HTWG_theme.css")


dashboard = dash.Dash(__name__, use_pages=True, external_stylesheets=[my_bootstrap])

dashboard.layout = html.Div(children=[
    dcc.Store(id='store_battery', storage_type='session', data=dict()),
    dcc.Store(id='store_fuelcell', storage_type='session', data=dict()),
    dcc.Store(id='store_fuellevel', storage_type='session', data=dict()),
    dcc.Store(id='store_gps', storage_type='session', data=dict()),
    dcc.Store(id='store_solar', storage_type='session', data=dict()),
    dcc.Store(id='store_system', storage_type='session', data=dict()),
    dcc.Store(id='store_weather', storage_type='session', data=dict()),
    dash.page_container
])


if __name__ == "__main__":
    print("......Launching DASHBOARD......")
    time.sleep(2)

    print("start websocket server")
    proc_ws = Process(target=websocket_server.start_ws)
    proc_ws.start()
    time.sleep(5)

    print("start mqtt server")
    proc_mqtt = Process(target=mqtt_receiver.launch_mqtt)
    proc_mqtt.start()
    time.sleep(2)

    dashboard.run_server(port=8050, host="0.0.0.0", debug=False)



