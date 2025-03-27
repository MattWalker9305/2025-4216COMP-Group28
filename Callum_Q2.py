import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

team_not_found = True

requested_team = input("Enter team:")
requested_year = input("Enter year:")


with open("2025-4216COMP-Group28/datasets/teams.csv", "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        team = row[1]
        team_id = row[0]
        if team == requested_team:
            team_id = row[0]
            team_not_found = False
            break
    if team_not_found:
        print("no team found")
    else:
        dates = []
        shot_conversion_rate = []

      
        with open("2025-4216COMP-Group28/datasets/teamstats.csv", "r") as f:
            team_stats = csv.reader(f)
            next(team_stats)

           
            for row in team_stats:
                current_team_id = row[1]
                season = row[2]
                shots = int(row[7])
                goals = int(row[5])
                date = row[3]

                
                if current_team_id == team_id and requested_year == season:
                    if shots > 0:
                        dates.append(date)
                        shot_conversion_rate.append((goals / shots) * 100)

        
        if dates:
            df = pd.DataFrame({"Date": dates, "Shot Conversion Rate": shot_conversion_rate})
            df["Date"] = pd.to_datetime(df["Date"])
            df = df.sort_values("Date")

            fig, ax = plt.subplots(figsize=(10, 5))

            ax.plot(df["Date"], df["Shot Conversion Rate"], "bo-", label="Shot Conversion Rate")

            fig.suptitle(f"Shot Conversion Rate for {requested_team} in {requested_year}", fontsize=20)
            ax.set_title("Shot Conversion Over Time", fontsize=14)
            ax.set_xlabel("Date", fontsize=12)
            ax.set_ylabel("Shot Conversion Rate (%)", fontsize=12)

            ax.set_xticks(df["Date"])  
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))  
            plt.xticks(rotation=90, ha="right", fontsize = 8) 

            fig.subplots_adjust(top=0.85, bottom=0.2)

            ax.grid(True)
            ax.legend()

            plt.show()
        







