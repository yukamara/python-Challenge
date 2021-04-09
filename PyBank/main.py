# Import modules
import os
import csv

# set the path for collecting the ellection data
budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    for row in csv_reader:
        print(row)

# TASKS
# 1. The total number of months included in the dataset
    for line in csv_reader:
        no_of_months = sum(1 for row in csv_reader)
        print(no_of_months)


# 2. The net total amount of "Profit/Losses" over the entire period
    #total_profit_loss = 0
    #for x in 
    profit_loss = ([sum(x) for x in zip(*csv_reader)])
    print(profit_loss)

# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# 4. The greatest increase in profits (date and amount) over the entire period


# 5. The greatest decrease in losses (date and amount) over the entire period
