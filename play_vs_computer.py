from model import TicTacToe
import neat

def play_game(net, config):
    ai = neat.nn.FeedForwardNetwork.create(net, config)
    sim = TicTacToe()
    sim.display_board()
    print("\n" * 2)
    while not sim.finished:
        player = sim.current_player()
        if player == 0:
            ai_move(sim, player, ai)
        else:
            human_move(sim, player)
        sim.display_board()
        print("\n" * 2)

def human_move(sim, player):
    x = int(input("x: "))
    y = int(input("y: "))
    sim.make_move(x, y, player)

def ai_move(sim, player, ai):
    states = sim.get_states(player)
    action = ai.activate(states)
    move = sim.accuator(action)
    sim.make_move(*move, player)