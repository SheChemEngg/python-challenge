
import os
import csv

# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

print('\nElection Results\n')
print('-'*20)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    num_votes = 0

    for row in csvreader:
        num_votes += 1
    print(f'\nTotal Votes: {num_votes}\n')
    print('-'*20)

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Iterate over each row in the CSV
    names = [row[2] for row in csvreader]
    candidate_name = sorted(set(names))
    candidate_list = list(candidate_name)

    # Dictionary = results, key = candidate name, value = number of votes
    results = {}

    for name in names:
        if name in results.keys():
            results[name] += 1
        else:
            results[name] = 1

    for candidate, votes in results.items():
        votes_percent = round((votes / num_votes) * 100, 3)
        print(f'\n{candidate}: {votes_percent}% ({votes})\n')

    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    winner = sorted_results[0][0]
    max_votes = sorted_results[0][1]

    print('-' * 20)
    print(f'\nWinner: {winner}\n')
    print('-' * 20)

#--------------------------------------------------------------------

# https://www.pythontutorial.net/python-basics/python-write-text-file/
# Specify the file to write to
output_path = os.path.join("..", "Analysis", "output.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write('\nElection Results\n\n\n')
    txtfile.write('-' * 20)
    txtfile.write(f'\n\n\nTotal Votes: {num_votes}\n\n\n')
    txtfile.write('-' * 20)
    txtfile.write('\n')

    for candidate, votes in results.items():
        votes_percent = round((votes / num_votes) * 100, 3)
        txtfile.write(f'\n\n{candidate}: {votes_percent}% ({votes})\n')

    txtfile.write('\n\n')
    txtfile.write('-' * 20)
    txtfile.write(f'\n\n\nWinner: {winner}\n\n\n')
    txtfile.write('-' * 20)
