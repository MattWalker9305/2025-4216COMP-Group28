import pandas as pd
import csv 
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
from dataclasses import dataclass
import classes_for_dataset as cfd

def team_season_points():
    team_not_found = True

    selected_team = input("Enter team: ")
    selected_year = input("Enter year: ")

    teams = cfd.read_file_to_array("datasets/teams.csv", cfd.Team)
    for row in teams:
           if row.name == selected_team:
               selected_team = row.teamID
               team_not_found = False
               break

    if team_not_found:
        print("no team found")
    else:
        print(selected_team)
        match_results = []

        ts = cfd.read_file_to_array("datasets/teamstats.csv", cfd.TeamStatistic)
        for row in ts:
            if row.teamID == selected_team and selected_year == row.season:
                match_results.append((row.date, row.result))
        
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