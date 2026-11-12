
import pandas as pd

# Read the CSV file
df = pd.read_csv("cfb.csv")
print(df.columns.tolist())

# Ask the user for a season
season = int(input("Enter a season to analyze: "))

# Find teams from the selected season
season_data = df[df["Season"] == season]

# Check if the season exists
if season_data.empty:
    print("Season not found.")

else:
    # Dictionary to organize teams
    categories = {
        "10 or more wins": [],
        "8-9 wins": [],
        "6-7 wins": [],
        "Fewer than 6 wins": []
    }

    # Loop through each team
    for index, row in season_data.iterrows():
        team = row["Team"]
        wins = row["Win"]

        if wins >= 10:
            categories["10 or more wins"].append(team)

        elif wins >= 8:
            categories["8-9 wins"].append(team)

        elif wins >= 6:
            categories["6-7 wins"].append(team)

        else:
            categories["Fewer than 6 wins"].append(team)

    # Display the results
    print()
    print("College Football Results for", season)

    for category, teams in categories.items():
        print()
        print(category + ":")

        for team in teams:
            print(" ", team)
