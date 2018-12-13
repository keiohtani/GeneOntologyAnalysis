import pandas as pd
import os

pd.set_option('display.max_row', 100)
pd.set_option('display.max_columns', 20)

def readData():
    df = pd.read_csv("data.csv")
    return df

def main():
    df = readData()
    df = df.loc[df.loc[:, 'Query cover'] > 0.6]
    arr = []
    nonAcceptedWords = ['hypothetical', 'predicted', 'PREDICTED', 'uncharacterized protein', 'Putative', 'putative', 'LOW QUALITY PROTEIN']
    for word in nonAcceptedWords:
        df = df.loc[~df.loc[:, 'Description'].str.contains(word)]
    # df = df.loc[df.loc[:, 'Description'].map(lambda desc: False if 'hypothetical' or 'predicted' or 'PREDICTED' or 'uncharacterized protein' or 'Putative' or 'Putative' or 'LOW QUALITY PROTEIN' in desc else True)]
    for i in range(0, 101):
        dfTemp = df.loc[df.loc[:, 'Ident'].map(lambda x: x == i/100)]
        if (dfTemp.loc[:, 'Query cover'].any()):
            arr.append(dfTemp.loc[:, 'Query cover'].idxmax())
    print(arr)
    result = df.loc[arr, :]
    result.to_csv(os.getcwd() + '/result.csv')
    print(result)

main()