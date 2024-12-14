import random
import time
import msvcrt
import os


def get_random_words():
    file_path = 'a2.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()

    words = [word.strip() for word in words]
    random_words = random.sample(words, 3)
    return random_words

def get_word_points(random_words):
    points = {}
    for word in random_words:
        l = len(word)
        points[word] = l * 10 + random.randint(-l * 2, l * 2)

    return points


def get_user_input(timeout):
    print(f'\nYou have {timeout} seconds. Start typing... ', end='', flush=True)
    start_time = time.time()
    typed_word = ""

    while time.time() - start_time < timeout:
        if msvcrt.kbhit():  
            char = msvcrt.getwch()  
            if char == '\r':  
                print()  
                return typed_word.strip()
            elif char == '\b':  
                typed_word = typed_word[:-1]
                print("\b \b", end='', flush=True)  
            else:
                typed_word += char
                print(char, end='', flush=True) 

    print('\nTime out. Please press Enter to continue')
    return None

def handle_input(user_word, random_words, word_points, enemy):
    if user_word in random_words:
        damage = word_points[user_word]
        enemy['health'] -= damage
    else:
        print(f'\nLose your turn')


def handle_player_turn(enemy):
    random_words = get_random_words()
    word_points = get_word_points(random_words)
    print(word_points)

    user_word = get_user_input(timeout=6)
    handle_input(user_word, random_words, word_points, enemy)

def handle_enemy_turn(player):
    player['health'] -= 50



def start_game():
    restart = 'y'
    while restart == 'y':
        os.system('cls')
        enemy = {'health': 500}
        player = {'health': 500}

        while enemy['health'] > 0 and player['health'] > 0:
            os.system('cls')
            print('You', player['health'], '      ', 'Enemy', enemy['health'])
            handle_player_turn(enemy)
            handle_enemy_turn(player)

        if player['health'] <= 0:
            print("\nGame Over! You lost.")
        elif enemy['health'] <= 0:
            print("\nCongratulations! You defeated the enemy.")
        restart = input('\nDo you want to play again? (y/n): ').strip().lower()

if __name__ == '__main__':
    start_game()
