d = {}

doc = []

with open("neko.txt.mecab") as f:
    lines = f.readlines()
    sentense = []
    for line in lines:
        line = line[:-1]
        if line == "EOS":
            if len(sentense) > 0:
                doc.append(sentense)
            sentense = []
            continue

        surface, rest = line.split("\t")
        rest = rest.split(",")

        assert len(rest) >= 6
        pos, pos1, base = rest[0], rest[1], rest[6]

        key = (surface, base, pos, pos1)
        d[key] = surface
        sentense.append(key)

results = []
for sentense in doc:
    found = False
    r = []
    for idx in range(len(sentense)):
        word = sentense[idx]
        found = True if word[2] == "名詞" else False
        if found:
            r.append(word[0])
        else:
            if len(r) > 1:
                results.append(" ".join(r))
            r = []

print(len(results))
for r in results:
    print(r)
