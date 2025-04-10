#making imports
import matplotlib.pyplot as plt
import numpy as np
import classes_for_dataset as cfd

#creating funtion for the menu to import 
def ShaunQ1Program():
#getting input from user
    chosenPlayer = input("Players full name: ")
    chosenSeason = input("Season: ")

#getting the player ID of the chosen player
    players = cfd.read_file_to_array('datasets/players.csv',cfd.Player)
    for player in players:
        if chosenPlayer == player.name:
            playerID = player.playerID
            break

#getting game ID's from users chosen season   
    gameIDs = []
    games = cfd.read_file_to_array('datasets/games.csv', cfd.Game)
    for game in games:
        if chosenSeason == game.season:
            gameIDs.append(game.gameID)

#storing players goals from each of their games into an array 
    goals = []
    appearances = cfd.read_file_to_array('datasets/appearances.csv', cfd.Appearance)
    for appearance in appearances:
        if playerID == appearance.playerID and appearance.gameID in gameIDs:
            goals.append(int(appearance.goals))

#creating an array that adds the players goals along the season
    cumulativeGoals = np.cumsum(goals)

#variables to use as the axis for the line chart
    x_values = list(range(1, len(goals) + 1))
    y_values = cumulativeGoals

#plotting the visualisation with title and labels
    plt.plot(x_values, y_values)
    plt.title(chosenPlayer + "'s goals over the " + chosenSeason + " season")
    plt.xlabel("Number of games")
    plt.ylabel("Number of goals")
    plt.show()

    