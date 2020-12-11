from flask import Flask, render_template, request, jsonify, redirect
import wikipedia
from werkzeug.exceptions import HTTPException
from bfs_simple import search_term

app = Flask(__name__)


@app.before_request
def before_request():
    if not request.is_secure:
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


@app.route("/")
def my_index():
    return render_template("index.html")


@app.errorhandler(Exception)
def internal_server_error(e):
    if isinstance(e, HTTPException):
        return render_template("index.html")
    return render_template("server_error.html")


@app.route("/api/meta/<term>", methods=["GET"])
def metadata_fetch(term):
    wikipedia.set_lang("en")
    search = term
    try:
        root = wikipedia.WikipediaPage(search)
    except (wikipedia.PageError, wikipedia.DisambiguationError):
        root = wikipedia.page(search)
    except:
        print("Meta api error on search term {root_term} -> {search}")

    res = {"title": root.title, "summary": root.summary, "url": root.url}
    return jsonify(res)


@app.route("/api/see/<search>")
def return_search(search):
    return jsonify(search_term(search))


if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0")
