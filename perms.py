import re
import numpy as np


def main():
    #for perm in algorithm_m():
    #    print(perm)
    test_rotations()


def algorithm_m_clean(n):
    result = {}

    for perm in algorithm_m(n):
        # before we can get rotations of this permutation,
        # we need to fix get_rotations()
        pass




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
             'Uw','Dw','Bw','Fw','Lw','Rw']

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

    first_move = moves[0]
    first_move_index = cubestart[first_move]

    # Now run through all other cube configurations,
    # and map the numbers back to moves.
    move_numbers = []
    for move in moves:
        move_numbers.append(cubes[first_move_index].index(move[0]))

    for i in range(1,len(cubes)):
        cube = cubes[i]
        xmoves = []
        for i, move_number in enumerate(move_numbers):
            old_face = cubes[first_move_index][move_number]
            new_face = cube[move_number]

            old_move = moves[i]
            new_move = re.sub(old_face,new_face,old_move)

            xmoves.append(new_move)

        # Assemble the moves to a string
        xmove = " ".join(xmoves)

        results.add(xmove)

    return results

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
    move1 = 'L'
    for move2 in ['D']:#moves:
        for move3 in ['Rw']:#moves:
            seq = " ".join([move1,move2,move3])
            sequences.append(seq)

    print("Length of sequence: %d"%(len(sequences)))

    for sequence in sequences:
        print(get_rotations(sequence))



if __name__=="__main__":
    main()

