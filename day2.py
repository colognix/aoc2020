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

## Task 1 ##

# prepare data, init counter
pwcs = [p.split(":") for p in input_sliced]
correctPWs = 0

# for each password
for pwc in pwcs:
    # retrieve policy and target character
    targetChar = pwc[0][-1]
    bounds = [int(i) for i in pwc[0][:-1].split("-")]
    noTargetChar = pwc[1].count(targetChar)
    # if policy is satisfied, count valid password
    if (noTargetChar >= bounds[0] and noTargetChar <= bounds[1]):
        correctPWs += 1
print(correctPWs)

## Task 2 ##
# init counter
correctPWs = 0

# for each password
for pwc in lines:
    # retrieve positions for this policy
    targetChar = pwc[0][-1]
    position = [int(i) for i in pwc[0][:-1].split("-")]
    # only accept pws that have target character only on one of the defined positions
    if (pwc[1][position[0]]) == targetChar:
        if (pwc[1][position[1]]) != targetChar:
            correctPWs += 1
    if (pwc[1][position[1]]) == targetChar:
        if (pwc[1][position[0]]) != targetChar:
            correctPWs += 1
    
print(correctPWs)
