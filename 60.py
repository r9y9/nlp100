import gzip
import json

import plyvel
from tqdm import tqdm
with gzip.open("artist.json.gz") as f:
    db = plyvel.DB("artist.ldb", create_if_missing=True)
    for line in tqdm(f):
        json_dict = json.loads(line)
        db.put(json_dict.get("name", "").encode("utf-8"),
               json_dict.get("area", "").encode("utf-8"))
    db.close()
