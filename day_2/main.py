if __name__ == "__main__":

	with open('input.txt','r') as f:
		data = f.readlines()
    

def strategy_one(guide):
    tool_score = 0
    win_score = 0
    for round in guide:
        round = round.split()
        if round[1] == 'X':
            tool_score += 1
            if round[0] == 'A':
                win_score += 3
            elif round[0] == 'C':
                win_score += 6
        if round[1] == 'Y':
            tool_score += 2
            if round[0] == 'A':
                win_score += 6
            elif round[0] == 'B':
                win_score += 3
        if round[1] == 'Z':
            tool_score += 3
            if round[0] == 'B':
                win_score += 6
            elif round[0] == 'C':
                win_score += 3 
    total_score = tool_score + win_score
    return total_score

def strategy_two(guide):
    tool_score = 0
    win_score = 0
    for round in data:
        round = round.split()
        if round[1] == 'X': # LOSS
            if round[0] == 'A': # ROCK
                tool_score += 3 # CHOOSE SCISSORS
            elif round[0] == 'B': # PAPER
                tool_score += 1 # CHOOSE ROCK
            elif round[0] == 'C': # SCISSORS
                tool_score += 2 #CHOOSE PAPER
        if round[1] == 'Y': # DRAW
            win_score += 3
            if round[0] == 'A': # ROCK
                tool_score += 1 # CHOOSE ROCK
            elif round[0] == 'B': # PAPER
                tool_score += 2 #CHOOSE PAPER
            elif round[0] == 'C': # SCISSORS
                tool_score += 3 # CHOOSE SCISSORS
        if round[1] == 'Z': #WIN
            win_score += 6
            if round[0] == 'A': # ROCK
                tool_score += 2 #CHOOSE PAPER
            elif round[0] == 'B': # PAPER
                tool_score += 3 # CHOOSE SCISSORS
            elif round[0] == 'C': # SCISSORS
                tool_score += 1 # CHOOSE ROCK
    total_score = tool_score + win_score
    return total_score



print(f'Total score after following the first strategy is: {strategy_one(data)} ')

print(f'Total score after following the second strategy is: {strategy_two(data)} ')