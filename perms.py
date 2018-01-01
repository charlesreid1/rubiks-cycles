from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
import re
import numpy as np


def main():
    algorithm_m()


def algorithm_m():
    """
    Knuth's Algorithm M for permutation generation,
    via AOCP Volume 4 Fascile 2
    """
    moves = ['U', 'D', 'B', 'F', 'L', 'R']

    n = 3

    # M1 - Initialize
    a = np.zeros(n,)
    m = np.ones(n,)*n

    j = n-1

    nvisits = 0
    while True:

        # M2 - visit
        ## print numbered tuple
        #print(" ".join([ str(int(aj)) for aj in a]))
        # print move sequence
        print(" ".join([ moves[int(aj)] for aj in a]))
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

    print("Visited %d permutations"%(nvisits))


def test_rotations():
    # Focusing on sequences of length 3 and up
    # Focusing on right hand sequences only
    # 
    # 12 possible right hand moves,
    # 3^12 total possibilities,
    # 24 rotational equivalents, 
    # 22,000 total unique 3-move sequences
    
    moves = ['U', 'D', 'B', 'F', 'L', 'R',
             'Uw','Dw','Bw','Fw','Lw','Rw']

    sequences = []
    move1 = 'U'
    for move2 in ['D']:#moves:
        for move3 in ['Uw']:#moves:
            seq = " ".join([move1,move2,move3])
            sequences.append(seq)

    print("Length of sequence: %d"%(len(sequences)))

    for sequence in sequences:
        print(get_rotations(sequence))


def get_rotations(sequence):
    """
    Given a cube sequence,
    find all 24 rotations of it.
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

    ### print("For new cube config:")
    ### print(cubes[0])
    ### print("Original move sequence is:")
    ### print(sequence)

    results.add(sequence)

    # Here we assume first move is a U.
    # Split the sequence into its moves,
    # and use the first cube configuration to map
    # moves to numbers.
    moves = sequence.split(" ")
    move_numbers = []
    for move in moves:
        move_numbers.append(cubes[0].index(move[0]))

    # Now run through all other cube configurations,
    # and map the numbers back to moves.
    for i in range(1,len(cubes)):
        cube = cubes[i]
        xmoves = []
        for i, move_number in enumerate(move_numbers):
            old_face = cubes[0][move_number]
            new_face = cube[move_number]

            old_move = moves[i]
            new_move = re.sub(old_face,new_face,old_move)

            xmoves.append(new_move)

        # Assemble the moves to a string
        xmove = " ".join(xmoves)

        ### print("For new cube config:")
        ### print(cube)
        ### print("New move sequence is:")
        ### print(xmove)

        results.add(xmove)

    return results


def get_cube():
    cube = RubiksCube444(solved_4x4x4,'URFDLB')
    return cube


if __name__=="__main__":
    main()

