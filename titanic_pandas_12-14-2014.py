__author__ = 'minnawin'

import pandas as pd
import numpy as np
import pylab as P

'''This script was created using PyCharm and is taken from the Kaggle Titanic 'Getting started with Python'
   the Pandas section.  Not all steps are included.
'''

#When using read_csv, set header=0 to skip the first line of the text when you know that
#the first row/line is the header.
df = pd.read_csv('../../Titanic/train.csv', header=0)
df['Age'].hist()
#Uncomment the following line to render the histogram of the ages in the train dataset.
#P.show()

#Map female and male values to 0 and 1 respectively, to make things easier to calculate.
#First, create a new column called 'Gender' to hold these values so we don't clobber the
#original data in the 'Sex' column.
df['Gender'] = df['Sex'].map( {'female': 0, 'male' : 1} ).astype(int)

print "PClass    #Male survivors \n======    ===============\n"
for i in range (1,4):
    print i,"          ", len(df[ (df['Sex'] == 'male' ) & (df['Pclass'] == i) & (df['Survived'] == 1) ])


#CLEAN UP DATA, ESPECIALLY the Age column, where there are Nan "values"....

#Calculate the median age for each passenger class.  Initialize the median_ages array to zeroes, then fill it with
#the median age for each passenger class.
median_ages = np.zeros( (2,3))
for i in range(0,2):
    for j in range(0,3):
        median_ages[i,j] = df[ (df['Gender'] == i) & (df['Pclass'] == j+1)] ['Age'].dropna().median()
print "\n----------------------1st Class  2nd Class  3rd Class\nMedian age of females %s       %s        %s\n "%(median_ages[0][1],median_ages[0][1],median_ages[0][2])
print "\n----------------------1st Class  2nd Class  3rd Class\nMedian age of males   %s       %s        %s\n "%(median_ages[1][1],median_ages[1][1],median_ages[1][2])

#Make a copy of the Age column and do any filtering on the copy to preserve the original data.
df['AgeFill'] = df['Age']
for i in range(0,2):
    for j in range(0,3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1),'AgeFill'] == median_ages[i,j]

#view the first 10 rows, to verify that the median ages are filled with the some numeric value.
#print df[ df['Age'].isnull() ][ ['Gender','Pclass', 'Age', 'AgeFill']].head(10)

#Check the mean, standard deviation, min and max values of the dataset.
#print df.describe()

#Determine which of the columns are not numerical types and drop them before we perform our analysis. We
#will also drop the 'Age' column, since we cleaned up any NaN values in the AgeFill
print df.dtypes[df.dtypes.map(lambda x: x=='object')]
df = df.drop(['Name','Sex','Ticket','Cabin','Embarked'], axis=1)
df = df.drop(['Age'], axis=1)

#Convert the data into a Numpy array, assigning the data to a new variable, train_data.
train_data = df.values
print "Data in numpy array: ",train_data


