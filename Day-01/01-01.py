# Open the data file
data = open("input.txt")
lines = data.readlines()

# Start the math
def calorie_counter(lines):

# Initiate a variable to hold the largest sum so far discovered and the current counbt
    big_elf = 0
    current_calories = 0

# For each line in the data file

    for line in lines:

        # Check to see if you can convert the line to an integer
        try:
            int(line)

            # If you can, add the integer value of the line to current_calories
            current_calories += int(line)

            # Check to see if the current total is larger than big_elf and replace it if true
            if current_calories > big_elf:
                big_elf = current_calories

        # If you *cannot* convert the line to an integer
        except ValueError:

            # Reset current_calories to 0 and continue to the next item on the list
            current_calories = 0
            continue


    print(f"The big elf has {big_elf} calories.")

calorie_counter(lines)