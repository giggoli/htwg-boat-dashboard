from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


system_SolSerial = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Serial number of solar generator"),
                html.Div(id="system_SolSerial ", children="no Value received")
            ]
        ),
    ],
)

system_AIS = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Active input source"),
                html.Div(id="system_AIS ", children="no Value received")
            ]
        ),
    ],
)

system_SYSBV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="System battery power"),
                html.Div(id="system_SYSBV", children="no Value received")
            ]
        ),
    ],
)

system_SYSBC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="System battery current"),
                html.Div(id="system_SYSBC", children="no Value received")
            ]
        ),
    ],
)

system_SYSBP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="System battery power"),
                html.Div(id="system_SYSBP", children="no Value received")
            ]
        ),
    ],
)

system_SYSSOC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery state of charge"),
                html.Div(id="SYSSOC", children="no Value received")
            ]
        ),
    ],
)

system_SYSSTATE = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery state"),
                html.Div(id="system_SYSSTATE", children="no Value received")
            ]
        ),
    ],
)

system_SYSCAH = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Battery consumend Amphours"),
                html.Div(id="system_SYSCAH", children="no Value received")
            ]
        ),
    ],
)

system_SYST2G = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="System time to go"),
                html.Div(id="system_SYST2G", children="no Value received")
            ]
        ),
    ],
)

system_PVCP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="PV DC-coupled power"),
                html.Div(id="system_PVCP", children="no Value received")
            ]
        ),
    ],
)

system_PVCC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="PV DC-coupled current"),
                html.Div(id="system_PVCC", children="no Value received")
            ]
        ),
    ],
)

system_SYSCP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="System charger power"),
                html.Div(id="system_SYSCP", children="no Value received")
            ]
        ),
    ],
)

system_SYSPWR = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="DC system power"),
                html.Div(id="system_SYSPWR", children="no Value received")
            ]
        ),
    ],
)

system_BUSCC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Victron Bus charge current"),
                html.Div(id="system_BUSCC", children="no Value received")
            ]
        ),
    ],
)

system_BUSCP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Victron Bus charge power"),
                html.Div(id="system_BUSCP", children="no Value received")
            ]
        ),
    ],
)