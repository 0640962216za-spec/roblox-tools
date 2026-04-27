import json


def load_roblox_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_roblox_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_roblox_data(original, new_data):
    if isinstance(original, dict) and isinstance(new_data, dict):
        merged = original.copy()
        merged.update(new_data)
        return merged
    raise ValueError('Both inputs must be dictionaries')


def filter_roblox_data(data, keys):
    return {key: data[key] for key in keys if key in data}
