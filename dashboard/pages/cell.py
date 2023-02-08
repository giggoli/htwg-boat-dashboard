import dash
from dash import dcc, html, Output, Input
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=2)

layout = html.Div(
    children=[
        html.H1(children="Cell"),
        html.P(children="More content here"),
        html.Div(dcc.Link("to home", href="/solar")),
        dbc.Button("klick", id="btn1", n_clicks=0),
        html.P(children="", id="lbl1")
    ],
    className="body"
)


@dash.callback(
    Output("lbl1", "children"),
    Input("btn1", "n_clicks"),
)
def btnClicked(n_clicks):
    return "{}".format(n_clicks)