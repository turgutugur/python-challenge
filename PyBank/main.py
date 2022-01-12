import os
import csv

csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

date = []
profit_losses = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)

    for row in csvreader:
        date.append(row[0])
        profit_losses.append(int(row[1]))
    for i in range(len(profit_losses)-1):
        change.append(profit_losses[i+1]-profit_losses[i])


increase = max(change)
decrease = min(change)

greatest_increase = profit_losses.index(max(profit_losses))
greatest_decrease = profit_losses.index(min(profit_losses))

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(profit_losses)}")
print(f"Avarage Change: ${round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {date[greatest_increase]} (${str(increase)})")
print(f"Greatest Decrease in Profits: {date[greatest_decrease]} (${str(decrease)})")
