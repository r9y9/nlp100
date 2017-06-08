from stemming.porter2 import stem
import sys
import numpy as np
vocab = {}


foobar = [".", ",", "(", ")", '"', "'"]

with open("sentiment.txt") as f:
    lines = f.readlines()
    for line in lines:
        line = line[:-1].lower().strip()
        words = line.split(" ")[1:]
        words = [word.strip() for word in words]
        words = filter(lambda x: x not in foobar, words)
        words = list(map(stem, words))
        for word in words:
            if word in foobar:
                continue
            if word in vocab:
                vocab[word] += 1
            else:
                vocab[word] = 1


def build_idx(vocab):
    word2idx = {}
    ind2word = {}
    count = 0
    for k, v in vocab.items():
        word2idx[k] = count
        ind2word[count] = k
        count += 1
    assert count == len(vocab)
    return word2idx, ind2word


def sentence2features(words, vocab, word2idx):
    N = len(vocab)
    x = np.zeros(N, dtype=np.int)
    for word in words:
        idx = word2idx[word]
        x[idx] += 1
    return x


K = 10
stopwords = sorted(vocab.items(), key=lambda x: x[1])[:: -1][: K]
for k, v in stopwords:
    print(k, v)
stopwords_dict = dict(stopwords)

print(len(vocab))
print(vocab.get("like"))
word2idx, idx2word = build_idx(vocab)


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
        line = line[:-1].lower().strip()
        y, words = line.split(" ")[0], line.split(" ")[1:]
        # 1 means possitive, 0 means negative
        y = 1 if (y == "+1") else 0
        words = [word.strip() for word in words]
        words = filter(lambda x: x not in foobar, words)
        words = list(map(stem, words))
        words = list(filter(is_not_stopword, words))
        x = sentence2features(words, vocab, word2idx)

        X.append(x)
        Y.append(y)

X = np.array(X)
Y = np.array(Y)
#Y = np.zeros((X.shape[0], 2), dtype=int)
#Y[np.arange(X.shape[0]), _Y] = 1

print(X.shape)
print(Y.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.33, random_state=12345)


model = LogisticRegression(penalty="l2", random_state=12345)
model.fit(X_train, Y_train)

Y_hat = model.predict(X_test)
print(np.mean(Y_hat == Y_test))

from sklearn.metrics import classification_report

print(classification_report(Y_test, Y_hat))

coef = model.coef_

print(coef.shape)
weights = coef.ravel()
K = 10
print("\nTopK:")
topK = weights.argsort()[-K:][::-1]
for k in topK:
    print(idx2word[k], weights[k])

print("\nBottomK:")
bottomK = weights.argsort()[:K]
for k in bottomK:
    print(idx2word[k], weights[k])
