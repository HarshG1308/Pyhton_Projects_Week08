import random
words = ['python', 'computer', 'programming', 'algorithm', 'coding']
word = random.choice(words)
board = '_' * len(word)
turns = 6
guessed = []
hangman = [
    """
     _______
    |/      +
    |      
    |      
    |       
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      
    |       
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |       |
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / 
    |
    """,
    """
     _______
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / \\
    |
    """
]
while turns > 0 and '_' in board:
    print(f'Word: {board}')
    print(f'Turns left: {turns}')
    print(f'Guessed letters: {", ".join(guessed)}')
    print(hangman[6-turns])
    guess = input('Guess a letter: ').lower()
    if not guess.isalpha() or len(guess) != 1:
        print('Invalid input! Please enter a single letter.')
        continue
    if guess in guessed:
        print(f'You already guessed {guess}!')
        continue
    guessed.append(guess)
    if guess in word:
        print(f'Correct! {guess} is in the word.')
        board = ''.join([c if c == guess or board[i] != '_' else '_' for i, c in enumerate(word)])
    else:
        print(f'Wrong! {guess} is not in the word.')
        turns -= 1
if '_' not in board:
    print(f'Congratulations, you won! The word was {word}.')
else:
    print(f'Sorry, you lost! The word was {word}.')
    print(hangman[6])