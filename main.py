board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


class SudokuSolver:
    def __init__(self, bo):
        self.board = bo

    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print('----------------------------')

            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(' |  ', end='')

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(f'{self.board[i][j]} ', end='')

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i, j

    def is_valid(self, num, pos):
        # Check row
        for i in range(len(self.board[0])):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(self.board)):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False

        # Check sub-grid
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, (box_y+1)*3):
            for j in range(box_x*3, (box_x+1)*3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True

    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find
        for i in range(1, 10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i

                if self.solve():
                    return True

            self.board[row][col] = 0

        return False


if __name__ == '__main__':
    board_1 = SudokuSolver(board)
    board_1.print_board()
    print()
    board_1.solve()
    print("Solving ....", end='\n\n')
    board_1.print_board()
