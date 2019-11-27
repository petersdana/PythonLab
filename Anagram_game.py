#In the Anagram game, the computer gives a valid dictionary word as per the length and level entered by the user.
#The player has to input just one valid anagram existing in the dictionary.
#If the player gets even one anagram correct he wins.
#All valid anagrams are displayed irrespective of whether the player wins or loses.
#Created by Vandana Rao on 27th Nov, 2019, Wednesday

import random

print ("\n\t THE ANAGRAM GAME")


checker = 0
word = 'null'
total_points = 0
c_attempts = 0
w_attempts = 0
u_ana_word = 'null'
r_check = 1


while u_ana_word != 'Q':
    while r_check == 1:
        w_length = input ("\n Enter word length: ")
        try:
            w_length = int(w_length)
        except:
            print ("\n Enter a valid number. \n")
            continue
        if w_length >= 16:
            print ("\n Exceeds the maximum length of a word in the dictionary. Please enter any number less than 16\n")
        if w_length <= 1:
            print ("\n Please enter a number more than 1\n")
        break
    while r_check == 1:
        if w_length == 2: #A two letter word can have only 1 anagram, so level automatically changes to difficult i.e only one or two anagrams are available
            level = 3
        else:
            level = input ("\n Enter the difficulty level. 1) Easy 2) Medium 3) Difficult : ")
        try:
            level = int(level)
        except:
            print ("\n Enter a valid number without any special characters. \n")
            continue
        if level < 1 or level > 3:
            print ("\n Enter level between 1 to 3 only \n")
        break

#Checker is to let the computer keep searching for a valid random word from the dictionary as per the user requirements.
    dictionary = open ("dictionary.txt")
    word_list = list()
    while checker == 0:
        for a_word in dictionary:
            a_word = a_word.strip()
            if len(a_word)== w_length:
                word_list.append(a_word)

        word = random.choice(word_list)  # Picking up a random word
        l_word = len(word)
        ana_words = list()

        dictionary = open ("dictionary.txt")

#Checking the anagrams of the word
        for d_word in dictionary:
            d_word = d_word.strip()
            t_word = word
            match = 0

            if len(d_word) == l_word:
                for d_letter in d_word:
                    counted = 0
                    for letter in t_word:
                        if letter == d_letter:
                            t_word = t_word[:counted] + t_word[counted+1:]
                            match = match + 1
                            break
                        counted = counted + 1


            if match == l_word:
                if d_word != word: # Making sure that the word itself doesn't appear in the list of anagrams
                    ana_words.append(d_word) #Creating a list of anagrams

    #Checking if the random word suits the difficulty level
        if len(ana_words)== 0:
            checker = 0
        elif level == 3 and len(ana_words) >= 2:
            checker = 0
        elif level == 2 and (len(ana_words) <= 2 or len(ana_words) >= 4):
            checker = 0
        elif level == 1 and len(ana_words) <= 4:
            checker = 0
        else:
            break

    print ("\n Find the anagram for: ", word)

    u_ana_word = input ("\n Input the anagram: ")
    u_ana_word = u_ana_word.upper()
    if u_ana_word == 'Q':
        print("\n Your total score is:",total_points)
        print("\n You have",c_attempts,"correct attempts and",w_attempts,"wrong attempts")
        print("\n Hope to play with you soon!\n")
        quit()
    if u_ana_word in ana_words: #Checking whether the answer is present in the list of anagrams
        print("\n The entered anagram is correct!\n\n Congratulations! You scored 5 points \n\n Set of possible anagrams is:", ana_words)
        total_points = total_points + 5
        c_attempts = c_attempts + 1
        print("\n Your total score is:",total_points)
        print("\n You have",c_attempts,"correct attempts and",w_attempts,"wrong attempts")
    else:
        print ("\n You have entered the wrong anagram.\n\n You could have chosen from the following:", ana_words)
        w_attempts = w_attempts + 1
        print("\n Your total score is:",total_points)
        print("\n You have",c_attempts,"correct attempts and",w_attempts,"wrong attempts")
