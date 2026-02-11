# A for loop can also be used to iterate through a list, tuple, string or even a dictionary...

name = "Brandon"

for letter in name:
    if letter == "n":
        print("This is letter n")
    else:
        print(letter)

print('====================')
# Below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print('====================')
if "Kajiado" in counties:
    print("Kajiado County")
else:
    print("Not found")


print('====================')
# The for loop can also be used to iterate through a dictionary


player = {
    "name": "Mbappe",
    "age": 25,
    "teams": ["PSG", "Monaco", "France"],
    "nationality": "French"
}

for key in player:
    print(key)

print('====================')
for values in player:
    print(player[values])
# print(player["name"])



print('====================')
# loop through the teams the player has played for
for team in player["teams"]:
    print(team)

