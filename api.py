import json
from flask import Flask as fla

def read_file(filename):
    with open(filename, "r") as my_data:
        data = my_data.read()
        return data

def convert_data(json_data):
    json_data = eval(json_data)
    return json_data

def find_all(data):
    return data

def find_user_by_id(data,id):
    return data[id]

app = fla(__name__)

@app.route("/")
def Home():
    return ("<h1>Data API</h1>")

@app.route("/users")
def Users():
    return find_all(convert_data)

@app.route("/user/<id>")
def User(id):
    return find_user_by_id(convert_data,int(id))

if __name__ == "__main__":
    read_data = read_file("data.json")
    convert_data = convert_data(read_data)
    # print(find_all(convert_data))
    # print(find_user_by_id(convert_data,1))
    app.run(debug=True)