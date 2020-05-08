print("You are in a new room. There is a piece of paper here. Would you like to read it y/n? ")
hi = input("Type: ")
hi = hi.lower()
def readPaper():
  print('''The paper reads:
  "Hello Manakivo, 
  
  I know that I will be long gone before you read this but I just wanted to tell you that "
  The ink is smudged here. After the smudge, it reads:
  "I hope that this letter finds you. I cannot escape. I cannot escape."
  ''')
if hi == "y":
    readPaper()
print("Work In Progress. this is Unfinished.")
