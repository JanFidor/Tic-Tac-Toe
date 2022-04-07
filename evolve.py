"""
Single-pole balancing experiment using a feed-forward neural network.
"""

from __future__ import print_function
import os
import pickle
import model
import neat
import visualize
from play_vs_computer import play_game

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

runs_per_net = 5
generations = 40

def eval_game(genomes, config):
    nets = [neat.nn.FeedForwardNetwork.create(genome, config) for genome in genomes]
    sim = model.TicTacToe()

    for i in range(runs_per_net):
        # Run the given simulation for up to num_steps time steps.
        while not sim.finished:
            player = sim.current_player()
            net = nets[player]
            states = sim.get_states(player)
            action = net.activate(states)
            move = sim.accuator(action)

            sim.make_move(*move, player)
        
        for i in range(len(genomes)):
            genome = genomes[i]
            if (genome.fitness is None):
                genome.fitness = 0
            genome.fitness += sim.get_fitness(i)


def eval_genomes(genomes, config):
    size = len(genomes)
    for i in range(size):
        for j in range(size):
            if j != i:
                opponents = [genomes[i][1], genomes[j][1]]
                eval_game(opponents, config)


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

    # Show winning neural network
    node_names = {}
    for i in range(1, 10):
        node_names[str(i)] = i
        node_names[str(-i)] = "-" + str(i)
    
    visualize.draw_net(config, winner, view=True, node_names=node_names,filename="winner-enabled-pruned.gv", show_disabled=False, prune_unused=True)
    play_game(winner, config)

if __name__ == '__main__':
    main()