import random
from colorama import Fore

def choose_word():
    #chooses a random number and uses that to select a word. The range is determined by the length of the list and the chosen word is passed back out.
    r_num = random.randint(0,len(word_list))
    chosen_word = word_list[r_num]
    chosen_word = "tests"
    return chosen_word

def guessing_method(c_word):
    #Will be used later but these are the lists that will contain the correct letters guessed by the player. I may have found a way to ignore this but it may just be
    #due to how the program is currently written. The loop might have issues displaying the old guesses if it isn't saved to a list.
    #One of the changes will be to move over to a message box to display the colors on the letters.
    wrong_letters = []
    misplaced_letters = []
    num_of_misplaced = {}

    #Variables to keep track of the number of turns and the current turn as well as a variable for the user's guess itself.
    maximum_turns = 5
    current_turn = 0
    print("There are five letters in the chosen word.")
    print("You have "+str(maximum_turns)+" Guesses to submit the correct word.")
    guess = ""

    #Loops through until the user has guessed 5 times or breaks out of the loop early if the guess is correct.
    while guess != c_word and current_turn !=5:
        guess = input("What is your Guess?\n")
        guess = guess.lower()
        #Checks to see if the guess contains any invalid non alphabet characters before continuing to see if it is the correct guess.
        if guess == c_word:
            print("Congratulations! You guessed the word!")
            exit()
        elif guess.isalpha() and len(guess) == 5:
            #Loops through and compares each letter in the guess with the letters in the chosen word.
            for i in range(5):
                #If the letter is the same and in the same position it displays as green.
                if guess[i] == c_word[i]:
                    print(Fore.GREEN + guess[i]+ Fore.RESET, end="")
                    if guess[i] in misplaced_letters:
                        misplaced_letters.remove(guess[i])
                    i += 1
                #If its the same but not in the correct position then it is yellow and adds it to the list of misplaced letters
                elif guess[i] in c_word and guess[i] != c_word[i]:
                    print(Fore.YELLOW + guess[i] + Fore.RESET, end="")
                    letter_count = c_word.count(guess[i])
                    if guess[i] not in misplaced_letters:
                        misplaced_letters.append(guess[i])
                    if guess[i] in misplaced_letters and guess[i] not in num_of_misplaced:
                        num_of_misplaced[guess[i]] = 1
                        print(str(num_of_misplaced[guess[i]]))
                    elif guess[i] in misplaced_letters and guess[i] in num_of_misplaced:
                        if num_of_misplaced[guess[i]] < letter_count:
                            num_of_misplaced[guess[i]] = num_of_misplaced[guess[i]] +1
                            print(str(num_of_misplaced[guess[i]]))
                    i += 1
                #Otherwise it is grey and it adds the letter to the list of letters not present in the word.
                else: 
                    print(Fore.WHITE + guess[i] + Fore.RESET, end="")
                    if guess[i] not in wrong_letters:
                        wrong_letters.append(guess[i])
                    i += 1  

            #Increments the current turn and reports that the user made an incorrect guess
            current_turn +=1
            print("\n"+"Incorrect Guess. Try again.")
            print("You have "+str(maximum_turns - current_turn)+" Guesses left.")
            print(num_of_misplaced)

            #Prints the list of Misplaced letters in the word and the list of guessed letters that aren't in the word so the user can keep track of previous guesses better.
            print("Misplaced Letters: ", end="")
            print(misplaced_letters)
            print("Wrong Letters: ", end="")
            print(wrong_letters)

        #Exits the program if the user submits a command to stop the game.
        elif guess == "quit" or guess == "end" or guess == "stop" or guess == "exit":
            exit()
        #Otherwise prints the message that the guess contained invalid characters or was an incorrect length.
        else:
            print("Invalid Guess.")
            current_turn +=1
    #prints the failure message if the loop was exited and the word was not guessed.
    if guess !=c_word:
        print("You have failed to guess the word: "+ c_word +" within five attempts. Restart the game to try again.")


#Opens and reads the words.txt file putting the data from it in the varible named words.
path = r"Word Guessing Game\words.txt"
file = open(path, "r")
words = file.read()
words = words.lower()

#Splits the data obtained from the words.txt file into individual 5 letter words.
word_list = words.split("\n")

#Calls the choose_word function
c_word = choose_word()

confirm = input("Are you ready to Play?")
if confirm == "Yes" or confirm == "yes":
    guessing_method(c_word)
else:
    print("Good Bye!")
    exit()