from flask import Flask, render_template
from flask import request
from flask import jsonify
import wikipedia
from werkzeug.exceptions import HTTPException
from bfs_simple import search_term

app = Flask(__name__)


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
        root = wikipedia.page(search)
    except wikipedia.PageError as e:
        try:
            search = wikipedia.search(search)
            root = wikipedia.page(search[0])
        except wikipedia.DisambiguationError as e:
            search = e.options[0]
            root = wikipedia.page(search)
        except:
            root = wikipedia.page(search)
    except wikipedia.DisambiguationError as e:
        try:
            search = wikipedia.search(search)[0]
            root = wikipedia.WikipediaPage(search)
        except wikipedia.DisambiguationError as e:
            search = e.options[0]
            root = wikipedia.page(search)
        except:
            root = wikipedia.page(search, auto_suggest=True)
    except:
        print("See api error on search term {root_term} -> {search}")

    res = {"title": root.title, "summary": root.summary, "url": root.url}
    return jsonify(res)


@app.route("/api/see/<search>")
def return_search(search):
    return jsonify(search_term(search))


if __name__ == "__main__":
    app.run(threaded=True)  # host="0.0.0.0"
