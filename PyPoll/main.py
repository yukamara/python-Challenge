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
 #   Candisates_list = len()
 #   for i in range(len(candidate_list)):
 #       vote_count["votes" + str(candidates_list[i])] = []
 #       for j in range(len(candidates)):
 #           vote_count["votes" + str(candidates_list[i])].append(votes[j])
 
    print("Candidate List")
    print("--------------------------------")
    for row in election_csv:
        print(row[2])

    vote_count = 0
    for row in election_csv:
        vote_count += 1
    print(f'The total number of votes is {vote_count}')  
        
# 2. A complete list of candidates who received votes
    for row in election_csv:
        complete_list = (row[-1])
        print(complete_list)
        print(len(complete_list))
    
    candidates_names = []
    for row in election_csv:
        candidates_names.append(row[-1])
    print(candidates_names)
    print(len(candidates_names))

    names =[]
    for i in election_csv:
        names.append(i['Candidate'])
    print(list(set(names)))
    print(len(names))

# 3. The percentage of votes each candidate won



# 4. The total number of votes each candidate won
    vote_dict = {}
    for name in (row[-1]):
        if name in vote_dict:
            vote_dict[name] += 1
        else:
            vote_dict[name] = 1

    print(vote_dict)

# 5. The winner of the election based on popular vote.

