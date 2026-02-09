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