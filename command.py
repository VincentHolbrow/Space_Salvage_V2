'''
This module contains a function to handle input and several player
action functions.
It basically handles everything the player can control.
'''

import maph
import entity


movedirs = {'n':(0,-1),'s':(0,1),'e':(1,0),'w':(-1,0)}
playerpos = 0,0
inventory = []
entitylist = [
    entity.Entity((2,0),'abomination'),
    entity.Entity((0,2), 'raygun'),
    entity.Entity((0,1), 'terminal')
    ]


def get_input():
    '''
    This function takes input and then triggers player actions
    based on the given input.
    '''
    tile = maph.maplayout[playerpos[1]][playerpos[0]]
    print (maph.tiletypes[tile]['desc'])    
    for entity in entitylist:
        if entity.position == playerpos:
            print (' You see a ' + entity.name)

    action = input(' What would you like to do?\n')
    try:
        if action[0] in movedirs:
            move(action[0])

        if action[0] == 'i':
            obj = input(' Inspect what?\n')
            inspect(obj)
        if action[0] == 'g':
            obj = input(' Grab what?\n')
            grab(obj)
        if action[0] == 'u':
            obj = input(' Use what?\n')
            use(obj)
    except:
        print(' Error: Invalid action.\n')


def move(movedir):
    '''
    This function changes the player position, if possible.
    '''
    global playerpos
    tile = maph.maplayout[playerpos[1]][playerpos[0]]
    if movedir in maph.tiletypes[tile]['exits']:
        playerpos = playerpos[0]+movedirs[movedir][0], \
            playerpos[1]+movedirs[movedir][1]
    else:
        print("You can't go that way.")


def inspect(obj):
    '''
    This functions prints a more detailed description of a given object
    in the same room as the player.
    '''
    objfound = False
    for entity in entitylist:
        if entity.name == obj:
            print(entity.inspect())
            objfound = True
    if not objfound:
        print(" That doesn't exist in this room.")


def grab(obj):
    '''
    This function removes an entity from the entity list and adds it to
    the inventory, if the entity type is 'item'
    '''
    global entitylist
    objfound = False
    for entity in entitylist:
        if entity.name == obj and entity.position == playerpos:
            objfound = True
            if entity.type == 'item':
                inventory.append(entity)
                entitylist.remove(entity)
                print(" You grab the "+ entity.name)
            else:
                print(" That's not an item you can grab.")
    if not objfound:
        print(" That doesn't exist in this room.")


    def use(obj):
        objfound = False
        for entity in inventory:
            if entity.name == obj and not objfound:
                entity.func()
                objfound = True
        for entity in entitylist:
            if entity.name == obj and not objfound and entity.pos == \
            playerpos:
                entity.func()
                objfound = True