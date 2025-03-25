import matt_walker_cw as mw
import os

menu_choice = True

while menu_choice:

    os.system('cls')
    choice = int(input("choose application: "))

    match choice:
        case 1:
            menu_choice = False
            exit
        case 2:
            mw.team_season_points()