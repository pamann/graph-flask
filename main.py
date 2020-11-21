from flask import (Flask, render_template)
# from pywikiapi import wikipedia as pywiki
# import wikipedia
# import time
# import json
# from concurrent.futures import ThreadPoolExecutor
# from concurrent import futures
# from multiprocessing import Pool
# import hashlib
from flask import request
from flask import jsonify

from bfs_simple import search_term

app = Flask("__main__")

@app.route("/")
def my_index():
    return render_template("index.html", flask_token="Hello   world")

@app.route("/see")
def return_search():
    search = request.args.get('search')
    # return jsonify(search)
    return jsonify(search_term(search))

app.run(debug=True)