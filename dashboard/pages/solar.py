import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json

import pages.components.solar_cards as solar_cards
import pages.components.solar_sys_cards as solar_sys_cards

dash.register_page(__name__, order=5)

layout = html.Div(
    children=[
        dcc.Store(id='store_solar', storage_type='session', data=dict()),
        dcc.Store(id='store_system', storage_type='session', data=dict()),
        WebSocket(id="solar_ws", url='ws://127.0.0.1:8123/daq/solar/data'),
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Solar")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([
                    solar_cards.solar_BV,
                    solar_cards.solar_CH,
                    solar_cards.solar_PVC,
                    solar_cards.solar_ROCH,
                    solar_cards.solar_SYSAH,
                    solar_cards.solar_YYD,
                    solar_cards.solar_YPVP,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([
                    solar_cards.solar_BC,
                    solar_cards.solar_CHM,
                    solar_cards.solar_EQP,
                    solar_cards.solar_SYSALRM,
                    solar_cards.solar_YTD,
                    solar_cards.solar_MPYD,
                    solar_cards.solar_UYPWR,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([
                    solar_cards.solar_BT,
                    solar_cards.solar_PVV,
                    solar_cards.solar_EQTR,
                    solar_cards.solar_SYSAL,
                    solar_cards.solar_MPTD,
                    solar_cards.solar_ERROR,
                    solar_cards.solar_MPPT,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),

        #### System ####
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="System")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([
                    solar_sys_cards.system_SolSerial,
                    solar_sys_cards.system_SYSBC,
                    solar_sys_cards.system_SYSSTATE,
                    solar_sys_cards.system_PVCP,
                    solar_sys_cards.system_SYSPWR,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([
                    solar_sys_cards.system_AIS,
                    solar_sys_cards.system_SYSBP,
                    solar_sys_cards.system_SYSCAH,
                    solar_sys_cards.system_PVCC,
                    solar_sys_cards.system_BUSCC,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([
                    solar_sys_cards.system_SYSBV,
                    solar_sys_cards.system_SYSSOC,
                    solar_sys_cards.system_SYST2G,
                    solar_sys_cards.system_SYSCP,
                    solar_sys_cards.system_BUSCP,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ],
)


@callback(
    output=[
        Output("solar_BV", "children", allow_duplicate=True),
        Output("solar_BC", "children", allow_duplicate=True),
        Output("solar_BT", "children", allow_duplicate=True),
        Output("solar_CH", "children", allow_duplicate=True),
        Output("solar_CHM", "children", allow_duplicate=True),
        Output("solar_PVV", "children", allow_duplicate=True),
        Output("solar_PVC", "children", allow_duplicate=True),
        Output("solar_EQP", "children", allow_duplicate=True),
        Output("solar_EQTR", "children", allow_duplicate=True),
        Output("solar_ROCH", "children", allow_duplicate=True),
        Output("solar_SYSALRM", "children", allow_duplicate=True),
        Output("solar_SYSAL", "children", allow_duplicate=True),
        Output("solar_SYSAH", "children", allow_duplicate=True),
        Output("solar_YTD", "children", allow_duplicate=True),
        Output("solar_MPTD", "children", allow_duplicate=True),
        Output("solar_YYD", "children", allow_duplicate=True),
        Output("solar_MPYD", "children", allow_duplicate=True),
        Output("solar_ERROR", "children", allow_duplicate=True),
        Output("solar_YPVP", "children", allow_duplicate=True),
        Output("solar_UYPWR", "children", allow_duplicate=True),
        Output("solar_MPPT", "children", allow_duplicate=True),
        Output("store_solar", "data")
    ],
    inputs=[
        Input("solar_ws", "message"),
    ],
    state=[
        State("solar_BV", "children"),
        State("solar_BC", "children"),
        State("solar_BT", "children"),
        State("solar_CH", "children"),
        State("solar_CHM", "children"),
        State("solar_PVV", "children"),
        State("solar_PVC", "children"),
        State("solar_EQP", "children"),
        State("solar_EQTR", "children"),
        State("solar_ROCH", "children"),
        State("solar_SYSALRM", "children"),
        State("solar_SYSAL", "children"),
        State("solar_SYSAH", "children"),
        State("solar_YTD", "children"),
        State("solar_MPTD", "children"),
        State("solar_YYD", "children"),
        State("solar_MPYD", "children"),
        State("solar_ERROR", "children"),
        State("solar_YPVP", "children"),
        State("solar_UYPWR", "children"),
        State("solar_MPPT", "children"),
        State("store_solar", "data")
    ],
    prevent_initial_call=True
)
def update_solar(msg, BV, BC, BT, CH, CHM, PVV, PVC, EQP, EQTR, ROCH, SYSALRM, SYSAL, SYSAH, YTD,
                 MPTD, YYD, MPYD, ERROR, YPVP, UYPWR, MPPT, storage):
    is_json, message_dict = validate_message(msg["data"])
    message = message_dict["Solar"]
    if is_json:
        BV = set_solar_BV(message["BV"])
        BC = set_solar_BC(message["BC"])
        BT = set_solar_BT(message["BT"])
        CH = set_solar_CH(message["CH"])
        CHM = set_solar_CHM(message["CHM"])
        PVV = set_solar_PVV(message["PVV"])
        PVC = set_solar_PVC(message["PVC"])
        EQP = set_solar_EQP(message["EQP"])
        EQTR = set_solar_EQTR(message["EQTR"])
        ROCH = set_solar_ROCH(message["ROCH"])
        SYSALRM = set_solar_SYSALRM(message["SYSALRM"])
        SYSAL = set_solar_SYSAL(message["SYSAL"])
        SYSAH = set_solar_SYSAH(message["SYSAH"])
        YTD = set_solar_YTD(message["YTD"])
        MPTD = set_solar_MPTD(message["MPTD"])
        YYD = set_solar_YYD(message["YYD"])
        MPYD = set_solar_MPYD(message["MPYD"])
        ERROR = set_solar_ERROR(message["ERROR"])
        YPVP = set_solar_YPVP(message["YPVP"])
        UYPWR = set_solar_UYPWR(message["UYPWR"])
        MPPT = set_solar_MPPT(message["MPPT"])

        storage["BV"] = BV
        storage["BC"] = BC
        storage["BT"] = BT
        storage["CH"] = CH
        storage["CHM"] = CHM
        storage["PVV"] = PVV
        storage["PVC"] = PVC
        storage["EQP"] = EQP
        storage["EQTR"] = EQTR
        storage["ROCH"] = ROCH
        storage["SYSALRM"] = SYSALRM
        storage["SYSAL"] = SYSAL
        storage["SYSAH"] = SYSAH
        storage["YTD"] = YTD
        storage["MPTD"] = MPTD
        storage["YYD"] = YYD
        storage["MPYD"] = MPYD
        storage["ERROR"] = ERROR
        storage["YPVP"] = YPVP
        storage["UYPWR"] = UYPWR
        storage["MPPT"] = MPPT

        return[
            BV, BC, BT, CH, CHM, PVV, PVC, EQP, EQTR, ROCH, SYSALRM, SYSAL, SYSAH, YTD,
            MPTD, YYD, MPYD, ERROR, YPVP, UYPWR, MPPT, storage
        ]
    else:
        return[
            BV, BC, BT, CH, CHM, PVV, PVC, EQP, EQTR, ROCH, SYSALRM, SYSAL, SYSAH, YTD,
            MPTD, YYD, MPYD, ERROR, YPVP, UYPWR, MPPT, storage
        ]

@callback(
    output=[
        Output("solar_BV", "children"),
        Output("solar_BC", "children"),
        Output("solar_BT", "children"),
        Output("solar_CH", "children"),
        Output("solar_CHM", "children"),
        Output("solar_PVV", "children"),
        Output("solar_PVC", "children"),
        Output("solar_EQP", "children"),
        Output("solar_EQTR", "children"),
        Output("solar_ROCH", "children"),
        Output("solar_SYSALRM", "children"),
        Output("solar_SYSAL", "children"),
        Output("solar_SYSAH", "children"),
        Output("solar_YTD", "children"),
        Output("solar_MPTD", "children"),
        Output("solar_YYD", "children"),
        Output("solar_MPYD", "children"),
        Output("solar_ERROR", "children"),
        Output("solar_YPVP", "children"),
        Output("solar_UYPWR", "children"),
        Output("solar_MPPT", "children")
    ],
    inputs=[Input("store_solar", "modified_timestamp")],
    state=[State("store_solar", "data")],     
)
def get_solar_storage(ts, data):
    if ts is None:
        raise PreventUpdate
    
    return[
        data.get("BV", "no Value received"),
        data.get("BC", "no Value received"),
        data.get("BT", "no Value received"),
        data.get("CH", "no Value received"),
        data.get("CHM", "no Value received"),
        data.get("PVV", "no Value received"),
        data.get("PVC", "no Value received"),
        data.get("EQP", "no Value received"),
        data.get("EQTR", "no Value received"),
        data.get("ROCH", "no Value received"),
        data.get("SYSALRM", "no Value received"),
        data.get("SYSAL", "no Value received"),
        data.get("SYSAH", "no Value received"),
        data.get("YTD", "no Value received"),
        data.get("MPTD", "no Value received"),
        data.get("YYD", "no Value received"),
        data.get("MPYD", "no Value received"),
        data.get("ERROR", "no Value received"),
        data.get("YPVP", "no Value received"),
        data.get("UYPWR", "no Value received"),
        data.get("MPPT", "no Value received")
    ]


@callback(
    output=[
        Output("system_SolSerial", "children", allow_duplicate=True),
        Output("system_AIS", "children", allow_duplicate=True),
        Output("system_SYSBV", "children", allow_duplicate=True),
        Output("system_SYSBC", "children", allow_duplicate=True),
        Output("system_SYSBP", "children", allow_duplicate=True),
        Output("system_SYSSOC", "children", allow_duplicate=True),
        Output("system_SYSSTATE", "children", allow_duplicate=True),
        Output("system_SYSCAH", "children", allow_duplicate=True),
        Output("system_SYST2G", "children", allow_duplicate=True),
        Output("system_PVCP", "children", allow_duplicate=True),
        Output("system_PVCC", "children", allow_duplicate=True),
        Output("system_SYSCP", "children", allow_duplicate=True),
        Output("system_SYSPWR", "children", allow_duplicate=True),
        Output("system_BUSCC", "children", allow_duplicate=True),
        Output("system_BUSCP", "children", allow_duplicate=True),
        Output("store_system", "data")
    ],
    inputs=[
        Input("solar_ws", "message"),
    ],
    state=[
        State("system_SolSerial", "children"),
        State("system_AIS", "children"),
        State("system_SYSBV", "children"),
        State("system_SYSBC", "children"),
        State("system_SYSBP", "children"),
        State("system_SYSSOC", "children"),
        State("system_SYSSTATE", "children"),
        State("system_SYSCAH", "children"),
        State("system_SYST2G", "children"),
        State("system_PVCP", "children"),
        State("system_PVCC", "children"),
        State("system_SYSCP", "children"),
        State("system_SYSPWR", "children"),
        State("system_BUSCC", "children"),
        State("system_BUSCP", "children"),
        State("store_system", "data")
    ],
    prevent_initial_call=True
)
def update_system(msg, SolSerial, AIS, SYSBV, SYSBC, SYSBP, SYSSOC, SYSSTATE, SYSCAH, SYST2G,
                  PVCP, PVCC, SYSCP, SYSPWR, BUSCC, BUSCP, storage):
    is_json, message_dict = validate_message(msg["data"])
    message = message_dict["System"]
    if is_json:
        SolSerial = set_system_SolSerial(message["SolSerial"])
        AIS = set_system_AIS(message["AIS"])
        SYSBV = set_system_SYSBV(message["SYSBV"])
        SYSBC = set_system_SYSBC(message["SYSBC"])
        SYSBP = set_system_SYSBP(message["SYSBP"])
        SYSSOC = set_system_SYSSOC(message["SYSSOC"])
        SYSSTATE = set_system_SYSSTATE(message["SYSSTATE"])
        SYSCAH = set_system_SYSCAH(message["SYSCAH"])
        SYST2G = set_system_SYST2G(message["SYST2G"])
        PVCP = set_system_PVCP(message["PVCP"])
        PVCC = set_system_PVCC(message["PVCC"])
        SYSCP = set_system_SYSCP(message["SYSCP"])
        SYSPWR = set_system_SYSPWR(message["SYSPWR"])
        BUSCC = set_system_BUSCC(message["BUSCC"])
        BUSCP = set_system_BUSCP(message["BUSCP"])

        storage["system_SolSerial"] = SolSerial
        storage["system_AIS"] = AIS
        storage["system_SYSBV"] = SYSBV
        storage["system_SYSBC"] = SYSBC
        storage["system_SYSBP"] = SYSBP
        storage["system_SYSSOC"] = SYSSOC
        storage["system_SYSSTATE"] = SYSSTATE
        storage["system_SYSCAH"] = SYSCAH
        storage["system_SYST2G"] = SYST2G
        storage["system_PVCP"] = PVCP
        storage["system_PVCC"] = PVCC
        storage["system_SYSCP"] = SYSCP
        storage["system_SYSPWR"] = SYSPWR
        storage["system_BUSCC"] = BUSCC
        storage["system_BUSCP"] = BUSCP

        return[
            SolSerial, AIS, SYSBV, SYSBC, SYSBP, SYSSOC, SYSSTATE, SYSCAH, SYST2G,
            PVCP, PVCC, SYSCP, SYSPWR, BUSCC, BUSCP, storage
        ]
    else:
        return[
            SolSerial, AIS, SYSBV, SYSBC, SYSBP, SYSSOC, SYSSTATE, SYSCAH, SYST2G,
            PVCP, PVCC, SYSCP, SYSPWR, BUSCC, BUSCP, storage
        ]

@callback(
    output=[
        Output("system_SolSerial", "children"),
        Output("system_AIS", "children"),
        Output("system_SYSBV", "children"),
        Output("system_SYSBC", "children"),
        Output("system_SYSBP", "children"),
        Output("system_SYSSOC", "children"),
        Output("system_SYSSTATE", "children"),
        Output("system_SYSCAH", "children"),
        Output("system_SYST2G", "children"),
        Output("system_PVCP", "children"),
        Output("system_PVCC", "children"),
        Output("system_SYSCP", "children"),
        Output("system_SYSPWR", "children"),
        Output("system_BUSCC", "children"),
        Output("system_BUSCP", "children"),
    ],
    inputs=[Input("store_system", "modified_timestamp")],
    state=[State("store_system", "data")]
)
def get_sytem_storage(ts, data):
    if ts is None:
        raise PreventUpdate
    
    return[
        data.get("system_SolSerial", "no Value received"),
        data.get("system_AIS", "no Value received"),
        data.get("system_SYSBV", "no Value received"),
        data.get("system_SYSBC", "no Value received"),
        data.get("system_SYSBP", "no Value received"),
        data.get("system_SYSSOC", "no Value received"),
        data.get("system_SYSSTATE", "no Value received"),
        data.get("system_SYSCAH", "no Value received"),
        data.get("system_SYST2G", "no Value received"),
        data.get("system_PVCP", "no Value received"),
        data.get("system_PVCC", "no Value received"),
        data.get("system_SYSCP", "no Value received"),
        data.get("system_SYSPWR", "no Value received"),
        data.get("system_BUSCC", "no Value received"),
        data.get("system_BUSCP", "no Value received")
    ]





def validate_message(msg):
    try:
        message = json.loads(msg)
        keys = ["BV", "BC", "BT", "CH", "CHM", "PVV", "PVC", "EQP", "EQTR",
                "ROCH", "SYSALRM", "SYSAL", "SYSAH", "YTD", "MPTD", "YYD",
                "MPYD", "ERROR", "YPVP", "UYPWR", "MPPT",]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"

    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]

def set_solar_BV(value):
    return f"{value} V"

def set_solar_BC(value):
    return f"{value} A"

def set_solar_BT(value):
    return f"{value} °C"
    

def set_solar_CH(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 1:
        content.children = "ON"
        content.color = "success"
        return content
    elif value == 4:
        content.children = "OFF"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_CHM(value):
    content = dbc.Alert(f"Value: {value} not defined", color="info", style={"textAlign": "center"})
    if value == 0:
        content.children = "OFF"
        content.color = "warning"
        return content
    elif value == 2:
        content.children = "Fault"
        content.color = "danger"
        return content
    elif value == 3:
        content.children = "Bulk"
        return content
    elif value == 4:
        content.children = "Absorption"
        return content
    elif value == 5:
        content.children = "Float"
        return content
    elif value == 6:
        content.children = "Storage"
        return content
    elif value == 7:
        content.children = "Equalize"
        return content
    elif value == 11:
        content.children = "Other"
        return content
    else:
        content.color = "warning"
        return content

def set_solar_PVV(value):
    return f"{value} V"

def set_solar_PVC(value):
    return f"{value} A"

def set_solar_EQP(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "NO"
        content.color = "primary"
        return content
    if value == 1:
        content.children = "Yes"
        content.color = "primary"
        return content
    if value == 2:
        content.children = "Error"
        content.color = "danger"
        return content
    elif value == 3:
        content.children = "Unavailable"
        content.color = "info"
        return content
    else:
        return content

def set_solar_EQTR(value):
    return f"{value} seconds"

def set_solar_ROCH(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "Open"
        content.color = "primary"
        return content
    if value == 1:
        content.children = "Closed"
        content.color = "primary"
        return content
    else:
        return content

def set_solar_SYSALRM(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Alarm"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Alarm"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_SYSAL(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Alarm"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Alarm"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_SYSAH(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Alarm"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Alarm"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_YTD(value):
    return f"{value} kWh"

def set_solar_MPTD(value):
    return f"{value} W"

def set_solar_YYD(value):
    return f"{value} kWh"

def set_solar_MPYD(value):
    return f"{value} W"

def set_solar_ERROR(value):
    content = dbc.Alert(f"Value: {value} not defined", color="danger", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Error"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Battery tempearture too high"
        return content
    if value == 2:
        content.children = "Battery voltage too high"
        return content
    if value == 3:
        content.children = "Battery temperature sensor misswired (+)"
        return content
    if value == 4:
        content.children = "Battery temperature sensor misswired (-)"
        return content
    if value == 5:
        content.children = "Battery temperature sensor disconnected"
        return content
    if value == 6:
        content.children = "Battery voltage sensor misswired (+)"
        return content
    if value == 7:
        content.children = "Battery voltage sensor misswired (-)"
        return content
    if value == 8:
        content.children = "Battery voltage sensor disconnected"
        return content
    if value == 9:
        content.children = "Battery voltage wire losses too high"
        return content
    if value == 17:
        content.children = "Charger temperature too high"
        return content
    if value == 18:
        content.children = "Charger over-current"
        return content
    if value == 19:
        content.children = "Charger current polarity reversed"
        return content
    if value == 20:
        content.children = "Bulk time limit reached"
        return content
    if value == 22:
        content.children = "Charger temperature sensor miswired"
        return content
    if value == 23:
        content.children = "Charger temperature sensor disconnected"
        return content
    if value == 34:
        content.children = "Input current too high"
        return content
    else:
        content.color = "warning"
        return content

def set_solar_YPVP(value):
    return f"{value} W"

def set_solar_UYPWR(value):
    return f"{value} kWh"

def set_solar_MPPT(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "Of"
        content.color = "danger"
        return content
    if value == 1:
        content.children = "Voltage/Current limited"
        content.color = "info"
        return content
    if value == 2:
        content.children = "MPPT active"
        content.color = "success"
        return content
    if value == 225:
        content.children = "Not available"
        return content
    else:
        return content

def set_system_SolSerial(value):
    return f"{value}"

def set_system_AIS(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "Unknown"
        return content
    if value == 1:
        content.children = "Grid"
        content.color = "success"
        return content
    if value == 2:
        content.children = "Generator"
        content.color = "success"
        return content
    if value == 3:
        content.children = "Shore power"
        content.color = "success"
        return content
    if value == 240:
        content.children = "Not connected"
        return content
    else:
        return content

def set_system_SYSBV(value):
    return f"{value} V"

def set_system_SYSBC(value):
    return f"{value} A"

def set_system_SYSBP(value):
    return f"{value} W"

def set_system_SYSSOC(value):
    return dbc.Progress(label=f"{value}%", value=value, style={"fontSize": "1em"})

def set_system_SYSSTATE(value):
    content = dbc.Alert(f"Value: {value} not defined", color="info", style={"textAlign": "center"})
    if value == 0:
        content.children = "idle"
        return content
    if value == 1:
        content.children = "charging"
        return content
    if value == 2:
        content.children = "discharging"
        return content
    else:
        content.color = "warning"
        return content

def set_system_SYSCAH(value):
    return f"{value} Ah"

def set_system_SYST2G(value):
    return f"{value} seconds"

def set_system_PVCP(value):
    return f"{value} W"

def set_system_PVCC(value):
    return f"{value} A"

def set_system_SYSCP(value):
    return f"{value} W"

def set_system_SYSPWR(value):
    return f"{value} W"

def set_system_BUSCC(value):
    return f"{value} A"

def set_system_BUSCP(value):
    return f"{value} W"
