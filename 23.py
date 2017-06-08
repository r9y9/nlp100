import gzip
import json


def get_uk_text():
    with gzip.open("./jawiki-country.json.gz") as f:
        for line in f:
            json_dict = json.loads(line)
            if "イギリス" in json_dict["title"]:
                return json_dict["text"]


import re
import numpy as np
r = re.compile(u"^=*(.+)=$")
doc = get_uk_text().split("\n")
for line in doc:
    match = r.match(line)
    if match:
        s = match.group(0)
        level2 = np.sum([c == "=" for c in s])
        assert level2 % 2 == 0
        print(level2 // 2 - 1, s)
