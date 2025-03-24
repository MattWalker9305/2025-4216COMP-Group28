import pandas as pd
import csv 
with open('datasets\teamstats.csv', 'r') as f:
    csv_reader = csv.reader(f)
    #header_row = next(csv_reader)
    #print(header_row)
    next(csv_reader)
    C = []
    for row in csv_reader:
        team = row[2]
        result = row[16]
        date = row[4]
        if "89" == team and result == "W" :
            C.append(date)
    print(C)
