#!/usr/bin/env python
# coding: utf-8

import os
import csv


def main():
    budget_csv = os.path.join("Data", "budget_data.csv")
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
        for value in changes:
            total_change += value
        average_change = total_change / len(changes)
        f = open("financial_analysis.txt", mode="w")
        f.write("Financial Analysis\n")
        f.write("--------------------------------\n")
        f.write(f'Total Months: {number_months}\n')
        f.write(f'Total: ${total_amount}\n')
        f.write("Average Change: {0:.2f}\n".format(round(average_change, 2)))
        f.write(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n')
        f.write(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n')
        f.close()
    f = open("financial_analysis.txt", mode="r")
    for line in f:
        print(line, end='')
    
  
if __name__ == "__main__":
    main()

