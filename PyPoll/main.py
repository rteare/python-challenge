import os
import csv

#Path to collect data from Resources folder
PyPol_csv = os.path.join("..", "Resources", "election_data.csv")

# List of variable
number_votes = 0
candidates = []
candidates_total_votes = []
winner_count = 0
winner = ""


# Reading CSV file
with open(PyPol_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    csv_firstRow = next(csvreader)

    # Read each row of data after the header
    for votes in csvreader:
        # Number of months
        number_votes = number_votes + 1
        
        # List of candidates
        candidates_name = votes[2]

            
# Print out Financial Analysis
print(f" ")
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {number_votes}")
print(f"-------------------------")
#print(f" {candidate_1}: {percentage} {total_votes}")
#print(f" {candidate_2}: {percentage} {total_votes}")
#print(f" {candidate_3}: {percentage} {total_votes}")
#print(f" {candidate_4}: {percentage} {total_votes}")
print(f"-------------------------")
#print(f"Winner: {candidate_1}")
print(f"-------------------------")

# Export to Text File
PyPoll_csv = os.path.join("..", "Resources", "Financial_Analysis.txt")

with open(PyPoll_csv, 'w') as txt:

    txt.writelines(f" \n")
    txt.writelines(f"Financial Analysis\n")
    txt.writelines(f"----------------------------\n")
    txt.writelines(f"Total Months: {number_months}\n")
    txt.writelines(f"Total: ${net_profit_total}\n")
    txt.writelines(f"Average Change: ${average_profit_change}\n")
    txt.writelines(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt.writelines(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")