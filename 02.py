s1 = "パトカー"
s2 = "タクシー"

r = [[s[0], s[1]] for s in zip(s1, s2)]
print("".join(["".join(s) for s in r]))
