#

import pandas as pd
import csv

def binarySearch(sequnce, item):
    start = 0
    end = len(sequence) - 1
    




def ShaunQ2Program():
    chosenLeague = input("Enter league: ")
    chosenSeason = input("Enter season: ")
    



    import csv
    with open('datasets/leagues.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            if chosenLeague == row[1]:
                leagueID = row[0]
    print(leagueID)