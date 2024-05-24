'''
This module contains a bunch of data about the types of entities in the
game, as well as an Entity class, 'entity' referring to any object,
item, or creature in the game.
'''


typedata = {
    'object': " You might be able to interact with this, but you won't"+\
    "be able to move it. ",
    'item': " You could pick this up if you tried, it might be useful.",
    'creature': " This thing is alive. "
}

entitydata = {
    'raygun':
        {
        'id':'a',
        'desc':"an old-style raygun, these haven't been in circulation for "+\
            "decades.\n Although outdated, they remain a reliable option for "+\
            "your alien-slaying needs.",
        'type':'item'
        },
    'abomination':
        {
        'id':'b',
        'desc':"a truly horrific monster.\n Your eyes don't know where to "+\
            "begin when processing this creature.\n Its melted flesh, covered "+\
            "in some strange mixture of blood and placenta;\n its "+\
            "deformed face, mouth uncontrollably agape, tracing a disturbing "+\
            "smile from neck to ear,\n just barely indicative that this "+\
            "freak child of demented experimentation was once human.\n"+\
            " You can't stand to look at this thing for very long.",
        'type':'creature'
        },
    'terminal':
        {
        'id':'c',
        'desc':"a computer terminal, probably containing all kinds of data "+\
            "about the ship. \n If you had the right keycard, you might be "+\
            "able to make use of it.",
        'type':'object'
        }
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