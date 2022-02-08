from collections import namedtuple

Coord = namedtuple("Coord", "x y")
One = Coord(54, 668)
Two = Coord(54, 596)
Three = Coord(54, 524)
Four = Coord(54, 452)
Five = Coord(54, 380)
Six = Coord(54, 308)
Seven = Coord(54, 236)
Eight = Coord(54, 164)
First = Coord(473, 661)
Second = Coord(473, 587)
Third = Coord(473, 513)
Fourth = Coord(473, 439)
Fifth = Coord(473, 365)
Sixth = Coord(473, 291)
Seventh = Coord(473, 218)
Eightth = Coord(473, 144)
margin = 20


def ingame(position, reference):
    abspos = Coord(reference[0]-position[0], reference[1]-position[1])
    #abspos = tuple(map(sub, reference, position))
    margin = 20
    if ((One.x - margin) <= abspos.x <= (One.x + margin) and (One.y - margin) <= abspos.y <= (One.y + margin)):
        #print("1st")
        return 8
    if ((Two.x - margin) <= abspos.x <= (Two.x + margin) and (Two.y - margin) <= abspos.y <= (Two.y + margin)):
        #print("2nd")
        return 7
    if ((Three.x - margin) <= abspos.x <= (Three.x + margin) and (Three.y - margin) <= abspos.y <= (Three.y + margin)):
        #print("3rd")
        return 6
    if ((Four.x - margin) <= abspos.x <= (Four.x + margin) and (Four.y - margin) <= abspos.y <= (Four.y + margin)):
        #print("4th")
        return 5
    if ((Five.x - margin) <= abspos.x <= (Five.x + margin) and (Five.y - margin) <= abspos.y <= (Five.y + margin)):
        #print("5th")
        return 4
    if ((Six.x - margin) <= abspos.x <= (Six.x + margin) and (Six.y - margin) <= abspos.y <= (Six.y + margin)):
        #print("6th")
        return 3
    if ((Seven.x - margin) <= abspos.x <= (Seven.x + margin) and (Seven.y - margin) <= abspos.y <= (Seven.y + margin)):
        #print("7th")
        return 2
    if ((Eight.x - margin) <= abspos.x <= (Eight.x + margin) and (Eight.y - margin) <= abspos.y <= (Eight.y + margin)):
        #print("8th")
        return 1
    else:
        return 0
    
def postgame(position, reference):
    abspos = Coord(reference[0]-position[0], reference[1]-position[1])
    print (abspos)
    margin = 20
    if ((First.x - margin) <= abspos.x <= (First.x + margin) and (First.y - margin) <= abspos.y <= (First.y + margin)):
        print("1st")
        return 8
    if ((Second.x - margin) <= abspos.x <= (Second.x + margin) and (Second.y - margin) <= abspos.y <= (Second.y + margin)):
        print("2nd")
        return 8
    if ((Third.x - margin) <= abspos.x <= (Third.x + margin) and (Third.y - margin) <= abspos.y <= (Third.y + margin)):
        print("3rd")
        return 6
    if ((Fourth.x - margin) <= abspos.x <= (Fourth.x + margin) and (Fourth.y - margin) <= abspos.y <= (Fourth.y + margin)):
        print("4th")
        return 6
    if ((Fifth.x - margin) <= abspos.x <= (Fifth.x + margin) and (Fifth.y - margin) <= abspos.y <= (Fifth.y + margin)):
        print("5th")
        return 4
    if ((Sixth.x - margin) <= abspos.x <= (Sixth.x + margin) and (Sixth.y - margin) <= abspos.y <= (Sixth.y + margin)):
        print("6th")
        return 4
    if ((Seventh.x - margin) <= abspos.x <= (Seventh.x + margin) and (Seventh.y - margin) <= abspos.y <= (Seventh.y + margin)):
        print("7th")
        return 2
    if ((Eightth.x - margin) <= abspos.x <= (Eightth.x + margin) and (Eightth.y - margin) <= abspos.y <= (Eightth.y + margin)):
        print("8th")
        return 2
    else:
        return 0