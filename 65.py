# Do the following commands in the mongo shell
"""
use nlp100
db.artists.find({name: "Queen"})
"""

from pymongo import MongoClient

client = MongoClient("localhost")
db = client.nlp100
collection = db.artists

for idx, data in enumerate(collection.find({"name": "Queen"})):
    assert isinstance(data, dict)
    print(idx, data)
