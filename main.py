import sys
import helperFunctions as helper
import dateProgram

if __name__ == "__main__":
    userInput = helper.stringifyExtension(input("Enter .ics file name: "), "ics")
    f = helper.validateFile(userInput, ".ics")
    dateProgram.start(f, userInput)
    f.close()
