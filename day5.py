def readInput(seperator):
    inPath = input('Please enter the path to the input file\n')
    input_raw = open(inPath).read()
    # obsolete end of lines
    noObseol = 0
    for c in input_raw[::-1]:
        if(c == '\n'):
            noObseol+=1
        else:
            break
    if noObseol != 0:
        input_clean = input_raw[:-noObseol]
    else:
        input_clean = input_raw
    input_sliced = input_clean.split(seperator)
    return input_sliced

seperator="\n"
seating = readInput(seperator)
# convert the seating to binary form and from that to integer for the seat ids
seatIds = [8*int(l[:7].replace("F","0").replace("B","1"),2)+int(l[7:].replace("L","0").replace("R","1"),2) for l in seating]

## Task 1 ##
print('The maximum seat Id is',max(seatIds))

## Task 2 ##
# as there is only one free seat except at front and back and we already know the highest seatId,
# we can use the maximum seatId as upper boundary and find the highest seat ID
print('The free seat has the Id',max([f for f in range(max(seatIds)) if f not in seatIds]))
