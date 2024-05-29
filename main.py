import command

'''
This program contains the main game loop for Space Salvage
Space Salvage is a text-based RPG
'''

def startsequence():
    print('.\n')
    startgame = open('startgame.txt', 'r')
    print(startgame.read())
    startgame.close()
    input("Press enter to continue...\n")
    command.help()

startsequence()

run = True
while run:
    print('----------------------------------------')
    command.get_input()
