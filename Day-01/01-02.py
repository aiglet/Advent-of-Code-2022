# Open the data file
data = open("input.txt")
lines = data.readlines()

# Start the math
def calorie_counter(lines):

# Initiate a variable to hold the largest sum so far discovered and the current counbt
    big_elf1 = 0
    big_elf2 = 0
    big_elf3 = 0
    current_calories = 0

# For each line in the data file

    for line in lines:

        # Check to see if you can convert the line to an integer
        try:
            int(line)

            # If you can, add the integer value of the line to current_calories
            current_calories += int(line)

        # If you *cannot* convert the line to an integer
        except ValueError:

            # Check the current total against the big_elf values and store them properly
            if current_calories > big_elf1:
                big_elf3 = big_elf2
                big_elf2 = big_elf1
                big_elf1 = current_calories
            elif current_calories > big_elf2:
                big_elf3 = big_elf2
                big_elf2 = current_calories
            elif current_calories > big_elf3:
                big_elf3 = current_calories

            # Reset current_calories to 0 and continue to the next item on the list
            current_calories = 0
            continue

    # Sum the three biggest elves to get the answer
    big_elf = big_elf1 + big_elf2 + big_elf3


    print(f"The three biggest elves have a total of {big_elf} calories.")

calorie_counter(lines)