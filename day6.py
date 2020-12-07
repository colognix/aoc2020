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

seperator="\n\n"
# answerMatrix contains the answers of each group, seperated by two newlines.
answerMatrix = readInput(seperator)
## Task 1 ##

#remove unneccessary markup - its not important who answered what right now!
answerMatrixSimple = []
for ans in answerMatrix:
    answerMatrixSimple += [ans.replace("\n","")]

# add up the number of different answers in each group
print('Task 1:', sum([len(set(ans)) for ans in answerMatrixSimple]))

## Task 2 ##

rightAnswerCount = 0
for group in answerMatrix:
    # who answered what?
    members = group.split("\n")
    # use the member with the least answers as base for performance reasons 
    memberAc = [len(m) for m in members]
    lowAc = memberAc.index(min(memberAc))
    # for each question that was answered by lowAc, add 1 to right answers if all answered it: 
    groupSize = len(members) 
    rightAnswerCount += sum([int(group.count(a) == groupSize) for a in members[lowAc]])
    
print('Task 2:', rightAnswerCount)
