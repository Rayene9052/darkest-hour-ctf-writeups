import random


with open("./src/wordlist.txt", "r") as file:
    words = file.read().strip().split(",")

random_word = random.choice(words)

def score(word, guess, i, score_value):
    if i == 1:
        return score_value
    w = word[0]
    g = guess[0]
    score_value = (score_value * (ord(w) - ord(g))) % 29
    return score(word[1:], guess[1:], i - 1, score_value)  

print("Welcome to guesser! You have 7 attempts to guess a 6-letter English word.")

attempts = 0
MAX_ATTEMPTS = len(random_word) + 1
word_score = 1

while attempts < MAX_ATTEMPTS:
    guess = input("What's your guess? ").lower()

    if len(guess) != len(random_word):
        print("Please enter a 6-letter word.")
        break

    if not guess.isalpha():
        print("Invalid input. Only letters are allowed.")
        break

    if guess == random_word:
        print("Well Played!")

        with open('/src/flag.txt', 'r') as f:
            flag = f.read()
            print(flag)
       

    word_score = score(random_word, guess, len(random_word), word_score)
    print(f"> Score is {word_score}")

    attempts += 1  

if guess != random_word:
    print("Try again ...")
