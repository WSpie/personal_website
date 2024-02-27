from openai import OpenAI
import os
import yaml
from pathlib import Path

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def load_config(config_path):
    config = yaml.safe_load(Path(config_path).read_text())
    return Namespace(**config)

def login(api_key):
    client = OpenAI(api_key=api_key) #load_config('config.yaml').windows_vscode
    return client
