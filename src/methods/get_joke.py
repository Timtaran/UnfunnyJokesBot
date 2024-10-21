import random

file = open("src/files/jokes.txt", "r", encoding="utf-8")
jokes = file.read().split("\n\n\n")
file.close()

print(jokes)


def get_joke():
    return random.choice(jokes)
