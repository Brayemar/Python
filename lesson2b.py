# Tuple
# A tuple is an immutable type of a list (it cannot be changed)
# To introduce a tuple, we use parenthesis ()

counties =("Nairobi", "Mombasa", "Nakuru", "Eldoret", "Kajiado", "Kisii")

print(counties)
print(type(counties))

# slicing of tuples
print(counties[3:])

# accessing of a tuple by use of the indexes
print(counties[5])

# NOTE: Below will generate an error
#Attribute Error
counties.append("Machakos")
print(counties)