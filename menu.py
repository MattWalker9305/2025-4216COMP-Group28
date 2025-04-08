import matt_walker_cw as mw
import Callum_C
import ShaunQ1
import Callum_Q2
import ShaunQ2
import os

menu_choice = True
while menu_choice:

    os.system('cls')
    choice = input("Enter a number to choose one of the below applictaions"
                       "\n1.) team points over a season"
                       "\n2.) team home and away goals scored in a season"
                       "\n3.) Player goals over a season"
                       "\n4.) Shot conversion rate for teams in a season"
                       "\n5.) Player xG vs G"
                       "\n6.) Each type of goal scored in a league over a season"
                       "\n0.) exit"
                       "\nchoose application: ")

    match choice:
        case "0":
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