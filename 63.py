import gzip
import json
import sys
import plyvel


def encode(tags):
    r = '{"tags" : ['
    for idx, tag in enumerate(tags):
        r += '{{"count" : "{}", "value" : "{}"}}'.format(
            tag["count"], tag["value"])
        if idx < len(tags) - 1:
            r += ","
    r += "]}"
    return r.encode("utf-8")


def decode(s):
    return json.loads(s)


from tqdm import tqdm

from os.path import isdir

if not isdir("63.ldb"):
    with gzip.open("artist.json.gz") as f:
        db = plyvel.DB("63.ldb", create_if_missing=True)
        for line in tqdm(f):
            json_dict = json.loads(line)
            r = encode(json_dict["tags"]) if "tags" in json_dict else b""
            db.put(json_dict.get("name", "").encode("utf-8"), r)
        db.close()
else:
    print("lmdb already created, skip building DB")

db = plyvel.DB("63.ldb", create_if_missing=False)
key = "カントリー娘。に紺野と藤本（モーニング娘。）".encode()
tags = decode(db.get(key))
tags = tags["tags"]
for tag in tags:
    print("Tag: {}, Count: {}".format(tag["value"], tag["count"]))

sys.exit(0)
