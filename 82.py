import numpy as np
import sys

vocab = {}

D = 5
with open("81.jl.out") as f:
    for line in f.readlines()[:1]:
        words = line[:-1].strip().split(" ")
        words = list(filter(lambda x: x != "", words))
        for idx in range(len(words)):
            randd = np.random.randint(1, D + 1)
            d = min(randd, idx + 1, len(words) - randd - 1)
            print(d)
            sys.stdout.write("{}\t".format(words[idx]))
            for i in range(-d, d + 1):
                if i != 0:
                    if idx + i < 0:
                        sys.stdout.write("N/A\t")
                    elif idx + i >= len(words):
                        sys.stdout.write("N/A\t")
                    else:
                        sys.stdout.write("{}\t".format(words[idx + i]))
            sys.stdout.write("\n")
