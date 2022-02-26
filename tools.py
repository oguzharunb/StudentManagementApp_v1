import repo as rp
import classes as cls

def Capitalizer(txt):
    outputList = []
    for x in txt.split(" "):
        outputList.append(x.capitalize())
    return " ".join(outputList)

def AddStudent():
    name = Capitalizer(SpaceDeleter(input("Please Enter a Name: ").strip()))
    branch = getBranch()
    rp.StudentList.append(cls.Student(name,branch))

def SpaceDeleter(txt):
    theOutput = txt
    while True:
        if theOutput.count("  ") != 0:
            theOutput = str(theOutput).replace("  "," ")
            continue
        break
    return theOutput

def ShowStudents(theList):

    print("ID".ljust(4) + "Name".ljust(25) + "Branch")
    print("".ljust(35,"-"))
    for x in theList:
        print(str(x.ID).ljust(4) + str(x.Name).ljust(25) + str(x.Branch))

def getBranch():
    print("Language (l)")
    print("History  (h)")
    print("Math     (m)")
    print("Science  (s)")
    while True:
        theBranch = input("input>>").lower().strip()
        if theBranch == "l":
            return "Language"
        elif theBranch == "h":
            return "History"
        elif theBranch == "m":
            return "Math"
        elif theBranch == "s":
            return "Science"
        else:
            print("invalid input, plase try again")

def ShowAppMenu():
    print("Add Student  (a)")
    print("Show Student (s)")
