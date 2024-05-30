'''
This module contains a bunch of data for the map, including the layout
and a bunch of room descriptions.
'''


maplayout = [
    ['0','4','1'],
    ['5','3',None],
    ['2',None,None]
    ]

tiletypes = {
    '0':{
        'exits':['s','e'],
        'desc':" Cold steel walls form a smooth cube around you.\n"+\
            " Your skiff sits, freshly out of fuel, in the landing bay"+\
            " behind you."+\
            " No turning back now.\n"
            ' There are doors to the South and East.'
    },
    '1':{
        'exits':['w'],
        'desc':' Beds line the walls of this room, and personal'
            " belongings are strewn about carelessly,\n though you hardly"
            " notice. \n What draws your eye is a central mound of corpses"
            " and viscera. \n They appear to be the bodies of former "
            "crewmates.\n"
            ' There is an exit to the West.'
    },
    '2':{
        'exits':['n'],
        'desc':' This cubic room is lined with rows of gun racks.\n'
            ' It seems that the scientists aboard this ship took '
            'security very seriously.\n Most of the equipment is '
            'completely melted, but some of it appears functional.\n'
            ' There is an exit to the North.'
    },
    '3':{
        'exits':[],
        'desc':' A reinforced glass canopy grants view of Station XT-16,'
        ' your destination.\n The various levers, dials, and switches are'
        ' entirely familiar;\n the control scheme is identical to that of'
        " your skiff.\n Piloting this ship shouldn't be an issue."

    },
    '4':{
        'exits':['e','w'],
        'desc': ' A vast empty hallway extends from the East to West,'
            " with a heavy-duty security door about halfway down.\n"
            ' The texture of the dimly lit steel flooring screws '
            'with your eyes.'
    },
    '5':{
        'exits':['n','s'],
        'desc':' You find yourself in an atrium of sorts, surrounded'
            ' by blinking lights and CRT monitors.\n A central terminal '
            'attached to a keyboard draws your attention.\n'
            ' There are doors to the North and South.'
    },
}