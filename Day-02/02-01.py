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
        elif line[0] == "B":
            their_score += 2
        elif line[0] == "C":
            their_score += 3

        # Calculate my score
        if line[2] == "X":
            my_score += 1
        elif line[2] == "Y":
            my_score += 2
        elif line[2] == "Z":
            my_score += 3

        # Add my score to the total
        total += my_score

        # Figure out who won
        if my_score > their_score:
            total += 6
        elif my_score == their_score:
            total += 3
        elif my_score < their_score:
            total += 0

        my_score = 0
        their_score = 0

    print(f"Your total score is {total}")




roshambo(lines)