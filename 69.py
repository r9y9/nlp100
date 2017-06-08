from bottle import get, post, run, template, request
from pymongo import MongoClient


@get('/')
def index():
    return """
    <form action="/" method="post">
    Name: <input name="name" type="text" />
    Alias name: <input name="alias_name" type="text" />
    Tag: <input name="tag" type="text" />
    <input value="Search" type="submit" />
    </form>
    """


@post("/")
def search():
    name = request.forms.name
    alias_name = request.forms.alias_name
    tag = request.forms.tag

    print(name, alias_name, tag)
    client = MongoClient("localhost")
    db = client.nlp100
    collection = db.artists

    cond = {"name": name}
    if len(alias_name) > 0:
        cond["aliases"] = {"$elemMatch": {"name": alias_name}}
    if len(tag) > 0:
        cond["tags"] = {"$elemMatch": {"value": tag}}

    print(cond)
    r = []
    for data in collection.find(cond).limit(5):
        data.pop("_id", None)
        r.append(data)

    return template("""
    <html>
    <ul>
    %for item in docments:
        <li>{{item}}</li>
    %end
    </ul>
    </html>

    """, docments=r)


if __name__ == "__main__":
    run(host='localhost', port=8080)
