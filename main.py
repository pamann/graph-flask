from flask import Flask, render_template
from flask import request
from flask import jsonify
import wikipedia

from bfs_simple import search_term

app = Flask("__main__")


@app.route("/")
def my_index():
    return render_template("index.html")


@app.route("/see/<search>")
def return_search(search):
    return jsonify(search_term(search))


@app.route("/meta/<term>")
def metadata_fetch(term):
    page = wikipedia.page(term, preload=True)
    res = {"title": page.title, "summary": page.summary, "image": page.images}
    return jsonify(res)


app.run(threaded=True, debug=True)