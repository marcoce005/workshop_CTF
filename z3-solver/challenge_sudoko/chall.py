N = 9

def print_sudoku(grid):
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end=" ")
        print()


def print_sudoku_as_flag(grid):
    flag = ""
    for i in range(N):
        for j in range(N):
            flag += str(grid[i][j])
    return f"ptm{{{flag}}}"


with open('sudoku.txt') as f:
    sudoku = f.readlines()
sudoku = [x.strip().split() for x in sudoku]
print_sudoku(sudoku)

# ptm{126437958895621473374985126457193862983246517612578394269314785548769231731852649}