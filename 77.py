import sys
import numpy as np

Y = []
Y_hat = []

with open("76.py.out") as f:
    lines = f.readlines()
    for line in lines:
        line = line[:-1]
        s = line.split("\t")
        label, predicted, prob, text = line.split("\t")
        y = 1 if label == "+1" else 0
        y_hat = 1 if predicted == "+1" else 0
        Y.append(y)
        Y_hat.append(y_hat)

Y = np.array(Y)
Y_hat = np.array(Y_hat)

print("Accuracy: {}".format(np.sum(Y == Y_hat) / len(Y)))
print("Precision +1: {}".format(np.sum(Y[Y_hat == 1]
                                       == Y_hat[Y_hat == 1]) / len(Y[Y_hat == 1])))
print("Recall +1: {}".format(np.sum(Y[Y == 1]
                                    == Y_hat[Y == 1]) / len(Y[Y == 1])))

from sklearn.metrics import classification_report
print(classification_report(Y, Y_hat, digits=7))

sys.exit(0)
