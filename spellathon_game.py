#The game is based on the game that appears daily in Times of India
#The orginal game has a center letter surrounded by six other letters in a hexagon
#The player has to make words using more than one letter as well as the center letter.
#Words that don't include the center letter don't qualify as a valid answer.
#One seven letter word has to be formed.
#In this game, the computer generates the word for the puzzle
#If a player spells more than half of the correct answers, he is considered a winner.
#Created by Vandana Rao on 4 Dec, 2019, Wednesday

import random

print ("\n\t Welcome to Spellathon Game")
print ("\n Spell as many words as possible using the center letter. \n\n One word should be a 7 letter word")

#i_string = input("\n Enter a 7 letter word: ")
#i_string = i_string.upper()

# Create a random and shuffled 7-letter word
ref_words = list()
dictionary = open ("dictionary.txt")
for d_word in dictionary:
    d_word = d_word.strip()
    if len(d_word) == 7:
        ref_words.append(d_word)

i_string = random.choice(ref_words)
#print ("\n The puzzle word is: ", i_string)
tup_string = tuple(i_string)
list_string = list(tup_string)
#print ("\n", list_string)
random.shuffle(list_string)
i_string = ''.join(list_string)
print ("\n The puzzle word is: ", i_string)

l_blank_word = len(i_string)

#Getting the middle letter
m_letter = i_string[3]
print ("\n Middle letter:",m_letter)

j_words = list()
l=2

#Making all possible words less than or equal to (but greater than 1) from the given word
while l <= l_blank_word:

    dictionary = open ("dictionary.txt") # Easy and fewer words

    for d_word in dictionary:
        d_word = d_word.strip()
        d_word = d_word.upper()
        t_word = i_string
        j_match = 0
    #print ("\n",d_word)


        if len(d_word) == l:
        #print ("\n",t_word,d_word)
            for letter in d_word:
                counted = 0
                for j_letter in t_word:
                    if j_letter == letter:
                        t_word = t_word[:counted] + t_word[counted+1:] #To eliminate matching repeat letters
                        j_match = j_match + 1
                        break
                    counted = counted + 1

        if j_match == l and m_letter in d_word: #The middle letter of the puzzle word should be a part of the word
            if d_word != i_string:
                j_words.append(d_word)

    l = l + 1

#print("\n Spellathon Answer:",j_words,"\n")

comp_length = len(j_words)

u_words = list(map(str, input("\n Enter possible words greater than 1 letter and using the middle letter: ").split()))

#Removing duplicate words from the user list (if any)
temp_list = list()
for words in u_words:
    words = words.upper()
    if words not in temp_list:
        temp_list.append(words)

u_words = temp_list

#print ("\n end",u_words)
#Checking if the words exist in the word list formed by the computer by refering to the dictionary
correct = 0
wrong = 0
wrong_words = list()
for c_word in u_words:
    if c_word in j_words:
        correct = correct + 1
    else:
        wrong = wrong + 1
        wrong_words.append(c_word)
        u_words.remove(c_word)    #Removing the wrong words or words that don't exist in the main list created by the computer
                                #This means that the word is not present in the reference dictionary or is not of the proper length
#print ("\n You got", correct, "correct words and",wrong,"wrong words")
if wrong != 0:
    print ("\n You got",wrong,"wrong words")
    print ("\n The words that are not in the reference dictionary are or don't include the middle letter: ", wrong_words)


user_length = len(u_words)

if user_length == comp_length:
    print ("\n Congratulations! You are a walking dictionary!! You got all the words correctly.")
elif user_length >= (comp_length/2):
    print("\n Congratulations! You know your words well! You got: ", user_length,"words out of",comp_length,"words correct")
else:
    print ("\n You can do better! Best of luck for the next try! You got: ", user_length,"words out of",comp_length,"words")

if user_length != comp_length:
    words_to_know = list(set(j_words) - set(u_words))
    print("\n Words which you could have typed: ",words_to_know, "\n")
