import yaml

def read_yaml(file):

    with open(file, encoding='utf-8') as f:

        data = yaml.safe_load(f)

        return data