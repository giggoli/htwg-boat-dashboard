import dash
import json
import dash_bootstrap_components as dbc


def validate_solar_message(msg):
    try:
        message = json.loads(msg)
        keys = ["BV", "BC", "BT", "CH", "CHM", "PVV", "PVC", "EQP", "EQTR",
                "ROCH", "SYSALRM", "SYSAL", "SYSAH", "YTD", "MPTD", "YYD",
                "MPYD", "ERROR", "YPVP", "UYPWR", "MPPT", "SolSerial",
                "AIS", "SYSBV", "SYSBC", "SYSBP","SYSSOC", "SYSSTATE",
                "SYSCAH", "SYST2G", "PVCP", "PVCC", "SYSCP", "SYSPWR", "BUSCC", "BUSCP"]
        # check if message contain for each key a value
        for key in keys:
            if key not in message:
                message[key] = "No Value received"

    except Exception as e:
        print(f"Dash exception: {e}")
        return [False, msg]
    else:
        return [True, message]

def set_solar_BV(value):
    return f"{value} V"

def set_solar_BC(value):
    return f"{value} A"

def set_solar_BT(value):
    return f"{value} °C"
    

def set_solar_CH(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 1:
        content.children = "ON"
        content.color = "success"
        return content
    elif value == 4:
        content.children = "OFF"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_CHM(value):
    content = dbc.Alert(f"Value: {value} not defined", color="info", style={"textAlign": "center"})
    if value == 0:
        content.children = "OFF"
        content.color = "warning"
        return content
    elif value == 2:
        content.children = "Fault"
        content.color = "danger"
        return content
    elif value == 3:
        content.children = "Bulk"
        return content
    elif value == 4:
        content.children = "Absorption"
        return content
    elif value == 5:
        content.children = "Float"
        return content
    elif value == 6:
        content.children = "Storage"
        return content
    elif value == 7:
        content.children = "Equalize"
        return content
    elif value == 11:
        content.children = "Other"
        return content
    else:
        content.color = "warning"
        return content

def set_solar_PVV(value):
    return f"{value} V"

def set_solar_PVC(value):
    return f"{value} A"

def set_solar_EQP(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "NO"
        content.color = "primary"
        return content
    if value == 1:
        content.children = "Yes"
        content.color = "primary"
        return content
    if value == 2:
        content.children = "Error"
        content.color = "danger"
        return content
    elif value == 3:
        content.children = "Unavailable"
        content.color = "info"
        return content
    else:
        return content

def set_solar_EQTR(value):
    return f"{value} seconds"

def set_solar_ROCH(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "Open"
        content.color = "primary"
        return content
    if value == 1:
        content.children = "Closed"
        content.color = "primary"
        return content
    else:
        return content

def set_solar_SYSALRM(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Alarm"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Alarm"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_SYSAL(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Alarm"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Alarm"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_SYSAH(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Alarm"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Alarm"
        content.color = "danger"
        return content
    else:
        return content

def set_solar_YTD(value):
    return f"{value} kWh"

def set_solar_MPTD(value):
    return f"{value} W"

def set_solar_YYD(value):
    return f"{value} kWh"

def set_solar_MPYD(value):
    return f"{value} W"

def set_solar_ERROR(value):
    content = dbc.Alert(f"Value: {value} not defined", color="danger", style={"textAlign": "center"})
    if value == 0:
        content.children = "No Error"
        content.color = "success"
        return content
    if value == 1:
        content.children = "Battery tempearture too high"
        return content
    if value == 2:
        content.children = "Battery voltage too high"
        return content
    if value == 3:
        content.children = "Battery temperature sensor misswired (+)"
        return content
    if value == 4:
        content.children = "Battery temperature sensor misswired (-)"
        return content
    if value == 5:
        content.children = "Battery temperature sensor disconnected"
        return content
    if value == 6:
        content.children = "Battery voltage sensor misswired (+)"
        return content
    if value == 7:
        content.children = "Battery voltage sensor misswired (-)"
        return content
    if value == 8:
        content.children = "Battery voltage sensor disconnected"
        return content
    if value == 9:
        content.children = "Battery voltage wire losses too high"
        return content
    if value == 17:
        content.children = "Charger temperature too high"
        return content
    if value == 18:
        content.children = "Charger over-current"
        return content
    if value == 19:
        content.children = "Charger current polarity reversed"
        return content
    if value == 20:
        content.children = "Bulk time limit reached"
        return content
    if value == 22:
        content.children = "Charger temperature sensor miswired"
        return content
    if value == 23:
        content.children = "Charger temperature sensor disconnected"
        return content
    if value == 34:
        content.children = "Input current too high"
        return content
    else:
        content.color = "warning"
        return content

def set_solar_YPVP(value):
    return f"{value} W"

def set_solar_UYPWR(value):
    return f"{value} kWh"

def set_solar_MPPT(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "Of"
        content.color = "danger"
        return content
    if value == 1:
        content.children = "Voltage/Current limited"
        content.color = "info"
        return content
    if value == 2:
        content.children = "MPPT active"
        content.color = "success"
        return content
    if value == 225:
        content.children = "Not available"
        return content
    else:
        return content

def set_system_SolSerial(value):
    return f"{value}"

def set_system_AIS(value):
    content = dbc.Alert(f"Value: {value} not defined", color="warning", style={"textAlign": "center"})
    if value == 0:
        content.children = "Unknown"
        return content
    if value == 1:
        content.children = "Grid"
        content.color = "success"
        return content
    if value == 2:
        content.children = "Generator"
        content.color = "success"
        return content
    if value == 3:
        content.children = "Shore power"
        content.color = "success"
        return content
    if value == 240:
        content.children = "Not connected"
        return content
    else:
        return content

def set_system_SYSBV(value):
    return f"{value} V"

def set_system_SYSBC(value):
    return f"{value} A"

def set_system_SYSBP(value):
    return f"{value} W"

def set_system_SYSSOC(value):
    return dbc.Progress(label=f"{value}%", value=value, style={"fontSize": "1em"})

def set_system_SYSSTATE(value):
    content = dbc.Alert(f"Value: {value} not defined", color="info", style={"textAlign": "center"})
    if value == 0:
        content.children = "idle"
        return content
    if value == 1:
        content.children = "charging"
        return content
    if value == 2:
        content.children = "discharging"
        return content
    else:
        content.color = "warning"
        return content

def set_system_SYSCAH(value):
    return f"{value} Ah"

def set_system_SYST2G(value):
    return f"{value} seconds"

def set_system_PVCP(value):
    return f"{value} W"

def set_system_PVCC(value):
    return f"{value} A"

def set_system_SYSCP(value):
    return f"{value} W"

def set_system_SYSPWR(value):
    return f"{value} W"

def set_system_BUSCC(value):
    return f"{value} A"

def set_system_BUSCP(value):
    return f"{value} W"