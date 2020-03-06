import json
from jsonschema import validate
import os


schema = {
	"$schema": "http://json-schema.org/draft-04/schema#",
	"type": "object",
	"properties": {
		"id": {
			"type": "string"
		},
		"text": {
			"type": "string"
		},
		"options": {
			"type": "array",
			"items": [
				{
					"type": "object",
					"properties": {
						"text": {
							"type": "string"
						},
						"scene": {
							"type": "string"
						}
					},
					"required": [
						"text",
						"scene"
					]
				}
			]
		}
	},
	"required": [
		"id",
		"text",
		"options"
	]
}


def contextualize(directory):
    directory = directory if directory else os.getcwd()
    return os.path.abspath(directory)


def check(directory):
    # is directory a directory?
    if not os.path.isdir(directory):
        return False, [], "{} is not a directory.".format(directory)
    # does the directory have json files in it?
    json_file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                path = os.path.join(root, file)
                json_file_paths.append(path)
    if not json_file_paths:
        return False, [], "{} does not contain any .json files.".format(directory)
    # do all of the json files conform to the schema?
    for json_file_path in json_file_paths:
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
        try:
            validate(instance = json_data, schema = schema)
        except Exception as exception:
            return False, [], exception
    # if you made it this far...
    return True, json_file_paths, "Directory successfully validated."


def load(json_file_paths):
    data = {}
    for json_file_path in json_file_paths:
        with open(json_file_path) as json_file:
            json_data = json.load(json_file)
        data[json_data["id"]] = json_data
    return data


def quit():
    print("\nGame over.")


def run(start_key, game):
    scene = game[start_key]
    options = scene["options"]
    print(scene["text"], "\n")
    for i, option in enumerate(options):
        print("\t", i, "\t", option["text"])
    print("\n")
    option_index = input("Enter an option index: ")
    if (option_index == "q"):
        return
    while (not option_index.isdigit()) or (int(option_index) < 0) or (int(option_index) > len(options) - 1):
        option_index = input("Enter a valid option index: ")
        if (option_index == "q"):
            return
    print("\n")
    option = options[int(option_index)]
    start_key = option["scene"]
    run(start_key, game)
