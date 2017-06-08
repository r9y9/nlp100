from lxml import etree

tree = etree.parse("nlp.txt.xml")
root = tree.getroot()

import sys
import numpy as np


def f(l):
    for idx, s in enumerate(l):
        if s != "NP":
            continue
        assert l[idx - 1] == "("
        nest = 1
        # search for closing bracket
        words = []
        for i in range(idx + 1, len(l)):
            if l[i] == "(":
                nest += 1
            elif l[i] == ")":
                nest -= 1
                if l[i - 1] != ")":
                    words.append(l[i - 1])
            if nest == 0:
                break
        if len(words) > 0:
            yield " ".join(words)


docment = root[0]
sentences = docment.find("sentences")
for sentence in sentences:
    parse = sentence.find("parse")
    s = parse.text
    s = s.replace('(', ' ( ').replace(')', ' ) ').split()
    l = np.array(s)

    for n in f(l):
        print(n)

sys.exit(0)
