#This program gives all possible combinations of words, for a word of given length, from a word that is longer than the required word
#This concept can be used for making all combinations of words from a given long word
#Program steps:
# 1. Enter a word (preferably longer than 3)
# 2. Enter the length of the word which you want to find 
# 3. All possible words of the given length are displayed, which can be made from the letters of the word entered in step 1.
#Created by Vandana Rao on 29 Nov 2019, Friday


i_string = input("\nEnter the letters in sequence with a space in between: ")
i_string = i_string.upper()
l_blank_word = input("\n Enter the number of letters in the word: ")
l_blank_word = int(l_blank_word)

j_words = list()
#j_match = 0

dictionary = open ("dictionary.txt")

for d_word in dictionary:
    d_word = d_word.strip()
    t_word = i_string
    j_match = 0
    #print ("\n",d_word)


    if len(d_word) == l_blank_word:
        #print ("\n",t_word,d_word)
        for letter in d_word: #from
            counted = 0
            for j_letter in t_word:#gfrom
                if j_letter == letter:
                    t_word = t_word[:counted] + t_word[counted+1:] #To eliminate matching repeat letters
                    j_match = j_match + 1
                    break
                counted = counted + 1

    if j_match == l_blank_word:
        j_words.append(d_word)

print("\n Jumble Answer:",j_words)
