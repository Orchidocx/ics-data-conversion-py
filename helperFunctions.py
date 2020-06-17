def stringifyExtension(userInput, extension):
    if "." in userInput:
        if userInput.split(".")[-1] == extension:
            return userInput
        return "{}.{}".format(userInput, extension)
    return "{}.{}".format(userInput, extension)

def validateFile(fileName, extension):
    while True:
        try:
            f = open(fileName, 'w+')
            return f
        except:
            fileName = stringifyExtension(input("Could not find file '{}'.\nPlease enter {} file name: ".format(fileName, extension)), "ics")