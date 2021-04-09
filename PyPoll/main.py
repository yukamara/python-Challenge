# Import modules
import os
import csv

# set the path for collecting the ellection data
election_csv = os.path.join('Resources', 'election_data.csv')

# access and read the election data file
with open(election_csv, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')


# TASKS
# 1. The total number of votes cast
    for row in csv_reader:
        total_votes_cast = sum(1 for row in csv_reader)
        print(total_votes_cast)


# 2. A complete list of candidates who received votes
    complete_list = []
    for row in csv_reader:
        if row[2] not in complete_list:
            complete_list.append(row[2])

    print(complete_list)
    names =[]
    for i in csv_reader:
        names.append(i['Candidate'])
    print(list(set(names)))

# 3. The percentage of votes each candidate won



# 4. The total number of votes each candidate won


# 5. The winner of the election based on popular vote.

