from rubikscubennnsolver.RubiksCube444 import RubiksCube444, solved_4x4x4


def main():
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
    for move2 in moves:
        for move3 in moves:
            seq = " ".join([move1,move2,move3])
            sequences.append(seq)

    print("Length of sequence: %d"%(len(sequences)))



def define_cubes():
    ucube = ["UBFLRD",
             "UFBRLD",
             "ULRFBD"
             "URLBFD"]

    dcube = ["DFBLRU",
             "DBFRLU",
             "DLRBFU",
             "DRLFBU"]

    lcube = ["LUDBFR",
             "LDUFBR",
             "LFBUDR",
             "LBFDUR"]

    rcube = ["RUDFBL",
             "RDUBFL",
             "RBFUDL",
             "RFBDUL"]

    fcube = ["FUDLRB",
             "FDURLB",
             "FRLUDB",
             "FLRDUB"]

    bcube = ["BUDRLF",
             "BDULRF",
             "BLRUDF",
             "BRLDUF"]


def get_cube():
    cube = RubiksCube444(solved_4x4x4,'URFDLB')
    return cube


if __name__=="__main__":
    main()
