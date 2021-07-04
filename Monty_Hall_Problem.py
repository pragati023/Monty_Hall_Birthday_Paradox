import random
notswapping = 0     # Tracks number of cases where not swapping wins
swapping = 0    # Tracks number of cases where swapping wins
N = 10000   # Changes number of cases(increase to increase accuracy)
for i in range(N):
    doors = ["GOAT", "GOAT", "GOAT"]    # List of items behind doors 1, 2, 3
    car_allotment = random.randrange(3)     # A car is allotted to one of the doors randomly
    doors[car_allotment] = "CAR"
    initial_choice = random.randrange(3)    # A door is chosen by the player randomly
    print(f"Case {i+1}:")
    print(f"Player has chosen door {initial_choice+1}")
    host_choices = []   # A list of choices for the host to reveal as part of game
    for j in range(3):
        if (doors[j] != "CAR") and (j != initial_choice):
            host_choices.append(j)
    door_reveal = random.choice(host_choices)   # Host randomly reveals a door which doesn't have a car
    print(f"Host has revealed a goat behind {door_reveal+1}")
    print("Our player has chosen to swap")  # As an experiment to show that swapping is beneficial, our player swaps
    second_choice = -1  # A new choice is made by the user where he/she swaps
    for k in range(3):
        if (k != initial_choice) and (k != door_reveal):
            second_choice = k
    if doors[second_choice] == "CAR":   # If our second_choice has a car
        swapping += 1   # The player won by swapping and it is recorded
        print("Player won by swapping")
    else:       # Otherwise if the car was chosen initially by the player
        notswapping += 1    # The player lost by not swapping and it is recorded
        print("Player lost by not swapping")
    print(doors)    # Prints the items behind each door
    print("\n")
print("Swapping = ", swapping/N)    # Probability that he wins by swapping
print("Not swapping = ", notswapping/N)     # Probability that he wins by not swapping
