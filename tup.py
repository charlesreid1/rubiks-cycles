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

    # test
    sequences = ['U U','D D','R R','L L','F F','B B']

    # study
    sequences = ['U R','R U','Uw Rw','Uw R']

    for seq in sequences:
        print("-"*40)
        print(seq)

        factors = factor_rotation(seq)

        factor_lengths = set([len(j) for j in factors])
        print("Factor sizes: %s"%(factor_lengths))
        print("Factors: %s"%(factors))
        print("Least common multiple: %d"%( ilcm(*factor_lengths) ))



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
        for m in rotmap:
            # shift item at index m[0] to item at index m[1]
            cube1[cube_prior.index(m[0])] = m[1]

        cube_prior = cube1.copy()

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


if __name__=="__main__":
    main()

