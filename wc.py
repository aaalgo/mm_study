#!/usr/bin/env python3
import sys
from glob import glob
from os import path
from wordcloud import WordCloud
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

stop = ['cell', 'protein', 'process']

for path in glob('chart*.th*'):
    print(path)
    bl = pd.read_table(path, header=0, index_col=None)
    buf = []
    for _, row in bl.iterrows():
        try:
            text = row.iloc[1]
            #print(text)
            buf.extend(text.split('~')[1].replace('-', ' ').split(' '))
        except:
            pass
    
    buf = list(filter(lambda x: not x in stop, buf))
    text = ' '.join(buf)
    print(text)
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    wordcloud.to_file('wc-' + path + '.png')
    pass

