# coding: utf-8

import pandas as pd

def initDict(dictpath_):
    cedict = pd.read_csv(dictpath_, sep='\s*∆\s*', names = ['trad', 'simp','pron','def'])
    cedict_lookup = {}
    for i in range(cedict.shape[0]):
        row = cedict.loc[i]
        simp = row['simp'].decode('utf8')
        pron = row['pron'].decode('utf8')
        definition = row['def'].decode('utf8')
        cedict_lookup[simp] = [pron, definition]
    return(cedict_lookup)
