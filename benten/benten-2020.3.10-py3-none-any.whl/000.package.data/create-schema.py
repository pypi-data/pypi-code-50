"""Short script that uses schema-salad to generate and post-process the CWL yml document into
a JSON format that is read in by Benten and converted into a set of Python classes for CWL types"""
#  Copyright (c) 2019 Seven Bridges. See LICENSE

import sys
import subprocess
import json


def remove_uris(d):
    if isinstance(d, dict):
        for k, v in d.items():
            d[k] = remove_uris(v)
        return d
    elif isinstance(d, list):
        return [remove_uris(v) for v in d]
    else:
        if isinstance(d, str):
            if d.startswith("https://w3id.org") or d.startswith("http://www.w3.org"):
                _v = d.split("#")[1]
                if "/" in _v:
                    _v = _v.split("/")[1]
                return _v
        return d


def main():
    print(sys.argv)
    if len(sys.argv) != 3:
        print("python create-schema.py <input.yml> <output.json>\n"
              "e.g. python create-schema.py CommonWorkflowLanguage.yml schema-v1.0.json")
        return

    #subprocess.call(f"schema-salad-tool --print-pre {sys.argv[1]} > {sys.argv[2]}", shell=True)
    subprocess.call(f"schema-salad-tool --print-avro {sys.argv[1]} > {sys.argv[2]}", shell=True)
    with open(sys.argv[2], "r") as f:
        d = json.load(f)
        d = remove_uris(d)

    with open(sys.argv[2], "w") as f:
        json.dump(d, f, indent=2)


if __name__ == "__main__":
    main()
