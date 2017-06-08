import pandas as pd
import sys
import numpy as np

countries = pd.read_csv("countries.csv")
names = np.array(countries["ISO 3166-1に於ける英語名"])
splitted_names = []
for name in names:
    s = name.split(" ")
    s = list(filter(lambda x: x != "", map(lambda b: b.strip(), s)))
    splitted_names.append(s)
if False:
    for name in splitted_names:
        print(name)

with open("80.py.out") as f:
    for line in f.readlines():
        words = line[:-1].split(" ")
        words = list(filter(lambda x: x != "", words))
        newwords = []
        idx = 0
        while idx < len(words):
            word = words[idx]
            found = False
            for c in splitted_names:
                cl = len(c)
                if idx + cl >= len(words):
                    break
                if len(c) > 1 and words[idx:idx + cl] == c:
                    newwords.append("_".join(c))
                    idx = idx + cl
                    found = True
            if not found:
                idx += 1
                newwords.append(word)

        words = newwords
        if len(words) > 0:
            for token in words:
                sys.stdout.write("{} ".format(token))
            sys.stdout.write("\n")

sys.exit(0)
