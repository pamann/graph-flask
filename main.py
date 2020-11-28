from flask import (Flask, render_template)
from flask import request
from flask import jsonify

from bfs_simple import search_term

app = Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html")

@app.route("/see/<search>", methods=['GET'])
def return_search(search):
    print(search)
    print(search_term(search))
    return jsonify(search_term(search))

app.run(debug=True)