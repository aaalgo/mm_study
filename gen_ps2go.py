#!/usr/bin/env python3
import pickle
import pandas as pd

gaf = pd.read_table('data/goa_human.gaf',
                    skiprows=23,
                    header=None,
                    index_col=None,
                    names=['c%d' % i for i in range(16)])
gene2go = {}
for _, row in gaf.iterrows():
    gene = row.iloc[2]
    go = row.iloc[4]
    gene2go.setdefault(gene, []).append(go)
    pass

anno = pd.read_csv('data/HG-U133_Plus_2.na36.annot.csv',
                    skiprows=25,
                    header=0,
                    quotechar='"')
ps2go = {}
with open('data/ps2go.txt', 'w') as f:
    for _, row in anno.iterrows():
        ps = row.loc['Probe Set ID']
        sym = row.loc['Gene Symbol']
        terms = list(set(gene2go.get(sym, [])))
        ps2go[ps] = terms
        f.write('%s\t%s\n' % (ps, ','.join(terms)))
        pass

with open('data/ps2go.pickle', 'wb') as f:
    pickle.dump(ps2go, f)



