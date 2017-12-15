# PyChat 2K17

import random

bot_name = "Guy"

def start():
    print("HHHHHHHHH     HHHHHHHHH                   lllllll lllllll")
    print("H:::::::H     H:::::::H                   l:::::l l:::::l")
    print("H:::::::H     H:::::::H                   l:::::l l:::::l")
    print("HH::::::H     H::::::HH                   l:::::l l:::::l")
    print("  H:::::H     H:::::H      eeeeeeeeeeee    l::::l  l::::l    ooooooooooo")
    print("  H:::::H     H:::::H    ee::::::::::::ee  l::::l  l::::l  oo:::::::::::oo")
    print("  H::::::HHHHH::::::H   e::::::eeeee:::::eel::::l  l::::l o:::::::::::::::o")
    print("  H:::::::::::::::::H  e::::::e     e:::::el::::l  l::::l o:::::ooooo:::::o")
    print("  H:::::::::::::::::H  e:::::::eeeee::::::el::::l  l::::l o::::o     o::::o")
    print("  H::::::HHHHH::::::H  e:::::::::::::::::e l::::l  l::::l o::::o     o::::o")
    print("  H:::::H     H:::::H  e::::::eeeeeeeeeee  l::::l  l::::l o::::o     o::::o")
    print("  H:::::H     H:::::H  e:::::::e           l::::l  l::::l o::::o     o::::o")
    print("HH::::::H     H::::::HHe::::::::e         l::::::ll::::::lo:::::ooooo:::::o")
    print("H:::::::H     H:::::::H e::::::::eeeeeeee l::::::ll::::::lo:::::::::::::::o")
    print("H:::::::H     H:::::::H  ee:::::::::::::e l::::::ll::::::l oo:::::::::::oo ")
    print("HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeee llllllllllllllll   ooooooooooo   ")
   


def end():
    pass

def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()

        if answer in ["y" , "yes", "yup"]:
            return True
        elif answer in ["n", "no", "nope"]:
            return False
   
def has_keyword(statement, keywords):
    for word in keywords:
        if word in statement or word == statement: 
            return True

    return False

def get_random_response():
    responses = [

                 "Uh, huh.",
                 "Oh, that's interesting",
                 "Do you really think so?",
                 "Ye boi",
                 "Da ting go skraa",
                 "Pa-pa-ka-ka-ka",
                 "Skidiki-pa-pa"

                 ]

    return random.choice(responses)

def get_response(statement):
    statement = statement.lower()    
    
    family_words = [" mother ", " father ", " brothe ", " sister "]
    teacher_words = [" cooper "]
    LoL = [" bronze 5 "]    
    if has_keyword(statement, family_words):
        response = "Tell me more about your family."
    elif has_keyword(statement, teacher_words):
        response = "I hear Mr. Cooper's class is really fun."
    elif has_keyword(statement, LoL):
        response = "git gud scrub"        
    else:
        response = get_random_response()

    return response

def play():
    talking = True         

    print("I'm" + " " + bot_name + ". What's your name?")
    user_name = input()
    print(bot_name + ": " + user_name + ", that's a cool name.") 
    
    while talking:
        statement = input(user_name +": ")       
        
        if statement == "Goodbye":
            talking = False
        else:
            response = get_response(statement)
            print(bot_name + ": " + response)

    print("Goodbye. It was nice talking to you.")

start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to chat again?")

end()
