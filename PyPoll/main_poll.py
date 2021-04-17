# Import modules
import os
import csv

# define function to analyze election data
def main():

    #  set the path for collecting the election data
    csv_read = os.path.join('Resources', 'election_data.csv') 
    csv_write = os.path.join('Analysis', 'Election_Analysis.txt')
    
    # initialize variables
    total_votes = 0
    winner = None
    # dictionary for candidates and count of votes
    candidate_votes = {}

    # read csv
    with open(csv_read, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        # skip header
        csv_header = next(f, None)
        # loop through data
        for row in reader:
            total_votes += 1
            candidate = row[2]
            if candidate not in candidate_votes.keys():
                candidate_votes[candidate] = 1
            else:
                candidate_votes[candidate] += 1
    # create output file
    output = (
        f"Election Results\n"
        f"----------------------\n"
        f"Total Votes\n"
        f"----------------------\n"
    )
    
    max_votes = float('-inf')   # this sets a lower bound for votes cast
    for candidate, votes in candidate_votes.items():
        votes_percent = votes / total_votes * 100
        output = output + f'{candidate}: {votes_percent:.3f}% ({votes})\n'

        if votes > max_votes:
            winner = candidate

        max_votes = votes

    output = output +  (f'----------------------\n'
                        f'Winner: {winner}\n'
                        f'----------------------\n'
    )

    print(output)

    with open(csv_write, 'w') as f:
        f.write(output)

if __name__ == '__main__':
    main()