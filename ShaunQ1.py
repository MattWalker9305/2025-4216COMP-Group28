import pandas as pd 

import csv
with open('datasets\players.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
    print(header_row)