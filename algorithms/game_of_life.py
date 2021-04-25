import copy


class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)
        board_rows = len(board)

        for i in range(board_rows):
            board_cols = len(board[i])

            for j in range(board_cols):
                alive_neighbours = 0

                if j > 0:
                    alive_neighbours += board_copy[i][j - 1]

                if j > 0 and i > 0:
                    alive_neighbours += board_copy[i - 1][j - 1]

                if i > 0:
                    alive_neighbours += board_copy[i - 1][j]

                if i > 0 and j < (board_cols - 1):
                    alive_neighbours += board_copy[i - 1][j + 1]

                if j < (board_cols - 1):
                    alive_neighbours += board_copy[i][j + 1]

                if i < (board_rows - 1) and j < (board_cols - 1):
                    alive_neighbours += board_copy[i + 1][j + 1]

                if i < (board_rows - 1):
                    alive_neighbours += board_copy[i + 1][j]

                if i < (board_rows - 1) and j > 0:
                    alive_neighbours += board_copy[i + 1][j - 1]

                if board_copy[i][j] and (alive_neighbours > 2):
                    board[i][j] = 0

                if board_copy[i][j] and (alive_neighbours in (2, 3)):
                    board[i][j] = 1

                if board_copy[i][j] and (alive_neighbours > 3):
                    board[i][j] = 0

                if (not board_copy[i][j]) and (alive_neighbours == 3):
                    board[i][j] = 1

        print(board)


if __name__ == '__main__':
    s = Solution()
    s.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
