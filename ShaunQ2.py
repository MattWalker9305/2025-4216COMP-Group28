import pandas as pd
import csv
import classes_for_dataset as cfd
from matplotlib import pyplot as plt


def ShaunQ2Program():
    chosenLeague = input("Enter league: ")
    chosenSeason = int(input("Enter season: "))

    leagues = cfd.read_file_to_array('datasets/leagues.csv', cfd.League, filter_func=lambda row: row['name'] == chosenLeague)
    leagueIDs = []
    for league in leagues: leagueIDs.append(league.leagueID)
    games = cfd.read_file_to_array('datasets/games.csv', cfd.Game, filter_func=lambda row: int(row['season']) == chosenSeason and row['leagueID'] in leagueIDs)

    gameIDs = []
    for game in games: gameIDs.append(game.gameID)
    goals = cfd.read_file_to_array('datasets/shots.csv', cfd.Shot, filter_func=lambda row: row['shotResult'] == 'Goal' and row['gameID'] in gameIDs)
    goalslen = len(goals)

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
    headGoalsLen = len(headGoals)
    leftGoalsLen = len(leftGoals)
    rightGoalsLen = len(rightGoals)

    slices = [headGoalsLen, leftGoalsLen, rightGoalsLen]
    plt.pie(slices)
    plt.show()

ShaunQ2Program()