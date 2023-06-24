
from os.path import isfile, exists

from file_manager import File


class _File:
    def __init__(self, path: str):
        self.path = path
    
    def read(self):
        with open(self.path, "r") as Read:
            return Read.read()


class Property:
    def __init__(self, file_path: str, *, prop_name: str = "Default"):
        self.properties = {}
        self.prop_name = prop_name
        if not exists(file_path) or not isfile(file_path):
            print("[PROPERTY][INIT]  File is not exists or is not file")
        else:
            self.file = _File(file_path)
            for string in self.file.read().splitlines():
                if "=" in string:
                    find = string.find("=")
                    self.properties.update({string[:find]: string[find + 1:len(string)]})

    def get(self, property_: str):
        if property_ not in self.properties:
            return None
        return self.properties[property_]

    def set(self, property_: str, value, *, name: str = None):
        self.properties.update({property_: value})
        if name is not None:
            name = " - " + name
        else:
            name = ""
        data = f"[ Bot Config{name} ]\n"
        for prop, value in self.properties.items():
            data += f"{prop}={value}\n"
        self.file.write(datas=data)
