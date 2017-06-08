with open("hightemp.txt") as f:
    lines = f.readlines()
    print("before:")
    for l in lines:
        print(l[:-1])
    r = []
    for l in lines:
        r.append(l.replace("\t", " "))
    print("after:")
    for l in r:
        print(l[:-1])
