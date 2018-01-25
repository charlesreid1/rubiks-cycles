from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from pprint import pprint
import os, re
import time
from sympy.core.numbers import ilcm

"""
Sequence Order

This file defines a method to compute
the order of a given sequence.

Charles Reid
January 2018
"""

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

    ## test
    #sequences = ['U U','D D','R R','L L','F F','B B']
    #sequences = ['U U U','D D D','R R R','L L L','F F F','B B B']

    # study
    sequences = ['R','U R U\' R\'','U R']
    #sequences = ['U','D','L','R','F','B']
    #sequences = ["U R U' R'"] 

    c = get_cube()
    center_squares = []
    for side_key in c.sides:
        side = c.sides[side_key]
        center_squares.append(set(side.center_pos))

    for seq in sequences:
        print("-"*40)
        print(seq)

        # do it.
        factors_list = factor_rotation(seq)
        
        factors_len = set()
        for factor in factors_list:
            if(True or set(factor) not in center_squares):
                factors_len.add(len(factor))

        print("Factor sizes: %s"%(factors_len))
        print("Factors:")
        print_factors(factors_list)
        print("Least common multiple: %d"%( ilcm(*factors_len) ))



def factor_rotation(rot):
    """
    For a given rotation, factor the resulting permutation.
    """
    cube0 = list(range(1,96+1))
    cube1 = cube0.copy()
    cube_prior = cube0.copy()
    r = get_cube()

    sequence = []

    # Needed to fix this to use the prior cube,
    # otherwise multiple move sequences were broken.
    for c,move in enumerate(rot.split(" ")):
        rotmap = r.rotation_map(move)

        ### # Print rotation map
        ### print(">"*40)
        ### print(move+":")
        ### print("-"*40)
        ### pprint(rotmap)
        ### print("<"*40)

        for m in rotmap:
            # shift item at index m[0] to item at index m[1]
            cube1[cube_prior.index(m[0])] = m[1]

        cube_prior = cube1.copy()

    print("\n")
    print_cube(cube0)
    print("\n")
    print_cube(cube1)
    print("\n")
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


def print_cube(cube):
    #print("(" + " ".join("%02d"%(j) for j in cube) + ")")
    print("(" + " ".join(str(j) for j in cube) + ")")


def print_factors(factors_list):
    ones_list = []
    for factor in factors_list:
        if(len(factor)>1):
            # Length > 1: print the factor separately
            print(factor)
        else:
            # Length==1: collect and print together
            ones_list.append(factor[0])
    print("Independent Pieces: %s"%(ones_list))


if __name__=="__main__":
    main()

