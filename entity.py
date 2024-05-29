'''
This module contains a bunch of data about the types of entities in the
game, as well as an Entity class, 'entity' referring to any object,
item, or creature in the game.
'''


typedata = {
    'object': " You might be able to interact with this, but you won't"
    "be able to move it. ",
    'item': " You could pick this up if you tried, it might be useful.",
    'creature': " This thing is alive. "
}

entitydata = {
    'raygun':
        {
        'id':'a',
        'desc':"an old-style raygun, these haven't been in circulation for "
            "decades.\n Although outdated, they remain a reliable option for "
            "your alien-slaying needs.",
        'type':'item'
        },
    'abomination':
        {
        'id':'b',
        'desc':"a truly horrific monster.\n Your eyes don't know where to "
            "begin when processing this creature.\n Its melted flesh, covered "
            "in some strange mixture of blood and placenta;\n its "
            "deformed face, mouth uncontrollably agape, tracing abn unsettling "
            "smile from ear to ear,\n just barely indicative that this "
            "freak child of demented experimentation was once human.\n"
            " You can't stand to look at this thing for very long.",
        'type':'creature'
        },
    'terminal':
        {
        'id':'c',
        'desc':"a computer terminal, probably containing all kinds of data "
            "about the ship. \n you might be able to make use of some of it.",
        'type':'object'
        },
    'security door':
        {
        'id':'d',
        'desc':"an enormously thick door."
        "\n If you had the right keycard, you might be "
            "able to open it.",
        'type':'object'
        },
    'keycard':
        {
        'id':'e',
        'desc':" a keycard with high-level security clearance.",
        'type':'item'
        },
}


class Entity():
    '''
    Class for every object, item, or creature in the game
    '''
    def __init__(self, startpos, name):
        self.position = startpos
        self.type = entitydata[name]['type']
        self.name = name

    def inspect(self):
        msg = " As you peer closer, you see "
        msg = msg + (entitydata[self.name]['desc']) + '\n' +\
              (typedata[self.type])
        return msg
    
    def func(self, entitylist, playerpos):
        if self.name == ('raygun'):
            if self.destroy(entitylist, 'abomination', playerpos):
                print (" You zap the abomination, reducing it to a pile of"
                       " red goo.\n Sifting through the goo in search of "
                       "anything of value, a keycard emerges.")
                entitylist.append(Entity(playerpos, 'keycard'))
        elif self.name == 'terminal':
            self.printmap()

    def destroy(self, entitylist, target, playerpos):
        targetfound = False
        for entity in entitylist:
            if target == entity.name and entity.position == playerpos:
                entitylist.remove(entity)
                targetfound = True
        return targetfound

    def printmap(self):
        print(" The green text on the screen of the terminal lights up, and"+\
              " a line of complete gibberish appears. You hit 'enter' and "+\
              "the following appears:\n")
        file = open('mapfile.txt','r')
        print(file.read())