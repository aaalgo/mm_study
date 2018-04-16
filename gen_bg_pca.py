#!/usr/bin/env python3
import math
import sys
import random
from tqdm import tqdm
import numpy as np
from sklearn.decomposition import PCA
import pickle

if __name__ == '__main__':

    expr = np.load('data/npy/bg.expr.npy')
    print(expr.shape)
    #expr = expr[:1000, :]
    expr = np.log(expr+1)

    pca = PCA(n_components=500)
    pca.fit(expr)
    print(pca.components_.shape)

    pickle.dump(pca, open('data/bg_pca.pickle', 'wb'))

