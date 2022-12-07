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

        # Turn the ranges of sections into sets
        set1 = set(range(int(start1), int(stop1)+1))
        set2 = set(range(int(start2), int(stop2)+1))

        # The overlap is where the two sets intersect
        overlaps = set1.intersection(set2)

        # If the intersection of the section sets is NOT empty, then there is an overlap
        if len(overlaps) > 0:
            total_overlaps +=1

    print(total_overlaps)


overlap(lines)
