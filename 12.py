with open("hightemp.txt") as f:
    lines = f.readlines()

with open("col1.txt", "w") as f1:
    with open("col2.txt", "w") as f2:
        cols = len(lines[0].split("\t"))
        for l in lines:
            splitted = l.split("\t")
            assert len(splitted) == 4
            f1.write("{}\n".format(splitted[0]))
            f2.write("{}\n".format(splitted[1]))
