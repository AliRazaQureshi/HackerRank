def TwoDArray(size):
    arr = []
    for _ in range(size):
        arr.append(list(map(str, input().strip().split())))
    return arr

def printMatrix(array):
    for row in array:
        for element in ''.join(row):
            print(element, end=" ")
        print("")

matrix_size = int(input())
printMatrix(TwoDArray(matrix_size))