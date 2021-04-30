import os
import csv

#Path to collect data from Resources folder
PyPoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# List of Variables
votes = []
canditates = []
total_votes = 0
khan = []
khan_votes = 0
khan_percent = 0
correy = []
correy_votes = 0
correy_percent = 0
li = []
li_votes = 0
li_percent = 0
otooley = []
otooley_votes = 0
otooley_percent = 0


# Reading CSV file
with open(PyPoll_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Total votes
    for vote in csvreader:
        votes.append(vote[0])
        canditates.append(vote[2])
        total_votes = len(votes)

    # Total votes per candidate
    for candidate in canditates:
        if candidate == "Khan":
            khan.append(candidate)
            khan_votes = len(khan)
        
        elif candidate == "Correy":
            correy.append(candidate)
            correy_votes = len(correy)
        
        elif candidate == "Li":
            li.append(candidate)
            li_votes = len(li)

        else:
            otooley.append(candidate)
            otooley_votes = len(otooley)
    
    # Percentage of Vote
    khan_percent = round((khan_votes / total_votes)*100, 3)
    correy_percent = round((correy_votes / total_votes)*100, 3)
    li_percent = round((li_votes / total_votes)*100, 3)
    otooley_percent = round((otooley_votes / total_votes)*100, 3)

    # Determine highest vote count
    if khan_votes > max(correy_votes, li_votes, otooley_votes):
        election_winner = "Khan"
    elif correy_votes > max(khan_votes, li_votes, otooley_votes):
        election_winner = "Correy"
    elif li_votes > max(khan_votes, correy_votes, otooley_votes):
        election_winner = "Li"
    else:
        election_winner = "O'Tooley"
    
               
    # Print out Election Results
    print(f" ")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    print(f"Khan: {khan_percent:.3f}% {khan_votes}")
    print(f"Correy: {correy_percent:.3f}% {correy_votes}")
    print(f"Li: {li_percent:.3f}% {li_votes}")
    print(f"O'Tooley: {otooley_percent:.3f}% {otooley_votes}")
    print(f"-------------------------")
    print(f"Winner: {election_winner}")
    print(f"-------------------------")

    # Export to Text File
    PyPoll_csv = os.path.join("PyPoll", "Resources", "Election_Results.txt")

    with open(PyPoll_csv, 'w') as txt:

        txt.write(f" \n")
        txt.write(f"Election Results\n")
        txt.write(f"----------------------------\n")
        txt.write(f"Total Votes: {total_votes}\n")
        txt.write(f"----------------------------\n")
        txt.write(f"Khan: {khan_percent:.3f}% {khan_votes}\n")
        txt.write(f"Correy: {correy_percent:.3f}% {correy_votes}\n")
        txt.write(f"Li: {li_percent:.3f}% {li_votes}\n")
        txt.write(f"O'Tooley: {otooley_percent:.3f}% {otooley_votes}\n")
        txt.write(f"----------------------------\n")
        txt.write(f"Winner: {election_winner}\n")
        txt.write(f"----------------------------\n")