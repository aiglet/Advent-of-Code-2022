# Open the file and split it into lines
data = open("input.txt")
lines = data.readlines()


def overlap(sections):
    total_overlaps = 0

    for line in sections:
        section1, section2 = line.split(",")

        start1, stop1 = section1.split("-")
        start2, stop2 = section2.split("-")

        if start1 == stop1:
            range_section2 = range(int(start2), (int(stop2)+1))
            for x in range_section2:
                if int(start1) == x:
                    total_overlaps += 1
        elif start2 == stop2:
            range_section1 = range(int(start1), (int(stop1)+1))
            for x in range_section1:
                if int(start2) == x:
                    total_overlaps += 1
        elif int(start1) <= int(start2):
            if int(stop1) >= int(stop2):
                total_overlaps += 1
        elif int(start1) >= int(start2):
            if int(stop1) <= int(stop2):
                total_overlaps += 1


    print(total_overlaps)

overlap(lines)