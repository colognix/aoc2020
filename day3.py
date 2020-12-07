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

input_sliced = readInput("\n")

# convert trees to ones 
geometry = [[int(field=="#") for field in l] for l in input_sliced]

## Task 1 ##

# initialize variables
i,j,trees = 0,0,0
width = len(geometry[1])
# traverse the slope, each tree adds one 
while(i < len(geometry)):
    trees += geometry[i][j]
    i += 1
    # if the right edge is reached, start back at left, as the pattern repeats
    j = (j+3) % width
print(trees)

## Task 2 ##
trees = 1
# for one bottom step, perform for right stepsizes and multiply to count according to rules
for step in [1,3,5,7]:
    i,j,curTrees = 0,0,0
    while(i < len(geometry)):
        curTrees += geometry[i][j]
        i += 1
        j = (j+step) % width
    trees *= curTrees

# finally perform for 2 bottom, 1 right step
i,j,curTrees = 0,0,0
while(i < len(geometry)):
    curTrees += geometry[i][j]
    i += 2
    j = (j+1) % width
trees *= curTrees
print(trees)
