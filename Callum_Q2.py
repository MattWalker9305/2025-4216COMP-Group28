import csv
import pandas as pd
import matplotlib.pyplot as plt

team_not_found = True

requested_team = input("Enter team:")
requested_year = input("Enter year:")

with open("2025-4216COMP-Group28/datasets/teams.csv", "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        team = row[1]
        team_id = row[0]
        if team == requested_team:
            team_id = row[0]
            team_not_found = False
            break
    if team_not_found:
        print("no team found")
    else:
        dates = []
        shot_conversion_rate = []

        with open("2025-4216COMP-Group28/datasets/teamstats.csv", "r") as f:
            team_stats = csv.reader(f)
            next(team_stats)

            for row in team_stats:
                current_team_id = row[1]
                season = row[2]
                shots = int(row[7])
                goals = int(row[5])
                date = row[3]
            if current_team_id == team_id and requested_year == season:
                if shots > 0:
                        dates.append(date)
                        shot_conversion_rate.append((goals / shots) *100)