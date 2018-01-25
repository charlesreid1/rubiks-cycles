import re
import numpy as np
from pprint import pprint

"""
Permutations

Functions for finding rotational permtuations.

This scipt supports countcycles.py
by finding all rotational permutations
of a given move sequence to help eliminate 
duplicates. 
"""

def main():
    captains, seq2captains = algorithm_m_clean(2)

    print("List of all length-2 permutations generated:")
    pprint(list(seq2captains.keys()))
    print("Total: %d"%(len(seq2captains.keys())))
    print("")
    print("List of rotationally unique length-2 permutations:")
    pprint(list(captains))
    print("Total: %d"%(len(captains)))


def algorithm_m_clean(n):
    """
    Knuth's Algorithm M for permutation generation,
    cleaned up to remove duplicate rotations.

    This generates the rotations:
    constructs a map of each sequence
    to its captain.
    """
    sequence_to_captain = {}
    captains = set()

    for perm in algorithm_m(n):
        # get all possible rotations of this 
        # move sequence (permutation)
        rotations = get_rotations(perm)

        # important: 
        # sort rotations in reverse lexicographic order,
        # extract captains after they are returned
        captain = rotations[0]

        # for each rotation,
        # set its captain.
        for rot in rotations:
            if rot not in sequence_to_captain:
                sequence_to_captain[rot] = captain
                captains.add(captain)

    captains = list(captains)
    return captains, sequence_to_captain



def algorithm_m(n):
    """
    Knuth's Algorithm M for permutation generation,
    via AOCP Volume 4 Fascile 2.
    This is a generator that returns permtuations 
    generated using the variable-radix method. 

    This generates ALL permutations.
    Many of these are rotations of one another,
    so use the get_rotations() function
    below to get all rotations of a given
    permutation.

    A better way to do this is to clean up 
    algorithm M so it only generates
    the original, plus the 24 rotations
    each in turn... 
    
    ...but that makes my brain hurt.
    """
    moves = ['U', 'D', 'B', 'F', 'L', 'R',
             'Uw','Dw','Bw','Fw','Lw','Rw',
             '2U','2D','2B','2F','2L','2R', ]

    # M1 - Initialize
    a = np.zeros(n,)
    m = np.ones(n,)*len(moves)

    j = n-1

    nvisits = 0
    while True:

        # M2 - visit
        move_sequence = " ".join([ moves[int(aj)] for aj in a])
        yield move_sequence 

        nvisits += 1

        # M3 - prepare to +1
        j = n-1

        # M4 - carry
        while( a[j] == m[j]-1):
            a[j] = 0
            j = j-1
        
        # M5 - increase unless done
        if(j<0):
            break
        else:
            a[j] = a[j] + 1


def get_rotations(sequence):
    """
    Given a cube sequence,
    find all 24 rotations of it.

    Need to fix this so it doesn't
    necessarily expect the U-first case.
    """
    cubes = ["UBFLRD",
             "UFBRLD",
             "ULRFBD",
             "URLBFD",
             "DFBLRU",
             "DBFRLU",
             "DLRBFU",
             "DRLFBU",
             "LUDBFR",
             "LDUFBR",
             "LFBUDR",
             "LBFDUR",
             "RUDFBL",
             "RDUBFL",
             "RBFUDL",
             "RFBDUL",
             "FUDLRB",
             "FDURLB",
             "FRLUDB",
             "FLRDUB",
             "BUDRLF",
             "BDULRF",
             "BLRUDF",
             "BRLDUF"]

    results = set()

    results.add(sequence)

    cubestart = {'U': 0,
                 'D': 4,
                 'L': 8,
                 'R':12,
                 'F':16,
                 'B':20}

    # Split the sequence into its moves,
    # and use the first cube configuration to map
    # moves to numbers.
    moves = sequence.split(" ")

    move0 = moves[0]

    first_move = move0[0]
    if(move0[0]=='2'):
        first_move = move0[1]

    first_move_index = cubestart[first_move]

    # Now run through all other cube configurations,
    # and map the numbers back to moves.
    move_numbers = []
    for move in moves:
        if(move[0]=='2'):
            move_numbers.append(cubes[first_move_index].index(move[1]))
        else:
            move_numbers.append(cubes[first_move_index].index(move[0]))

    for i in range(len(cubes)):
        cube = cubes[i]
        xmoves = []
        for j, move_number in enumerate(move_numbers):
            old_face = cubes[first_move_index][move_number]
            new_face = cube[move_number]

            old_move = moves[j]
            new_move = re.sub(old_face,new_face,old_move)

            xmoves.append(new_move)

        # Assemble the moves to a string
        xmove = " ".join(xmoves)

        results.add(xmove)

    # reversed is slightly more convenient, 
    # starts with U instead of B
    return list(reversed(sorted(list(results))))

def test_rotations():
    # Focusing on sequences of length 3 and up
    # Focusing on right hand sequences only
    # 
    # 12 possible right hand moves,
    # 3^12 total possibilities,
    # 24 rotational equivalents, 
    # 22,000 total unique 3-move sequences
    
    moves = ['U', 'D', 'B', 'F', 'L', 'R',
             'Uw','Dw','Bw','Fw','Lw','Rw',
             '2U','2D','2B','2F','2L','2R', ]

    sequences = []
    move1 = 'L'
    for move2 in ['D']:#moves:
        for move3 in moves:
            seq = " ".join([move1,move2,move3])
            sequences.append(seq)

    print("Length of sequence: %d"%(len(sequences)))

    for sequence in sequences:
        print(get_rotations(sequence))



if __name__=="__main__":
    main()

