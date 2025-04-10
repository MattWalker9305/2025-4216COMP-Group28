#imports
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import classes_for_dataset as cfd

#defined function to link to main menu
def callum_C2():
    team_not_found = True

#Request user input
    requested_team = input("Enter team:")
    requested_year = input("Enter year:")

#creating an array of all the teams
    teams = cfd.read_file_to_array('2025-4216COMP-Group28/datasets/teams.csv', cfd.Team)

    #searching throught the array to find teamIDs
    for row in teams:
        if row.name == requested_team:
            team_id = row.teamID
            team_not_found = False
            break
    if team_not_found:
            print("no team found")
    else:
            dates = []
            shot_conversion_rate = [] #Creates empty lists

        
            team_stats = cfd.read_file_to_array('2025-4216COMP-Group28/datasets/teamstats.csv', cfd.TeamStatistic)
            for row in team_stats:
    
                    if row.teamID == team_id and requested_year == row.season:
                        if int(row.shots) > 0: #Checks shots is greater than 0 to avoid division by 0 error
                            dates.append(row.date)
                            shot_conversion_rate.append(float(row.goals) / float(row.shots) * 100) #Calculates shot conversion rate

            #create a dataframe
            if dates:
                df = pd.DataFrame({"Date": dates, "Shot Conversion Rate": shot_conversion_rate})
                df["Date"] = pd.to_datetime(df["Date"])
                df = df.sort_values("Date")

                average_conversion_rate = sum(shot_conversion_rate) / len(shot_conversion_rate)

#Plotting/creating visualiation
                fig, ax = plt.subplots(figsize=(10, 5))

                ax.plot(df["Date"], df["Shot Conversion Rate"], "bo-", label="Shot Conversion Rate")

                ax.axhline(y=average_conversion_rate, color='r', linestyle='--', label=f"Average Shot Conversion Rate: {average_conversion_rate:.2f}%")

                fig.suptitle(f"Shot Conversion Rate for {requested_team} in {requested_year}", fontsize = 20)
                ax.set_title("Shot Conversion Over Time", fontsize = 14)
                ax.set_xlabel("Date", fontsize = 12)
                ax.set_ylabel("Shot Conversion Rate (%)", fontsize = 12)

                ax.set_xticks(df["Date"])  
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))  
                plt.xticks(rotation = 90, ha = "right", fontsize = 8) 

                fig.subplots_adjust(top = 0.85, bottom = 0.2)

#format the visualisation
                ax.grid(True)
                ax.legend()

                plt.show()
        







