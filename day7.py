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
    input_clean = input_raw[:-noObseol]
    input_sliced = input_clean.split(seperator)
    return input_sliced

def prepare_data(input_sliced):
    
    bagMap = [b.split("contain") for b in input_sliced]
    # bagenanigans will contain all combinations of one inner and one outer bag including cardinality
    bagenanigans = []
    for b in bagMap:
        # remove unneccessary markup
        outerBag = b[0].replace("bags","").replace(" ","")        
        innerBags = b[1].split(",")
        innerBags = [b.replace("bags","").replace("bag","").replace(" ","").replace(".","") for b in innerBags]
        
        # add entry in bagenanigans for each inner bag
        bagenanigans += [[outerBag, b[1:], b[0]] for b in innerBags]
        
        # some bags don't contain other bags, those can be discarded for our purpose
        bagenanigans = [b for b in bagenanigans if "n" not in b[2]]
        
    return bagenanigans
        
seperator = "\n"
input_sliced = readInput(seperator)
bagenanigans = prepare_data(input_sliced)

## Task 1 ##

shinyBags = ['shinygold']
numBags = 0
# at each recursion, shinyBags contains another layer of "parent bags"
# stop when no new possibilities are found
while(numBags < len(shinyBags)):
    numBags = len(shinyBags)
    shinyBags += [b[0] for b in bagenanigans if (b[1] in shinyBags and b[0] not in shinyBags)]
    
# shinygold is not counted, remove duplicates
print(len(set(shinyBags))-1, 'colors of bags can eventually contain at least one shiny gold bag.')


## Task 2 ##

# for each occurrence of 
def getInnerBagCount(bagColor, bagAttributeMap):
    bagCount = 1
    for b in bagAttributeMap:
        if (b[0]==bagColor):
            bagCount += int(b[2])*getInnerBagCount(b[1], bagAttributeMap)
    return bagCount

# shinygold is not counted
print('There are',getInnerBagCount('shinygold',bagAttributeMap)-1,'individual bags required inside my single shiny gold bag.')
