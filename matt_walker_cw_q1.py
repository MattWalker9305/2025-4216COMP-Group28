import pandas as pd
import csv 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from dataclasses import dataclass

@dataclass
class TeamStatistic:
    gameID: str
    teamID: str
    season: str
    date: dt.datetime
    location: str
    goals: int
    xGoals: float
    shots: int
    shotsOnTarget: int
    deep: int
    ppda: float
    fouls: int
    corners: int
    yellowCards: int
    redCards: int
    result: str

def team_season_points():
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
            reader = csv.DictReader(f)
            ts = [TeamStatistic(**row) for row in reader]
            
            for row in ts:
                if row.teamID == team_id and selected_year == row.season:
                    match_results.append((row.date, row.result))
        
        print (ts[3])

        match_results.sort(key=lambda x: x[0])

        data = pd.DataFrame(match_results, columns=['date', 'result'])
        data['date'] = pd.to_datetime(data['date'])
        
        data['points'] = data['result'].map({'W': 3, 'D': 1, 'L': 0})
    
        data['cumulative_points'] = data['points'].cumsum()

        fig, ax = plt.subplots()
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m.%Y"))
        ax.set_xticks(data['date'])
        ax.plot(data['date'], data['cumulative_points'], 'go:')
        ax.tick_params(axis='x', labelrotation=90)

        ax.set_xlabel('Date')
        ax.set_ylabel('Points')

        print(data)
        plt.show()