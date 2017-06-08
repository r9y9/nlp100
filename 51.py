with open("50.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        for word in line.split(" "):
            if len(word) > 0:
                print(word)
        print("")
