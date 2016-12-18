import json

def parse_config():
  with open('config.json', 'r') as f:
    return json.load(f)
