# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:09:01 2021

@author: LatinVan9
"""
#Read The whole file
import pandas as pd

df = pd.read_csv('data1.csv')

print(df.to_string()) 

#Read selected rows with conditions
df_conditional=df[df['Col6']>20]
print(df_conditional)

#Read selected rows
df_selected=df[1:3]
print(df_conditional)

#Print selected colums from the data loaded
print(df['Col3'])

#Read selected columns from file
df_col = pd.read_csv('data1.csv',  usecols=['Col1', 'Col5'])
print(df_col)

#Rename the header
df.rename(columns={'Col1':'Changed_Label'},inplace=True)


#Add A column with pre-filled values
df['new_column'] = 'New Col'

#Remove a row
df.drop(3,axis=0,inplace=True)

#Remove multiple rows
df.drop([1,4],axis=0,inplace=True)

#Remove conditional rows
df = df.drop(df[df.Col6 <=12].index)

#Add A row at the end of file
new_row = {'Changed_Label':'A_End', 
           'Col2':'B_End', 'Col3':'C_End',
           'Col4':'D_End', 'Col5':'E_End',
           'Col6':15, 'new_column':'Test_It'}
df=df.append(new_row,ignore_index=True)

#Modify a cell
df.at[0,'Col2']='CHANGED'

#Remove A column
del df['Col4']

#Write on the same file
#df.to_csv('data1.csv',index=False)

#Output to a new CSV file
df.to_csv('Modified_Data.csv',index=False)



