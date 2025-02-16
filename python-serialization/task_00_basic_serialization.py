import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to a JSON file.
    :param data: Dictionary to serialize
    :param filename: Filename of the JSON file
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_and_deserialize(filename):
    """
    Loads and deserializes a JSON file into a Python dictionary.
    :param filename: Filename of the JSON file
    :return: Dictionary with deserialized data
    """
    with open(filename, 'r') as file:
        return json.load(file)
