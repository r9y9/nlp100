import gzip
import json


def get_uk_text():
    with gzip.open("./jawiki-country.json.gz") as f:
        for line in f:
            json_dict = json.loads(line)
            if "イギリス" in json_dict["title"]:
                return json_dict["text"]


import re
r = re.compile("\[\[File:(.+)\]\]")
doc = get_uk_text()
for it in r.finditer(doc):
    print(it.group(0))
