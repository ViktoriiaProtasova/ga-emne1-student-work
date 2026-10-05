spaceship = {"name": "Voyager", "captain": "James Smith", "speed": 28000, "operational": True}

for key, value in spaceship.items():
    if key == 'captain':
        print(f"{key.capitalize()} {value}")

spaceship['speed'] = 30000
spaceship["destination"] = "Mars"

print(spaceship)



