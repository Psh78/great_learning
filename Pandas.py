# PANDA IS USED FOR 'DATA MANIPULATION'
# PANDA stands for 'Panel Data' and is the core library for the data manipulation and data analysis
# PANDA consists of single and multi-dimensinoal data-structures for data-manipulation
# single dimensional data structures are called 'Series Object' and multi-dimensional data structures are called 'Data-Frame'
# A series object is a one-dimensional labeled array

import pandas as pd

#using Series-Object
"""
s1=pd.Series([1,2,3,4])
print((s1))
"""
#changing the attribute of indexing to alphabets
"""
s1=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s1)
"""
#series object from dictionary
#here a,b,c,d are keys that became indexes and the ints are numbers
"""
print(pd.Series({'a':10,'b':20,'c':30}))#here we created a dictionary Series-object
print(pd.Series({'a':10,'b':20},index=['b','c','a','d'])) #on this line c and d keys are not present in the dictionarty so they give NaN or none in the output
"""
#Extracting invidivual values from series:
"""
p1=pd.Series([1,2,3,4])
print('Extracting a single element:',p1[2])#Extracting a single element
print('Extracting elements from the back:',p1[-3:])#Extracting elements from the back
print('Extracting a sequence of elements:',p1[2:])#Extracting a sequence of elements
"""
#Basic MATH operations on Series
#adding a scalar value to a series elements
"""
p1=pd.Series([1,2,3,4])
p2=pd.Series([4,3,2,1])
print('adding a sclar value to a series elements.. here adding 5:',p1+5)
print('adding two series Objects:',p1+p2)
"""
#PANDAS DATA-FRAME OR MULTI-DIMENSIONAL DATA STRUCTURE
# We create a data-rame using dictionary
"""
p1=pd.DataFrame({'Name':['Prashanth','Poojitha','Ramya'],'Marks':[90,80,70]})
print(p1)
"""
#DATA-FRAME IN-BUILT FUNCTIONS:
#they are head(),shape(),describe(),tall()
#head()-to see first five records of a data-frame
#tail()-to see last five records of a data-frame
#shape-to know number of rows and columns in a data-frame
#describe()-to know general information about a data-frame

c=pd.read_csv('survey.csv')
"""
print('prints the first five records of this data-frame',c.head())
print('prints the last five records of the data-frame',c.tail())
print('prints the number of rows and columns in a data-frame',c.shape)
print('prints the general information about a data-frame',c.describe())
"""
#iloc and loc methods
#structure is <filename>.[<first to desired rows>,<first to desired columns>]
"""
print(c.iloc[0:3,5:7])
"""
#loc--- The only difference between iloc and loc is that instead of indexees of columns, we give names of the columns 
#syntax is ---- <filename>.lic([first to destined rows, ("<start columns names","destined end columns names")])
"""
print(c.loc[0:1,("Units","Value")])
"""
#we can remove the columns from the data-frame using "drop"
#Structure is <filename>.drop(<column name>,axis="<1 for vertical and 0 for columns>")
"""
print('prints by removing "Year" column',c.drop(["Year","Value","Units"],axis=1))
print('prints by removing 0 column',c.drop(0,axis=0))
"""
#More pandas Functions
#Mean,Minimum,Median,Maximum
#syntax is same. But we have to change the functions....
#syntax is--- <filename>.<function_name>
"""
print(c['Units','Year'].mean())
"""
"""
print(c.min())
print(c.median())
print(c.max())
"""
#Apply method is used to apply a particular method for rows and columns
"""
def double_make(s):
    return s*2

print(c[['Units','Year']].apply(double_make))
"""
#value_counts() and sort_values()
#value_counts()--returns the no.of times a value is repeated in a certain column..
#syntax is--- <filename>['<column_name>].value_counts()
#sort_values()-- used to sort the given column
#syntax is--- <filename>.sort_values(by='<column_name>')
"""
print('Value counts is:',c['Units'].value_counts())
print('sort values:',c.sort_values(by='Units'))
"""
