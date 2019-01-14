
def addition(x, y):
    if x == 0:
        return y
    else:
        return addition((x - 1), (y + 1))

#print(addition(3, 5))
