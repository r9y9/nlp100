import sys
N = int(sys.argv[1])
with open("hightemp.txt") as f:
    lines = f.readlines()
    p = len(lines) // N
    for n in range(N):
        b = p * n
        e = p * n + p if n < N else N
        print("n = {}".format(n))
        with open("xa{}".format(chr(ord("a") + n)), "w")as fo:
            for l in lines[b:e]:
                fo.write(l)
