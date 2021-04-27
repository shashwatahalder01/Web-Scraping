import pandas as pd
import os 
from pathlib import Path
import requests

def getdiff():
    a=os.path.join(os.getcwd(),'data','a.xlsx')
    b=os.path.join(os.getcwd(),'data','b.xlsx')

    sheet1 = pd.read_excel(a)
    sheet2 = pd.read_excel(b)
    # print(df1)
    # print(df1.equals(df2))
    # print(df2)

    # # if df1.equals(df2):
    # #     print('not unique')
    # # else:
    # #     print('unique')
    c=[]
    for i,j in zip(sheet1,sheet2):    
        # Creating empty lists to append the columns values    
        a,b =[],[]
        # Iterating the columns values
        for m, n in zip(sheet1[i],sheet2[j]):
            # Appending values in lists
            a.append(m)
            b.append(n)
        # Iterating the list's values and comparing them
        for m, n in zip(range(len(a)), range(len(b))):
            if a[m] != b[n]:
                # print('Column name : \'{}\' and Row Number : {}'.format(i,m))
                # print(sheet1[i][m])
                c.append(sheet1[i][m])
                # googleSearch(sheet1[i][m])
    return c;            
