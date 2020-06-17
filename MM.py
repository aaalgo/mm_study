#!/usr/bin/env python3
import sys
import os
import pickle
import numpy as np
import pandas as pd
from openpyxl import load_workbook

# load probeset to gene mapping
def load_mapping ():
    anno = pd.read_csv('meta/HG-U133_Plus_2.na36.annot.csv',
                        skiprows=25,
                        header=0,
                        quotechar='"')
    lookup = {}
    for _, row in anno.iterrows():
        ps = row.loc['Probe Set ID']
        sym = row.loc['Gene Symbol']
        lookup[ps] = sym
        pass
    return lookup

#load_annotation()

def load_uams ():
    info = pd.read_excel('data/TT45_218 patient test parameters cleaned to upload 20180222 pf.xlsx',
                            sheet_name = 'BL_PC_Data',
                            header = 0,
                            index_col = 0,
                            dtype={'CelName': str, 'TxtName': str})
    links = pd.read_excel('data/TT45_218 patient test parameters cleaned to upload 20180222 pf.xlsx',
                            sheet_name = 'TT45 218 patids with matched bl',
                            header = 0,
                            index_col = 0,
                            dtype=str)
    return info, links

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


if __name__ == '__main__':
    lookup = load_mapping()
    with open('data/gene_id.pkl', 'wb') as f:
        pickle.dump(lookup, f)

    '''
    load_chr_mapping_to_pickle()
    sys.exit(0)
    info = load_info()
    #print(info.iloc[0])
    print(info["isotype"].unique())
    links = load_links()
    print(links.iloc[0, :])
    '''
    pass
