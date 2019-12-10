# I am coding blindly (using a Chromebook at school) so it may not work

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
elif whatToDo == "take":
    print("You must supply an object.")
elif whatToDo == "pull window":
    if windowExists == True:
        print("You cannot pull that.")
