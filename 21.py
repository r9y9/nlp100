import gzip
import json


def get_uk_text():
    with gzip.open("./jawiki-country.json.gz") as f:
        for line in f:
            json_dict = json.loads(line)
            if "イギリス" in json_dict["title"]:
                return json_dict["text"]


import re


doc = get_uk_text().split("\n")
for line in doc:
    if re.search("Category", line) is not None:
        print(line)
