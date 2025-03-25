import csv
import pandas as pd

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
        homeGoals = []
        awayGoals = []

        with open("2025-4216COMP-Group28/datasets/games.csv", "r") as f:
            games = csv.reader(f)
            next(games)

            for row in games:
                home_team_id = row[4]
                away_team_id = row[5]
                home_goals = int(row[6])
                away_goals = int(row[7])
                season = row[2]
                if home_team_id == team_id and requested_year == season:
                    homeGoals.append(home_goals)
                elif away_team_id==team_id and requested_year==season:
                    awayGoals.append(away_goals)

    

print(pd.Series(homeGoals).cumsum())
print(pd.Series(awayGoals).cumsum())

                    
                    

                











  
   