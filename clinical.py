#!/usr/bin/env python3
import sys
import pandas as pd
from MM import *

# age, gender, ISS
def sc2_calc_clinical (df):
    df["age"] = df["D_Age"]
    df["gender"] = pd.Categorical(df["D_Gender"], categories=["Male", "Female", "NA"])
    df["gender"] = df["gender"].cat.codes #astype(float)
    df["iss"] = df["D_ISS"]
    df["os"] = df["D_OS"]
    df["os_flag"] = df["D_OS_FLAG"]
    pass

def ISS_txt2num (v):
    if v == 'I':
        return 1
    elif v == 'II':
        return 2
    elif v == 'III':
        return 3
    return None

def uams_calc_clinical (df):
    dt_format = '%m/%d/%Y'
    df["age"] = df["Age"]
    df["gender"] = pd.Categorical(df["Gender"], categories=["Male", "Female", "NA"])
    df["gender"] = df["gender"].cat.codes #astype(float)
    df["iss"] = df["ISS_Stage"].apply(ISS_txt2num)
    df["FDDeath"] = pd.to_datetime(df["FDDeath"])
    df["BL_Date"] = pd.to_datetime(df["BL_Date"], format=dt_format)
    df["os"] = (df["FDDeath"] - df["BL_Date"]) / np.timedelta64(1, 'D')
    # death
    df["os_flag"] = pd.notna(df["os"]).astype(int)
    pass

def extract_clinical (df):
    return df[["age", "gender", "iss", "os", "os_flag"]]

sc2 = load_dream_sc2()
sc2_calc_clinical(sc2)

uams, _ = load_uams()
uams_calc_clinical(uams)
#print(uams[["FDDeath", "BL_Date", "os"]])
#print(uams['gender'])

COHORTS = ["EMTAB4032", "GSE24080", "MMRF", "UAMS"]

cohorts = {"EMTAB4032": extract_clinical(sc2.loc[sc2['Study'] == 'EMTAB4032']),
           "GSE24080": extract_clinical(sc2.loc[sc2['Study'] == 'GSE24080UAMS']),
           "MMRF": extract_clinical(sc2.loc[sc2['Study'] == 'MMRF']),
           "UAMS": extract_clinical(uams)}


TH = 18 * 30

def filter_survive_x (df):
    live = df.loc[(df['os_flag'] == 0) & (df['os'] > TH)]
    dead = df.loc[(df['os_flag'] == 1) & (df['os'] < TH)]
    return live, dead

def filter_survive (df):
    live = df.loc[(df['os_flag'] == 0)]
    dead = df.loc[(df['os_flag'] == 1)]
    return live, dead

for k in COHORTS:
    df = cohorts[k]
    print(k)
    #print(df.describe())
    live, dead = filter_survive(df)
    live_long, dead_short = filter_survive_x(df)
    nl = live.shape[0]
    nll = live_long.shape[0]
    nd = dead.shape[0]
    nds = dead_short.shape[0]
    no = df.shape[0] - nl - nd
    print(k, nl, '>', nll, nd, '>', nds, no)
    print(live.describe())
    print()
    print(live_long.describe())
    print()
