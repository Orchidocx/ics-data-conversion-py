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
    firstBeginEventFound = False
    firstEndEventFound = False
    offset = 0
    for line in f:
        result += line
        if line == "BEGIN:VEVENT\n":
            firstBeginEventFound = True
        if "DTSTART;" in line:
            print('in start')
        if "DTEND;" in line:
            print('in end')

def iterateFile():
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