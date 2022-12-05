# Open the file and split it into lines
data = open("input.txt")
lines = data.readlines()


# This function strips newline and ' characters from the input
def clean_lines(dirty_list):
    interim_list = []
    for item in dirty_list:
        interim_list.append(item.replace("\n", ""))

    final_list = []

    for item in interim_list:
        final_list.append(item.replace("'", ""))

    return final_list


# This function returns the values of the letters
def letter_values(letter):
    value = 0

    values = [0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "x", "y", "z"]
    values2 = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
               "U", "V", "W", "X", "Y", "Z"]

    if letter in values:
        value = values.index(letter)
    elif letter in values2:
        value += values2.index(letter) + 26

    return value


# Here's our main function!
def get_badge(input_lines):

    # Clean up the input
    working_lines = clean_lines(input_lines)

    # Variable to hold our totals
    badge_total = 0

    # While our list is long enough to work with...
    while len(working_lines) > 2:

        # Take the first three lines of the working_lines (note that the slice does NOT include the final item)
        group = working_lines[0:3]

        # Turn our working lines into sets (which makes sure each letter only appears once in each bucket)
        set1 = set(group[0])
        set2 = set(group[1])
        set3 = set(group[2])

        # This gets the item that is unique to buckets 1 and 2
        sub_badge = set1.intersection(set2)

        # This gets the item that is unique to all the buckets and makes it into a string
        badge_unique = ",".join(sub_badge.intersection(set3))

        # This calculates the value of the item we just found and adds it to the total
        badge_total += letter_values(badge_unique)

        # This removes the lines we just worked on from the working list
        del working_lines[0:3]

    print(badge_total)


get_badge(lines)
