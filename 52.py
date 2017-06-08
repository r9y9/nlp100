from stemming.porter2 import stem

with open("51.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        print(stem(line))
