# names = ["debbie", "laya", "vigdis", "saymeen", "jessie", "elizabeth", "maggie", "devansshi", "liyana", "alina", "muskaan"]
# print(names)
# #for length of a variable do or for the amount of variables in an array
# len("elizabeth")
# #or
# len(names[1])
# #to call on a specific part of an array use its index in []
#     #remember we go 0,1,2....
# print(names[0])

# #a fixed loop is a for loop
# for x in range(len(names)):     #x can be anything its a variable   #and use len(array) as it ensures no info error
#     print(names[x])

# name = input("what name do you want? ")     #how to input
# #to add a variable to an array
# names.append(name)
# print(name)

#PRACTICE
colours = []
colour = ""
for x in range(3):
    colour = input("what colour would you like?  ")
    colours.append(colour)

print(colours)