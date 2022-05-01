"""
Single-pole balancing experiment using a feed-forward neural network.
"""

from __future__ import print_function
import os
import pickle
import neat
from tournament import Tournament
import visualize
from play_vs_computer import play_game

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

games_per_round = 3
generations = 40


def eval_genomes(genomes, config):
    for _, genome in genomes:
        genome.fitness = 0.0
    id_net_pairs = [(id, neat.nn.FeedForwardNetwork.create(genome, config), genome) for id, genome in genomes[:256]]

    sim = Tournament(id_net_pairs)
    sim.play_tournament()



def main():
    # Load the config file, which is assumed to live in the same directory as this script.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)

    pop = neat.Population(config)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.StdOutReporter(True))

    winner = pop.run(eval_genomes, generations)

    # Save the winner.
    with open('winner', 'wb') as f:
        pickle.dump(winner, f)

    print(winner)

    # Show winning neural network
    node_names = {}
    for i in range(1, 10):
        node_names[-i] = "ai: " + str(i)
        node_names[-i - 9] ="opponent: " + str(i)
        node_names[i - 1] = "output: " + str(i)

    print(node_names)
    
    
    # visualize.draw_net(config, winner, view=True, node_names=node_names,filename="winner-enabled-pruned.gv", show_disabled=False, prune_unused=True)
    # play_game(winner, config)

if __name__ == '__main__':
    main()