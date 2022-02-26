import time
import classes as cls
import os
import repo as rp
import tools as tls

print("Welcome to Student Management App")

tls.ShowAppMenu()

while True:
    theInput = input("Menu Input>>")

    if theInput == "a":
        tls.AddStudent()
        print("The Student has been successfully registered")
        time.sleep(0.5)
        os.system("cls")
    elif theInput == "s":
        tls.ShowStudents(rp.StudentList)
    else:
        print("Invalid input, Please try again.")