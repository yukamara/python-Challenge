# Import modules
import os
import csv

# set the path for collecting the ellection data
csv_path = os.path.join('Resources', 'election_data.csv')

# access and read the election data file
with open(csv_path, newline='') as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',')

# TASKS
# 1. The total number of votes cast
    vote_count = 0     # Initializing vote count                                                                                                                                                                                                                                   
    for row in election_csv:    # Looping through the rows to count the votes
        vote_count += 1
    print(f'The total number of votes is {vote_count}') #The result or the total votes count

# 2. A complete list of candidates who received votes
with open(csv_path, newline='') as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',')
    
    list_of_candidates = []
    for row in election_csv:
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])
    print(f'The candidates who received votes are {list_of_candidates}')

# 3. The percentage of votes each candidate won
with open(csv_path, newline='') as csvfile:
    election_csv = csv.reader(csvfile, delimiter=',') 
       


# 4. The total number of votes each candidate won
    vote_dict = {}
    for name in (row[2]):
        if name in vote_dict.keys():
            vote_dict[name] += 1
        else:
            vote_dict[name] = 1
    print(vote_dict)

# 5. The winner of the election based on popular vote.

