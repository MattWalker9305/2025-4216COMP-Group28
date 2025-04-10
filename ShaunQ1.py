import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import classes_for_dataset as cfd

def ShaunQ1Program():
    chosenPlayer = input("Players full name: ")
    chosenSeason = input("Season: ")

    import csv
    players = cfd.read_file_to_array('datasets/players.csv',cfd.Player)
    for player in players:
        if chosenPlayer == player.name:
            playerID = player.playerID
            break
        
    gameIDs = []
    games = cfd.read_file_to_array('datasets/games.csv', cfd.Game)
    for game in games:
        if chosenSeason == game.season:
            gameIDs.append(game.gameID)

    goals = []
    appearances = cfd.read_file_to_array('datasets/appearances.csv', cfd.Appearance)
    for appearance in appearances:
        if playerID == appearance.playerID and appearance.gameID in gameIDs:
            goals.append(int(appearance.goals))

    cumulativeGoals = np.cumsum(goals)

    x_values = list(range(1, len(goals) + 1))
    y_values = cumulativeGoals

    plt.plot(x_values, y_values)
    plt.title(chosenPlayer + "'s" + " goals over the " + chosenSeason + " season")
    plt.xlabel("Number of games")
    plt.ylabel("Number of goals")
    plt.show()