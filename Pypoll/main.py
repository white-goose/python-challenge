
import os
import csv

csvpath = os.path.join('election_data2.csv')

poll = {}

total_votes = 0

with open(csvpath, 'r', newline = '') as csvfile:
    csvread = csv.reader(csvfile, delimiter = ',')

    next(csvread, None)

    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
print(total_votes) 

candidates = []
num_votes = []

for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

clean_data = list(zip(candidates, num_votes, vote_percent))

winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

output = os.path.join('election_results.txt')

with open(output, 'w') as writefile:
    writefile.writelines('Election Results \n------------------------- \nTotal Votes: '+ str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        writefile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    writefile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

with open(output, 'r') as readfile:
    print(readfile.read())