import os
import csv

csvpath = os.path.join('budget_data.csv')

months = []
profit = []

with open(csvpath, 'r', newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    next(csvreader, None)

    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1])) 

total_months = len(months)

greatest_increase = profit[0]
greatest_decrease = profit[0]
total_revenue = 0
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

average_change = round(sum(changes) / len(changes), 2)

output = os.path.join('pybank_output', 'pybank.txt')

with open(output, 'w') as writefile: 
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------\n')
    writefile.writelines(f'Total Months: {total_months}\n')
    writefile.writelines(f'Total: $ {total_revenue}\n')
    writefile.writelines(f'Average Change: ${average_change}\n')
    writefile.writelines(f'Greatest Increase in Profit: {greatest_increase_month} (${max(changes)})\n')
    writefile.writelines(f'Greatest Decrease in Profit: {greatest_decrease_month} (${min(changes)})\n')

with open(output, 'r') as readfile:
    print(readfile.read())