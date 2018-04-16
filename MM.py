#!/usr/bin/env python3
import sys
import os
import pickle
import numpy as np
import pandas as pd
from openpyxl import load_workbook
#from sklearn.model_selection import StratifiedKFold
#from sklearn.metrics import accuracy_score, f1_score, roc_curve, roc_auc_score
#import matplotlib
#matplotlib.use('Agg')

#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import plotly.offline as py
#import plotly.graph_objs as go


#load_annotation()

def load_uams ():
    meta = pd.read_excel('data/TT45_218 patient test parameters cleaned to upload 20180222 pf.xlsx',
                            sheet_name = 'BL_PC_Data',
                            header = 0,
                            index_col = 0,
                            dtype={'CelName': str, 'TxtName': str})
    links = pd.read_excel('data/TT45_218 patient test parameters cleaned to upload 20180222 pf.xlsx',
                            sheet_name = 'TT45 218 patids with matched bl',
                            header = 0,
                            index_col = 0,
                            dtype=str)
    return meta, links

def load_uams2 ():
    meta = pd.read_excel('data/20180206_Huang_EnlargedPopulation CleanedToUpload 20180409 pf.xlsx',
                            sheet_name = 'PC_Data',
                            header = 0,
                            index_col = 0)
    links = pd.read_excel('data/20180206_Huang_EnlargedPopulation CleanedToUpload 20180409 pf.xlsx',
                            sheet_name = 'Cel_txt file info',
                            header = 0,
                            index_col = 0,
                            dtype=str)
    return meta, links

'''
def load_chr_mapping_to_pickle ():
    lookup = {}
    with open('data/gencode.v19.annotation.gtf', 'r') as f:
        for l in f:
            if l[:3] == 'chr':
                fs = l.strip().split('\t')
                chrom = fs[0]
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
                lookup[name] = chrom
                pass
    with open('data/chromsome.pkl', 'wb') as f:
        pickle.dump(lookup, f)
    '''

def load_dream_sc2 ():
    anno = pd.read_csv('data/dream/sc2_Training_ClinAnnotations.csv',
                        header=0, index_col=None,
                        quotechar='"')
    #print(anno['MA_probeLevelExpFile'])
    #print(anno['MA_probeLevelExpFileSamplId'])
    #print(anno['MA_geneLevelExpFile'])
    return pd.read_csv('data/dream/sc2_Training_ClinAnnotations.csv',
                    header=0, index_col=None,
                    na_values="NA",
                    dtype={'Study': str,
                           'D_Age': float,
                           'D_Gender': 'category',
                           'D_OS': float,
                           'D_OS_FLAG': int,
                           'D_PFS': float,
                           'D_PFS_FLAG': int,
                           'D_ISS': float,
                           'MA_probeLevelExpFileSamplId': str},
                    quotechar='"')


if __name__ == '__main__':
    load_dream_sc2()
    '''
    load_dream()
    sys.exit(0)
    lookup = load_mapping()
    with open('data/gene_id.pkl', 'wb') as f:
        pickle.dump(lookup, f)
    #load_chr_mapping_to_pickle()
    sys.exit(0)
    info = load_info()
    #print(info.iloc[0])
    print(info["isotype"].unique())
    links = load_links()
    print(links.iloc[0, :])
    pass
    '''
