team1_scored =int(input("Enter the total runs scored by Team1: "))
team1_faced =int(input("Enter the total overs faced by Team1: "))
team1_conceded =int(input("Enter the total runs conceded by Team1: "))
team1_bowled =int(input("Enter the total overs bowled by Team1: "))

team2_scored =int(input("Enter the total runs scored by Team2: "))
team2_faced =int(input("Enter the total overs faced by Team2: "))
team2_conceded =int(input("Enter the total runs conceded by Team2: "))
team2_bowled =int(input("Enter the total overs bowled by Team2: "))

team1_Nrr =(team1_scored/team1_faced)-(team1_conceded/team1_bowled)
print("Team1 Net Run Rate=",round(team1_Nrr,2))
team2_Nrr =(team2_scored/team2_faced)-(team2_conceded/team1_bowled)
print("Team2 Net Run Rate=",round(team2_Nrr,2))

if team1_Nrr>team2_Nrr:
    print("Team1 has a higher Net Run Rate and tops the points table.")
elif team2_Nrr>team1_Nrr:
    print("Team2 has a higher Net Run Rate and tops the points table.")
else:
    team1_w =int(input("Enter number of wickets taken by Team 1: "))
    team2_w =int(input("Enter number of wickets taken by Team 2: "))
    
    if team1_w>team2_w:
        print("Team1 has a higher Net Run Rate and more wickets and tops the points table")
    elif team2_w>team1_w:
        print("Team2 has a higher Net Run Rate and more wickets and tops the points table")
    else:
        print("Both teams have the same Net run rate and wickets taken and are tied on points")

