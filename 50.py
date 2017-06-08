import re
import sys
with open("nlp.txt") as f:
    lines = f.readlines()
    for line in lines:
        ss = re.split(r"([\.;:\?!]\s[A-Z])", line)
        sentences = ss[::2]
        omake = ss[1::2]
        for idx in range(1, len(sentences)):
            sentences[idx - 1] = sentences[idx - 1] + omake[idx - 1][:-1]
            sentences[idx] = omake[idx - 1][-1] + sentences[idx]

        sentences = list(map(lambda s: s.replace("\n", ""), sentences))

        for s in sentences:
            if len(s) > 0:
                print(s)
sys.exit(0)
