'''
This module contains a bunch of data for the map, including the layout
and a bunch of room descriptions.
'''


maplayout = [
    ['0','4','1'],
    ['5','0','5'],
    ['2','4','3']
    ]

tiletypes = {
    '0':{
        'exits':['s','e'],
        'desc':' Cold steel walls form a cube around you.\n'+\
            ' There are doorways to the South and East.'
    },
    '1':{
        'exits':['s','w'],
        'desc':' Cold steel walls form a cube around you.\n'+\
            ' There are doorways to the South and West.'
    },
    '2':{
        'exits':['n','e'],
        'desc':' Cold steel walls form a cube around you.\n'+\
            ' There are doorways to the North and East.'
    },
    '3':{
        'exits':['n','w'],
        'desc':' Cold steel walls form a cube around you.\n'+\
            ' There are doorways to the North and West.'
    },
    '4':{
        'exits':['e','w'],
        'desc': ' A vast hallway extends from the East to West\n'+\
            ' The pattern of the textured steel flooring screws '+\
            'with your eyes.'
    },
    '5':{
        'exits':['n','s'],
        'desc':' A vast hallway extends from the North to South\n'+\
            ' The pattern of the textured steel flooring screws '+\
            'with your eyes.'
    },
}