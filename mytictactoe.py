import random

#winning_combos = ( [0, 1, 2], [3, 4, 5], [6, 7, 8],
#        [0, 3, 6], [1, 4, 7], [2, 5, 8],
#        [0, 4, 8], [2, 4, 6])
        #[1, 2, 3], [4, 5, 6], [7, 8, 9],
        #[1, 4, 7], [2, 5, 8], [3, 6, 9],
        #[1, 5, 9], [3, 5, 7])


def available_moves(board):
    """what spots are left empty?"""
    return [k for k, v in enumerate(board) if v is 0]


def available_combos(board, player):
    """what combos are available?"""
    return available_moves(board) + get_squares(board,player)


def complete(board):
    """is the game over?"""
    if 0 not in [v for v in board]:
        return True
    if winner(board) != None:
        return True
    return False


def won(board,player):
    return winner(board) == player


def tied(board):
    return complete(board) == True and winner(board) is None

def winner(board):
    threes = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
    for each in threes:
        total = board[each[0]-1] + board[each[1]-1] + board[each[2]-1]
        if total == -3:
            return "O"
        elif total == 3:
            return "X"
    return None
#def winner(board):
#    for player in ("X", "O"):
#        positions = get_squares(board,player)
#        for combo in winning_combos:
#            win = True
#            for pos in combo:
#                if pos not in positions:
#                    win = False
#            if win:
#                return player
#    return None


def get_squares(board, player):
    """squares that belong to a player"""
    if player =="X":
        return [k for k, v in enumerate(board) if v == 1]
    else:
        return [k for k, v in enumerate(board) if v == -1]


def make_move(board, position, player):
    """place on square on the board"""
    if player == "X":
        board[position] = 1
    elif player == "O":
        board[position] = -1
    else:
        board[position] = 0
    return board




def get_enemy(player):
    if player == "X":
        return "O"
    return "X"


def alphabeta(node, player, alpha, beta,symbol):
  if complete(node):
    if won(node,get_enemy(symbol)):
        return -1
    elif tied(node):
        return 0
    elif won(node,symbol):
        return 1
  for move in available_moves(node):
      node = make_move(node,move, player)
      val = alphabeta(node, get_enemy(player), alpha, beta,symbol)
      node = make_move(node,move, 0)
      if player == symbol:
          if val > alpha:
              alpha = val
          if alpha >= beta:
             return beta
      else:
          if val < beta:
              beta = val
          if beta <= alpha:
              return alpha
  if player == symbol:
      return alpha
  else:
      return beta


def determine(board, player):
      a = -2
      choices = []
      if len(available_moves(board)) == 9:
          return 4
      for move in available_moves(board):
          make_move(board,move, player)
          val = alphabeta(board, get_enemy(player), -2, 2,player)
          make_move(board,move, 0)
          if val > a:
              a = val
              choices = [move]
          elif val == a:
              choices.append(move)
      return random.choice(choices)


def mymove(board,mysymbol):
    print "Board as seen by the machine:",
    print board
    print "The machine is playing:",
    print mysymbol
    return determine(board,mysymbol)+1
