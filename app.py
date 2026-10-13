from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(status="Branch A and Branch B say hi")

@app.route("/status")
def status():
    return jsonify(status="running")

if __name__ == "__main__":
    app.run(port=5000)
