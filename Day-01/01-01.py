# Open the data file
data = open("test.txt")
lines = data.readlines()

# Start the math
def calorie_counter(lines):

# Initiate a variable to hold the largest sum so far discovered and the current counbt
    big_elf = 0
    current_calories = 0

# Go through the data file

    for line in lines:
        if "\n" in line:
            if current_calories > big_elf:
                big_elf == current_calories
                current_calories == 0
            else:
                current_calories == 0
        else:
            current_calories += int(line)

    print(big_elf)

# For each line, if it has data, add it to the current total
# If the line is blank, compare the current total to BigElf
# If the current total is bigger, replace BigElf with that total
# Zero out the current total and move to the next line

calorie_counter(lines)