import flask
from flask import Flask, request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/monitoring', methods=['GET'])
def monitoring():
    return jsonify({"message:": "I'm alive. :)"})


@app.route('/structured', methods=["POST"])
def structured_data():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
