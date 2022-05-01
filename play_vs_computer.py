from tic_tac_toe import TicTacToe
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
    sim.make_move(x, y)

def ai_move(sim, player, ai):
    player_states = sim.get_states(player)
    opponent_states = sim.get_states(1 - player)

    action = ai.activate(player_states + opponent_states)
    move = sim.accuator(action)
    sim.make_move(*move)