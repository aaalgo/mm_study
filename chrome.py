#!/usr/bin/env python3
import sys
import pickle

chromes = {}
for i in range(1, 23):
    chromes['chr' + str(i) + '+'] = [1000000000, 0]
    chromes['chr' + str(i) + '-'] = [1000000000, 0]
chromes['chrX+'] = [1000000000, 0]
chromes['chrX-'] = [1000000000, 0]
chromes['chrY+'] = [1000000000, 0]
chromes['chrY-'] = [1000000000, 0]
chromes['chrM+'] = [1000000000, 0]
chromes['chrM-'] = [1000000000, 0]
#print(chromes)

lookup = {}
with open('meta/gencode.v19.annotation.gtf', 'r') as f:
    for l in f:
        if l[:3] == 'chr':
            fs = l.strip().split('\t')
            chrome = fs[0]
            start = int(fs[3])
            end = int(fs[4])
            strand = fs[6]
            if start > end:
                print(chrome, start, end, strand)
            be = chromes[chrome + strand]
            if start < be[0]:
                be[0] = start
            if end > be[1]:
                be[1] = end
            name_off = l.find('gene_name')
            if name_off < 0:
                continue
            name_off = l.find('"', name_off)
            if name_off < 0:
                continue
            name_off += 1
            name_end = l.find('"', name_off)
            if name_end < 0:
                continue
            name = l[name_off:name_end]
            #print(chrome, start, end, strand, name)
            lookup.setdefault(name, []).append([chrome, start, end, strand])
            pass
    #with open('data/chromsome.pkl', 'wb') as f:
    #    pickle.dump(lookup, f)
with open('data/chrome.pkl', 'wb') as f:
    pickle.dump((chromes, lookup), f) 
