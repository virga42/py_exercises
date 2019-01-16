
def addition(x, y):
    if x == 0:
        return y
    else:
        return addition((x - 1), (y + 1))

#print(addition(3, 5))

arr = ( (11,  2,   4), 
        ( 4,  5,   6),
        (10,  8, -12) )

def abs_diff(x, y):
    return abs(x - y)

def dd(arr):
    matrix_size = len(arr)
    total_diag_back = 0
    total_diag_forward = 0
    for i in range(0, matrix_size):
        total_diag_back += arr[i][i]
        total_diag_forward += arr[i][matrix_size-i-1]
    return abs_diff(total_diag_back, total_diag_forward)

