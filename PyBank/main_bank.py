# Import modules
import os
import csv

# set the path for collecting the ellection data
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')


    for row in budget_csv:
        profit_loss = (row[1])
        print(profit_loss)

# TASKS
# 1. The total number of months included in the dataset
    month_count = 0     # initialize noumber of months
    for row in budget_csv:  # loop through rows to compute the number of months
        month_count += 1
    print(f'The total number of months is {month_count}') # Result for total number of months
   



# 2. The net total amount of "Profit/Losses" over the entire period
with open(csvpath, newline='') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=',')


    for row in budget_csv:
        net_profit_loss = (sum(profit_loss))
        print(f'The total profit/loss is {net_profit_loss}')

    for row in budget_csv:
        total_profit_loss += (sum(row[1]))
        print(total_profit_loss)

# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#    Profit_change = []
#    for each number in row[i]

# 4. The greatest increase in profits (date and amount) over the entire period


# 5. The greatest decrease in losses (date and amount) over the entire period
