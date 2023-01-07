import os
import csv

budget_csv = os.path.join("Resources/budget_data.csv")


total = 0
with open(budget_csv) as csvfile:
    csvreader= csv.DictReader(csvfile)
    
    for i in csvreader:
        total = total +1
print(total)


