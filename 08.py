def ciper(s):
    r = []
    for c in s:
        n = ord(c)
        if n >= ord("a") and n <= ord("z"):
            r.append(chr(219 - n))
        else:
            r.append(c)
    return "".join(r)


s = "Hello youtube"
c = ciper(s)
r = ciper(c)
print(s)
print(c)
print(r)
