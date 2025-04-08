import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def ShaunQ1Program():
    chosenPlayer = input("Players full name: ")
    chosenSeason = input("Season: ")

    import csv
    with open('datasets/players.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            if chosenPlayer == row[1]:
                playerID = row[0]
                break
        
    gameIDs = []
    with open('datasets/games.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            if chosenSeason == row[2]:
                gameIDs.append(row[0])

    goals = []
    with open('datasets/appearances.csv', 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for row in csv_reader:
            if playerID == row[1] and row[0] in gameIDs:
                goals.append(int(row[2]))

    cumulativeGoals = np.cumsum(goals)

    x_values = list(range(1, len(goals) + 1))
    y_values = cumulativeGoals

    plt.plot(x_values, y_values)
    plt.title(chosenPlayer + "'s" + " goals over the " + chosenSeason + " season")
    plt.xlabel("Number of games")
    plt.ylabel("Number of goals")
    plt.show()