import numpy as np


def get_orientations(scaffold):
    """
    Returns a list of transformations done on the scaffold by reflection and swapping of axis.
    Note: Does not also rotate scaffold, only applies permutation matrices (and their negatives).
    :param scaffold: Shape to be transformed
    :return: List of shapes having undergone transformations
    """
    orientation_mats = []
    for i in range(4):
        matrix = np.eye(4, dtype=int)
        matrix[[0, i]] = matrix[[i, 0]]
        orientation_mats.append(matrix)
        orientation_mats.append(np.multiply(matrix, -1))

    transformed_shapes = [np.matmul(scaffold, mat) for mat in orientation_mats]

    return transformed_shapes


# A list of vectors that represent all combinations of four tiles in a line.
adj_4 = [
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [2, 0, 0, 0],
    [3, 0, 0, 0]
]

# TODO: Implement diagonal orientations as a win condition.
