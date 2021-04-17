isldata = [
{"team": "mumbai", "mp": 20, "won": 12, "draw": 4, "loss": 4, "pts": 40},
{"team": "atk", "mp": 20, "won": 12, "draw": 4, "loss": 4, "pts": 40},
{"team": "northeast", "mp": 20, "won": 8, "draw": 9, "loss": 3, "pts": 33},
{"team": "goa", "mp": 20, "won": 7, "draw": 10, "loss": 3, "pts": 31},
{"team": "hyderabad", "mp": 20, "won": 6, "draw": 11, "loss": 3, "pts": 29}
]

team_name = list(map(lambda data: data["team"], isldata))
# print(team_name)

points = max(list(map(lambda data: data["pts"], isldata)))
# print(points)
highest = list(filter(lambda data: data["pts"] == points, isldata))
highest_team = list(map(lambda team: team["team"], highest))
# print(highest_team)

range_team = list(filter(lambda data: 40 >= data["pts"] >= 30, isldata))
print(len(range_team))