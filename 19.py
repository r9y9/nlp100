with open("hightemp.txt") as f:
    lines = f.readlines()
    d = {}
    for idx, l in enumerate(lines):
        l = l.split("\t")
        key = l[0]
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    for k, v in sorted(d.items(), key=lambda x: x[1])[::-1]:
        print(k, v)

# cut -f 1 hightemp.txt | sort | uniq -c | sort -nr | awk '{print $2}'
