def get_scores(my_move, opponent_move):
    if my_move == 1 and opponent_move == 1:
        return (3, 3)
    elif my_move == 1 and opponent_move == 0:
        return (0, 5)
    elif my_move == 0 and opponent_move == 1:
        return (5, 0)
    else:
        return (1, 1)


def name_amen(my_history, opponent_history, rounds):
    round_num = len(my_history)
    if round_num < 3:
        return 1
    if round_num == 5 and all(move == 0 for move in opponent_history[:5]):
        name_amen.mode = 'full_defect'
    elif round_num == 5 and all(move == 1 for move in opponent_history[:5]):
        name_amen.mode = 'exploit'
    elif round_num == 5:
        name_amen.mode = 'mixed'

    mode = getattr(name_amen, 'mode', 'mixed')

    if mode == 'full_defect':
        return 0
    if mode == 'exploit':
        if round_num % 5 == 0:
            return 0
        return 1
    if opponent_history and opponent_history[-1] == 0:
        return 1
    if round_num % 6 == 0:
        return 0
    return 1


def reset_strategy_state():
    if hasattr(name_amen, 'mode'):
        del name_amen.mode


def simulate(strategy1, strategy2, rounds=2042):
    history1, history2 = [], []
    score1, score2 = 0, 0
    for _ in range(rounds):  # Fixed the typo here
        move1 = strategy1(history1, history2, rounds)
        move2 = strategy2(history2, history1, rounds)
        s1, s2 = get_scores(move1, move2)
        score1 += s1
        score2 += s2
        history1.append(move1)
        history2.append(move2)
    return score1, score2


def tit_for_tat(my_history, opponent_history, rounds):
    if not opponent_history:
        return 1
    return opponent_history[-1]


def always_cooperate(my_history, opponent_history, rounds):
    return 1


def always_defect(my_history, opponent_history, rounds):
    return 0


reset_strategy_state()
print("vs Tit for Tat:", simulate(name_amen, tit_for_tat))
reset_strategy_state()
print("vs Always Cooperate:", simulate(name_amen, always_cooperate))
reset_strategy_state()
print("vs Always Defect:", simulate(name_amen, always_defect))
