import json

def import_json(filepath:str):
    # Load the JSON file
    with open('json/trivia_template.json', 'r') as file:
        data = json.load(file)
    return data

def load_category(json_object:dict,category:str):
    return json_object[category]