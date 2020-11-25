from flask import (Flask, render_template)
from flask import request
from flask import jsonify

from bfs_simple import search_term

app = Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html")

@app.route("/see/<search>")
def return_search(search):
    search = search
    # search = request.args.get('search')
    # return render_template("index.html", data=jsonify(search_term(search)))
    return jsonify(search_term(search))

app.run(threaded=True)