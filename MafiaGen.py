import random
import os

#To Do:
#
#
#
#
#
#
# 
# 
# GLOBAL
Maf_Ratio = 4
Twins_YN = 0
def Clr_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


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

if player_num >=7:
    while True:
        try:
            If_Twins = str(input("Do you want to play with the TWINS role? Y/N?     "))
            if If_Twins == ("N"):
                Twins_YN = int(0)
                break
            elif If_Twins == ("Y"):
                Twins_YN = int(1)
                break
            else:
                print("Invalid Input")
        except:
            print("Invalid Input")

players = []
for i in range(player_num):
    name = input(f"Enter name for player {i+1}: ")
    players.append(name)


roles = []

mafia_count = max(1, player_num // Maf_Ratio)
roles.extend(["Mafia"] * mafia_count)

if Twins_YN == 1:
    roles.extend(["Twins"] * 2)

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

def rolesheet():
    print("How the game works:\n\nPhases:\n\nDay phase: All players discuss and then vote on who they suspect is either Mafia or Evil.\nThe voted palyer is killed.\n\nNight phase:\nSpecial roles (Mafia, Detective, Doctor, ect) secretly act. The host is tasked with revealing what\nhappened in the morning.\n\n\nRoles and what they do:\n\n\nMafia: Secretly chooses who to kill at night!\n\nDetective: Investigates someone each night. if they tried to kill someone the detective finds clues!\n\nDoctor: Protects someone from death each night, they can attempt to protect themselves ONCE.\n\nSerial Killer: Must kill someone every two nights\n\nJester: Get voted out by the town to win the whole game!\n\nVigilante: A player of the town team that can kill once at night. If the player chosen wasn't evil they will die of guilt the next night.\n\nTwins: two players, if one dies the other dies with them.")
    os.system('pause')



while True:
    try:
        Clr_terminal()
        choice = input("Welcome GM! Here is your operation panel!\n\nTo print the whole player list Enter 1\nTo Reveal all players Enter 2\nTo display rules & roles Enter 3\nTo quit the program enter QUIT\n\nEnter command:  ")
        if choice == "1":
            print("\n")
            GmSheet()
            os.system('pause')
            Clr_terminal()
        if choice == "2":
            Clr_terminal()
            print("\n")
            Reveal()
            Clr_terminal()
        if choice == "3":
            Clr_terminal()
            rolesheet()
            Clr_terminal()
        if choice == "QUIT":
            Clr_terminal()
            print("Game Concluded, Thanks for playing!")
            os.system('pause')
            break
    except ValueError:
        Clr_terminal()
        print("Error! Invalid Value!")

