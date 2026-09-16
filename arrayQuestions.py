# # 1
# songs = [ 
# "Neon Skyline", 
# "Midnight Code", 
# "Pixel Dreams", 
# "Static Hearts", 
# "Northern Lights", 
# "Binary Sunset" 
# ] 
# print(songs[0], ",", songs[2], ",", songs[5])
# songs[1] = input("what is your second song?  ")
# x = int(0)
# for x in range(len(songs)):
#     print(str(songs[x]), int(x + 1))
# getSongToPlay = input("go on what song do you want (posistion)? ")
# print(songs[int(getSongToPlay) - 1])

# #2
# days = [ 
# "Monday", "Tuesday", "Wednesday", "Thursday" , "Friday" , "Saturday" , "Sunday" 
# ] 
 
# steps = [ 
# 6840, 9125, 7550, 10420, 8320, 12110, 5890 
# ] 

# for l in range(len(days)):
#     print("on" , days[l], "there was" , steps[l] , "steps")

# total = 0
# for i in range(len(days)):
#     total = total + int(steps[i])
# print(total)
# average = total / len(steps)
# print(average)
# count = 0
# for y in range(len(steps)):
#     if steps[y] >= 8000:
#        count = count + 1
# print("there are" , count , "days with over 8000 steps")

# getTarget = int(input("what is your target amount of steps? "))
# coolNumber = 0
# for k in range(len(steps)):
#     if steps[k] >= getTarget:
#         coolNumber = coolNumber + 1
# print("there are" , coolNumber , "days with over" , getTarget ,  "steps")
# print("percentage is" , coolNumber/len(steps) * 100)