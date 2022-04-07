"""
Test the performance of the best genome produced by evolve-feedforward.py.
"""

from __future__ import print_function
import os
import pickle
import model
import neat
import visualize
from play_vs_computer import play_game
    
    

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# load the winner
with open('./winner','rb') as f:
    c = pickle.load(f)

print('Loaded genome:')
print(c)

# Load the config file, which is assumed to live in
# the same directory as this script.
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config')
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)

sim = model.TicTacToe()

play_game(c, config)

########################
# Simulate the performance of the loaded network
########################    
    

