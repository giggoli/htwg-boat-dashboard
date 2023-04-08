import json
import os

class ConfigError(Exception):
    pass

def __load_config(path):
    with open(path, "r") as file:
        config_dir = json.loads(file.read())
    return config_dir

def __check_config_dir(config_dir):
    if "broker_ip" not in config_dir:
        raise ConfigError('config does not contain key "broker_ip"')
    if type(config_dir["broker_ip"]) is not str:
        raise ConfigError('entry "broker_ip" of config is not str')
    if "broker_port" not in config_dir:
        raise ConfigError('config does not contain key "broker_port"')
    if type(config_dir["broker_port"]) is not int:
        raise ConfigError('entry "broker_port" of config is not int')
    if "client_name" not in config_dir:
        raise ConfigError('config does not contain key "client_name"')
    if type(config_dir["client_name"]) is not str:
        raise ConfigError('entry "client_name" of config is not str')
    if "topics" not in config_dir:
        raise ConfigError('config does not contain key "topics"')
    if type(config_dir["topics"]) is not list:
        raise ConfigError('entry "broker_port" of config is not list')
    

def getConfig():
    cnf_path = os.path.join(os.path.dirname(__file__), 'config.json')
    config = __load_config(cnf_path)
    __check_config_dir(config)
    return config

    
