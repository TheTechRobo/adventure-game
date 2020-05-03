import runpy
crowbar = True
lightOn = False
able2GetOut = False
def room1():
    print("You are in a room, with a Python Software Foundation poster. There is no visible escape other than a small barred window.")
    print("There is a crowbar.")
crowbarExists = True
room1()
while True:
    whatToDo = input(">")
    if whatToDo.lower() == "take crowbar":
        if crowbarExists is True:
            print("Taken.")
            crowbarTaken = True
            crowbarExists = False
        elif crowbarExists is False:
            print("You have already taken that!")
        elif whatToDo.lower() == "take":
            print("You must supply an object.")
    elif "take" in whatToDo.lower() and whatToDo != "take": #It SHOULD in theroy see if it is `take' with another word (if there is take but the input is not exactly take)
        print("I don't see that here...")
    elif whatToDo.lower() in "pull window":
        print("You cannot pull that.")
    elif whatToDo.lower() in "pull bars":
        print("You cannot pull that. Maybe if you had a tool...")
    elif whatToDo.lower() in "yeet crowbar":
        if crowbarTaken is True:
            print("You throw the crowbar across the room. But it just bounces back.")
    elif whatToDo.lower() in "pry bars":
        if lightOn is False:
            print("You pry the bars, but they look like they aren't going to budge. There however is an LED on the bars.")
        elif lightOn is True:
            print("The bars bend and you can get out!!")
            able2GetOut = True
    elif whatToDo.lower() == "look poster":
        print("You look closer, and it looks like there is a small lock.")
    elif whatToDo.lower() in "pick lock":
        if crowbarTaken is True:
            print("You use the crowbar to pick the lock.\n Something lights up.")
            lightOn = True
        else:
            print("You try to use your fingernails but the lock wont budge.")
    elif whatToDo.lower() in "look":
        if lightOn is True:
            print("You are in a room, with a PSF poster. \nThere is a light on the bars!!")
        else:
            print("You are in a room, with a PSF poster. \nDidn't I already say this?")
    elif whatToDo.lower() in "crawl":
        if able2GetOut is True:
            print("You crawl out and now are out of that room!... But...")
            print("SyntaxError: unfinished program, check back later") #delete when room2 finished
            runpy.run_path(path_name="room2.py")
