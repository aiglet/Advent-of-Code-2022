# Open the file and split it into lines
data = open("test.txt")
lines = data.readlines()

# This function splits a string in half and returns both halves separately
def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

def rucksack_priority_sum(contents):

    # Let's have a variable
    priority_total = 0
    priority_items = ""

    # This sets up the values for the letters based on the index of the letter in the list
    values = [0, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    values2 = [0, "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Iterate through the input
    for line in contents:

        # Split the line into its two containers
        container1, container2 = splitstring(line)

        set1 = set(container1)
        set2 = set(container2)
        result = str(set1.intersection(set2))
        priority_items += result

    unique_priority = set(priority_items)

    for item in unique_priority:
        if item in values:
            priority_total += values.index(item)
        elif item in values2:
            priority_total += values2.index(item) + 26

    print(priority_total)






    print(f"The total is {priority_total}")



rucksack_priority_sum(lines)