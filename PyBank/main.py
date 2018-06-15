import os
import csv
from statistics import mean 

csvpath = os.path.join("raw_data", "budget_data_1.csv")
csvfile = open(csvpath, newline='')
csvreader = csv.reader(csvfile, delimiter=',')
next(csvreader, None)
csvlist = list(csvreader)
print(csvlist)

dates = []
revenues = []

for x in csvlist:
    dates.append(x[0])
    revenues.append(int(x[1]))

monthly_change = []

monthly_change = [revenues[i+1] - revenues[i] for i in range(len(revenues)-1)]

rev_total = sum(revenues)
print(rev_total)
max_change = max(monthly_change)
print(max_change)
min_change = min(monthly_change)
print(min_change)
avg_change = round(mean(monthly_change))
print(avg_change)
total_months = len(csvlist)
print(total_months)

max_month = None
min_month = None

initial_val = None
for row in csvlist:
    if initial_val is None:
        initial_val = int(row[1])
        continue
    if int(row[1]) - initial_val == min_change:
        min_month = row[0]  
    initial_val = int(row[1])

    initial_val2 = None
    for row in csvlist:
        if initial_val2 is None:
            initial_val2 = int(row[1])
            continue
        if abs(int(row[1]) - initial_val2) == max_change:
            max_month = row[0]
        initial_val2 = int(row[1])
       
print("Financial Analysis Budget 1")
print("-----------------------------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total Revenue: ${rev_total}")
print(f"Average Revenue Change: ${avg_change}")
print(f"Maximum Revenue Gain: ${max_change} in {max_month}")
print(f"Largest Revenue Loss: ${min_change} in {min_month}")

txt_file = open("Financial_Analysis_Budget_1.txt", "w")
txt_file.write("Financial Analysis Budget 1 \n")
txt_file.write("-----------------------------------------------------------------------------\n")
txt_file.write(f"Total Months: {total_months}\n")
txt_file.write(f"Total Revenue: ${rev_total}\n")
txt_file.write(f"Average Revenue Change: ${avg_change}\n")
txt_file.write(f"Maximum Revenue Gain: ${max_change} in {max_month}\n")
txt_file.write(f"Largest Revenue Loss: ${min_change} in {min_month}\n")
txt_file.close()