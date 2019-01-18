"""
Hacker Rank exercises

"""


def diagonalDifference(arr):
    """ diagonal difference of an array """
    matrix_size = len(arr)
    total_diag_back = 0
    total_diag_forward = 0
    for i in range(matrix_size):
        total_diag_back += arr[i][i]
        total_diag_forward += arr[i][matrix_size-i-1]
    return abs(total_diag_back - total_diag_forward)

