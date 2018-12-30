# Rubiks Cube: Cycles

An investigation into cycles on 3x3 and 4x4 Rubiks Cubes. See [this series of blog posts on charlesreid1.github.io](https://charlesreid1.github.io/tag/rubiks-cube.html) for more information.

Files:

* `manual_order.py` - manually apply sequences to cubes
    to determine their order.

* `perms.py` - provide supporing functions to `manual_order.py` 
    to find rotational permutations of a move sequence.

* `sequence_order.py` - use tuples and tuple factoring
    to determine the order of a move sequence.

Uses cube representation from this library: [dwalton76/rubiks-cube-NxNxN-solver](https://github.com/dwalton76/rubiks-cube-NxNxN-solver)

(Note: counting the order of a cycle does not require solving the cube)
