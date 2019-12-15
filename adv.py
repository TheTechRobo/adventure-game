# I am coding blindly (#lazy) so it may not work
crowbar = True
def room1():
    print("You are in a room, with a Python Software Foundation poster. There is no visible escape other than a small barred window.")
    if crowbarExists == True:
        print("There is a crowbar.")
    windowExists = True
    crowbarExists = True
room1()
whatToDo = input(">")
if whatToDo.lower() in "take crowbar":
    if crowbarExists == True:
        print("Taken.")
        crowbarTaken = True
        crowbarExists = False
    elif crowbarExists == False:
        print("You have already taken that!")
    else:
        print("I don't see that here.")
elif whatToDo.lower() in "take":
    print("You must supply an object.")
elif "take" in whatToDo and whatToDo != "take": #It SHOULD in theroy see if it is `take' with another word (if there is take but the input is not exactly take
    print("I don't see that here...")
elif whatToDo.lower() in "pull window":
    if windowExists == True:
        print("You cannot pull that.")
elif whatToDo.lower() in "pull bars":
        print("You cannot pull that. Maybe if you had a tool...")
elif whatToDo.lower() in "yeet crowbar":
    if crowbarExists == True:
        print("You throw the crowbar across the room. But it just bounces back.")
