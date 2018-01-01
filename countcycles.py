from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4
from pprint import pprint
import json

def count_cycles():
    sequence_test(2)
    print("Done with sequences of length 2")
    sequence_test(3)
    print("Done with sequences of length 3")



def sequence_test(n):

    from perms import algorithm_m_clean
    results = {}
    for seq in algorithm_m_clean(n):
        results[seq] = get_cross_cycles(seq)

    # results dictionary:
    # keys are N-move sequences
    # values are number of repeat cycles/supercycles
    filename = "sequence%d.json"%(n)
    with open(filename,'w') as f:
        json.dump(results, f, indent=4, sort_keys=True)


def sanity_check():
    """
    Run a quick sanity check.

    U R U' R' = 6 repetitions of sequence, 
                1 center cycle (of course)
    L U = 105 repetitions of sequence, 
          105 center cycles (of course),
          15 cross cycles of 105/15 = 7 inner cycles each
    """
    sequences = ["U R U' R'",
                 "U' L'",
                 "L U",
                 "Uw L'"]
    results = {}

    for sequence in sequences:
        #results[sequence] = get_cycles(sequence)
        #results[sequence] = get_center_cycles(sequence)
        results[sequence] = get_cross_cycles(sequence)

    pprint(results)



def get_cycles(sequence):
    """
    Given a 4x4 cube and a move sequence,
    this determines the total number of 
    cycles needed to go from a solved state
    back to a solved state.
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



def get_center_cycles(sequence):
    """
    Given a 4x4 cube and a move sequence,
    this determines the number of center cycles
    (between which centers are solved)
    and inner cycles. 
    """
    rr = get_cube()

    moves = sequence.split(" ")
    centercyclecount = 0
    innercyclecount = 0

    maxcount = 10000
    while True:
        # Apply this sequence to the cube
        for move in moves:
            rr.rotate(move)

        # Increment cycle count
        innercyclecount += 1

        # Check if center solved
        if(rr.centers_solved()):
            centercyclecount += 1
            innercyclecount = 0

        # Check if solved
        if(rr.solved()):
            return (centercyclecount, innercyclecount)

        if(centercyclecount>maxcount):
            return (-1,-1) # Tap out



def get_cross_cycles(sequence):
    """
    Given a 4x4 cube and a move sequence,
    this determines the number of cross cycles
    (between which crosses are solved),
    center cycles (between which centers are solved),
    and inner cycles.
    """
    rr = get_cube()

    moves = sequence.split(" ")
    crosscyclecount = 0
    centercyclecount = 0
    innercyclecount = 0

    maxcount = 10000
    while True:
        # Apply this sequence to the cube
        for move in moves:
            rr.rotate(move)

        # Increment cycle count
        innercyclecount += 1

        # Check if center solved
        if(rr.centers_solved()):
            centercyclecount += 1

        # Check if crosses solved
        if(rr.crosses_solved()):
            crosscyclecount += 1

        # Check if solved
        if(rr.solved()):
            return (crosscyclecount, centercyclecount, innercyclecount)

        if(crosscyclecount>maxcount):
            return (-1, -1,-1) # Tap out



def get_cube():
    """
    Get a 4x4 Rubiks Cube.
    """
    order = 'URFDLB'
    cube = RubiksCube444(solved_4x4x4, order)
    return cube



if __name__=="__main__":
    count_cycles()
