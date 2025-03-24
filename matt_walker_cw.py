import pandas as pd
import csv 
import matplotlib as plt
import numpy as np

team_not_found = True

selected_team = input("Enter team: ")
selected_year = input("Enter year: ")

with open('datasets/teams.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        team = row[1]
        team_id = row[0]
        if team == selected_team:
            team_id = row[0]
            team_not_found = False
            break

if team_not_found:
    print("no team found")
else:
    match_results = []
 
    with open('datasets/teamstats.csv', 'r') as f:
        teamstats = csv.reader(f)
        next(teamstats)
        
        for row in teamstats:
            match_team_id = row[1]
            result = row[15]
            season = row[2]
            date = row[3]
            if match_team_id == team_id and selected_year == season:
                match_results.append((date, result))
    
    match_results.sort(key=lambda x: x[0])

    data = pd.DataFrame(match_results, columns=['date', 'result'])
    data['date'] = data['date'].apply(lambda x: x.split(' ')[0]) 
    data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d')
    
    data['points'] = data['result'].map({'W': 3, 'D': 1, 'L': 0})
   
    data['cumulative_points'] = data['points'].cumsum()
   
    print(data)