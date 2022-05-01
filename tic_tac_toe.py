# Cart pole dynamics and modelling

import random
from this import d
from tkinter import N
import math


class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[None] * size for _ in range(self.size)]
        self.moves_made = 0
        self.finished = False
        self.winner = None

    def current_player(self):
        return self.moves_made % 2

    def is_move_valid(self, x, y):
        return self.board[y][x] == None
    
    def make_move(self, x, y):
        self.moves_made += 1
        self.board[y][x] = self.current_player()
        self.end_move()
    
    def end_move(self):
        self.check_winner(self.winner_from_rows())
        self.check_winner(self.winner_from_columns())
        self.check_winner(self.winner_from_diagonals())
        if self.is_filled():
            self.finished = True
        
    def check_winner(self, winner):
        if winner != None:
            self.finished = True
            self.winner = winner

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
        if lst.count(first) == len(lst) and first != None:
            return first
        return None
        
    
    def accuator(self, moves):
        filtered_moves = [move * filter for move, filter in zip(moves, self._legal_move_filter())]
        sorted_moves = reversed(sorted(enumerate(filtered_moves), key=lambda x:x[1]))
        
        location = list(sorted_moves)[0][0]
        return location % self.size, location // self.size
        
    
    def _legal_move_filter(self):
        return [self.is_move_valid(i % self.size, i // self.size) for i in range(self.size**2)]
    
    
    def get_states(self, player):
        return [self.map_state(player, i % self.size, i // self.size) for i in range(self.size**2)]
    
    def map_state(self, player, x, y):
        return 1.0 if self.board[y][x] == player else 0.0


    def display_board(self):
        for row in reversed(self.board):
            print(self.get_displayable_row(row))
    
    def get_displayable_row(self, row):
        sign_map = {0:"O", 1:"X", None:"-"}
        row_displayable = list(map(lambda x: sign_map[x], row))
        return row_displayable






    

        

