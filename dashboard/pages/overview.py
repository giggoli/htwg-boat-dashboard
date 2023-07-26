import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
from dash.exceptions import PreventUpdate

from pages.components.solar_helper import validate_solar_message, set_solar_BV, set_solar_BC, set_solar_PVV, set_solar_PVC, set_solar_CH
from pages.components.battery_helper import validate_battery_message, set_battery_SoC, set_battery_BV, set_battery_B_RC, set_battery_BC
from pages.components.fuelcell_helper import validate_fuelcell_message, set_fuelcell_soc, set_fuelcell_sop, set_fuelcell_sov, set_fuelcell_status
from pages.components.fuellevel_helper import validate_fuellevel_message, set_fuellevel_FA
set_fuellevel_FA

dash.register_page(__name__, path="/")

home_button = dbc.Button(dbc.NavLink([html.Div("Back to all values")], href="/battery", active="exact"),color="primary", outline=True)




solar_content = html.Div(children=[
    dbc.Row([html.H5("Solar"),]),
    dbc.Row([
        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Battery voltage"),
                    html.Div(id="solar_BV_2", children="no Value received")
                ])
            ]),
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="PV voltage"),
                    html.Div(id="solar_PVV_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),

        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Battery current"),
                    html.Div(id="solar_BC_2", children="no Value received")
                ])
            ]),
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="PV current"),
                    html.Div(id="solar_PVC_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
    ]),
    dbc.Card([dbc.CardBody(
        [
            html.H4(children="Charger on/off"),
            html.Div(id="solar_CH_2", children="no Value received")
        ])
    ]),
])

battery_content = html.Div(children=[
    dbc.Row([html.H5("Battery"),]),
    dbc.Row([
        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Battery state of charge"),
                    html.Div(id="battery_SoC_2", children="no Value received")
                ])
            ]),
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="AEC voltage"),
                    html.Div(id="battery_BV_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),

        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="AEC remaining capacity"),
                    html.Div(id="battery_B_RC_2", children="no Value received")
                ])
            ]),
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="AEC current"),
                    html.Div(id="battery_BC_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
    ]), 
])

fuelcell_content = html.Div(children=[
    dbc.Row([html.H5("Fuelcell"),]),
    dbc.Row([
        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Output current"),
                    html.Div(id="fuelcell_SOC_2", children="no Value received")
                ])
            ]),
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Output power"),
                    html.Div(id="fuelcell_SOP_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),

        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Output voltage"),
                    html.Div(id="fuelcell_SOV_2", children="no Value received")
                ])
            ]),
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Status"),
                    html.Div(id="fuelcell_status_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
    ]),    
])

fuellevel_content = html.Div(children=[
    dbc.Row([html.H5("Fuellevel"),]),
    dbc.Row([
        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Fuellevel"),
                    html.Div(id="fuellevel_FL_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),

        dbc.Col([
            dbc.Card([dbc.CardBody(
                [
                    html.H4(children="Fuelamount"),
                    html.Div(id="fuellevel_FA_2", children="no Value received")
                ])
            ]),
        ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
    ]),
])

websockets = html.Div(
    children=[
        WebSocket(id="solar_ws2", url='ws://127.0.0.1:8123/daq/solar/data'),
        WebSocket(id="battery_ws2", url='ws://127.0.0.1:8123/daq/battery/data'),
        WebSocket(id="fuelcell_ws2", url="ws://127.0.0.1:8123/daq/fuelcell/data"),
        WebSocket(id="fuellevel_ws2", url='ws://127.0.0.1:8123/daq/fuellevel/data'),
    ]
)

layout = dbc.Container(
        dbc.Row(
            [
                dbc.Col([],xs=1, sm=1, md=1, lg=1, xl=1, xxl=1),
                dbc.Col([
                    websockets,
                    solar_content,
                    battery_content,
                    fuelcell_content,
                    fuellevel_content,
                    home_button
                ],xs=10, sm=10, md=10, lg=10, xl=10, xxl=10, className="overview-row"),
                dbc.Col([],xs=1, sm=1, md=1, lg=1, xl=1, xxl=1),
            ]
        ), fluid=True
)

@callback(
    output=[
        Output("solar_BV_2", "children"),
        Output("solar_PVV_2", "children"),
        Output("solar_BC_2", "children"),
        Output("solar_PVC_2", "children"),
        Output("solar_CH_2", "children"),
    ],
    inputs=[
        Input("solar_ws2", "message"),
    ],
    state=[
        State("solar_BV_2", "children"),
        State("solar_PVV_2", "children"),
        State("solar_BC_2", "children"),
        State("solar_PVC_2", "children"),
        State("solar_CH_2", "children"),
    ],
    prevent_initial_call=True
)
def update_solar_view(solar_msg, bv, pvv, bc, pvc, ch):
    if solar_msg is  None:
        raise PreventUpdate
    is_json, msg = validate_solar_message(solar_msg["data"])
    
    if is_json:
        bv = set_solar_BV(msg["BV"])
        bc = set_solar_BC(msg["BC"])
        pvv = set_solar_PVV(msg["PVV"])
        pvc = set_solar_PVC(msg["PVC"])
        ch = set_solar_CH(msg["CH"])
        return [bv, bc, pvv, pvc, ch]
    else:
        return [bv, bc, pvv, pvc, ch]


@callback(
    output=[
        Output("battery_SoC_2", "children"),
        Output("battery_BV_2", "children"),
        Output("battery_B_RC_2", "children"),
        Output("battery_BC_2", "children"),
    ],
    inputs=[
        Input("battery_ws2", "message"),
    ],
    state=[
        State("battery_SoC_2", "children"),
        State("battery_BV_2", "children"),
        State("battery_B_RC_2", "children"),
        State("battery_BC_2", "children"),
    ],
    prevent_initial_call=True
)
def update_battery_view(battery_msg, soc, bv, brc, bc):
    if battery_msg is  None:
        raise PreventUpdate
    is_json, msg = validate_battery_message(battery_msg["data"])
    if is_json:
        soc = set_battery_SoC(msg["SoC"])
        bv = set_battery_BV(msg["BV"])
        brc = set_battery_B_RC(msg["B_RC"])
        bc = set_battery_BC(msg["BC"])
        return [soc, bv, brc, bc]
    else:
        return [soc, bv, brc, bc]


@callback(
    output=[
        Output("fuelcell_SOC_2", "children"),
        Output("fuelcell_SOP_2", "children"),
        Output("fuelcell_SOV_2", "children"),
        Output("fuelcell_status_2", "children"),
    ],
    inputs=[
        Input("fuelcell_ws2", "message"),
    ],
    state=[
        State("fuelcell_SOC_2", "children"),
        State("fuelcell_SOP_2", "children"),
        State("fuelcell_SOV_2", "children"),
        State("fuelcell_status_2", "children"),
    ],
    prevent_initial_call=True
)
def update_fuelcell_view(fuelcell_msg, soc, sop, sov, status):
    if fuelcell_msg is  None:
        raise PreventUpdate
    is_json, msg = validate_fuelcell_message(fuelcell_msg["data"])
    if is_json:
        soc = set_fuelcell_soc(msg["SOC"])
        sop = set_fuelcell_sop(msg["SOP"])
        sov = set_fuelcell_sov(msg["SOV"])
        status = set_fuelcell_status(msg["status"])
        return [soc, sop, sov, status]
    else: 
        return [soc, sop, sov, status]        

@callback(
    output=[
        Output("fuellevel_FL_2", "children"),
        Output("fuellevel_FA_2", "children"),
    ],
    inputs=[
        Input("fuellevel_ws2", "message"),
    ],
    state=[
        State("fuellevel_FL_2", "children"),
        State("fuellevel_FA_2", "children"),
    ],
    prevent_initial_call=True
)
def update_fuellevel_view(fuellevel_msg, fl, fa):
    if fuellevel_msg is  None:
        raise PreventUpdate
    is_json, msg = validate_fuellevel_message(fuellevel_msg["data"])
    if is_json:
        fl = set_fuellevel_FA(msg["FL"])
        fa = set_fuellevel_FA(msg["FA"])
        return [fl, fa]
    else:
        return [fl, fa]