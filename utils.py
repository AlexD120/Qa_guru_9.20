import json


def load_schema(path=''):
    with open(path) as file:
        return json.loads(file.read())