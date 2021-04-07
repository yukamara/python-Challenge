# Import modules
import os
import csv

# set the path for collecting the ellection data
election_csv = os.path.join('Resources', 'election_data.csv')

# access and read the election data file
with open(election_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

#    for row in csv_reader:
#        print(row)

# TASKS
# 1. The total number of votes cast
    total_votes_cast = sum(1 for row in csv_reader) - 1 # I subtract 1 because the code sums everything including the header row
    print(total_votes_cast)


# 2. A complete list of candidates who received votes


# 3. The percentage of votes each candidate won


# 4. The total number of votes each candidate won


# 5. The winner of the election based on popular vote.








# 1. The total number of months included in the dataset


# 2. The net total amount of "Profit/Losses" over the entire period


# 3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# 4. The greatest increase in profits (date and amount) over the entire period


# 5. The greatest decrease in losses (date and amount) over the entire period
