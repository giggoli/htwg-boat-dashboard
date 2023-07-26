import dash
import json
import dash_bootstrap_components as dbc


def validate_fuelcell_message(msg):
    try:
        message = json.loads(msg)
        keys = ["status_e_i", "status_e_s", "SOC_e_i", "SOC_e_s", "SOV_e_i",
            "SOV_e_s","SOP_e_i","SOP_e_s","status","SOC","SOV","SOP",]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"

    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]
    
def set_fuelcell_status_e_i(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_status_e_s(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_soc_e_i(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_soc_e_s(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_sov_e_i(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_sov_e_s(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_sop_e_i(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_sop_e_s(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_status(value):
    if value == "0":
        return dbc.Alert("OK", color="success", style={"textAlign": "center"})
    elif value == "1":
        return dbc.Alert("ERROR", color="danger", style={"textAlign": "center"})
    else:
        return dbc.Alert(f"ERROR {value} not defined", color="warning", style={"textAlign": "center"})

def set_fuelcell_soc(value):
    return dbc.Alert(f"{value} A", color="primary", style={"textAlign": "center"})

def set_fuelcell_sov(value):
    return dbc.Alert(f"{value} V", color="primary", style={"textAlign": "center"})

def set_fuelcell_sop(value):
    return dbc.Alert(f"{value} W", color="primary", style={"textAlign": "center"})