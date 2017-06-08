from pymongo import MongoClient

client = MongoClient("localhost")
db = client.nlp100
collection = db.artists

# db.artists.find({"tags": {$elemMatch: {value: "dance"}}})
# db.artists.find({"tags": {$elemMatch: {value:
# "dance"}}}).sort({"rating.count" :-1}).limit(10)

docs = collection.find({"tags": {"$elemMatch": {"value": "dance"}}}).sort(
    "rating.count", -1).limit(10)

for idx, doc in enumerate(docs):
    print(idx + 1, doc["name"], doc["rating"])
