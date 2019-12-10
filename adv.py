# I am coding blindly (#lazy) so it may not work
crowbar = True
def room1():
    print("You are in a room, with a Python Software Foundation poster. There is no escape other than a small barred window.")
    if crowbarTaken not True:
        print("There is a crowbar.")
    windowExists = True
    crowbarExists = True
room1()
whatToDo = input(">")
if whatToDo == "take crowbar":
    if crowbarExists == True:
        print("Taken.")
        crowbarTaken = True
    else:
        print("I don't see that.")
elif whatToDo == "take":
    print("You must supply an object.")
elif "take" in whatToDo and whatToDo != "take": #It SHOULD in theroy see if it is `take' with another word (if there is take but the input is not exactly take
elif whatToDo == "pull window":
    if windowExists == True:
        print("You cannot pull that.")
