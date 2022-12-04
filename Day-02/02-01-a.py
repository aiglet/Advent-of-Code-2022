# Open the file and split it into lines
data = open("input.txt")
lines = data.readlines()

def roshambo(lines):

    # Let's have a variable.
    total_score = 0

    # Comment to remind me of what the values are.
    '''
        A, X = Rock, 1 point
        B, Y = Paper, 2 points
        C, Z = Scissors, 3 points
        Win = 6 points
        Tie = 3 points
    '''

    # Iterate through all my lines
    for line in lines:
        # Play each round and add the resulting total to the total score each time
        if line[0] == "A":
            if line[2] == "X":
                total_score += 4
            elif line[2] == "Y":
                total_score += 8
            elif line[2] == "Z":
                total_score += 3
        elif line[0] == "B":
            if line[2] == "X":
                total_score += 1
            elif line[2] == "Y":
                total_score += 5
            elif line[2] == "Z":
                total_score += 9
        elif line[0] == "C":
            if line[2] == "X":
                total_score += 7
            elif line[2] == "Y":
                total_score += 2
            elif line[2] == "Z":
                total_score += 6


    print(f"The final score is {total_score}")

roshambo(lines)
