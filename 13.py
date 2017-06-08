with open("col1.txt") as f1:
    f1lines = f1.readlines()
    with open("col2.txt") as f2:
        f2lines = f2.readlines()
        assert len(f1lines) == len(f2lines)

        for i in range(len(f1lines)):
            print("{}\t {}".format(f1lines[i][:-1], f2lines[i][:-1]))
