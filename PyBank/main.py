import os
import csv

#Path to collect data from Resources folder
PyBank_csv = os.path.join("..", "Resources", "budget_data.csv")

# List of variable
number_months = 0
net_profit_total = 0
previous_net_profit = 0
profit_change = 0
net_profit_change = []
average_profit_change = 0
max_profit_change = 0
min_profit_change = 0
max_profit_date = 0
min_profit_date = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]

# Reading CSV file
with open(PyBank_csv) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    csv_firstRow = next(csvreader)
    number_months += 1
    net_profit_total += int(csv_firstRow[1])
    previous_net_profit = int(csv_firstRow[1])

    # Read each row of data after the header
    for month in csvreader:
        # Number of months
        number_months = number_months + 1
        
        # Total Profit/Loss
        net_profit_total = net_profit_total +int(month[1])
        
        # Changes of Profits
        profit_change = int(month[1]) - previous_net_profit
        previous_net_profit = int(month[1])
        net_profit_change += [profit_change]

        # Average change of Profit by month
        average_profit_change = round(sum(net_profit_change)/len(net_profit_change), 2)

        # Loop through looking for greatest profit increse
        if profit_change > greatest_increase[1]:
            greatest_increase[0] = month[0]
            greatest_increase[1] = profit_change
        
        # Loop through looking for greatest profit decrease
        if profit_change < greatest_decrease[1]:
            greatest_decrease[0] = month[0]
            greatest_decrease[1] = profit_change
            
# Print out Financial Analysis
print(f" ")
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {number_months}")
print(f"Total: ${net_profit_total}")
print(f"Average Change: ${average_profit_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export to Text File
PyBank_csv = os.path.join("..", "Resources", "Financial_Analysis.txt")

with open(PyBank_csv, 'w') as txt:

    txt.writelines(f" \n")
    txt.writelines(f"Financial Analysis\n")
    txt.writelines(f"----------------------------\n")
    txt.writelines(f"Total Months: {number_months}\n")
    txt.writelines(f"Total: ${net_profit_total}\n")
    txt.writelines(f"Average Change: ${average_profit_change}\n")
    txt.writelines(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt.writelines(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")