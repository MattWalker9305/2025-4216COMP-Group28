import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import classes_for_dataset as cfd
from collections import defaultdict

def team_season_points():
    team_not_found = True

    selected_team = input("Enter team: ")
    selected_year = input("Enter year: ")

    teams = cfd.read_file_to_array("datasets/teams.csv", cfd.Team)
    for row in teams:
           if row.name == selected_team:
               selected_team_id = row.teamID
               team_not_found = False
               break

    if team_not_found:
        print("no team found")
    else:
        match_results = []

        team_statistics = cfd.read_file_to_array("datasets/teamstats.csv", cfd.TeamStatistic)
        for row in team_statistics:
            if row.teamID == selected_team_id and selected_year == row.season:
                match_results.append((row.date, row.result))
        
        match_results.sort(key=lambda x: x[0])

        data = pd.DataFrame(match_results, columns=['date', 'result'])
        data['date'] = pd.to_datetime(data['date'])
        
        data['points'] = data['result'].map({'W': 3, 'D': 1, 'L': 0})
    
        data['cumulative_points'] = data['points'].cumsum()

        fig, ax = plt.subplots()
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m.%Y"))
        ax.set_xticks(data['date'])
        ax.plot(data['date'], data['cumulative_points'], 'go:')
        ax.tick_params(axis='x', labelrotation=90)

        ax.set_title(f"Points scored by {selected_team} over a season")
        ax.set_xlabel('Date')
        ax.set_ylabel('Points')
        
        print(data)
        plt.legend(['Points scored at certain date'], loc='upper left')
        plt.show()
        
def player_xG_VS_G():
    selected_season = int(input("Enter a season (2014-2020):"))
    #start_time=time.time()
    games = cfd.read_file_to_array('datasets/games.csv', cfd.Game, filter_func=lambda row: int(row['season']) == selected_season)
    game_ids = []
    for game in games: game_ids.append(game.gameID)
    players = cfd.read_file_to_array('datasets/players.csv', cfd.Player)
    appearances = cfd.read_file_to_array('datasets/appearances.csv', cfd.Appearance, filter_func=lambda row: row['gameID'] in game_ids)
    
    player_groups = defaultdict(list)
    for appearance in appearances:
        player_groups[appearance.playerID].append(appearance)


    data = pd.DataFrame.from_dict(player_groups, orient='index')
    print(data)
            
    #end_time=time.time()
    #print(f"done {end_time - start_time:.6f} seconds" )

    # for performance in best_player_performance: print(performance.playerID)
player_xG_VS_G()