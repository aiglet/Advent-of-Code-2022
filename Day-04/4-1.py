# Open the file and split it into lines
data = open("test.txt")
lines = data.readlines()



def overlap(sections):
    total_overlaps = 0

    for line in sections:
        splits = line.split(",")
        section1 = splits[0]
        section2 = splits[1]

        print(section1, section2)

        if section1[0] < section2[0]:
            if section1[2] > section2[2]:
                total_overlaps += 1
        elif section1[0] > section2[0]:
            if section1[2] < section2[2]:
                total_overlaps += 1
        elif section1[0] == section1[2]:
            if section1[0] in list(section2):
                total_overlaps += 1
        elif section2[0] == section2[2]:
            if section2[0] in list(section1):
                total_overlaps += 1

    print(total_overlaps)

overlap(lines)