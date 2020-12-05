from flask import Flask, render_template
from flask import request
from flask import jsonify
import wikipedia
import os
import logging
from bfs_simple import search_term

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")


@app.route("/")
def my_index():
    # return app.root_path
    return render_template("index.html")


@app.route("/api/meta/<term>", methods=["GET"])
def metadata_fetch(term):
    wikipedia.set_lang("en")
    search = term
    search_list = wikipedia.search(search)
    suggest_term = wikipedia.suggest(search)

    try:
        root = wikipedia.WikipediaPage(search)
    except (wikipedia.PageError, wikipedia.DisambiguationError) as e:
        try:
            if len(search_list) >= 1:
                search = search_list[0]
            else:
                search = suggest_term
            root = wikipedia.WikipediaPage(search)
        except wikipedia.DisambiguationError as e:
            try:
                search = e.options[0]
                root = wikipedia.WikipediaPage(search)
            except:
                root = wikipedia.page(search, auto_suggest=True)
        except:
            try:
                root = wikipedia.page(search, auto_suggest=True)
            except:
                print("Meta api error on search term {term} -> {search}")

    res = {"title": root.title, "summary": root.summary, "url": root.url}
    return jsonify(res)


@app.route("/api/see/<search>")
def return_search(search):
    return jsonify(search_term(search))


if __name__ == "__main__":
    app.run(threaded=True, debug=True, host="0.0.0.0")  # , port=8080)
