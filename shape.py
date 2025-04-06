import math

def rotation(length,angle):
    angle %= 90
    angle = angle*math.pi/180
    length = math.sin(angle)*length + math.cos(angle)*length
    return length

def scale(length,old_distance,new_distance):
    length *= old_distance/new_distance
    return length


""""
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7
o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7  o7

                       ----------------------
                      |                      |
                      |         o7           |
                      |                      |
"""