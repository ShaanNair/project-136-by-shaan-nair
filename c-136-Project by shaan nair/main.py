from flask import Flask, jsonify, request 
from data import data 
app = Flask(__name__)
@app.route("/")
def getdata():
    return jsonify({
        "data":data, 
        "message": "success" 
    })
@app.route("/solarsystem")
def solarsystem():
    name = request.args.get("name")
    solarsystem_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data":solarsystem_data, 
        "message": "success" 
    })
if __name__=="__main__":
    app.run()