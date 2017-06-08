import h5py
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE

h5file = h5py.File("96.jl.h5")
X = h5file["X"].value

# n_samples x n_features
assert X.shape[1] == 300


df = pd.read_csv("./countries.csv")
labels = np.array(df.iloc[:, 1])

from sklearn.decomposition import TruncatedSVD
X = TruncatedSVD(n_components=50, random_state=0).fit_transform(X)

X_t = TSNE(learning_rate=100, random_state=0).fit_transform(X)

# https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
fig, ax = plt.subplots()
ax.scatter(X_t[:, 0], X_t[:, 1], c=np.arange(len(labels)))
for idx, name in enumerate(labels):
    ax.annotate(name, (X_t[idx, 0], X_t[idx, 1]), size=8)

plt.show()
