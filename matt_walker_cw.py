import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import classes_for_dataset as cfd
from collections import defaultdict

def team_season_points():
    team_not_found = True

    #taking user inputs 
    selected_team = input("Enter team: ")
    selected_year = input("Enter season: ")

    #creating an array of all the teams in team.csv
    teams = cfd.read_file_to_array("datasets/teams.csv", cfd.Team)
    #looping through each team in array teams
    for team in teams:
           if team.name == selected_team:
               #setting the selected_team_id variable to the matching teams id
               selected_team_id = team.teamID
               team_not_found = False
               break

    #validation, if no team found then dont continue
    if team_not_found:
        print("no team found")
        time.sleep(5)
    else:
        match_results = []
        #creating array of team statistics where its the selected team and in the selected season
        team_statistics = cfd.read_file_to_array("datasets/teamstats.csv", cfd.TeamStatistic, filter_func=lambda team_statistic: team_statistic['teamID'] == selected_team_id and team_statistic['season'] == selected_year)
        for team_statistic in team_statistics:
                #adding the date and result of each match to the match result array
                match_results.append((team_statistic.date, team_statistic.result))
        #sorting based on date, gives dates in correct order
        match_results.sort(key=lambda x: x[0])

        #putting the date and result into a pandas dataframe
        data = pd.DataFrame(match_results, columns=['date', 'result'])
        data['date'] = pd.to_datetime(data['date'])
        #changes the result to a number, lets us calculate points
        data['points'] = data['result'].map({'W': 3, 'D': 1, 'L': 0})
        #working out total points after each game
        data['cumulative_points'] = data['points'].cumsum()

        #plotting 
        fig, ax = plt.subplots()
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m.%Y"))
        #displaying all dates on x-axis
        ax.set_xticks(data['date'])
        ax.plot(data['date'], data['cumulative_points'], 'go:')
        #stopping dates overlapping, increasing readability
        ax.tick_params(axis='x', labelrotation=90)

        #setting titles/labels
        ax.set_title(f"Points scored by {selected_team} over a season")
        ax.set_xlabel('Date')
        ax.set_ylabel('Points')
        plt.legend(['Points scored at certain date'], loc='upper left')
        
        #output dataframe
        print(data)
        
        ax.grid(True)
        #output visualisation
        plt.show()
        
def player_xG_VS_G():
    #user integer input
    selected_season = int(input("Enter a season (2014-2020):"))
    #create an array of all games matching the requested sesaon
    games = cfd.read_file_to_array('datasets/games.csv', cfd.Game, filter_func=lambda game: int(game['season']) == selected_season)
    game_ids = []
    # add the game id of all games in the games array to game_ids
    for game in games: game_ids.append(game.gameID)
    #create an array of all players
    players = cfd.read_file_to_array('datasets/players.csv', cfd.Player)
    #create an array of all appearances where the game id matches one in game_ids 
    appearances = cfd.read_file_to_array('datasets/appearances.csv', cfd.Appearance, filter_func=lambda appearance: appearance['gameID'] in game_ids)
    
    #create a dictionary of all players appearances in a season, linked under the player id of the player.
    player_groups = defaultdict(list)
    for appearance in appearances:
        player_groups[appearance.playerID].append(appearance)

    player_data = []
    #create a dictionary of all players with their player ids
    player_dict = {player.playerID: player.name for player in players}

    #going through each playerid and then the appearance matched to them
    for player_id, appearances in player_groups.items():
        #working out totals in a season
        total_xG = sum([float(appearance.xGoals) for appearance in appearances])
        total_goals = sum([int(appearance.goals) for appearance in appearances])

        #finding the player name to match the playerid
        player_name = player_dict.get(player_id, "Unknown Player")

        #adding the details to a array of objects all linked together.
        player_data.append({
            'playerID': player_id,
            'playerName': player_name,
            'total_xG': total_xG,
            'total_goals': total_goals
        })
    
    #creating dataframe from array
    data = pd.DataFrame(player_data)
    print(data)
    #finding top 10 preforming players based on xg
    top_players = data.sort_values(by='total_xG', ascending=False).head(10)
    fig, ax = plt.subplots()
    #plotting all players total xG vs their total goals
    ax.scatter(data['total_xG'], data['total_goals'])
    #overlapping with top players total xG vs their goals in colour red
    ax.scatter(top_players['total_xG'], top_players['total_goals'], color = 'red')
    #displaying the players name next to the top 10 players
    for i, row in top_players.iterrows():
        ax.text(row['total_xG'], row['total_goals'], row['playerName'], fontsize=8)
    #adding the minimum and maximum x and y axis length, ensure graph takes up most amount of room
    #no unnecessary blank space
    ax.set_xlim([min(data['total_xG']) - 1, max(data['total_xG']) + 1])
    ax.set_ylim([min(data['total_goals']) - 1, max(data['total_goals']) + 1])
    #labeling axis
    ax.set_xlabel("Players total expected goals")
    ax.set_ylabel("Players total goals")
    ax.set_title(f"xG vs Goals for players in {selected_season}")
    plt.legend(['Goals scored vs xG for each player', 'Top preforming players, based on XG'], loc='upper left')
    #display visualisation
    plt.show()