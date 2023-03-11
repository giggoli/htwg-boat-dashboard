from dash import dcc, html
import dash_bootstrap_components as dbc

fuelcell_status_e_i = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Indication (Status)"),
                html.Div(id="fuelcell_status_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_status_e_s = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Status (Status)"),
                html.Div(id="fuelcell_status_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOC_e_i = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Indication (SOC)"),
                html.Div(id="fuelcell_SOC_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOC_e_s = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Status (SOC)"),
                html.Div(id="fuelcell_SOC_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOV_e_i = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Indication (SOV)"),
                html.Div(id="fuelcell_SOV_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOV_e_s = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Status (SOV)"),
                html.Div(id="fuelcell_SOV_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOP_e_i = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Indication (SOP)"),
                html.Div(id="fuelcell_SOP_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOP_e_s = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Error Status (SOP)"),
                html.Div(id="fuelcell_SOP_e_i", children="no Value received")
            ]
        ),
    ],
)

fuelcell_status = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Status"),
                html.Div(id="fuelcell_status", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOC = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Output current"),
                html.Div(id="fuelcell_SOC", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOV = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Output voltage"),
                html.Div(id="fuelcell_SOV", children="no Value received")
            ]
        ),
    ],
)

fuelcell_SOP = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4(children="Output power"),
                html.Div(id="fuelcell_SOP", children="no Value received")
            ]
        ),
    ],
)