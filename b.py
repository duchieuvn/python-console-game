import random
import time
import msvcrt
import os

def get_random_words():
    
    random_words = random.sample(wordlist, 3)
    return random_words

def get_word_points(random_words):
    points = {}
    for word in random_words:
        l = len(word)
        points[word] = l * 10 + random.randint(-l * 2, l * 2)
    return points

def display_health(level, player, enemy):
    player_health = 0 if player['health'] < 0 else player['health']
    enemy_health = 0 if enemy['health'] < 0 else enemy['health']
    print(f"-------------------------- LEVEL {level} --------------------------")
    print(f"Player: {player_health:3}/500   {'=' * (player_health // 10)}")
    print(f"Enemy : {enemy_health:3}/{enemy['enemy_level_health']}   {'=' * (enemy_health // 10)}")
    print("-------------------------------------------------------------------")

def display_words(word_points):
    print(">>> Type one of these words:")
    for word, points in word_points.items():
        print(f"  {word:15} => {points:3} damage")
    print("\n========================================================")

def get_user_input(timeout):
    print(f"You have {timeout} seconds to type", flush=True)
    start_time = time.time()
    typed_word = ""

    while time.time() - start_time < timeout:
        if msvcrt.kbhit():  
            char = msvcrt.getwch()  
            if char == "\r":  
                print()  
                return typed_word.strip()
            elif char == "\b":  
                typed_word = typed_word[:-1]
                print("\b \b", end="", flush=True)  
            else:
                typed_word += char
                print(char, end="", flush=True) 

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
    restart = input("Do you want to play again? (y/n): ").strip().lower()
    if restart == "y":
        print("\nRestarting the game...\n")
    else:
        print("\nThanks for playing! Goodbye!")

    return restart

def display_winning_message():
    winning_banner = r"""
        ===========================
        |||||||||||||||||||||||||||
        ||        YOU WIN        ||
        ||        YOU WIN        ||
        ||        YOU WIN        ||
        ||        YOU WIN        ||
        ||        YOU WIN        ||
        |||||||||||||||||||||||||||
        ===========================
    """
    print(winning_banner)
    time.sleep(4)

def display_losing_message():
    winning_banner = r"""
        ==========================
        ||||||||||||||||||||||||||
        ||       GAME OVER      ||
        ||       GAME OVER      ||
        ||       GAME OVER      ||
        ||||||||||||||||||||||||||
        ===========================
    """
    print(winning_banner)
    time.sleep(4)

def handle_level_result(level, player, enemy):
    os.system("cls")
    display_health(level, player, enemy)

    if player['health'] <= 0:
        display_losing_message()
        return 0
    elif enemy['health'] <= 0:
        display_winning_message()
        return 1

def level_game_loop(level, player, enemy):
    enemy_level_health = enemy['base_health'] + 50*level
    enemy['health'] = enemy_level_health
    enemy['enemy_level_health'] = enemy_level_health

    player['health'] = player['base_health']
    
    while enemy['health'] > 0 and player['health'] > 0:
        os.system("cls")
        display_health(level, player, enemy)
        handle_player_turn(enemy)
        if enemy['health'] > 0:
            handle_enemy_turn(player)

def game_innit():
    player = {
            "health": 500,
            "base_health": 500
            }
    enemy = {
        "health": 300,
        "base_health": 100
    }

    file_path = "a2.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        words = file.readlines()

    wordlist = [word.strip() for word in words]

    return wordlist, player, enemy

wordlist, player, enemy = game_innit()

def start_game():
    restart = "y"
    while restart == "y":
        os.system("cls")
        
        for level in range(1, 6):
            level_game_loop(level, player, enemy)
            win = handle_level_result(level, player, enemy) 
            if not win:
                break  
            
        restart = handle_game_restart()    

if __name__ == "__main__":
    start_game()
