#making imports
import classes_for_dataset as cfd
import matplotlib.pyplot as plt
import time

#creating funtion for the menu to import 
def ShaunQ2Program():
#getting inputs from user
    chosenLeague = input("Enter league: ")
    chosenSeason = input("Enter season (2014-2020): ")

#validation 
    leagueNotFound = True
    seasonNotFound = True

#getting the league ID of users chosen league
    leagues = cfd.read_file_to_array('datasets/leagues.csv', cfd.League, filter_func=lambda row: row['name'] == chosenLeague)
    leagueIDs = []
#appending chosen league ID into array
    for league in leagues:
        leagueIDs.append(league.leagueID)
        leagueNotFound = False
#taking all of the games from the chosen league and season
    games = cfd.read_file_to_array('datasets/games.csv', cfd.Game, filter_func=lambda row: row['season'] == chosenSeason and row['leagueID'] in leagueIDs)

#taking game ID's from all of the games 
    gameIDs = []
    for game in games:
        gameIDs.append(game.gameID)
        seasonNotFound = False

#Telling the user if there is an invalid input
    if leagueNotFound == True:
        print("League not found")
        time.sleep(3)
    elif seasonNotFound == True:
        print("Season not found")
        time.sleep(3)
    else:

    #putting goals from all of the games into array
        goals = cfd.read_file_to_array('datasets/shots.csv', cfd.Shot, filter_func=lambda row: row['shotResult'] == 'Goal' and row['gameID'] in gameIDs)
        
    #sorting types of goals into their groups
        headGoals = []
        leftGoals = []
        rightGoals = []
        for goal in goals:
            if goal.shotType == 'Head':
                headGoals.append(goal)
            elif goal.shotType == 'RightFoot':
                rightGoals.append(goal)
            elif goal.shotType == 'LeftFoot':
                leftGoals.append(goal)
    #using len() to see how many of each type of goal there is
        headGoalsLen = len(headGoals)
        leftGoalsLen = len(leftGoals)
        rightGoalsLen = len(rightGoals)

    #creating and plotting pie chart with title and labels 
        slices = [headGoalsLen, leftGoalsLen, rightGoalsLen]
        labels = ['Header', 'Left foot', 'Right foot']
        plt.pie(slices, labels=labels, autopct='%1.1f%%')
        plt.title('Types of goals scored over a season')

        plt.show()

