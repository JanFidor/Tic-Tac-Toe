from tic_tac_toe import TicTacToe
import math
import random

class Tournament:
    def __init__(self, genomes):
        self.id_to_genome = {id : genome for id, genome in genomes}
        self.population_size = len(genomes)


    def play_tournament(self):
        future_games = self.id_to_genome.keys
        random.shuffle(future_games)

        for _ in range(math.log2(self.population_size)):
            curr_games = future_games.copy()
            future_games = []
            for i in range(0, len(curr_games), 2):
                nets = [self.id_to_genome[net_id] for net_id in curr_games[i : i + 2]]
                winner_id = self.get_winner_id(nets)
                self.id_to_genome[winner_id].fitness += 1.0
                future_games.append(winner_id)


    # players -> iterable of 2 net id's
    def get_winner_id(self, players, games_number=3):
        random.shuffle(players)
        scores = {id : 0 for id in players}
        for _ in range(games_number):
            winner_id = self.play_game(players)
            if winner_id != None:
                scores[winner_id] += 1
        
        if max(scores.values) == min(scores.values):
            return random.choice(scores.keys)
        
        return max(scores.items, lambda x: x[1])[0]
        
    
    def play_game(self, players):
        sim = TicTacToe()
        while not sim.finished:
            player = sim.current_player()
            net_id = players[player]
            move_x, move_y = self._get_net_action(net_id, sim)
            sim.make_move(move_x, move_y)
        
        # return id of winner
        return players[sim.winner] if sim.winner != None else None
    

    def _get_net_action(self, net_id, sim):
        player = sim.current_player()

        player_states = sim.get_states(player)
        opponent_states = sim.get_states(1 - player)

        net = self.id_to_genome[net_id]
        action = net.activate(player_states + opponent_states)
        move = sim.accuator(action)

        return move