def parse_input(path):
  with open(path) as f:
    return f.read().split()


move_points = {'X': 1, 'Y': 2, 'Z': 3}


def score(opponent_move, my_move):
  round_points = 0
  if (opponent_move == 'A'
      and my_move == 'X') or (opponent_move == 'B'
                              and my_move == 'Y') or (opponent_move == 'C'
                                                      and my_move == 'Z'):
    round_points = 3
  elif (opponent_move == 'A'
        and my_move == 'Y') or (opponent_move == 'B'
                                and my_move == 'Z') or (opponent_move == 'C'
                                                        and my_move == 'X'):
    round_points = 6

  return round_points + move_points[my_move]


def partOne():
  strategy = parse_input('solutions/two_input.txt')
  points = 0
  while (strategy):
    my_move = strategy.pop()
    opponent_move = strategy.pop()
    points += score(opponent_move, my_move)
  return points


def main():
  print(partOne())


if __name__ == "__main__":
  main()
