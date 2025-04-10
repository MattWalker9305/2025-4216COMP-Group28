#Imports
import csv
import pandas as pd
import matplotlib.pyplot as plt
import classes_for_dataset as cfd

#defined function
def callum_C1():
    team_not_found = True

#request user inputs
    requested_team = input("Enter team:")
    requested_year = input("Enter year:")

#creating an array of all the teams
    teams = cfd.read_file_to_array('2025-4216COMP-Group28/datasets/teams.csv', cfd.Team)

    #searching throught the array to find teamIDs
    for row in teams:
        if row.name == requested_team:
            team_id = row.teamID
            team_not_found = False
            break

#response if no team matched
    if team_not_found:
            print("no team found")
    else:
            homeGoals = []
            awayGoals = [] #empty lists created

            games = cfd.read_file_to_array('2025-4216COMP-Group28\datasets\games.csv', cfd.Game)
                
#checks if teamId and year match the away or home team
            for row in games:
                   
                    if row.homeTeamID == team_id and requested_year == row.season:
                        homeGoals.append(row.homeGoals)
                    elif row.awayTeamID == team_id and requested_year == row.season:
                        awayGoals.append(row.awayGoals)
            

            total_home_goals = sum(list(map(int, homeGoals)))
            total_away_goals = sum(list(map(int, awayGoals)))

        
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

            plt.tight_layout()
            plt.show()

        
    
            print(pd.Series(homeGoals).cumsum())
            print(pd.Series(awayGoals).cumsum())

                    
                    

                











  
   