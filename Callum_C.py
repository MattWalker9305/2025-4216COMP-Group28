import csv
import pandas as pd
import matplotlib.pyplot as plt
def callum_C1():
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
                    elif away_team_id == team_id and requested_year==season:
                        awayGoals.append(away_goals)

            total_home_goals = sum(homeGoals)
            total_away_goals = sum(awayGoals)

        
            #bar chart
            labels = ['Goals Scored At Home', 'Goals Scored Away']
            values = [total_home_goals, total_away_goals]
            
            plt.figure(figsize=(10, 5))
            plt.subplot(1, 2, 1)
            plt.bar(labels, values, color=['blue', 'red'])
            

            for i, v in enumerate(values):
                plt.text(i, v + 0.1, str(v), ha = "center", fontsize = 12, fontweight = "bold")
                
            plt.xlabel('Where The Goal Was Scored')
            plt.ylabel('Number of Goals')
            plt.title(f'Total Home vs Away Goals for {requested_team} in {requested_year}')


            #pie chart
            plt.subplot(1, 2, 2)
            plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['blue', 'red'], startangle=90)
            plt.title(f'Percentage of Home vs Away Goals')

            plt.show()

        

            print(pd.Series(homeGoals).cumsum())
            print(pd.Series(awayGoals).cumsum())

                    
                    

                











  
   