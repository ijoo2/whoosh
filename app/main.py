from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/search', methods=['GET'])
def search():
    # implement api call
    params = request.args
    url = "http://api.wordnik.com:80/v4/word.json"
    r = requests.get(url, params=params)
    pass


if __name__ == '__main__':
    app.run()