#leagues ranked by situation of goal per season

#Import necessary libraries

import pandas as pd
import matplotlib.pyplot as plt
import classes_for_dataset as cfd

def Joe_Q1():

#Create inital menu for first user input
    
    goalSituation = input("Choose Goal Situation : \n1.Corner\n2.Open Play\n3.Direct Freekick\n4.Set Piece\n5.Penalty\n")

    if goalSituation == ('1'):
        goalSituation = 'FromCorner'
    if goalSituation == ('2'):
        goalSituation = ('OpenPlay')
    if goalSituation == ('3'):
        goalSituation = ('DirectFreekick')
    if goalSituation == ('4'):
        goalSituation = ('SetPiece')
    if goalSituation == ('5'):
        goalSituation = ('Penalty')

#Create second user input
        
    seasonEntered = input("Choose a season from 2015 to 2019 :\n")

#Setup inital variable for data collection and sorting

    gamesID = []
    gamesNeededID = []
    leaguesID = []
    
#Loads shot table to read data and append variables
    
    shots = cfd.read_file_to_array('dataset/shots.csv', cfd.Shot)
    for shot in shots:
                if goalSituation == shot.situation and shot.shotResult == 'Goal':
                    gamesID.append(shot.gameID)

#Loads game table to read data and append variables
                    
    games = cfd.read_file_to_array('dataset/games.csv', cfd.Game)
    for game in games:
                if game.gameID in gamesID and seasonEntered == game.season:
                    leaguesID.append(game.leagueID)
    
    leagues = cfd.read_file_to_array('dataset/leagues.csv', cfd.League)

#Counts total goals

    premTotal = leaguesID.count('1')
    serieaTotal = leaguesID.count('2')
    bundesligaTotal = leaguesID.count('3')
    laligaTotal = leaguesID.count('4')
    ligueTotal = leaguesID.count('5')

#Creates variables for chart and plots chart

    fig, axs = plt.subplots()
    
    names = ['Premier League', 'Serie A', 'Bundesliga', 'La Liga', 'Ligue 1']
    values = [premTotal, serieaTotal, bundesligaTotal, laligaTotal, ligueTotal]

    plt.bar(names, values, color = 'green')
    plt.title("Leagues Ranked by Situation of Shot per Season")
    plt.show()

#Requests user to continue or exit
    
    while True:
        
        restartChoice = input("Look at another stat? Y/N\n")
    
        if restartChoice.lower() == ('y'):
            Joe_Q1()
        elif restartChoice.lower() == ('n'):
            exit()
        else:
            print ('Invalid Input Please Try Again')

#Run programme

Joe_Q1()

    

    

    
    

    

    

    
    
    

    

    
    
    
