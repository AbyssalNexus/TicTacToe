import random

class Ai:
    # prototype for the AI class
    def __init__(self, sign):
        self.sign = sign
        self.opponent_sign = 'O' if sign == 'X' else 'X'

    def get_next_action(self, board):
        pass

class RandomAi(Ai):
    # the RandomAi class
    def get_next_action(self, board):
        # ランダムに空のマス目を選択
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
        print(empty_cells)
        print(board)
        if empty_cells:
            return random.choice(empty_cells)
        else:
            return None
        
class MinimaxAi(Ai):
    # the MinimaxAi class
    def get_next_action(self, board):
        # ミニマックス法で最適な手を選択
        best_score = -float('inf')
        best_action = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == '':
                    board[i][j] = self.sign
                    score = self.minimax(board, False)
                    board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_action = (i, j)
        return best_action
    
    def minimax(self, board, is_maximizing):
        winner = self.check_winner(board)
        if winner == self.sign:
            return 1
        elif winner == self.opponent_sign:
            return -1
        elif self.is_board_full(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = self.sign
                        score = self.minimax(board, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = self.opponent_sign
                        score = self.minimax(board, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != '':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != '':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != '':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != '':
            return board[0][2]
        return None

    def is_board_full(self, board):
        return all(all(cell != '' for cell in row) for row in board)