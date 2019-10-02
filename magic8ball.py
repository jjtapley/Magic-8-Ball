#Magic 8 ball

import random

#create list of possible fortune answers:

fortunes = ["It is certain", 
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]

#create game function that starts the 8 ball
def game():
    print ("I am the Magic 8 Ball - teller of fortunes.")
    print ("Ask me a question and I will reveal your answer")
    question = input ("What would you like to know about the future? ")

    print(" ")
    print("Looking into it..... ")
    print(" ")

#function that randomly chooses the fortune
def random_fortunes():
    random_fortunes = random.choice(fortunes)
    return random_fortunes

game()
print(random_fortunes())
play_again = input("Would you like to play again? y/n ")
while play_again == "y":
    game()
    print(random_fortunes())
    play_again = input("Would you like to play again? y/n ")
else:
    print ("Thank you for visiting The Magic 8 Ball - come back soon for more fortunes")


    
    
