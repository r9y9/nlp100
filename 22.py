import gzip
import json


def get_uk_text():
    with gzip.open("./jawiki-country.json.gz") as f:
        for line in f:
            json_dict = json.loads(line)
            if "イギリス" in json_dict["title"]:
                return json_dict["text"]


import re

r = re.compile("\[\[Category:(.+)\]\]")
doc = get_uk_text().split("\n")
for line in doc:
    match = r.match(line)
    if match:
        print(match.group(1))
