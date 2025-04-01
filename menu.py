import matt_walker_cw as mw
import Callum_C
import ShaunQ1
import Callum_Q2
import os

menu_choice = True

while menu_choice:

    os.system('cls')
    choice = int(input("1.) exit"
                       "\n2.) team points over a season"
                       "\n3.) team home and away goals scored in a season"
                       "\n4.) Player goals over a season"
                       "\n5.) Shot conversion rate for teams in a season"
                       "\nchoose application: "))

    match choice:
        case 1:
            menu_choice = False
            exit
        case 2:
            mw.team_season_points()
        case 3:
            Callum_C.callum_C1()
        case 4:
            ShaunQ1.ShaunQ1Program()
        case 5:
            Callum_Q2.callum_C2()
