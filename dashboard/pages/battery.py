import dash
from dash import dcc, html, callback, Input, Output, State
import dash_bootstrap_components as dbc
from dash_extensions import WebSocket
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import json
import pages.components.battery_cards as battery_cards
from pages.components.battery_helper import *
import pages.sidebar as sidebar

dash.register_page(__name__, order=1)

page_layout = html.Div(
    children=[
        WebSocket(id="battery_ws", url='ws://127.0.0.1:8123/daq/battery/data'),
        dbc.Row(
            [
                dbc.Col([
                    html.H3(children="Battery")
                ],xs=12, sm=12, md=12, lg=12, xl=12, xxl=12)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col(
                [
                    battery_cards.battery_SoC,
                    battery_cards.battery_SoH,
                    battery_cards.battery_E_NID,
                    battery_cards.battery_B_TR,
                    battery_cards.battery_B_RC,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                
                dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    battery_cards.battery_BV,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_MSCV,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_mSCV,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    battery_cards.battery_BC,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_PCC,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_PDC,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    battery_cards.battery_B_HS,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_HMT,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_CMT,
                                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                        ]
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    battery_cards.battery_SWV,
                                ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                            dbc.Col(
                                [
                                    battery_cards.battery_B_IM,
                                ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                        ],
                    )
                ],xs=8, sm=8, md=8, lg=8, xl=8, xxl=8),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        battery_cards.battery_B_LC,
                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
                dbc.Col(
                    [
                        battery_cards.battery_B_AC,
                    ],xs=6, sm=6, md=6, lg=6, xl=6, xxl=6),
            ], className="row-buffer"
        ),
        dbc.Row(
            [
                dbc.Col(
                [
                    battery_cards.battery_BSR,
                    battery_cards.battery_BORC,
                    battery_cards.battery_E_NE,
                    battery_cards.battery_E_OV,
                    battery_cards.battery_E_OUT,
                    battery_cards.battery_E_H,
                    battery_cards.battery_E_CPC,
                    battery_cards.battery_W_NE,
                    battery_cards.battery_W_OV,
                    battery_cards.battery_W_OUT,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col(
                [
                    battery_cards.battery_BLVW,
                    battery_cards.battery_BORE,
                    battery_cards.battery_E_ST,
                    battery_cards.battery_E_UV,
                    battery_cards.battery_E_P,
                    battery_cards.battery_E_CP,
                    battery_cards.battery_E_CD,
                    battery_cards.battery_W_ST,
                    battery_cards.battery_W_UV,
                    battery_cards.battery_W_P,
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col(
                [
                    battery_cards.battery_BHVW,
                    battery_cards.battery_E_OC,
                    battery_cards.battery_E_D,
                    battery_cards.battery_E_C,
                    battery_cards.battery_E_CM,
                    battery_cards.battery_E_S,
                    battery_cards.battery_W_OC,
                    battery_cards.battery_W_D,
                    battery_cards.battery_W_C,
                    battery_cards.battery_B_RS,
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
        Output("battery_BSR", "children", allow_duplicate=True),
        Output("battery_BLVW", "children", allow_duplicate=True),
        Output("battery_BHVW", "children", allow_duplicate=True),
        Output("battery_BORC", "children", allow_duplicate=True),
        Output("battery_BORE", "children", allow_duplicate=True),
        Output("battery_SoC", "children", allow_duplicate=True),
        Output("battery_E_NE", "children", allow_duplicate=True),
        Output("battery_E_ST", "children", allow_duplicate=True),
        Output("battery_E_OC", "children", allow_duplicate=True),
        Output("battery_E_OV", "children", allow_duplicate=True),
        Output("battery_E_UV", "children", allow_duplicate=True),
        Output("battery_E_D", "children", allow_duplicate=True),
        Output("battery_E_OUT", "children", allow_duplicate=True),
        Output("battery_E_P", "children", allow_duplicate=True),
        Output("battery_E_C", "children", allow_duplicate=True),
        Output("battery_E_H", "children", allow_duplicate=True),
        Output("battery_E_CP", "children", allow_duplicate=True),
        Output("battery_E_CM", "children", allow_duplicate=True),
        Output("battery_E_CPC", "children", allow_duplicate=True),
        Output("battery_E_CD", "children", allow_duplicate=True),
        Output("battery_E_S", "children", allow_duplicate=True),
        Output("battery_W_NE", "children", allow_duplicate=True),
        Output("battery_W_ST", "children", allow_duplicate=True),
        Output("battery_W_OC", "children", allow_duplicate=True),
        Output("battery_W_OV", "children", allow_duplicate=True),
        Output("battery_W_UV", "children", allow_duplicate=True),
        Output("battery_W_D", "children", allow_duplicate=True),
        Output("battery_W_OUT", "children", allow_duplicate=True),
        Output("battery_W_P", "children", allow_duplicate=True),
        Output("battery_W_C", "children", allow_duplicate=True),
        Output("battery_E_NID", "children", allow_duplicate=True),
        Output("battery_BV", "children", allow_duplicate=True),
        Output("battery_BC", "children", allow_duplicate=True),
        Output("battery_B_MSCV", "children", allow_duplicate=True),
        Output("battery_B_mSCV", "children", allow_duplicate=True),
        Output("battery_B_HS", "children", allow_duplicate=True),
        Output("battery_SoH", "children", allow_duplicate=True),
        Output("battery_B_HMT", "children", allow_duplicate=True),
        Output("battery_B_CMT", "children", allow_duplicate=True),
        Output("battery_SWV", "children", allow_duplicate=True),
        Output("battery_B_RS", "children", allow_duplicate=True),
        Output("battery_B_RC", "children", allow_duplicate=True),
        Output("battery_B_TR", "children", allow_duplicate=True),
        Output("battery_B_LC", "children", allow_duplicate=True),
        Output("battery_B_IM", "children", allow_duplicate=True),
        Output("battery_B_PCC", "children", allow_duplicate=True),
        Output("battery_B_PDC", "children", allow_duplicate=True),
        Output("battery_B_AC", "children", allow_duplicate=True),
        Output("store_battery", "data")
    ],
    inputs=[
        Input("battery_ws", "message"),
    ],
    state=[
        State("battery_BSR", "children"),
        State("battery_BLVW", "children"),
        State("battery_BHVW", "children"),
        State("battery_BORC", "children"),
        State("battery_BORE", "children"),
        State("battery_SoC", "children"),
        State("battery_E_NE", "children"),
        State("battery_E_ST", "children"),
        State("battery_E_OC", "children"),
        State("battery_E_OV", "children"),
        State("battery_E_UV", "children"),
        State("battery_E_D", "children"),
        State("battery_E_OUT", "children"),
        State("battery_E_P", "children"),
        State("battery_E_C", "children"),
        State("battery_E_H", "children"),
        State("battery_E_CP", "children"),
        State("battery_E_CM", "children"),
        State("battery_E_CPC", "children"),
        State("battery_E_CD", "children"),
        State("battery_E_S", "children"),
        State("battery_W_NE", "children"),
        State("battery_W_ST", "children"),
        State("battery_W_OC", "children"),
        State("battery_W_OV", "children"),
        State("battery_W_UV", "children"),
        State("battery_W_D", "children"),
        State("battery_W_OUT", "children"),
        State("battery_W_P", "children"),
        State("battery_W_C", "children"),
        State("battery_E_NID", "children"),
        State("battery_BV", "children"),
        State("battery_BC", "children"),
        State("battery_B_MSCV", "children"),
        State("battery_B_mSCV", "children"),
        State("battery_B_HS", "children"),
        State("battery_SoH", "children"),
        State("battery_B_HMT", "children"),
        State("battery_B_CMT", "children"),
        State("battery_SWV", "children"),
        State("battery_B_RS", "children"),
        State("battery_B_RC", "children"),
        State("battery_B_TR", "children"),
        State("battery_B_LC", "children"),
        State("battery_B_IM", "children"),
        State("battery_B_PCC", "children"),
        State("battery_B_PDC", "children"),
        State("battery_B_AC", "children"),
State("store_battery", "data")
    ],
    prevent_initial_call=True
)
def update_battery(msg, BSR, BLVW, BHVW, BORC, BORE, SoC, E_NE, E_ST, E_OC, E_OV, E_UV,
                   E_D, E_OUT, E_P, E_C, E_H,E_CP, E_CM, E_CPC, E_CD, E_S, W_NE, W_ST, W_OC,
                   W_OV, W_UV, W_D, W_OUT, W_P, W_C, E_NID, BV, BC, B_MSCV, B_mSCV, B_HS,
                   SoH, B_HMT, B_CMT, SWV, B_RS, B_RC, B_TR, B_LC, B_IM, B_PCC, B_PDC, B_AC, storage):
    if msg is None:
        raise PreventUpdate
    is_json, message = validate_battery_message(msg["data"])
    if is_json:
        BSR = set_battery_BSR(message["BSR"])
        BLVW = set_battery_BLVW(message["BLVW"])
        BHVW = set_battery_BHVW(message["BHVW"])
        BORC = set_battery_BORC(message["BORC"])
        BORE = set_battery_BORE(message["BORE"])
        SoC = set_battery_SoC(message["SoC"])
        E_NE = set_battery_E_NE(message["E_NE"])
        E_ST = set_battery_E_ST(message["E_ST"])
        E_OC = set_battery_E_OC(message["E_OC"])
        E_OV = set_battery_E_OV(message["E_OV"])
        E_UV = set_battery_E_UV(message["E_UV"])
        E_D = set_battery_E_D(message["E_D"])
        E_OUT = set_battery_E_OUT(message["E_OUT"])
        E_P = set_battery_E_P(message["E_P"])
        E_C = set_battery_E_C(message["E_C"])
        E_H = set_battery_E_H(message["E_H"])
        E_CP = set_battery_E_CM(message["E_CP"])
        E_CM = set_battery_E_CM(message["E_CM"])
        E_CPC = set_battery_E_CPC(message["E_CPC"])
        E_CD = set_battery_E_CD(message["E_CD"])
        E_S = set_battery_E_S(message["E_S"])
        W_NE = set_battery_W_NE(message["W_NE"])
        W_ST = set_battery_W_ST(message["W_ST"])
        W_OC = set_battery_W_OC(message["W_OC"])
        W_OV = set_battery_W_OV(message["W_OV"])
        W_UV = set_battery_W_UV(message["W_UV"])
        W_D = set_battery_W_D(message["W_D"])
        W_OUT = set_battery_W_OUT(message["W_OUT"])
        W_P = set_battery_W_P(message["W_P"])
        W_C = set_battery_W_C(message["W_C"])
        E_NID = set_battery_E_NID(message["E_NID"])
        BV = set_battery_BV(message["BV"])
        BC = set_battery_BC(message["BC"])
        B_MSCV = set_battery_B_MSCV(message["B_MSCV"])
        B_mSCV = set_battery_B_mSCV(message["B_mSCV"])
        B_HS = set_battery_B_HS(message["B_HS"])
        SoH = set_battery_SoH(message["SoH"])
        B_HMT = set_battery_B_HMT(message["B_HMT"])
        B_CMT = set_battery_B_CMT(message["B_CMT"])
        SWV = set_battery_SWV(message["SWV"])
        B_RS = set_battery_B_RS(message["B_RS"])
        B_RC = set_battery_B_RC(message["B_RC"])
        B_TR = set_battery_B_TR(message["B_TR"])
        B_LC = set_battery_B_LC(message["B_LC"])
        B_IM = set_battery_B_IM(message["B_IM"])
        B_PCC = set_battery_B_PCC(message["B_PCC"])
        B_PDC = set_battery_B_PDC(message["B_PDC"])
        B_AC = set_battery_B_AC(message["B_AC"])

        storage["BSR"] = BSR
        storage["BLVW"] = BLVW
        storage["BHVW"] = BHVW
        storage["BORC"] = BORC
        storage["BORE"] = BORE
        storage["SoC"] = SoC
        storage["E_NE"] = E_NE
        storage["E_ST"] = E_ST
        storage["E_OC"] = E_OC
        storage["E_OV"] = E_OV
        storage["E_UV"] = E_UV
        storage["E_D"] = E_D
        storage["E_OUT"] = E_OUT
        storage["E_P"] = E_P
        storage["E_C"] = E_C
        storage["E_H"] = E_H
        storage["E_CP"] = E_CP
        storage["E_CM"] = E_CM
        storage["E_CPC"] = E_CPC
        storage["E_CD"] = E_CD
        storage["E_S"] = E_S
        storage["W_NE"] = W_NE
        storage["W_ST"] = W_ST
        storage["W_OC"] = W_OC
        storage["W_OV"] = W_OV
        storage["W_UV"] = W_UV
        storage["W_D"] = W_D
        storage["W_OUT"] = W_OUT
        storage["W_P"] = W_P
        storage["W_C"] = W_C
        storage["E_NID"] = E_NID
        storage["BV"] = BV
        storage["BC"] = BC
        storage["B_MSCV"] = B_MSCV
        storage["B_mSCV"] = B_mSCV
        storage["B_HS"] = B_HS
        storage["SoH"] = SoH
        storage["B_HMT"] = B_HMT
        storage["B_CMT"] = B_CMT
        storage["SWV"] = SWV
        storage["B_RS"] = B_RS
        storage["B_RC"] = B_RC
        storage["B_TR"] = B_TR
        storage["B_LC"] = B_LC
        storage["B_IM"] = B_IM
        storage["B_PCC"] = B_PCC
        storage["B_PDC"] = B_PDC
        storage["B_AC"] = B_AC
        
        return[
            BSR, BLVW, BHVW, BORC, BORE, SoC, E_NE, E_ST, E_OC, E_OV, E_UV,
            E_D, E_OUT, E_P, E_C, E_H, E_CP, E_CM, E_CPC, E_CD, E_S, W_NE, W_ST, W_OC,
            W_OV, W_UV, W_D, W_OUT, W_P, W_C, E_NID, BV, BC, B_MSCV, B_mSCV, B_HS,
            SoH, B_HMT, B_CMT, SWV, B_RS, B_RC, B_TR, B_LC, B_IM, B_PCC, B_PDC, B_AC, storage
        ]
    else:
        return[
            BSR, BLVW, BHVW, BORC, BORE, SoC, E_NE, E_ST, E_OC, E_OV, E_UV,
            E_D, E_OUT, E_P, E_C, E_H, E_CP, E_CM, E_CPC, E_CD, E_S, W_NE, W_ST, W_OC,
            W_OV, W_UV, W_D, W_OUT, W_P, W_C, E_NID, BV, BC, B_MSCV, B_mSCV, B_HS,
            SoH, B_HMT, B_CMT, SWV, B_RS, B_RC, B_TR, B_LC, B_IM, B_PCC, B_PDC, B_AC, storage
        ]

@callback(
    output=[
        Output("battery_BSR", "children"),
        Output("battery_BLVW", "children"),
        Output("battery_BHVW", "children"),
        Output("battery_BORC", "children"),
        Output("battery_BORE", "children"),
        Output("battery_SoC", "children"),
        Output("battery_E_NE", "children"),
        Output("battery_E_ST", "children"),
        Output("battery_E_OC", "children"),
        Output("battery_E_OV", "children"),
        Output("battery_E_UV", "children"),
        Output("battery_E_D", "children"),
        Output("battery_E_OUT", "children"),
        Output("battery_E_P", "children"),
        Output("battery_E_C", "children"),
        Output("battery_E_H", "children"),
        Output("battery_E_CP", "children"),
        Output("battery_E_CM", "children"),
        Output("battery_E_CPC", "children"),
        Output("battery_E_CD", "children"),
        Output("battery_E_S", "children"),
        Output("battery_W_NE", "children"),
        Output("battery_W_ST", "children"),
        Output("battery_W_OC", "children"),
        Output("battery_W_OV", "children"),
        Output("battery_W_UV", "children"),
        Output("battery_W_D", "children"),
        Output("battery_W_OUT", "children"),
        Output("battery_W_P", "children"),
        Output("battery_W_C", "children"),
        Output("battery_E_NID", "children"),
        Output("battery_BV", "children"),
        Output("battery_BC", "children"),
        Output("battery_B_MSCV", "children"),
        Output("battery_B_mSCV", "children"),
        Output("battery_B_HS", "children"),
        Output("battery_SoH", "children"),
        Output("battery_B_HMT", "children"),
        Output("battery_B_CMT", "children"),
        Output("battery_SWV", "children"),
        Output("battery_B_RS", "children"),
        Output("battery_B_RC", "children"),
        Output("battery_B_TR", "children"),
        Output("battery_B_LC", "children"),
        Output("battery_B_IM", "children"),
        Output("battery_B_PCC", "children"),
        Output("battery_B_PDC", "children"),
        Output("battery_B_AC", "children"),
    ],
    inputs=[Input("store_battery", "modified_timestamp")],
    state=[State("store_battery", "data")],
)
def get_battery_storage(ts, data):
    if ts is None:
        raise PreventUpdate
    
    return[
        data.get("BSR", "no Value received"),
        data.get("BLVW", "no Value received"),
        data.get("BHVW", "no Value received"),
        data.get("BORC", "no Value received"),
        data.get("BORE", "no Value received"),
        data.get("SoC", "no Value received"),
        data.get("E_NE", "no Value received"),
        data.get("E_ST", "no Value received"),
        data.get("E_OC", "no Value received"),
        data.get("E_OV", "no Value received"),
        data.get("E_UV", "no Value received"),
        data.get("E_D", "no Value received"),
        data.get("E_OUT", "no Value received"),
        data.get("E_P", "no Value received"),
        data.get("E_C", "no Value received"),
        data.get("E_H", "no Value received"),
        data.get("E_CP", "no Value received"),
        data.get("E_CM", "no Value received"),
        data.get("E_CPC", "no Value received"),
        data.get("E_CD", "no Value received"),
        data.get("E_S", "no Value received"),
        data.get("W_NE", "no Value received"),
        data.get("W_ST", "no Value received"),
        data.get("W_OC", "no Value received"),
        data.get("W_OV", "no Value received"),
        data.get("W_UV", "no Value received"),
        data.get("W_D", "no Value received"),
        data.get("W_OUT", "no Value received"),
        data.get("W_P", "no Value received"),
        data.get("W_C", "no Value received"),
        data.get("E_NID", "no Value received"),
        data.get("BV", "no Value received"),
        data.get("BC", "no Value received"),
        data.get("B_MSCV", "no Value received"),
        data.get("B_mSCV", "no Value received"),
        data.get("B_HS", "no Value received"),
        data.get("SoH", "no Value received"),
        data.get("B_HMT", "no Value received"),
        data.get("B_CMT", "no Value received"),
        data.get("SWV", "no Value received"),
        data.get("B_RS", "no Value received"),
        data.get("B_RC", "no Value received"),
        data.get("B_TR", "no Value received"),
        data.get("B_LC", "no Value received"),
        data.get("B_IM", "no Value received"),
        data.get("B_PCC", "no Value received"),
        data.get("B_PDC", "no Value received"),
        data.get("B_AC", "no Value received")
    ]

