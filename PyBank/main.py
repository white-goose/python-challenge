import os
import csv

# create file path and save as file
csvpath = os.path.join('budget_data.csv')

#emply lists for month and revenue data
months = []
profit = []

#read csv and parse data into lists
#revenue list will be list of integers
with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1])) 

#find total months
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set total revenue = 0 
greatest_increase = profit[0]
greatest_decrease = profit[0]
total_revenue = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
changes = []
previous_profit = 0
for i in range(len(profit)):
    if profit[i] >= greatest_increase:
        greatest_increase = profit[i]
        greatest_increase_month = months[i]
    elif profit[i] <= greatest_decrease:
        greatest_decrease = profit[i]
        greatest_decrease_month = months[i]
    total_revenue += profit[i]

    if previous_profit:
        changes.append(profit[i] - previous_profit)
        previous_profit = profit[i]
    else:
        previous_profit = profit[i]  
#print(max(changes))
#calculate average_change
average_change = round(sum(changes) / len(changes), 2)

#sets path for output file
output = os.path.join('pybank_output', 'pybank.txt')

# opens the output destination in write mode and prints the summary
with open(output, 'w') as writefile: 
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------\n')
    writefile.writelines(f'Total Months: {total_months}\n')
    writefile.writelines(f'Total: $ {total_revenue}\n')
    writefile.writelines(f'Average Change: ${average_change}\n')
    writefile.writelines(f'Greatest Increase in Profit: {greatest_increase_month} (${max(changes)})\n')
    writefile.writelines(f'Greatest Decrease in Profit: {greatest_decrease_month} (${min(changes)})\n')

#opens the output file in r mode and prints to terminal
with open(output, 'r') as readfile:
    print(readfile.read())