from stemming.porter2 import stem

vocab = {}

with open("sentiment.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line[:-1].lower()
        words = line.split(" ")[1:]
        words = list(map(stem, words))
        for word in words:
            if word in vocab:
                vocab[word] += 1
            else:
                vocab[word] = 1


K = 50
stopwords = sorted(vocab.items(), key=lambda x: x[1])[::-1][:K]
for k, v in stopwords:
    print(k, v)
stopwords_dict = dict(stopwords)


def f(x, stopwords_dict=stopwords_dict):
    if x in stopwords_dict:
        return True
    return False


def test_stopwords():
    assert f(".") == True
    assert f("a") == True
    assert f("of") == True
    assert f("apple") == False


test_stopwords()
