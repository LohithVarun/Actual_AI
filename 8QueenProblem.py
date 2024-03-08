def is_safe(row, col, queens):
    for i in range(row):
        if queens[i] == col or (queens[i] - i) == (col - row) or (queens[i] + i) == (col + row):
            return False
    return True

def solve(row, n, queens):
    if row == n:
        return True
    for col in range(n):
        if is_safe(row, col, queens):
            queens[row] = col
            if solve(row + 1, n, queens):
                return True
    queens[row] = -1
    return False

def print_board(n, queens):
    for row in range(n):
        for col in range(n):
            if queens[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()

n = 8
queens = [-1 for i in range(n)]
if solve(0, n, queens):
    print_board(n, queens)
