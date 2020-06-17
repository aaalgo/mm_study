#!/usr/bin/python3
import sys
import random
import pickle
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import cv2

with open('data/gene_id.pkl', 'rb') as f:
    id_to_gene = pickle.load(f)

with open('data/chrome.pkl', 'rb') as f:
    chromes, gene2chr = pickle.load(f)


images = {}
for k, v in chromes.items():
    images[k] = [0, 0]
    pass

with open('missing.xxx', 'w') as mis:
    for l in open('data/aucs/bl', 'r'):
        gene, score = l.strip().split('\t')
        score = float(score)
        #if score > 0.2: #< 0.95:
        #    continue
        loci = []
        names = id_to_gene[gene]
        for x in names.split('/'):
            x = x.strip()
            if len(x) == 0:
                continue
            if x in gene2chr:
                loci = gene2chr[x]
                break
            pass
        for chrome, start, end, strand in loci:
            chrome = chrome + strand
            l = images[chrome]
            l[0] += score
            l[1] += 1
            pass
        pass

names = ['%d' % x for x in range(1,23)]
names.append('X')
names.append('Y')

Y = []
for name in names:
    pos = images['chr' + name + '+']
    neg = images['chr' + name + '-']
    s, c = pos
    s1, c1 = neg
    s += s1
    c += c1
    Y.append(s/c)


objects = names
x_pos = np.arange(len(objects))
 
plt.figure(figsize=(16, 6))
plt.ylim(0,1)
plt.bar(x_pos, Y, align='center', alpha=0.5)
plt.xticks(x_pos, objects)
plt.ylabel('average AUC')
plt.savefig('chromosome1.png')
