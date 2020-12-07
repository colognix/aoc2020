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

input_sliced = readInput("\n\n")

## Task 1 ##

# count the number of fields using shortcut
def validFields(f):
    return f.count(":")
# retrieve the number of correct passports by checking no of fields
# adjust count for cases where cid is not present
print(len([f for f in input_sliced if ((not ("cid" in f) and (validFields(f) > 6)) or validFields(f) > 7)]))

## Task 2 ##

# ... guess what
def validField(f):
    vals = f.split(":")
    validNums = ["0","1","2","3","4","5","6","7","8","9"]
    validLits = ["a","b","c","d","e","f"]
    if (vals[0] == "byr"):
        byr = vals[1]
        if (int(byr) >= 1920 and int(byr) <= 2002):
            return 1;
        else:
            return 0;
    elif (vals[0] == "iyr"):
        iyr = vals[1]
        if (int(iyr) >= 2010 and int(iyr) <= 2020):
            return 1;
        else:
            return 0;
    elif (vals[0] == "eyr"):
        eyr = vals[1]
        if (int(eyr) >= 2020 and int(eyr) <= 2030):
            return 1;
        else:
            return 0;
    elif (vals[0] == "hgt"):
        hgt = vals[1]
        if ("in" in hgt):
            hgt = hgt.replace("in","");
            if (int(hgt) >= 59 and int(hgt) <= 76):
                return 1;
            else:
                return 0;
        elif ("cm" in hgt):
            hgt = hgt.replace("cm","")
            if (int(hgt) >= 150 and int(hgt) <= 193):
                return 1;
            else:
                return 0;
        else:
            return 0;
    elif (vals[0] == "hcl"):
        hcl = vals[1]
        if hcl[0]=="#":
            if len([c for c in hcl[1:] if c not in validNums+validLits]) > 0:
                return 0;
            return 1;
        else:
            return 0;
    elif (vals[0] == "ecl"):
        if (vals[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            return 1;
        else:
            return 0;
    elif (vals[0] == "pid"):
        if (len(vals[1]) == 9):
            if (len([f for f in vals[1] if f in validNums]) == 9):
                return 1;
            else:
                return 0;
        else:
            return 0;
    elif (vals[0] == "cid"):
        return 0;
    else:
        return 0;
    
# validation routine for one passport
# returns number of valid fields - cid is not counted (7 to be accepted)
def validate(pp):
    # use inner sum to flatten format issue results
    return sum([validField(f) for f in sum([p.split(" ") for p in pp.split("\n")],[])])

# number of passports that are valid
print(len([pp for pp in input_sliced if validate(pp) > 6]))
