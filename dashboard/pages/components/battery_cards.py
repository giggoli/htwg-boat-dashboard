from dash import dcc, html
import dash_bootstrap_components as dbc

battery_BSR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Relay"),
                html.Div(id="battery_BSR", children="no Value received")
            ]
        ),
    ],
)

battery_BLVW = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Low voltage warning"),
                html.Div(id="battery_BLVW", children="no Value received")
            ]
        ),
    ],
)

battery_BHVW = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="High voltage warning"),
                html.Div(id="battery_BHVW", children="no Value received")
            ]
        ),
    ],
)

battery_BORC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Open relay crash"),
                html.Div(id="battery_BORC", children="no Value received")
            ]
        ),
    ],
)

battery_BORE = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Open relay error"),
                html.Div(id="battery_BORE", children="no Value received")
            ]
        ),
    ],
)

battery_SoC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery state of charge"),
                html.Div(id="battery_SoC", children="no Value received")
            ]
        ),
    ],
)

battery_E_NE = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error no error"),
                html.Div(id="battery_E_NE", children="no Value received")
            ]
        ),
    ],
)

battery_E_ST = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error selftest"),
                html.Div(id="battery_E_ST", children="no Value received")
            ]
        ),
    ],
)

battery_E_OC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error over current"),
                html.Div(id="battery_E_OC", children="no Value received")
            ]
        ),
    ],
)

battery_E_OV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error over voltage"),
                html.Div(id="battery_E_OV", children="no Value received")
            ]
        ),
    ],
)

battery_E_UV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error under voltage"),
                html.Div(id="battery_E_UV", children="no Value received")
            ]
        ),
    ],
)

battery_E_D = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error DIGOVLD"),
                html.Div(id="battery_E_D", children="no Value received")
            ]
        ),
    ],
)

battery_E_OUT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error over under temperature"),
                html.Div(id="battery_E_OUT", children="no Value received")
            ]
        ),
    ],
)

battery_E_P = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error over PARAMINIT"),
                html.Div(id="battery_E_P", children="no Value received")
            ]
        ),
    ],
)

battery_E_C = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error communication"),
                html.Div(id="battery_E_C", children="no Value received")
            ]
        ),
    ],
)

battery_E_H = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error HVIL"),
                html.Div(id="battery_E_H", children="no Value received")
            ]
        ),
    ],
)

battery_E_CP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error contactor plus"),
                html.Div(id="battery_E_CP", children="no Value received")
            ]
        ),
    ],
)

battery_E_CM = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error contactor minus"),
                html.Div(id="battery_E_CM", children="no Value received")
            ]
        ),
    ],
)

battery_E_CPC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error contactor pre charge"),
                html.Div(id="battery_E_CPC", children="no Value received")
            ]
        ),
    ],
)

battery_E_CD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error cell delta"),
                html.Div(id="battery_E_CD", children="no Value received")
            ]
        ),
    ],
)

battery_E_S = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error service"),
                html.Div(id="battery_E_S", children="no Value received")
            ]
        ),
    ],
)

battery_W_NE = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning no error"),
                html.Div(id="battery_W_NW", children="no Value received")
            ]
        ),
    ],
)

battery_W_ST = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning selftest"),
                html.Div(id="battery_W_ST", children="no Value received")
            ]
        ),
    ],
)

battery_W_OC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning over current"),
                html.Div(id="battery_W_OC", children="no Value received")
            ]
        ),
    ],
)

battery_W_OV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning over voltage"),
                html.Div(id="battery_W_OV", children="no Value received")
            ]
        ),
    ],
)

battery_W_UV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning under voltage"),
                html.Div(id="battery_W_UV", children="no Value received")
            ]
        ),
    ],
)

battery_W_D = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning DIGOVLD"),
                html.Div(id="battery_W_D", children="no Value received")
            ]
        ),
    ],
)

battery_W_OUT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning over under temperature"),
                html.Div(id="battery_W_OUT", children="no Value received")
            ]
        ),
    ],
)

battery_W_P = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning over PARAMINIT"),
                html.Div(id="battery_W_P", children="no Value received")
            ]
        ),
    ],
)

battery_W_C = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Warning communication"),
                html.Div(id="battery_W_C", children="no Value received")
            ]
        ),
    ],
)

battery_E_NID = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error node ID"),
                html.Div(id="battery_E_NID", children="no Value received")
            ]
        ),
    ],
)

battery_BV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC voltage"),
                html.Div(id="battery_BV", children="no Value received")
            ]
        ),
    ],
)

battery_BC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC current"),
                html.Div(id="battery_BC", children="no Value received")
            ]
        ),
    ],
)

battery_B_MSCV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC system maximum string cell voltage"),
                html.Div(id="battery_B_MSCV", children="no Value received")
            ]
        ),
    ],
)

battery_B_mSCV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC system minimum string cell voltage"),
                html.Div(id="battery_B_mSCV", children="no Value received")
            ]
        ),
    ],
)

battery_B_HS = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC system heater status"),
                html.Div(id="battery_B_HS", children="no Value received")
            ]
        ),
    ],
)

battery_SoH = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC SoH"),
                html.Div(id="battery_SoH", children="no Value received")
            ]
        ),
    ],
)

battery_B_HMT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC hottest module temperature"),
                html.Div(id="battery_B_HMT", children="no Value received")
            ]
        ),
    ],
)

battery_B_CMT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC coldest module temperature"),
                html.Div(id="battery_B_CMT", children="no Value received")
            ]
        ),
    ],
)

battery_SWV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC SW version"),
                html.Div(id="battery_SWV", children="no Value received")
            ]
        ),
    ],
)

battery_B_RS = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC relay status"),
                html.Div(id="battery_B_RS", children="no Value received")
            ]
        ),
    ],
)

battery_B_RC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC remaining capacity"),
                html.Div(id="battery_B_RC", children="no Value received")
            ]
        ),
    ],
)

battery_B_TR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC time remaining"),
                html.Div(id="battery_B_TR", children="no Value received")
            ]
        ),
    ],
)

battery_B_LC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC lifetime charged kWh"),
                html.Div(id="battery_B_LC", children="no Value received")
            ]
        ),
    ],
)

battery_B_IM = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC ISO monitor"),
                html.Div(id="battery_B_IM", children="no Value received")
            ]
        ),
    ],
)

battery_B_PCC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC permitted charge current"),
                html.Div(id="battery_B_PCC", children="no Value received")
            ]
        ),
    ],
)

battery_B_PDC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC permitted discharge current"),
                html.Div(id="battery_B_PDC", children="no Value received")
            ]
        ),
    ],
)

battery_B_AC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="AEC alive counter"),
                html.Div(id="battery_B_AC", children="no Value received")
            ]
        ),
    ],
)