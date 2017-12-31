from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from pprint import pprint

def get_cube():
    """
    Get a 4x4 Rubiks Cube.
    """
    order = 'URFDLB'
    cube = RubiksCube444(solved_4x4x4, order)
    return cube


def get_cycles(sequence):
    """
    Given a 4x4 cube and a move sequence,
    this determines the total number of 
    cycles needed to go from a solved state
    back to a solved state.

    Don't worry about supercycles for now...
    """
    # For each sequence, start with a fresh cube.
    rr = get_cube()

    # Rotate this sequence an indefinite number of times,
    # checking if cube is solved after each move.
    moves = sequence.split(" ")
    cyclecount = 0

    maxcount = 10000

    while True:
        # Apply this sequence to the cube
        for move in moves:
            rr.rotate(move)

        # Increment cycle count
        cyclecount += 1

        # Check if solved
        if(rr.solved()):
            return cyclecount

        if(cyclecount>maxcount):
            return -1 # Tap out



def sanity_check():
    """
    Run a quick sanity check.

    URU'R' = 6 repetitions of sequence, 1 supercycle 

    LU = 105 repetitions of sequence, 15 supercycles of 7 sequences each
    """
    sequences = ["U R U' R'",
                 "L U"]
    results = {}

    for sequence in sequences:
        results[sequence] = get_cycles(sequence)

    pprint(results)


if __name__=="__main__":
    sanity_check()

