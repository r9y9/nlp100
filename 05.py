s = "I am an NLPer"


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


print(ngram(s))
print(ngram(s.split(" ")))
