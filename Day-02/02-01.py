# Open the file and split it into lines
data = open("input.txt")
lines = data.readlines()

# For each line, determine the input and the total
# Add the total to the running total

def roshambo(lines):

    # Initiate a variable to hold the total
    total = 0
    their_score = 0
    my_score = 0

    for line in lines:

        # Calculate their score
        if line[0] == "A":
            their_score += 1
            print("They played Rock.")
        elif line[0] == "B":
            their_score += 2
            print("They played Paper.")
        elif line[0] == "C":
            their_score += 3
            print("They played Scissors.")

        # Calculate my score
        if line[2] == "X":
            my_score += 1
            print("I played Rock.")
        elif line[2] == "Y":
            my_score += 2
            print("I played Paper.")
        elif line[2] == "Z":
            my_score += 3
            print("I played Scissors.")

        # Add my score to the total
        total += my_score

        # Figure out who won
        if my_score > their_score:
            total += 6
            print(f"I won. My total score is {total}.")
        elif my_score == their_score:
            total += 3
            print(f"We tied. My total score is {total}.")
        elif my_score < their_score:
            total += 0
            print(f"I lost. My total score is {total}.")


        my_score = 0
        their_score = 0

    print(f"Your total score is {total}")




roshambo(lines)