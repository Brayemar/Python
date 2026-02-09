# A Dictionary is a data type that stores data in terms of key - value pair.
# It is introduced by the use of calibraces{}
# The values stored inside of a dictionary can be of any data type.
# To access the values in a dictionary we use the keys


phonebook ={
    "Benson" : "254764312322",
    "Mary" : "254764312322",
    "Stephen" : "254764637422"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out benson's number
print(phonebook["Benson"])

print('========================')

player = {
    "name" : "Messi",
    "age" : "40",
    "teams" : ["PSG", "Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (254774542, 254222411, 25435267)
    }
}

# print the second team
print(player["teams"][1])

print("The second number of Messi is: ", player["more"]["phone"][1])

# research on IF....ELSE statements in python
