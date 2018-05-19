print ("Welcome to the Fanfiction Generator!!!")
print (" First, enter the names that you would like to use. Then, choose your template. And finally, fill in the blanks that we give you.")
name1 = input("FIRST PERSON:")
name2 = input("SECOND PERSON:")
template = input("WHAT TEMPLATE?")
if template == ("pg-1"):
    action1 = input("Please give me an action word.")
    descriptive1 = input("Please give me a decriptive word.")
    noun1 = input("Please give me a noun.")
    game1 = input("Please give me a game.")
    descriptive2 = input("Please give me another descriptive word.")
    noun2 = input("And finally, give me one more noun.")
    storystartready = input("Okay, are you ready to read your story? Y/N:")
    if storystartready == ("y"):
        print("Once apon a time, in a far away land, " + name1 + " was playing " + game1 + " with his pet " + noun1 + ".")
    
