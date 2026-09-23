getTarget = input("what number should I look for?  ")
found = False
numbers = [12, 18, 22, 35, 40, 51]
for i in range(len(numbers)):
        if numbers[i] == getTarget:
            print(numbers[i])  # Return the index if the target is found
