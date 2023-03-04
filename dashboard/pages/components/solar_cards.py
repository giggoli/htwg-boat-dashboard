import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


solar_BV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery voltage"),
                html.Div(id="solar_BV", children="no Value received")
            ]
        ),
    ],
)
solar_BC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery current"),
                html.Div(id="solar_BC", children="no Value received")
            ]
        ),
    ],
)

solar_BT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery temperature"),
                html.Div(id="solar_BT", children="no Value received")
            ]
        ),
    ],
)

solar_CH = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Charger on/off"),
                html.Div(id="solar_CH", children="no Value received")
            ]
        ),
    ],
)

solar_CHM = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Charger mode"),
                html.Div(id="solar_CHM", children="no Value received")
            ]
        ),
    ],
)

solar_PVV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="PV voltage"),
                html.Div(id="solar_PVV", children="no Value received")
            ]
        ),
    ],
)

solar_PVC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="PV current"),
                html.Div(id="solar_PVC", children="no Value received")
            ]
        ),
    ],
)

solar_EQP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Equalization pending"),
                html.Div(id="solar_EQP", children="no Value received")
            ]
        ),
    ],
)

solar_EQTR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Equalization time remaining"),
                html.Div(id="solar_EQTR", children="no Value received")
            ]
        ),
    ],
)

solar_ROCH = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Relay on charger"),
                html.Div(id="solar_ROCH", children="no Value received")
            ]
        ),
    ],
)

solar_SYSALRM = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="System alarm"),
                html.Div(id="solar_SYSALRM", children="no Value received")
            ]
        ),
    ],
)

solar_SYSAL = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Low voltage alarm"),
                html.Div(id="solar_SYSAL", children="no Value received")
            ]
        ),
    ],
)

solar_SYSAH = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="High volatge alarm"),
                html.Div(id="solar_ESYSAH", children="no Value received")
            ]
        ),
    ],
)

solar_YTD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Yield today"),
                html.Div(id="solar_YTD", children="no Value received")
            ]
        ),
    ],
)

solar_MPTD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Maximum charge power today"),
                html.Div(id="solar_MPTD", children="no Value received")
            ]
        ),
    ],
)

solar_YYD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Yield yesterday"),
                html.Div(id="solar_YYD", children="no Value received")
            ]
        ),
    ],
)

solar_MPYD = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Maximum charge power yesterday"),
                html.Div(id="solar_MPYD", children="no Value received")
            ]
        ),
    ],
)

solar_ERROR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error code"),
                html.Div(id="solar_ERROR", children="no Value received")
            ]
        ),
    ],
)

solar_YPVP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Yield PV power"),
                html.Div(id="solar_YPVP", children="no Value received")
            ]
        ),
    ],
)

solar_UYPWR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Yield user power"),
                html.Div(id="solar_UYPWR", children="no Value received")
            ]
        ),
    ],
)

solar_MPPT = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="MPP operation mode"),
                html.Div(id="solar_MPPT", children="no Value received")
            ]
        ),
    ],
)