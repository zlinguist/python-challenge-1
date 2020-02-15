#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


poll_csv = os.path.join("Data", "election_data.csv")


# In[8]:


with open(poll_csv, mode="r") as poll_file:
    reader = csv.reader(poll_file)
#     for row in reader:
#         print(row)
#         break
    header = next(reader)
    print(header)     


# In[7]:


with open(poll_csv, mode="r") as poll_file:
    reader = csv.reader(poll_file)
#     for row in reader:
#         print(row)
#         break
    header = next(reader)
#     print(header)
    total_votes = 0
    for row in reader:
        total_votes += 1
    print(total_votes)


# In[16]:


with open(poll_csv, mode="r") as poll_file:
    reader = csv.reader(poll_file)
    header = next(reader)
    total_votes = 0
    candidate_totals = {}
    for row in reader:
        total_votes += 1
        if row[2] in candidate_totals:
            candidate_totals[row[2]] += 1
        else:
            candidate_totals[row[2]] = 1 
    print(total_votes)
    print(candidate_totals)


# In[21]:


with open(poll_csv, mode="r") as poll_file:
    reader = csv.reader(poll_file)
    header = next(reader)
    total_votes = 0
    candidate_totals = {}
    for row in reader:
        total_votes += 1
        if row[2] in candidate_totals:
            candidate_totals[row[2]] += 1
        else:
            candidate_totals[row[2]] = 1
    candidate_percentage = {}
    for candidate in candidate_totals.keys():
        candidate_percentage[candidate] = float(candidate_totals[candidate]/total_votes)*100
    print(candidate_percentage)


# In[29]:


with open(poll_csv, mode="r") as poll_file:
    reader = csv.reader(poll_file)
    header = next(reader)
    total_votes = 0
    candidate_totals = {}
    for row in reader:
        total_votes += 1
        if row[2] in candidate_totals:
            candidate_totals[row[2]] += 1
        else:
            candidate_totals[row[2]] = 1
    candidate_percentage = {}
    for candidate in candidate_totals.keys():
        candidate_percentage[candidate] = float(candidate_totals[candidate]/total_votes)*100
#     print(candidate_percentage)
    for candidate in candidate_percentage:
        print(f'{candidate} {candidate_percentage[candidate]:.3f}')


# In[33]:


with open(poll_csv, mode="r") as poll_file:
    reader = csv.reader(poll_file)
    header = next(reader)
    total_votes = 0
    candidate_totals = {}
    for row in reader:
        total_votes += 1
        if row[2] in candidate_totals:
            candidate_totals[row[2]] += 1
        else:
            candidate_totals[row[2]] = 1
    candidate_percentage = {}
    for candidate in candidate_totals.keys():
        candidate_percentage[candidate] = float(candidate_totals[candidate]/total_votes)*100
    print("Election Results")
    print("-------------------------")
    for candidate in candidate_percentage:
        print(f'{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_totals[candidate]})')
    print("-------------------------")
    winner = ""
    winner_percent = 0.0
    for candidate in candidate_percentage:
        if candidate_percentage[candidate] > winner_percent:
            winner_percent = candidate_percentage[candidate]
            winner = candidate
    print(f'Winner: {winner}')
    print("-------------------------")


# In[ ]:


# final script should both print to terminal and export to a text file
# also wrap all this in a main function and then call the function in the final script

