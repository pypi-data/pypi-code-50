from flask import Flask, render_template, request, jsonify
import os
import argparse
from search_fs import search
app = Flask(__name__)

DB_FILE = os.environ['SEARCH_FS_DB']

@app.route('/<name>')
def index(name=None):
    return render_template('index.html.j2', name=name)

sample = {
    'name': 'filename',
    'size': '-50GB',
    'type': 'a or f or d',
    'strict_dir': False,
    'directories': []
}
@app.route('/api/search', methods=['POST'])
def search_api():
    req = request.get_json()

    ns = argparse.Namespace()
    ns.database=DB_FILE
    ns.name=req.get('name', None)
    ns.size=req.get('size', None)
    ns.type=req.get('type', None)
    ns.strict_dir=req.get('strict_dir', False)
    ns.directories = req.get('directories', [])

    results = list(search.search(ns))

    return jsonify(results)
