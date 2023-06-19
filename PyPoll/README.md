#### PyPoll Script Description

os module is useful in interacting with the operating system.
csv module is used to read from, and write into CSV files.

A name ‘csvreader’ is given to the file including the path.
The file is then opened using ‘UTF-8’ encoding.

Header-row is skipped, and only data is included for calculations.

    import os
    import csv
    csvpath = os.path.join("..", "Resources", "election_data.csv")

    with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skip the header row
        header = next(csvreader)
-------------------------------------------------------------------

Number of rows are counted to obtain the number of votes cast.

    num_votes = 0

    for row in csvreader:
        num_votes += 1
    print(f'\nTotal Votes: {num_votes}\n')

-------------------------------------------------------------------

From the 3rd column, the name on each ballot is read and a set is created with only the unique names in the column.  The set is converted into a list: ‘candidate_list’.
    
    # Iterate over each row in the CSV
    names = [row[2] for row in csvreader]
    candidate_name = sorted(set(names))
    candidate_list = list(candidate_name)

-------------------------------------------------------------------

An empty dictionary: ‘results’, is created, in which ‘key’ would be the name of each candidate and the corresponding ‘value’ would be the number of votes each candidate received.
The number of votes is counted by the number of times each candidate’s name appears in the 3rd column.
For each name in the column, if the name appears as ‘key’ in ‘results’, then the ‘value’ is incremented by 1.
If the name is not in ‘results’, the name is added as ‘key’, along with the ‘value’ as 1.

The dictionary is then sorted by ‘value’ in descending order so as to obtain the maximum number of votes and the corresponding name of the candidate as the winner.
‘results’ is printed and a winner declared.

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

    print(f'\nWinner: {winner}\n')
    
-------------------------------------------------------------------

The output in the required format is written to an output text file.

    output_path = os.path.join("..", "Analysis", "output.txt")
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


### Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

* The total number of votes cast

* A complete list of candidates who received votes

* The percentage of votes each candidate won

* The total number of votes each candidate won

* The winner of the election based on popular vote

Your analysis should align with the following results:

#### Election Results

#### -------------------------

#### Total Votes: 369711

#### -------------------------
#### Charles Casper Stockham: 23.049% (85213)

#### Diana DeGette: 73.812% (272892)

#### Raymon Anthony Doane: 3.139% (11606)

#### -------------------------
#### Winner: Diana DeGette
#### -------------------------