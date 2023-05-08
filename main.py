from random import choice
from imgs.ascii_imgs import *
from words_list import word_list

game_is_on = True
display = []
lives = 6
list_of_repeat_words = []


def create_display(word):
    for i in range(len(word)):
        display.append("_")


def exam_display(user_guess):
    global lives
    if user_guess in list_of_repeat_words:
        print("The letter has already been repeated")
    for index in range(len(rnd_answer)):
        if user_guess == rnd_answer[index]:
            display[index] = user_guess
            list_of_repeat_words.append(user_guess)
    if user_guess not in rnd_answer:
        lives -= 1
        print("Letter not found")
        print(stages[lives])


def check_win():
    global game_is_on
    win = "".join(display)
    if win == rnd_answer:
        print("Win")
        print(win)
        game_is_on = False
    if lives == 0:
        print("Game Over")
        exit()


rnd_answer = choice(word_list)
create_display(rnd_answer)
print(logo)
while game_is_on:
    print("".join(display))
    guess = input("Guess a letter: ").lower()
    exam_display(guess)
    check_win()
