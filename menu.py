import matt_walker_cw as mw
import Callum_C
import ShaunQ1
import Callum_Q2
import ShaunQ2
import MariaQ1
import MariaQ2
import JoeQ1
import JoeQ2
import os

menu_choice = True
while menu_choice:

    #Clear the terminal, enhance the readability 
    os.system('cls')

    #Accept user input
    choice = input("Enter a number to choose one of the below applictaions"
                       "\n1.) team points over a season"
                       "\n2.) team home and away goals scored in a season"
                       "\n3.) Player goals over a season"
                       "\n4.) Shot conversion rate for teams in a season"
                       "\n5.) Player xG vs G"
                       "\n6.) Each type of goal scored in a league over a season"
                       "\n7.) Shot results by situation"
                       "\n8.) Team discipline(Yellow and Red Cards)"
                       "\n9.) Leagues Ranked by Goal Situation)"
                       "\n10.) Types of Shot per Player)"
                       "\n0.) exit"
                       "\nchoose application: ")
    #Match user input to menu number, repeat menu if none found.
    match choice:
        case "0":
            #Quit menu when chosen
            menu_choice = False
            exit
        case "1":
            mw.team_season_points()
        case "2":
            Callum_C.callum_C1()
        case "3":
            ShaunQ1.ShaunQ1Program()
        case "4":
            Callum_Q2.callum_C2()
        case "5":
            mw.player_xG_VS_G()
        case "6":
            ShaunQ2.ShaunQ2Program()
        case "7":
            MariaQ1.MariaQ1Program()
        case "8":
            MariaQ2.MariaQ2Program()
        case "9":
            JoeQ1.Joe_Q1()
        case "10":
            JoeQ2.Joe_Q2()
