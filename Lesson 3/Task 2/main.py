def rhombus(size, iterations = 0):
    if size <= 0:
        return
    print(' ' * (size - 1) + '*' * (2 * iterations + 1))
    rhombus(size - 1, iterations + 1)
    print(' ' * (size - 1) + '*' * (2 * iterations + 1))

rhombus(int(input("Size > ")))