def ngram(words, N=2):
    d = {}
    for idx in range(len(words)):
        if idx + N - 1 >= len(words):
            continue
        key = tuple(words[idx:idx + N])
        if key in d:
            d[key] += 1
        else:
            d[key] = 1

    return d


s1 = "paraparaparadise"
s2 = "paragraph"
X = ngram(s1)
Y = ngram(s2)
print(X)
print(Y)


def dict_add(X, Y):
    d = X.copy()
    for k, v in Y.items():
        if k in X:
            d[k] += v
        else:
            d[k] = v
    return d


def dict_sub(X, Y):
    d = {}
    for k, v in Y.items():
        if not k in X:
            d[k] = v
    return d


def dict_mul(X, Y):
    d = {}
    for k, v in Y.items():
        if k in X:
            d[k] = v + X[k]
    return d


print("add:")
print(dict_add(X, Y))
print("sub:")
print(dict_sub(X, Y))
print("mul:")
print(dict_mul(X, Y))

print(("s", "e") in X)
print(("s", "e") in Y)
