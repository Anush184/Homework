#yaml to py parser
import yaml

in_file = "yaml_in"
out_file = "json_out.json"


def yaml_load(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        return data


def yaml_dump(filepath, data):
    with open(filepath, "w", encoding="utf-8") as file:
        yaml.dump(data, file, indent=4)


if __name__ == "__main__":
    print(yaml_load("yaml_in.yaml"))
