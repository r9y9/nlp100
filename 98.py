import h5py
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

h5file = h5py.File("96.jl.h5")
X = h5file["X"].value

# n_samples x n_features
assert X.shape[1] == 300


df = pd.read_csv("./countries.csv")
labels = np.array(df.iloc[:, 1])


Z = ward(X)
dendrogram(Z, labels=labels)
plt.show()
