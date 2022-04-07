# Cart pole dynamics and modelling

import random
from this import d
from tkinter import N

class Player:
    def __init__(self, number, symbol):
        self.number = number
        self.symbol = symbol


class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [["-"] * size for _ in range(self.size)]
        self.moves_made = 0
        self.finished = False
        self.winner = None

    def current_player(self):
        return self.moves_made % 2

    def is_move_valid(self, x, y):
        return self.board[y][x] == "-"
    
    def make_move(self, x, y, player):
        self.moves_made += 1
        self.board[y][x] = player
        self.end_move()
    
    def end_move(self):
        if self.is_winner(self.winner_from_rows()): return
        if self.is_winner(self.winner_from_columns()): return
        if self.is_winner(self.winner_from_diagonals()): return
        self.finished = self.is_filled()
        
    def is_winner(self, winner):
        if winner != None:
            self.finished = True
            self.winner = winner
            return True
        return False

    def is_filled(self):
        return self.moves_made == self.size**2

    def winner_from_rows(self):
        for row in self.board:
            winner = self.winner_or_none(row)
            if winner != None:
                return winner
        return None
    
    def winner_from_columns(self):
        for i in range(self.size):
            column = [self.board[j][i] for j in range(self.size)]
            winner = self.winner_or_none(column)
            if winner != None:
                return winner
        return None

    def winner_from_diagonals(self):
        lower_diagonal = [self.board[i][i] for i in range(self.size)]
        upper_diagonal = [self.board[self.size - i - 1][i] for i in range(self.size)]
        
        winner_lower = self.winner_or_none(lower_diagonal)
        if winner_lower != None:
            return winner_lower
        return self.winner_or_none(upper_diagonal)
    
            
    def winner_or_none(self, lst):
        first = lst[0]
        if lst.count(first) == len(lst) and first != "-":
            return first
        return None
    
    def get_fitness(self, player):
        if self.winner == None:
            return self.moves_made

        return self.moves_made + (self.winner == player) * 2 * (self.size + 1) - (self.size + 1)
    
    def accuator(self, moves):
        sorted_moves = list(reversed(sorted(enumerate(moves), key=lambda x:x[1])))
        for move in sorted_moves:
            location = move[0]
            x, y = location % self.size, location // self.size
            if self.is_move_valid(x, y):
                return x, y
    
    def get_states(self, player):
        return [self.map_state(player, i % self.size, i // self.size) for i in range(self.size**2)]
    
    def map_state(self, player, x, y):
        if self.board[y][x] == "-":
            return 0
        return 1 if self.board[y][x] == player else -1
    
    def display_board(self):
        for row in reversed(self.board):
            print(row)


    

        

