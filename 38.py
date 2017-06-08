d = {}

doc = []

freq = {}

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
        if not surface in freq:
            freq[surface] = 1
        else:
            freq[surface] += 1


a = sorted(freq.items(), key=lambda x: x[1])[::-1]
b = list(map(lambda x: x[1], a))

from matplotlib import pyplot as plt
import numpy as np

plt.hist(b, bins=512, range=(np.min(b), np.max(b)), log=True)
plt.show()
