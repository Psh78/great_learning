# Matplotlib is a python library used for data visualization
# You can create bar plots, scatter-plots, histograms and a lot more with matplotlib

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#plotting basic linear plot in which y is twice of x
"""
x=np.arange(1,11)
print(x)

y= 2*x
print(y)
"""
"""
plt.plot(x,y)
plt.show()
"""

#Adding title and labels
#we can add titles, x and y labels as ... 
#plt.title("<title name>") --- to add title to the plot
#plt.xlabel("<title name>") --- to add title to the x axis or x plot
#plt.ylabel('<title name>') --- to add title to the y axis or y plot
"""
plt.plot(x,y)
plt.title("line plot")
plt.xlabel('time')
plt.ylabel('speed')
plt.show()
"""
# We can change the different aspects of the plot such as color, line style, and line width as..
"""
plt.plot(x,y,color='r',lineStyle=':',linewidth=2)
plt.title('x and y plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
"""
# Converting two lines into same plot
"""
x=np.arange(1,11)
y1=2*x
y2=3*x
"""
"""
plt.plot(x,y1,color='r',linestyle=':',linewidth=2)
plt.plot(x,y2,color='g',linestyle='-',linewidth=3)
plt.title('Line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.show()
"""

# Adding subplots i.e., multipl plots in a single screen 
"""
plt.subplot(1,2,1)
plt.plot(x,y1,color='g',linestyle=':',linewidth=2)
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(x,y2,color='r',linestyle='-',linewidth=3)
plt.grid(True)
plt.show()
"""

#BAR PLOTS
#first we create a dictionary with keys and values. Then convert them to individual lists and assgin the keys and values to different variables 
# then we use function. syntax--- plt.bar(<first variable>,<second variable>)
# to print horizontal bar plot we use ---- plt.barh(<first variable>,<second variable>)
"""
student={ 'bob':50,'hari':80,'manish':69}
Names = list(student.keys())
Marks = list(student.values())

plt.barh(Names,Marks,color='g',linestyle=':',linewidth=0.5)
plt.title('Students marks:')
plt.xlabel('Name of the student')
plt.ylabel('Marks')
plt.show()
"""

#Scatter plot
#scatter plot is drawn for a list of different elemetns or numbers...The intersection of elements is represented as points
# syntax is--- plt.scatter(<first variable>,<second variable>)
"""
x=[1,2,3,4,5]
y=[6,7,8,9,0]
z=[3,4,5,2,9]
#Changing the Aesthetics of scatter plot
#to change plot shape we use marker variable
plt.scatter(x,y,marker='*',color='g',s=100)#here s is the size of mark
#plotting two scatter plots in the same screen 
plt.scatter(x,z,marker='^',color='r',s=50)
plt.show()
"""
# Adding sub-plots
"""
x=[1,2,3,4,5]
y=[6,7,8,9,0]
z=[3,4,5,2,9]

plt.subplot(1,2,1)
plt.scatter(x,y,marker='^',c='r',s=100)

plt.subplot(1,2,2)
plt.scatter(x,z,marker='*',c='g',s=100)
plt.show()
"""

# Histogram
# a bar graph is used for categorical values and histogram is used for numerical values
"""
x=(1,2,4,5,3,8,2,5,6,2,3,4,4,2,6,2,3,4,1,5)
plt.hist( x,color='r',bins=2)#color can be changed using color
#bins is used to change the no.of blocks of histogram. In the above code all the values in the histogram are represented with only two bars or bins
plt.show()
"""
#creating a histogram for a csv file
"""
x=pd.read_csv('survey.csv')
x.head()
plt.hist(x['Value'],bins=20,color='g')
plt.show()
"""

# Box-plot
# a box-plot is a pictorial representatin of a five number summary. which shows the values in parts of---  0 or Min, 25%, 50%, 75%, 100 or Max values
# No of list are made based on desired number of boxes. and then made lists and then represented by using synta --- plt.boxplot(<list naem>)x=[1,2,3,4,5]
#the middle line is the median 
"""
x=[1,2,3,4,5]
y=[6,7,8,9,0]
z=[1,4,6,7,8]
data=list([x,y,z])
plt.boxplot(data)
plt.show()
"""
#violen plot:
#it is same as box plot but looks in shape of a violen
"""
x=[1,2,3,4,5]#median is 3
y=[6,7,8,9,0]# median is 8
z=[1,4,6,7,8]# median is 6
data=list([x,y,z])
plt.violinplot(data,showmedians=True)# to show median value we write showmedians=True
plt.show()
"""

# Pie-Chart

employee=['raju','akash','lilly','hema']
salary=[35,100,56,87]
#plt.pie(salary,labels=employee)
#plt.show()
#chaing the aesthetics of pie-chart----like adding the percentages or colors
"""
plt.pie(salary, labels= employee, autopct='%0.1f%%',colors=['red','green','teal','magenta'])# autopct is used to add percentage and by using colors we can change the colors
plt.show()
"""
# DoughNut-Chart
"""
plt.pie(salary,labels=employee,radius=2)
plt.pie([1],colors=['w'],radius=1)
plt.show()
"""


# SEABORN LINE PLOT
# seaborn is built on matplot and is used for visualization
import seaborn as sns
"""
fmri=sns.load_dataset('fmri')
fmri.head()
fmri.shape
#here markers=True is usd to mark the points on the line, and hue is used to add another line onto the available graph
fmri=sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event',style='event',markers=True)
plt.show()

"""
# SeaBorn bar-plot
"""
# The white grid behind the bar plot is set using the style word in the nextline. It us set as white color
sns.set(style='whitegrid')
#we need pandas to load any data set. So we used pandas in the next line
poke=pd.read_csv("survey.csv")
sns.barplot(x='Year',y='Units',data=poke)
plt.show()
"""

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

print(len(verse))
print(verse.find('and'))
print(verse.rfind('you'))#rfind is used to find the last occurrance
print(verse.count('you'))
length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')
print(message.format(length,first_idx,last_idx,count))