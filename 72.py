from stemming.porter2 import stem
import sys
import numpy as np
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


def build_idx(vocab):
    word2idx = {}
    count = 0
    for k, v in vocab.items():
        word2idx[k] = count
        count += 1
    assert count == len(vocab)
    return word2idx


def sentence2features(words, vocab, word2idx):
    N = len(vocab)
    x = np.zeros(N, dtype=np.int)
    for word in words:
        idx = word2idx[word]
        x[idx] += 1
    return x


K = 13
stopwords = sorted(vocab.items(), key=lambda x: x[1])[:: -1][: K]
for k, v in stopwords:
    print(k, v)
stopwords_dict = dict(stopwords)

print(len(vocab))
print(vocab.get("like"))
word2idx = build_idx(vocab)


def is_stopword(x, stopwords_dict=stopwords_dict):
    if x in stopwords_dict:
        return True
    return False


def is_not_stopword(x, stopwords_dict=stopwords_dict):
    return not is_stopword(x, stopwords_dict)


X = []
Y = []
with open("sentiment.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line[: -1].lower()
        y, words = line.split(" ")[0], line.split(" ")[1:]
        y = 0 if (y == "+1") else 1
        words = list(map(stem, words))
        words = list(filter(is_not_stopword, words))
        x = sentence2features(words, vocab, word2idx)

        X.append(x)
        Y.append(y)

X = np.array(X)
Y = np.array(Y)

print(X.shape)
print(Y.shape)

sys.exit(0)
