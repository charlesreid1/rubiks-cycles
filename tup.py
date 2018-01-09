from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from pprint import pprint
import os, re


def main():
    '''
    # Corners:
    # Clockwise, starting from U or D,
    # each corner consists of three faces
    Corners = ((13,33,20),(16,49,36),( 4,65,52),( 1,17,68),
               (81,32,45),(84,48,61),(96,64,77),(93,80,29))

    # Centers:
    Fcenter = (38,39,43,42)
    Rcenter = (54,55,59,58)
    Bcenter = (70,71,75,74)
    Lcenter = (22,23,27,26)
    Ucenter = ( 6, 7,11,10)
    Dcenter = (86,87,91,90)

    # Dedges:
    Uface = ((14,34),(15,35),(12,50),( 8,51),( 3,66), (2,67),( 5,18),( 9,19))
    Dface = ((82,46),(83,47),(88,62),(92,63),(95,78),(94,79),(89,30),(85,31))
    Sface = ((37,24),(41,28),(53,40),(57,44),(69,56),(73,60),(21,72),(25,76))
    '''

    # Use the built-in tuple representation
    # (UU...UULL...LLFF... etc...)
    # Now we just need a color map and we have an integer tuple.

    face2col = {}
    face2col['U'] = 0
    face2col['D'] = 1
    face2col['F'] = 2
    face2col['B'] = 3
    face2col['R'] = 4
    face2col['L'] = 5

    

    # ----------------------------
    print("-"*40)
    print("Move Sequence: R U R' U'")

    r = get_cube()

    cube0 = list([face2col[j] for i,j in enumerate(r.state) if(i>0) ])

    r.rotate('R')
    r.rotate('U')
    r.rotate('R\'')
    r.rotate('U\'')

    cube1 = list([face2col[j] for i,j in enumerate(r.state) if(i>0) ])

    print(cube0)
    print(cube1)
    m = []
    for c0,c1 in zip(cube0,cube1):
        if(c0==c1):
            m.append(0)
        else:
            m.append(1)
    print(m)
    print(sum(m))


    # ------------------------------
    print("-"*40)
    print("Move Sequence: R U")


    r = get_cube()

    cube0 = list([face2col[j] for i,j in enumerate(r.state) if(i>0) ])

    r.rotate('R')
    r.rotate('U')

    cube1 = list([face2col[j] for i,j in enumerate(r.state) if(i>0) ])

    print(cube0)
    print(cube1)
    m = []
    for c0,c1 in zip(cube0,cube1):
        if(c0==c1):
            m.append(0)
        else:
            m.append(1)
    print(m)
    print(sum(m))


def get_cube():
    """
    Get a 4x4 Rubiks Cube.
    """
    order = 'URFDLB'
    cube = RubiksCube444(solved_4x4x4, order)
    return cube


if __name__=="__main__":
    main()

