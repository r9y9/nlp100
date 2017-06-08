import plyvel
from tqdm import tqdm

db = plyvel.DB("artist.ldb", create_if_missing=False)
r = []
for k, v in tqdm(db):
    if v == b"Japan":
        r.append(k.decode("utf-8"))

for k in r:
    print(k)
print("Total: {}".format(len(r)))
