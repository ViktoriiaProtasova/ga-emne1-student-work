scoreboard = {"Anna": 120, "John": 95, "Maria": 150, "Peter": 80, "Emma": 110}

print(scoreboard['Anna'])

scoreboard['Anna'] = 100
scoreboard['John'] = 150
scoreboard['Maria'] = 95

scoreboard['Ole'] = 120

for key, value in scoreboard.items():
    print(key, value)
