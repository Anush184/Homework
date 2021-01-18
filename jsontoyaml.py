#json to yaml parser
import json
import yaml


def json_load(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def yaml_dump(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        yaml.dump(data, file, indent=4)
    with open(filepath, "r", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    dic = json_load("json_in")
    yaml_dump("json_in.json", dic)
