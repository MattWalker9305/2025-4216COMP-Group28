
import matplotlib.pyplot as plt
import seaborn as sns
import classes_for_dataset as cfd
from classes_for_dataset import Shot, Game

def MariaQ1Program():
    # Ask user for a season to filter by
    user_season = input("Enter season (2015-2020): ")

    # Load shots and games
    shots = cfd.read_file_to_array("datasets/shots.csv", Shot)
    games = cfd.read_file_to_array("datasets/games.csv", Game)

    # Get gameIDs that match the selected season
    season_game_ids = [g.gameID for g in games if g.season == user_season]

    # Filter shots based on those gameIDs
    filtered_shots = [s for s in shots if s.gameID in season_game_ids and s.situation and s.shotResult]

    if not filtered_shots:
        print("No data found for that season.")
        return

    # Prepare data for plotting
    situations = [s.situation for s in filtered_shots]
    results = [s.shotResult for s in filtered_shots]

    # Plot
    plt.figure(figsize=(12, 6))
    sns.countplot(x=situations, hue=results)
    plt.title(f"Shot Results by Situation - Season {user_season}")
    plt.xlabel("Situation")
    plt.ylabel("Number of Shots")
    plt.xticks(rotation=45)
    plt.legend(title="Shot Result")
    plt.tight_layout()
    plt.show()
