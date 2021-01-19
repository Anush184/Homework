# yaml to text parser
import json
import yaml
import os


def yaml_to_text(filepath):
    try:
        name, extension = os.path.splitext(filepath)
        if extension == ".yaml":
            with open(filepath, "r", encoding="utf-8") as f:
                obj = yaml.load(f, Loader=yaml.FullLoader)
            yaml_txt = yaml.dump(obj, indent=2, sort_keys=False)
            with open("output_yaml.txt", "w") as f:
                f.write(yaml_txt)
        else:
            print(f"'{name}' not a yaml file.")
    except OSError:
        print("Problem reading: " + filepath)


def json_to_text(filepath):
    try:
        name, extension = os.path.splitext(filepath)
        if extension == ".json":
            with open(filepath, "r", encoding="utf-8") as json_file:
                obj = json.load(json_file)
            json_obj = json.dumps(obj, indent=2)
            with open("output_json.txt", "w") as f:
                f.write(json_obj)
        else:
            print(f"'{name}' not a json file.")

    except OSError:
        print("Problem reading: " + filepath)


def json_to_yaml(file_json, file_yaml):
    try:
        name, extension = os.path.splitext(file_json)
        if extension == ".json":
            with open(file_json, "r", encoding="utf-8") as file:
                data = json.load(file)
            with open(file_yaml, "w", encoding="utf-8") as file:
                yaml.dump(data, file, sort_keys=False, indent=4)
            with open(file_yaml, "r", encoding="utf-8") as file:
                print(file.read())
        else:
            print(f"{file_json} not a json file.")
    except OSError:
        print("Problem reading: " + file_json)


def yaml_to_json(file_yaml, file_json):
    try:
        name, extension = os.path.splitext(file_yaml)
        if extension == ".yaml":
            with open(file_yaml, "r", encoding="utf-8") as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
            with open(file_json, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, sort_keys=False)
            with open(file_json, "r", encoding="utf-8") as file:
                print(file.read())
        else:
            print(f"{file_yaml} not a yaml file.")
    except OSError:
        print("Problem reading: " + file_yaml)


yaml_to_text("yaml_in.yaml")
json_to_text('json_in.json')
json_to_yaml("json_in.json", "yaml_file.yaml")
yaml_to_json("yaml_in.yaml", "json_file.yaml")
