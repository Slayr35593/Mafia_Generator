import random
import os

#To Do:
#Impliment twin system
#GM control screen
#Reprint player list if confusion
#
#
#
# 
# 
# GLOBAL
Maf_Ratio = 4

def Clr_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    try:
        If_Twins = str(input("Do you want to play with the TWINS role? Y/N?     "))
        if If_Twins == ("N"):
            Twins_YN = False
            break
        elif If_Twins == ("Y"):
            Twins_YN = True
            break
        else:
            print("Invalid Input")
    except:
        print("Invalid Input")


Clr_terminal()


Special_Roles = {
    5: ["Detective"],
    6: ["Doctor"],
    7: ["Jester"],
    9: ["Vigilante"],
    13: ["Serial Killer"],
}

while True:
    try:
        player_num = int(input("Welcome to Mafia! Enter a player count between 5-30 players! "))
        if 5 <= player_num <= 30:
            break
        else:
            print("Enter valid number between 5-30 players")
    except ValueError:
        print("Not a valid number, try again!")

players = []
for i in range(player_num):
    name = input(f"Enter name for player {i+1}: ")
    players.append(name)


roles = []

mafia_count = max(1, player_num // Maf_Ratio)
roles.extend(["Mafia"] * mafia_count)

for count, role_list in Special_Roles.items():
    if player_num >= count:
        roles.extend(role_list)

while len(roles) < player_num:
    roles.append("Innocent")


random.shuffle(roles)
player_roles = dict(zip(players, roles))


def GmSheet():
    for player, role in player_roles.items():
        print(f"{player} is {role}")

print("\nAll roles assigned!\n")
def Reveal():
    for player, role in player_roles.items():
        Clr_terminal()
        print(f"{player} is... (press any key to reveal)")
        os.system('pause')
        print(role)
        os.system('pause')
        Clr_terminal()

print("Good luck, and have fun!")

os.system('pause')
Clr_terminal()


while True:
    try:
        choice = input("Welcome GM! Here is your operation panel!\n\nTo print the whole player list Enter 1\nTo Reveal all players Enter 2\nTo quit the program enter QUIT\n\nEnter command:  ")
        if choice == "1":
            print("\n")
            GmSheet()
            os.system('pause')
            Clr_terminal()
        if choice == "2":
            print("\n")
            Reveal()
            Clr_terminal()
        if choice == "QUIT":
            Clr_terminal()
            print("Game Concluded, Thanks for playing!")
            os.system('pause')
            break
    except ValueError:
        Clr_terminal()
        print("Error! Invalid Value!")
