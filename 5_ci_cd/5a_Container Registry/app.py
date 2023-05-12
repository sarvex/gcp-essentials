# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h3>Hello, World!</h3>"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)