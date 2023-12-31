#Magic 8-Ball
# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

# magic8.py
import random

# User Name Variable
Name_user = input("What is your name? ")

# Question variable
Yes_no_question = input("Is it a 'Yes' or 'No' question you’d like to ask the Magic 8-Ball, " + Name_user + ": ")

def if_question():
    if Yes_no_question.lower() == "yes":
        return input("What is your question? ")
    else:
        return "Ask again"

user_question = if_question()

print(Name_user + " asks: " + user_question)

random_number = random.randint(1, 9)
print(random_number)

# core logic Control flow if / elif / else
if random_number == 1:
    print("Yes - definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good")
elif random_number == 9:
    print("Very doubtful")
else:
    print("Error")