#yaml to json parser
import yaml
import json


def yaml_load(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data


def json_dump(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    with open(filepath, "r", encoding="utf-8") as file:
        print(file.read())


if __name__ == "__main__":
    dic = yaml_load("yaml_in.yaml")
    json_dump("yaml_in.yaml", dic)
