#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[9]:


budget_csv = os.path.join("Data", "budget_data.csv")


# In[10]:


print(budget_csv)


# In[12]:


get_ipython().system('ls -l Data/budget_data.csv')


# In[13]:


get_ipython().system('head -n 5 Data/budget_data.csv')


# In[23]:


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(header)
#     for row in csvreader:
#         print(row[1])
#         break
    number_months = 0
    total_amount = 0
    for row in csvreader:
        number_months += 1
        total_amount += int(row[1])
    print(number_months, total_amount)


# In[32]:


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    previous_value = None
    changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]
    for row in csvreader:
        if previous_value:
            change = int(row[1]) - previous_value
            changes.append(change)
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        previous_value = int(row[1])
#     print(changes[:5])
    print(greatest_increase)
    print(greatest_decrease)


# In[33]:


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    previous_value = None
    changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]
    for row in csvreader:
        if previous_value:
            change = int(row[1]) - previous_value
            changes.append(change)
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        previous_value = int(row[1])
#     print(changes[:5])
    print(greatest_increase)
    print(greatest_decrease)
    total_change = 0
    for value in changes:
        total_change += value
    average_change = total_change / len(changes)
    print(average_change)


# In[34]:


# need both print to terminal and export a text file
# also, for final version, wrap this into a main() function in the file and then call the function


# In[43]:


with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    previous_value = None
    changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]
    number_months = 0
    total_change = 0
    total_amount = 0
    for row in csvreader:
        if previous_value:
            change = int(row[1]) - previous_value
            changes.append(change)
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]
        previous_value = int(row[1])
        number_months += 1
        total_amount += int(row[1])
#     print(changes[:5])
#     print(greatest_increase)
#     print(greatest_decrease)
    for value in changes:
        total_change += value
    average_change = total_change / len(changes)
#     print(average_change)
    print("Financial Analysis")
    print("--------------------------------")
    print(f'Total Months: {number_months}')
    print(f'Total: ${total_amount}')
    print("Average Change: {0:.2f}".format(round(average_change, 2)))
    print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
    print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')


# In[44]:


f = open("financial_analysis.txt", mode="w")
f.write(...)


# In[ ]:




