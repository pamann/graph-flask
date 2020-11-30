from flask import Flask, render_template
from flask import request
from flask import jsonify
import wikipedia

from bfs_simple import search_term

app = Flask("__main__")


@app.route("/")
def my_index():
    return render_template("index.html")


<<<<<<< HEAD
@app.route("/api/meta/<term>")
def metadata_fetch(term):
    page = wikipedia.page(term, preload=True)
    res = {"title": page.title, "summary": page.summary, "image": page.images}
    return jsonify(res)


=======
>>>>>>> b8619e1 (Configured lint)
@app.route("/api/see/<search>", methods=["GET"])
def return_search(search):
    return jsonify(search_term(search))


<<<<<<< HEAD
app.run(threaded=True, debug=True)
=======
app.run(debug=True)
>>>>>>> b8619e1 (Configured lint)
