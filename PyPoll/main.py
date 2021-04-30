import os
import csv

#Path to collect data from Resources folder
PyPoll_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Reading CSV file
with open(PyPoll_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # zip the csv data into tuples to better analyze
    election_data = list(zip(*csvreader))

    # define column data starting point 
    voter_id_column = election_data[0][1:]
    county_column = election_data[1][1:]
    candidate_column = election_data[2][1:]

    # counting the amout of rows in to determin the total votes in the election
    total_votes = len(voter_id_column)

    # find list of candidates in the election
    candidates = set(candidate_column)

    # define data variable for dictionary
    data = {}

    # for loop to find candidate data
    for candidate in candidates:
        votes = len([x for x in candidate_column if x == candidate])

        # percentage of vote calculation
        percentage_vote = 100 * votes / total_votes

        # dicitionary components
        data[votes] = (candidate, percentage_vote)

        # define results by creating a list
        results = list(data.keys())

        #sort the votes
        results.sort(reverse=True)


    # declair the victor
    winner_key = max(results)

    # declair winner name
    winner = data[winner_key][0]  
               
    # Print out Election Results
    print(f" ")
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    #
    for key in results:
            value = data[key]
            politician = value[0]
            percent_votes = value[1]
            number_votes = key

            print(f"{politician}: {percent_votes:.3f}% ({number_votes})")#print(f"{politician}: {percent_votes:.3f}% ({number_votes})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")

    # Export to Text File
    PyPoll_csv = os.path.join("PyPoll", "Resources", "Election_Results.txt")

    with open(PyPoll_csv, 'w') as txt:

        txt.write(f" \n")
        txt.write(f"Election Results\n")
        txt.write(f"----------------------------\n")
        txt.write(f"Total Votes: {total_votes}\n")
        txt.write(f"----------------------------\n")
        txt.write(f"{politician}: {percent_votes:.3f}% ({number_votes})\n")
        txt.write(f"----------------------------\n")
        txt.write(f"Winner: {winner}\n")
        txt.write(f"----------------------------\n")