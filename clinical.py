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

cohorts = {"EMTAB4032": extract_clinical(sc2.ix[sc2['Study'] == 'EMTAB4032']),
           "GSE24080": extract_clinical(sc2.ix[sc2['Study'] == 'GSE24080UAMS']),
           "MMRF": extract_clinical(sc2.ix[sc2['Study'] == 'MMRF']),
           "UAMS": extract_clinical(uams)}


def filter_survive (df):
    live = df.ix[(df['os_flag'] == 0) and (df['os'] > 180)]
    dead = df.ix[(df['os_flag'] == 1) and (df['os'] < 180)]
    return live, dead

for k, df in cohorts.items():
    print(k)
    print(df.describe())
    print()
    #live, dead = filter_survive(df)
    #print(k, live.shape[0], dead.shape[0])

