ns = []
with open("hightemp.txt") as f:
    lines = f.readlines()
    for idx, l in enumerate(lines):
        l = l.split("\t")
        ns.append(l[2])

for n in sorted(ns):
    print(n)
