#How a player was most likely to shoot

#Imports libraries

import pandas as pd
import matplotlib.pyplot as plt
import classes_for_dataset as cfd

def Joe_Q2():

#Sets up initasl user input

    Player = (input('Enter player name: '))
    Player = Player.title()

#Sets up variable for data collection and sorting
    
    playersID = []
    shootersID = []
    typeShot = []

#Load player table to read data and append variables
    
    players = cfd.read_file_to_array('dataset/players.csv', cfd.Player)
    for player in players:
        if player.name == Player:
            playersID.append(player.playerID)

#Load shots table to read data and append variables

    shots = cfd.read_file_to_array('dataset/shots.csv', cfd.Shot)
    for shot in shots:
        if shot.shooterID in playersID:
            typeShot.append(shot.shotType)

#Counts total for each type of shot
            
    leftShot = typeShot.count('LeftFoot')
    rightShot = typeShot.count('RightFoot')
    headShot = typeShot.count('Head')
    totalShots = leftShot + rightShot + headShot

#Creates variables for chart and plots chart

    x = ([leftShot, rightShot, headShot])
    sliceNames = [leftShot, rightShot, headShot]
    sliceColours = ['#22577a', '#38a3a5', '#57cc99']
    shotNames = ['Left Foot', 'Right Foot', 'Head Shot']

    plt.title('Types of shot for ' + Player)
    plt.pie(x, labels = sliceNames, colors = sliceColours)
    plt.legend(title = "Shot Type", labels = shotNames, loc = 'upper left')
    plt.show()

#Requests user to continue or exit

    while True:
        
        Choice = (input('Choose another player? Y/N\n'))

        if Choice.lower() == 'y':
              Joe_Q2()
        elif Choice.lower() == 'n':
            print ('Returning to menu')
            exit()
        else :
            print ('Invalid Input Please Try Again')