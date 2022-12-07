# Open the file and split it into lines
data = open("input.txt")
lines = data.readlines()


def overlap(sections):
    total_overlaps = 0

    for line in sections:
        # Split the line into two sections on the comma
        section1, section2 = line.split(",")

        # Split the sections into their starts and stops on the hyphen
        start1, stop1 = section1.split("-")
        start2, stop2 = section2.split("-")

        # Check for the possible conditions that would indicate an overlap
        if int(start1) <= int(start2) or int(stop1) >= int(stop2):
                total_overlaps += 1
        elif int(start1) >= int(start2) or int(stop1) <= int(stop2):
                total_overlaps += 1

    print(total_overlaps)


overlap(lines)
