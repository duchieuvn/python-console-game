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

def display_health(player, enemy):
    print("\n-------------------------- Battle Status --------------------------")
    print(f"Player: {player['health']}/500   {'=' * (player['health'] // 10)}")
    print(f"Enemy : {enemy['health']}/500   {'=' * (enemy['health'] // 10)}")
    print("-------------------------------------------------------------------\n")

def display_words(word_points):
    print("\n>>> Type one of these words:")
    for word, points in word_points.items():
        print(f"  {word:15} => {points:>3} damage")
    print("\n========================================================")

def get_user_input(timeout):
    print(f'You have {timeout} seconds', flush=True)
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

    print('\nTime out! Press Enter to continue.')
    return None

def handle_input(user_word, random_words, word_points, enemy):
    if user_word in random_words:
        damage = word_points[user_word]
        print(f"\nYou dealt {damage} damage to the enemy!")
        enemy['health'] -= damage
    else:
        print("\nIncorrect word! You lose your turn.")

def handle_player_turn(enemy):
    random_words = get_random_words()
    word_points = get_word_points(random_words)
    display_words(word_points)

    user_word = get_user_input(timeout=6)
    handle_input(user_word, random_words, word_points, enemy)

def handle_enemy_turn(player):
    print("\nThe enemy attacks and deals 50 damage!")
    player['health'] -= 50
    time.sleep(1)

def start_game():
    restart = 'y'
    while restart == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        enemy = {'health': 500}
        player = {'health': 500}

        while enemy['health'] > 0 and player['health'] > 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            display_health(player, enemy)
            handle_player_turn(enemy)
            if enemy['health'] > 0:
                handle_enemy_turn(player)

        os.system('cls' if os.name == 'nt' else 'clear')
        display_health(player, enemy)
        if player['health'] <= 0:
            print("\nGame Over! You lost. Better luck next time!\n")
        elif enemy['health'] <= 0:
            print("\nCongratulations! You defeated the enemy!\n")

        restart = input('Do you want to play again? (y/n): ').strip().lower()
        if restart == 'y':
            print("\nRestarting the game...\n")
        else:
            print("\nThanks for playing! Goodbye!")

if __name__ == '__main__':
    start_game()
