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

for sentense in doc:
    for idx in range(1, len(sentense) - 1):
        curr_word = sentense[idx]
        prev_word = sentense[idx - 1]
        next_word = sentense[idx + 1]
        if curr_word[0] == "の" and prev_word[2] == "名詞" \
           and next_word[2] == "名詞":
            print(prev_word[0], curr_word[0], next_word[0])
