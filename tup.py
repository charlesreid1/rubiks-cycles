from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from pprint import pprint
import os, re
import time
from sympy.core.numbers import ilcm

def get_cube():
    """
    Get a 4x4 Rubiks Cube.
    """
    order = 'URFDLB'
    cube = RubiksCube444(solved_4x4x4, order)
    return cube


def main():
    # Built in tuple representation has the problem
    # that it treats all colors as interchangeable
    # We need a tuple that treats each of the faces
    # or pieces as separate, independent, but connected
    # units.
    sequences = ['U R','Uw Rw','U 2R D F']
    for seq in sequences:
        factors = factor_rotation(seq)
        print("-"*40)
        print(seq)
        print("Factor sizes: %s"%(set([len(j) for j in factors])))
        print("Factors: %s"%(factors))


def get_face2col():
    face2col = {}
    face2col['U'] = 0
    face2col['D'] = 1
    face2col['F'] = 2
    face2col['B'] = 3
    face2col['R'] = 4
    face2col['L'] = 5
    return face2col



def factor_rotation(rot):
    """
    For a given rotation, factor the resulting permutation.
    """
    cube0 = list(range(1,96+1))
    cube1 = cube0.copy()
    r = get_cube()
    sequence = []
    for move in rot.split(" "):
        rotmap = r.rotation_map(move)
        for m in rotmap:
            cube1[cube0.index(m[0])] = m[1]

    factors = factor_permutation(cube0,cube1)
    return factors



def factor_permutation(perm_top,perm_bot):
    """
    Factor a permutation into its lowest terms
    """
    MAX = 96
    # Need a way to also mark them as used... bit vector
    used_vector = [0,]*len(perm_top)

    i = 0
    start = perm_top[0]
    used_vector[0] = 1

    factors = []

    # If we still have values to pick out:
    while(0 in used_vector):

        factor = []

        while(True):
            used_vector[i] = 1
            leader = perm_top[i]
            follower = perm_bot[i]

            # Why is this B?
            i = perm_top.index(follower)
            while(used_vector[i]==1):
                i += 1
                if(i>=MAX):
                    break

            if(i>=MAX):
                break
            elif(follower==start):
                break
            else:
                factor.append(follower)

        # add start to end
        factor.append(start)

        factors.append(factor)
        try:
            #import pdb; pdb.set_trace()
            i = used_vector.index(0)
            start = perm_top[i]
        except ValueError:
            break

    factorsize = set()
    check = 0
    for factor in factors:
        factorsize.add(len(factor))
        check += len(factor)
    return factors






def do_rotation(rot):

    face2col = get_face2col()

    print("-"*40)
    print("Move Sequence: %s"%(rot))

    r = get_cube()

    cube0 = list([face2col[j] for i,j in enumerate(r.state) if(i>0) ])

    for move in rot.split(" "):
        r.rotate(move)

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





if __name__=="__main__":
    main()

