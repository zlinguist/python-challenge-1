#!/usr/bin/env python
# coding: utf-8

import os
import csv


def main():
    poll_csv = os.path.join("Data", "election_data.csv")
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
            #for candidate in candidate_percentage:
            #print(f'{candidate} {candidate_percentage[candidate]:.3f}')
        winner = ""
        winner_percent = 0.0
        for candidate in candidate_percentage:
            if candidate_percentage[candidate] > winner_percent:
                winner_percent = candidate_percentage[candidate]
                winner = candidate

        f = open("election_results.txt", mode="w")
        f.write("Election Results\n")
        f.write("------------------------------\n")
        f.write(f'Total Votes: {total_votes}\n')
        f.write("------------------------------\n")
        for candidate in candidate_percentage:
            f.write(f'{candidate}: {candidate_percentage[candidate]:.3f}% ({candidate_totals[candidate]})\n')
        f.write("------------------------------\n")
        f.write(f'Winner: {winner}\n')
        f.write("------------------------------\n")
        f.close()
    f = open("election_results.txt", mode="r")
    for line in f:
        print(line, end='')
    f.close()




if __name__ == "__main__":
    main()


# In[ ]:




