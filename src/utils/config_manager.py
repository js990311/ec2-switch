import sys
import os
import json

def get_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.getcwd()

def load_config_file():
    if not os.path.exists(os.path.join(get_path(), "config.json")):
        return {}
    try:
        with open(os.path.join(get_path(), "config.json"), "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        return {}