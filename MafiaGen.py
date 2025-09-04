import random
import os

#GLOBAL
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

print("Welcome GM! Here is the roles sheet!\n")
GmSheet()

