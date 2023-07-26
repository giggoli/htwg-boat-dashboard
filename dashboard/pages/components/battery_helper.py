import dash
import json
import dash_bootstrap_components as dbc


def validate_battery_message(msg):
    try:
        message = json.loads(msg)
        keys = [ "BSR", "BLVW", "BHVW", "BORC", "BORE", "SoC", "E_NE", "E_ST", "E_OC",
                "E_OV", "E_UV", "E_D", "E_OUT", "E_P", "E_C", "E_H", "E_CP", "E_CM",
                "E_CPC", "E_CD", "E_S", "W_NE", "W_ST", "W_OC", "W_OV", "W_UV", "W_D",
                "W_OUT", "W_P", "W_C", "E_NID", "BV", "BC", "B_MSCV", "B_mSCV", "B_HS",
                "SoH", "B_HMT", "B_CMT", "SWV", "B_RS", "B_RC", "B_TR", "B_LC", "B_IM",
                "B_PCC", "B_PDC","B_AC"]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"

    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]
    

def set_battery_BSR(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_BLVW(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_BHVW(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_BORC(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_BORE(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_SoC(value):
    return dbc.Progress(label=f"{value} %", value=value, style={"fontSize":"1em"})

def set_battery_E_NE(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_ST(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_OC(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_OV(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_UV(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_D(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_OUT(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_P(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_C(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_H(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_CM(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_CPC(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_CD(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_S(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "ERROR"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_NE(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_ST(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_OC(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_OV(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_UV(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_D(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_OUT(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_P(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_W_C(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_E_NID(value):
    return f"{value}"

def set_battery_BV(value):
    return f"{value} V"

def set_battery_BC(value):
    return f"{value} A"

def set_battery_B_MSCV(value):
    return f"{value} V"

def set_battery_B_mSCV(value):
    return f"{value} V"

def set_battery_B_HS(value):
    return f"{value}"

def set_battery_SoH(value):
    return dbc.Progress(label=f"{value} %", value=value, style={"fontSize":"1em"})

def set_battery_B_HMT(value):
    return f"{value} °C"

def set_battery_B_CMT(value):
    return f"{value} °C"

def set_battery_SWV(value):
    return f"{value}"

def set_battery_B_RS(value):
    content = dbc.Alert(style={"textAlign": "center"})
    if value == "0":
        content.children = "OK"
        content.color = "success"
        return content
    elif value == "1":
        content.children = "WARNING"
        content.color = "danger"
        return content
    else:
        content.children = f"Value: {value} not defined"
        content.color = "warning"
        return content

def set_battery_B_RC(value):
    return f"{value} Ah"

def set_battery_B_TR(value):
    return f"{value} minutes"

def set_battery_B_LC(value):
    return f"{value} kWh"

def set_battery_B_IM(value):
    return f"{value} kΩ"

def set_battery_B_PCC(value):
    return f"{value} A"

def set_battery_B_PDC(value):
    return f"{value} A"

def set_battery_B_AC(value):
    return f"{value}"