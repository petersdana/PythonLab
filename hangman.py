#Hangman game
#Created on 18th Nov, 2019, Monday by Vandana Rao
import random

print ("\n Welcome to the game - Hangman!")
print ("\n The computer has four categories of words. You can choose any one category.")
print ("\n The computer will select a word from that category for the player to guess. ")
print ("\n The player will get 10 chances to guess the word correctly ")

player = input ("\n\n Enter your name: ")
print ("\n Hi,",player,"! Let\'s play Hangman!")

category = input ("\n\n Enter the catergory you would like to play - \'fruit\', \'country\',\'animal\',\'thing\': ")
category = category.lower()
print ("\n",category)

#Check if Category enetered is correct
if category != 'fruit' and category != 'country' and category != 'animal' and category != 'thing':
    print ("\n Please enter the category correctly")
    exit ()

if category == 'fruit':
    game_word = ["mango","strawberry","apple","banana","jackfruit","guava","pineaplle","grape","orange","watermelon","pear","plum"]
elif category == 'country':
    game_word = ["india","england","russia","nigeria","venezuela","canada","australia","singapore","dubai","egypt","france","combodia"]
elif category == 'animal':
    game_word = ["tiger","panda","buffalo","orangutan","goat","elephant","bear","deer","lion","antelope","hyena","giraffe","hippopotamus"]
elif category == 'thing':
    game_word = ["fan","refrigerator","door","lamp","knife","bicycle","mobile","computer","utensil","laptop","machine","clock"]

#r_number = input ("\n Enter a number between 0 to 12: ")
#r_number = int(r_number)

#print (game_word [r_number])

#main_word = game_word [r_number]
main_word = random.choice(game_word)
l_word = len(main_word)

print_word = '_'

i=0
while i < l_word-1:
  print_word = print_word + '_'
  i = i + 1

print ("\n Guess the letters in the word: ", print_word)

chance = 0

#print_word = ' '
while chance < 15:
    g_letter = input("\n Enter a letter: ")
    g_letter = g_letter.lower()
    count = 1
    for letter in main_word :

        if letter == g_letter:
            #print ("\n At check point 1", print_word, count,print_word[:count-1], print_word[count+1:])
            if count == 1:
                print_word =  g_letter + print_word[count:]
                #print ("\n At check point 1", print_word, count)
            elif count > 1 and count < len(main_word):
                #print ("\n At check point 2", print_word[0:count-1], count, print_word[count:len(main_word)])
                print_word = print_word[0:count-1] + g_letter + print_word[count:len(main_word)]
                #print ("\n At check point 2_1", print_word)
            else:
                print_word = print_word[:count-1] + g_letter
                print ("\n At check point 3", print_word, count)
        else:
            print_word = print_word
            #print ("\n At check point 4", print_word, count)
        count = count + 1

    print ("\n", print_word)
    chance = chance + 1
    if chance == 15:
        print ("\n All chances over. Man is Hanged! :( ")
    if print_word == main_word:
        print ("\n You won!!")
        break
