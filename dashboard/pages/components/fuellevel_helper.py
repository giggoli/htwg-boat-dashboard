import dash
import json
import dash_bootstrap_components as dbc

def validate_fuellevel_message(msg):
    try:
        message = json.loads(msg)
        keys = ["ID", "FL", "FA", "TEMP", "ERROR"]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"
                
    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]


def set_fuellevel_ID(value):
    return f"{value}"

def set_fuellevel_FL(value):
    return dbc.Progress(label=f"{value}%", value=value, style={"fontSize": "1em"})

def set_fuellevel_FA(value):
    return dbc.Alert(f"{value} ml", color="primary", style={"textAlign": "center"})

def set_fuellevel_TEMP(value):
    return f"{value}"

def set_fuellevel_ERROR(value):
    if value == 0:
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == 1:
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="light", style={"textAlign": "center"})