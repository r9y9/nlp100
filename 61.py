import plyvel

db = plyvel.DB("artist.ldb", create_if_missing=False)
key = "カントリー娘。に紺野と藤本（モーニング娘。）".encode()
area = db.get(key)
print(area)
