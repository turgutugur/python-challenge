import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    Otooley = 0

    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    total_votes = []  

    for row in csvreader:
        votes+=1
        if candidates[0]==row[2]:
            Khan+=1
        if candidates[1]==row[2]:
            Correy+=1
        if candidates[2]==row[2]:
            Li+=1
        if candidates[3]==row[2]:
            Otooley+=1

    total_votes.append(Khan)
    total_votes.append(Correy)
    total_votes.append(Li)
    total_votes.append(Otooley)
    winner = candidates[total_votes.index(max(total_votes))]

print("Election Results")
print("-------------------------")
print("Total Votes: ", votes)
print("-------------------------")
print(f'{candidates[0]}: {"%.3f%%" % (Khan/votes*100)} ({Khan})')
print(f'{candidates[1]}: {"%.3f%%" % (Correy/votes*100)} ({Correy})')
print(f'{candidates[2]}: {"%.3f%%" % (Li/votes*100)} ({Li})')
print(f'{candidates[3]}: {"%.3f%%" % (Otooley/votes*100)} ({Otooley})')
print("------------------------")
print("Winner:", winner)
print("------------------------")
