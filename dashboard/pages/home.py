import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc


dash.register_page(__name__, path="/", order=0)

card_selector = html.Div(
    [
        dbc.Button("Select Cards", id="card_selector",n_clicks=0),
        dbc.Modal(
            [
                dbc.ModalHeader(
                    dbc.ModalTitle("Select Cards"),
                    close_button = False,
                ),
                dbc.ModalBody(
                    html.P("content of modal"),
                ),
                dbc.ModalFooter(
                    dbc.Button("set", id="set_cards", n_clicks=0)
                ),
            ],
            id="modal_card_selector",
            is_open = False,
            backdrop = "static",
            centered = True,
        )
    ]
)


#############################
#### LAYOUT of the page #####
#############################
layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col([
                    html.H4(children="Welcome to the Dashboard"),
                    html.P("On this Page you can selcet a bunch of cards top get a quick look at stats from the Boat. But be aware that after a reload you'll have to select the cards again.")
                ],xs=11, sm=11, md=11, lg=11, xl=11, xxl=11),
                dbc.Col([
                    card_selector,
                ],xs=1, sm=1, md=1, lg=1, xl=1, xxl=1)
            ], className="row-title"
        ),
        dbc.Row(
            [
                dbc.Col([
                    html.Div(children="", id="selected_cards")
                ],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
                dbc.Col([],xs=4, sm=4, md=4, lg=4, xl=4, xxl=4),
            ], className="row-buffer"
        ),
    ]
)

# TODO: -after set the cards should be shown
#       -can we let the values for the seission?


#############################
######### Callbacks #########
#############################
# open card selector
@dash.callback(
    Output("modal_card_selector", "is_open"),
    Output("selected_cards", "children"),
    Input("card_selector", "n_clicks"),
    Input("set_cards", "n_clicks"),
    State("modal_card_selector", "is_open"),
    State("selected_cards", "children"),
    prevent_initial_call = True
)
def open_select_cards(open_clicks, set_clicks, is_open, cards_old):
    button_id = dash.callback_context.triggered_id
    
    if button_id == "card_selector":
        return not is_open, cards_old
    if button_id == "set_cards":
        return not is_open, set_clicks
