import random

def generate_puzzle(colors, positions):
    return random.choices(colors, k=positions)

def evaluate_guess(puzzle, guess):
    result = ''
    for i in range(len(puzzle)):
        if guess[i] == puzzle[i]:
            result += '*'
        elif guess[i] in puzzle:
            result += 'o'
        else:
            result += ' '
    return result

def play_game(colors, positions, max_rounds):
    puzzle = generate_puzzle(colors, positions)
    print(f"Playing Mastermind with 6 colors and 4 positions")
    rounds = 0
    while rounds < max_rounds:
        guess = input("What is your guess?: ").strip()[:positions]
        print("Your guess is", guess)
        clue = evaluate_guess(puzzle, guess)
        print(clue)
        rounds += 1
        if clue == '*' * positions:
            print("Congratulations! You solved the puzzle!")
            print("You solved it after", rounds, "rounds.")
            return

    print("Game over! You reached the maximum number of rounds.")
    print("The puzzle was:", ''.join(puzzle))

colors = ['1', '2', '3', '4', '5', '6']
positions = 4
max_rounds = 10
play_game(colors, positions, max_rounds)