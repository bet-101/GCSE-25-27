age = [3, 8, 14, 5, 11]
found = False
target = 14

for x in range(len(age)):
    print(age[x])
    if age[x] == target:
        found == True
        print("found it!!")
        print(found)
