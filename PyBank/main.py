# Import modules
import os
import csv

# set the path for collecting the ellection data
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')

    for row in budget_csv:
        print(row[1])

# TASKS
# 1. The total number of months included in the dataset
    for row in budget_csv:
        no_of_months = sum(1 for row in budget)
        print(no_of_months)


# 2. The net total amount of "Profit/Losses" over the entire period
    
    for row in budget_csv:
        total_profit_loss += sum(int(row[1]))
        print(total_profit_loss)

# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# 4. The greatest increase in profits (date and amount) over the entire period


# 5. The greatest decrease in losses (date and amount) over the entire period
