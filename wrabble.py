### Wrabble 01-10-2024 ***

# Imports and Global Variables
import random
import time
from words_list import WORDS_ARRAY
from logo import wrabble_logo
from tiles import STARTING_TILES
FIVE_CURRENT_TILES = []
five_current_letters = []
five_current_points = []
USED_TILES = []
NEXT_TILE = []
MADE_WORDS = []
MADE_POINTS = []
PLAYER_SCORE = 0
TIME_DELAY = 3

##### FUNCTION #1 - TILE AUDIT #####
def tile_audit():
    print("*" * 18, " START OF TILE AUDIT ", "*" * 18)
    print("--- 5 current tiles are: ---")
    for tile in FIVE_CURRENT_TILES:
        print(tile)
    print("--- Next tile is: ---")
    print(NEXT_TILE)
    print(f"--- Starting tiles left: {len(STARTING_TILES)} ---")
    for tile in STARTING_TILES:
        print(tile)
    print(f"--- Used tiles: {len(USED_TILES)} ---")
    for tile in USED_TILES:
        print(tile)
    print("TOTAL LETTERS:")
    print(len(FIVE_CURRENT_TILES) + len(NEXT_TILE) + len(STARTING_TILES) + len(USED_TILES))
    print("*" * 19, " END OF TILE AUDIT ", "*" * 19)

##### FUNCTION #2 - FILL FIVE TILES #####
def fill_five_tiles():
    while len(FIVE_CURRENT_TILES) < 5:
        if len(STARTING_TILES) == 0:  # Check if starting_tiles is empty before trying to draw
            return False  # Return False if no more tiles are left
        new_tile = random.choice(STARTING_TILES)
        STARTING_TILES.remove(new_tile)
        FIVE_CURRENT_TILES.append(new_tile)  # Add the new tile to five_current_tiles
    return True  # Return True if tiles were successfully filled

##### FUNCTION #3 - GET NEXT TILE #####
def get_next_tile():
    if len(STARTING_TILES) > 0:
        new_tile = random.choice(STARTING_TILES)
        STARTING_TILES.remove(new_tile)
        NEXT_TILE.append(new_tile)
    else:
        NEXT_TILE.clear()  # Ensure NEXT_TILE is empty if no more tiles are available

##### FUNCTION #4 - MOVE NEXT TILE to 5 TILES #####
def move_next_tile_to_5_tiles():
    if len(NEXT_TILE) > 0:
        FIVE_CURRENT_TILES.append(NEXT_TILE[0])
        NEXT_TILE.clear()
    else:
        print("No next letter to move to the current letters.")

##### FUNCTION #5 - GET LETTERS[1] AND POINTS[2] FROM TILES #####
def convert_five_tiles_to_letters_and_points():
    global five_current_letters
    global five_current_points
    five_current_letters = [tile[1] for tile in FIVE_CURRENT_TILES]
    five_current_points = [tile[2] for tile in FIVE_CURRENT_TILES]
    tile_number = 0
    print("Your letters are:")
    for tile in five_current_letters:
        print(f"{five_current_letters[tile_number]} = {five_current_points[tile_number]} points")
        tile_number += 1
def convert_next_tile_to_letters_and_points():
    if len(NEXT_TILE) > 0:
        next_letter = NEXT_TILE[0][1]
        next_letter_points = NEXT_TILE[0][2]
        print("The next letter is:")
        print(f"{next_letter} = {next_letter_points} points")
        print("*" * 50)
    else:
        print("The next letter is:")
        print("--- No next letter available ---"
              "")
        print("*" * 50)

##### FUNCTION 6: SHOW MADE WORDS #####
def show_made_words_and_score():
    print(f"Total Points: {PLAYER_SCORE}")
    print("Words Played:")
    word_number = 0
    for word in MADE_WORDS:
        print(f"{word_number + 1}. {MADE_WORDS[word_number]} = {MADE_POINTS[word_number]} points")
        word_number += 1
    print("*" * 50)

##### FUNCTION 7: END GAME #####
def end_game():
    time.sleep(TIME_DELAY)
    print("##### GAME OVER: THERE ARE NO MORE TILES LEFT #####")
    print("Thanks for playing:")
    print(wrabble_logo)
    show_made_words_and_score()  # Display final score and words made


##### FUNCTION 8: SHOW REMAINING TILES
def show_remaining_tiles():
    # Full set of possible letters (A to Z)
    all_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    tile_counts = {letter: 0 for letter in all_letters}  # Initialize all counts to 0

    # Count occurrences of each letter in STARTING_TILES
    for tile in STARTING_TILES:
        letter = tile[1]  # Assuming letter is at position [1]
        tile_counts[letter] += 1

    # Display the counts of each letter
    print(f"Remaining Letters: {len(STARTING_TILES)}")
    for letter in all_letters:
        print(f"{letter}:{tile_counts[letter]}", end=" ")
    print() # For a new line
    print("-" * 50)

#####################################################################################
################################# INTRO #############################################
print("Let's play")
print(wrabble_logo)
print("-" * 50)

# Give player 5 letters
fill_five_tiles()

# Get next letter
get_next_tile()

################################# BEGIN GAME ########################################

##### MAIN GAME LOOP #####
game_on = True
while game_on:

    # Show player their tiles + next letter
    show_remaining_tiles()
    convert_five_tiles_to_letters_and_points()
    convert_next_tile_to_letters_and_points()

    # Are there at least 5 letters left?
    if len(FIVE_CURRENT_TILES) < 5:
        game_on = False
        end_game()
        break
    else:
        ##################### GET USER DECISION #########################################
        player_choice = input("Would you like to:\n(1) Play a Word\n(2) Delete a Letter\n(3) Shuffle Letters\n(4) End Game\n")
        print("*" * 50)

        ##################### OPTION 1: USER PLAYS A WORD ###############################
        if player_choice == "1":
            # Ask player to enter their word
            your_word = input("Make your word:\n").upper()

            # Possibility 1: Word is not 5 letters
            if len(your_word) != 5:
                print(f"Error: Your word {your_word} is not 5 letters long.")
                print("-" * 50)
                time.sleep(TIME_DELAY)

            # Possibility 2: Word is 5 letters but uses different letters to what player has
            elif sorted(your_word) != sorted(five_current_letters):
                print(f"Error: your word {your_word} does not use the letters "
                      f"{FIVE_CURRENT_TILES[0][1]}{FIVE_CURRENT_TILES[1][1]}"
                      f"{FIVE_CURRENT_TILES[2][1]}{FIVE_CURRENT_TILES[3][1]}"
                      f"{FIVE_CURRENT_TILES[4][1]} ")
                print("-" * 50)
                time.sleep(TIME_DELAY)

            # Possibility 3: Word used 5 letters player has but is NOT a word
            elif your_word not in WORDS_ARRAY and sorted(your_word) == sorted(five_current_letters):
                print(f"Sorry, your word '{your_word}' is not a valid word")
                print("-" * 50)
                time.sleep(TIME_DELAY)

            # Possibility 4: User plays a valid word
            elif your_word in WORDS_ARRAY and sorted(your_word) == sorted(five_current_letters):
                # Add up word points
                word_points = 0
                for tile in five_current_points:
                    word_points += tile

                # Add word points to player score
                PLAYER_SCORE += word_points
                print(f"Success!! You made the word '{your_word}' for {word_points} points!!")
                print("-" * 50)

                # Add word to List of MADE_WORDS
                MADE_WORDS.append(your_word)

                # Add word points to the MADE_POINTS list
                MADE_POINTS.append(word_points)

                # Show made words and score
                show_made_words_and_score()

                # Add tiles to USED_TILES
                for tile in FIVE_CURRENT_TILES:
                    USED_TILES.append(tile)

                # Clear out FIVE_CURRENT_TILES
                FIVE_CURRENT_TILES.clear()

                # Move NEXT_TILE to FIVE_CURRENT_TILES and clear out NEXT_TILE
                move_next_tile_to_5_tiles()

                # Fill up FIVE_CURRENT_TILES so it has 5 tiles
                if not fill_five_tiles():  # Check if there are no more tiles left
                    game_on = False
                    end_game()
                    break

                # Get a new NEXT_TILE after the old one has been moved
                get_next_tile()

                time.sleep(TIME_DELAY)

        elif player_choice == "2":
            # Ask player to enter which letter to delete:
            letter_to_delete = input(f"Which letter would you like to delete from these?\n"
                                    f"{FIVE_CURRENT_TILES[0][1]}{FIVE_CURRENT_TILES[1][1]}"
                                    f"{FIVE_CURRENT_TILES[2][1]}{FIVE_CURRENT_TILES[3][1]}"
                                    f"{FIVE_CURRENT_TILES[4][1]}\n").upper()

            # Check letter is in the five_current_letters
            if letter_to_delete not in five_current_letters:
                print(f"Error: The letter {letter_to_delete} is not one of your 5 letters.")
                print("-" * 50)
                time.sleep(TIME_DELAY)
            else:
                # Find the tile that matches the letter entered by the user
                found_tile = None
                for tile in FIVE_CURRENT_TILES:
                    if tile[1] == letter_to_delete:  # Check if the second item matches the letter
                        found_tile = tile

                        # Inform user of the deletion
                        if NEXT_TILE:  # Check if NEXT_TILE is not empty
                            print(f"You deleted {found_tile[1].upper()} for {NEXT_TILE[0][1]}")
                        else:
                            print(f"There are no more tiles available.")
                        print("-" * 50)

                        # Remove that tile from FIVE_CURRENT_TILES
                        FIVE_CURRENT_TILES.remove(found_tile)

                        # Add that tile to USED_TILes
                        USED_TILES.append((found_tile))

                        # Move NEXT_TILE into FIVE_CURRENT_TILES
                        move_next_tile_to_5_tiles()

                        # Get a new NEXT_TILE after the old one has been moved
                        get_next_tile()

                        # Exit the loop when the tile is found
                        ## This ensures only ONE instance of the letter is deleted
                        break
                time.sleep(TIME_DELAY)

        elif player_choice == "3":
            random.shuffle(FIVE_CURRENT_TILES)
            time.sleep(TIME_DELAY)

        elif player_choice == "4":
            game_on = False
            print("-" * 50)
            print("***** GAME OVER: YOU HAVE ENDED THE GAME *****")
            show_made_words_and_score()
            print("-" * 50)

