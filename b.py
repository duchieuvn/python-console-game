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

def display_health(player, enemy, enemy_level_health):
    player_health = 0 if player['health'] < 0 else player['health']
    enemy_health = 0 if enemy['health'] < 0 else enemy['health']
    print("\n-------------------------- Battle Status --------------------------")
    print(f"Player: {player_health:3}/500   {'=' * (player_health // 10)}")
    print(f"Enemy : {enemy_health:3}/{enemy_level_health}   {'=' * (enemy_health // 10)}")
    print("-------------------------------------------------------------------")

def display_words(word_points):
    print(">>> Type one of these words:")
    for word, points in word_points.items():
        print(f"  {word:15} => {points:3} damage")
    print("\n========================================================")

def get_user_input(timeout):
    print(f'You have {timeout} seconds to type', flush=True)
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

    return None

def handle_input(user_word, random_words, word_points, enemy):
    if user_word in random_words:
        damage = word_points[user_word]
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
    player['health'] -= 50

def handle_game_restart():
    restart = input('Do you want to play again? (y/n): ').strip().lower()
    if restart == 'y':
        print("\nRestarting the game...\n")
    else:
        print("\nThanks for playing! Goodbye!")

    return restart

def handle_level_result(player, enemy):
    os.system('cls')
    display_health(player, enemy)
    if player['health'] <= 0:
        print("\nGame Over! You lost. Better luck next time!\n")
        return 0
    elif enemy['health'] <= 0:
        print("\nCongratulations! You defeated the enemy!\n")
        return 1

def level_game_loop(level, player, enemy):
    enemy_level_health = enemy['enemy_base_health'] + 50*level
    enemy['health'] = enemy_level_health
    enemy['enemy_level_health'] = enemy_level_health
    
    while enemy['health'] > 0 and player['health'] > 0:
        os.system('cls')
        print(f'--------level {level}-------------')
        display_health(player, enemy, enemy_level_health)
        handle_player_turn(enemy)
        if enemy['health'] > 0:
            handle_enemy_turn(player)

def start_game():
    restart = 'y'
    while restart == 'y':
        os.system('cls')
        player = {'health': 500}
        enemy = {
            'health': 300,
            'enemy_base_health': 300
        }

        for level in range(1, 6):
            level_game_loop(level, player, enemy)
            win = handle_level_result(player, enemy) 
            if not win:
                break  
            
        restart = handle_game_restart()    

if __name__ == '__main__':
    start_game()
