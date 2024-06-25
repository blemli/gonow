#!/usr/bin/env python3
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/config/set', methods=['POST'])
def respond():
    if request.json:
        with open("static/config.json", "w") as configfile:
            json.dump(request.json, configfile)
        return Response(status=200)
    return Response(status=500)


@app.route("/config/get", methods=["GET"])
def config_get():
    return app.send_static_file("config.json")


@app.route("/schema.json", methods=["GET"])
def config_schema():
    return app.send_static_file("schema.json")


@app.route("/", methods=["GET"])
def edit():
    return app.send_static_file('edit.html')


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=8080)
