import random

options = ["R", "P", "S"]
name = input("Enter your name: \n")
user_choice = input(f'''Pick a choice between : {options}
>>Enter your choice here: ''')


while user_choice.upper() not in options:
    print(f"""Sorry {name}, but you chose the wrong option ❌ ⚠️.
Please choose amongst the provided options: {options}.\n
Let's try again.\n""")
    user_choice = input(f'''Pick a choice between : {options}\n
>>Enter your choice here: ''')
else:
   if user_choice.upper() in options:
       print(f"\nWelcome {name.title()}.")
player = user_choice.upper()
cpu_choice = random.choice(options)
cpu = cpu_choice.upper()
print(f"\nYour choice was {player} ")
print(f"The computer's choice was {cpu}.")
print(f"\nPlayer ({player}) : CPU ({cpu})")

while player == cpu:
    print("It's a tie 🤝 !!!\n")
    user_choice = input(f'''Pick a choice between : {options} \n
>Enter your choice here: ''')
else:

    if (cpu == "R" and player == "S") or \
    (cpu == "S" and player == "P") or \
    (cpu =="P" and player == "R"):
        print("\nComputer 💻 Won 💥 !!!")

    elif (player == "R" and cpu == "S") or \
    (player == "S" and cpu == "P") or \
    (player == "P" and cpu == "R"):
        print(f"\n{name.title()} Player 🕺 Won 🔥 !!!")




