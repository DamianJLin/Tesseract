import numpy as np
import itertools as itt


# TEST
def print_mat_list(mat_list, msg=''):
    print('=' * 20, end='')
    print(' ' + msg + ' ', end='')
    print('=' * 20)
    print('l = {}'.format(len(mat_list)))
    # for i in mat_list:
    #     for j in i:
    #         print(j)
    #     print()
    print(np.asarray(mat_list))


def get_orientations(scaffold):
    """
    Returns a list of transformations done on the scaffold by reflection and swapping of axis.
    Note: Does not also rotate scaffold, only applies permutation matrices (and their negatives).
    :param scaffold: Shape to be transformed
    :return: List of shapes having undergone transformations
    """
    o_mats = []

    def powerset(iterable):
        """Generates the powerset of iterable."""
        s = list(iterable)
        return itt.chain.from_iterable(itt.combinations(s, k) for k in range(len(s) + 1))

    # Powerlist (list of all sub-lists) of [0, 1, 2, 3]
    powerlist = list(powerset([0, 1, 2, 3]))

    # For each permutation of eye(4), get the all the possible row-negatives.

    # Permutations of eye(4)
    perms = [list(i) for i in itt.permutations(np.eye(4, dtype=int))]

    for mat in perms:

        for rows in powerlist:

            # Make a non-referential copy of mat
            mat_copy = np.asarray(mat)
            # Take the negatives of rows in this particular sub-list
            for r in rows:
                mat_copy[r] = np.negative(mat[r])

            # Append a non-referential copy of mat_copy
            o_mats.append(np.asarray(mat_copy))

    # Multiply with scaffold
    transformed = np.matmul(scaffold, o_mats)

    # Keep only unique elements
    transformed_unique = []
    seen = set()

    for elem in transformed:
        if str(elem) in seen:
            continue
        else:
            transformed_unique.append(elem)
            seen.add(str(elem))

    # Return
    return transformed_unique


# A list of vectors that represent all combinations of four tiles in a line, including diagonals.
adj_1 = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [2, 0, 0, 0],
    [3, 0, 0, 0]
]

adj_2 = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [2, 2, 0, 0],
    [3, 3, 0, 0]
]

adj_3 = [
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [2, 2, 2, 0],
    [3, 3, 3, 0]
]

adj_4 = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3]
]

# TEST
if __name__ == '__main__':
    print_mat_list(get_orientations(adj_1), 'ADJ_1')
    print_mat_list(get_orientations(adj_2), 'ADJ_2')
    print_mat_list(get_orientations(adj_3), 'ADJ_3')
    print_mat_list(get_orientations(adj_4), 'ADJ_4')
