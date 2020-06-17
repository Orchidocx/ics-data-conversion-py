def showBanner():
    print("Welcome to the Simple ICS Date Conversion Program!")

def showInstructions():
    print("To enter a new start date, use either format:")
    print("MM/DD/YYYY\tMM/DD/YY\tMM/DD")
    print("MM-DD-YYYY\tMM-DD/YY\tMM-DD")

def start(f):
    showBanner()
    showInstructions()
    userInput = input("Please enter a new starting date: ")
    parsedDate = parseDateInput(userInput)
    while parsedDate == "":
        print("Please enter a valid date format.")
        showInstructions()
        userInput = input("Please enter a new starting date: ")
        parsedDate = parseDateInput(userInput)
    result = ""
    firstEndEventFound = False
    offset = 0
    for line in f:
        result += line
        if "DTSTART;" in line:
            lineSplit = line.split(":")
            first = lineSplit[:-1]
            last = lineSplit[-1]
            if(firstEndEventFound):
                # If true, then offset is initialized already. Otherwise, get offset
                newDate = updateDate(last, offset)
            else:
                # offset not initialized yet. declare here
                offset = setOffset(last, parsedDate)
                newDate = updateDate(last, offset)
        if "DTEND;" in line:
            print(line.split(':')[-1])
        if line == "END:VEVENT\n":
            firstEndEventFound = True

def setOffset(a, parsedDate):
    yearA = int(a[:4])
    monthA = int(a[4:6])
    dayA = int(a[6:8])
    yearB = 0
    monthB = 0
    dayB = 0
    if(len(parsedDate) == 4):
        yearB = yearA
        monthB = int(parsedDate[:2])
        dayB = int(parsedDate[2:])
    else:
        yearB = int(parsedDate[:4])
        monthB = int(parsedDate[4:6])
        dayB = int(parsedDate[6:8])
    offsetYear = yearB - yearA
    offsetMonth = monthB - monthA
    offsetDay = dayB - dayA
    return [offsetYear, offsetMonth, offsetDay]

def updateDate(a, offset):
    year = int(a[:4]) + offset[0]
    month = int(a[4:6]) + offset[1]
    day = int(a[6:8]) + offset[2]
    result = stringifyDate(year, month, day)
    return "{}{}".format(result, a[8:])

def stringifyDate(year, month, day):
    pass

def parseDateInput(userInput):
    resultArray = []
    if '-' in userInput:
        resultArray = userInput.split('-')
    if '/' in userInput:
        resultArray = userInput.split('/')
    
    if(validateInput(resultArray)):
        resultString = icsDateFormatter(resultArray)
        return resultString
    return ""
        

def validateInput(arr):
    if(len(arr) == 2 or len(arr) == 3):
        for item in arr:
            try:
                int(item)
            except:
                return False
        return True
    return False

def icsDateFormatter(arr):
    if(len(arr) == 2):
        return "{:02d}{:02d}".format(int(arr[0]),int(arr[1]))
    if(len(arr) == 3):
        year = int(arr[-1])
        if(year < 2000):
            #assumed that events created are realistically in the year 2000+  
            year += 2000
        return "{:04d}{:02d}{:02d}".format(year, int(arr[0]), int(arr[1]))