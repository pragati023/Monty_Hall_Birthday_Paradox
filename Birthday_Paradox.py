import random
total = 0   # Tracks total cases
pair_exist = 0  # Tracks how many cases have pairs
N = 1000  # Changes number of cases(increase to increase accuracy)
num = 72    # Number of people whose birthdays are simulated
for j in range(N):
    birthdays = []  # List to store list of "num" birthdays
    temp = []   # Temp list - checks presence of a pair
    pair = -1   # Checks status of finding a pair (equal to the day where pair was found)
    check = False   # Checks if a pair is found in the particular case
    for i in range(num):
        birthdays.append(random.choice(range(1, 366)))  # Randomly assigns a day of the year( b/w 1 to 365) to the list
    print(f"Case {j+1}:")   # Prints the case number
    print(birthdays)    # Prints the list of birthdays
    for i in birthdays:     # Checks if a pair exists
        if i not in temp:
            temp.append(i)
        else:
            pair = i    # Stores the day when pair is found
            break
    if pair != -1:
        pair_exist += 1     # Increase the count of cases where pair exist by 1
        check = True
    if check:   # This statement executes when pair is found
        print(f"Pair found at {pair} day.")
    else:   # This statement executes when pair is not found
        print("No pair found.")
    total += 1 # Increases the count of total cases by 1
    print("")
print(f"Probability of same birthday = {pair_exist/total}")      # Prints the probability of same birthday
