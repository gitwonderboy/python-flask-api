import json
from flask import Flask as fla

def read_file(filename):
    with open(filename, "r") as my_data:
        data = my_data.read()
        return data

def convert_data(json_data):
    json_data = eval(json_data)
    return json_data

if __name__ == "__main__":
    read_data = read_file("data.json")
    print(convert_data = convert_data(read_data))