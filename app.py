from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<int:id>', methods=['GET'])
def get_name(id):
    r = requests.get("http://pokeapi.co/api/v2/pokemon/%d" % id)
    name = r.json().get("name")
    res = "Cannot find pokemon with id %d" % id
    if name:
        res = "The pokemon with id %d is %s" % (id, name)
    return res


@app.route('/pokemon/<string:name>', methods=['GET'])
def get_id(name):
    r = requests.get("http://pokeapi.co/api/v2/pokemon/%s" % name)
    id = r.json().get("id",-1)
    res = "Cannot find pokemon named %s" % name.capitalize()
    if id != -1:
        res = "%s has id %d" % (name.capitalize(), id)
    return res


if __name__ == '__main__':
    app.run()
