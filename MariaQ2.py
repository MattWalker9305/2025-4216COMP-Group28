
import matplotlib.pyplot as plt
import classes_for_dataset as cfd
from classes_for_dataset import TeamStatistic, Team

def MariaQ2Program():
    # Ask user for a team name
    selected_team = input("Enter team name: ").strip().lower()

    # Load data
    teams = cfd.read_file_to_array("datasets/teams.csv", Team)
    teamstats = cfd.read_file_to_array("datasets/teamstats.csv", TeamStatistic)

    # Find the teamID that matches user input
    matching_teams = [t for t in teams if selected_team in t.name.lower()]
    if not matching_teams:
        print("Team not found.")
        return

    team_id = matching_teams[0].teamID
    team_name = matching_teams[0].name

    # Filter stats by team
    stats = [s for s in teamstats if s.teamID == team_id]

    if not stats:
        print("No stats found for that team.")
        return

    # Prepare totals
    seasons = sorted(list(set(s.season for s in stats)))
    yellow = [sum(s.yellowCards for s in stats if s.season == season) for season in seasons]
    red = [sum(s.redCards for s in stats if s.season == season) for season in seasons]

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(seasons, yellow, label="Yellow Cards", color="gold")
    plt.bar(seasons, red, bottom=yellow, label="Red Cards", color="red")
    plt.title(f"Discipline Stats for {team_name}")
    plt.xlabel("Season")
    plt.ylabel("Total Cards")
    plt.legend()
    plt.tight_layout()
    plt.show()
