from pywikiapi import wikipedia as pywiki
import wikipedia
import time
import json
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
from multiprocessing import Pool
from multiprocessing import Queue
import numpy as np
import hashlib

nodes = set()
links = set()
site = pywiki("en")
pool = ThreadPoolExecutor(8)  # 8 threads, adjust to taste and # of cores
jobs = []
link_counts = {}


def query_wiki(ttls, tier):
    global site
    for page in site.query(
        titles=ttls,
        format="json",
        pllimit="max",
        lhlimit="max",
        prop=["links", "linkshere", "description"],
        redirects=True,
    ):
        page = page.pages[0]
        if "description" in page:
            return process_comp_jobs(page, tier, page.description)


def process_comp_jobs(tt_page_s, tier, desc):
    if "links" in tt_page_s and "linkshere" in tt_page_s:
        l = [v.title.title() for v in tt_page_s.links]
        lh = [v.title.title() for v in tt_page_s.linkshere]
        lset = set(l)
        lhset = set(lh)

        if tier == 2:
            tt_bidi_links = list(lset.intersection(lhset))
            tt_bidi_links = set(tt_bidi_links)

        elif tier == 1:
            tt_bidi_links = list(lset.intersection(lhset))
            tt_bidi_links = set(tt_bidi_links)
        aggregate_nodes(tt_bidi_links, tier, desc)
        aggregate_links(tt_page_s.title, tt_bidi_links)
        return tt_bidi_links


def fetch_links(root_term):
    global nodes
    global links
    global jobs

    nodes = set()
    links = set()

    wikipedia.set_lang("en")
    suggest = wikipedia.suggest(root_term)

    try:
        search_r = suggest if suggest else root_term
        root = wikipedia.page(search_r)
    except wikipedia.DisambiguationError as e:
        root = e.options[0]

    summary = root.summary.split(".")[0]
    aggregate_nodes([search_r], 3, summary)
    bidi_links = query_wiki(search_r, 2)

    with ThreadPoolExecutor(8) as executor:  # start threaded bidi links of second tier
        for bidi_link in bidi_links:
            jobs.append(executor.submit(query_wiki, bidi_link, 1))
        query_pool = Pool(processes=50)
        [query_pool.apply_async(query_wiki, (p, 1)) for p in futures.as_completed(jobs)]

        query_pool.close()
        query_pool.terminate()
        query_pool.join()


def aggregate_links(nodeid, res):
    global links
    obj = [(nodeid, link_dest) for link_dest in res]
    links = links.union(set(obj))


def aggregate_nodes(n_list, v, desc=""):
    global nodes
    if v == 1:
        desc = ""
    obj = set([(node, v, desc) for node in n_list])
    nodes = nodes.union(set(obj))


def search_term(search):
    global nodes
    global links

    search = search.title()
    fetch_links(search)
    # unpack sets of tuples into lists of dicts
    l_nodes = [
        {
            "name": name,
            "id": hashlib.md5(name.encode("utf-8")).hexdigest(),
            "val": val,
            "description": desc,
        }
        for (name, val, desc) in nodes
    ]
    l_links = [
        {
            "source": hashlib.md5(src.encode("utf-8")).hexdigest(),
            "target": hashlib.md5(dest.encode("utf-8")).hexdigest(),
        }
        for (src, dest) in links
        for n in l_nodes
        if src in n["name"]
    ]
    graph = {"nodes": l_nodes, "links": l_links}
    return graph
