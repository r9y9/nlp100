import sys
N = int(sys.argv[1])
with open("hightemp.txt") as f:
    lines = f.readlines()
    for l in lines[:min(N, len(lines))]:
        print(l[:-1])
