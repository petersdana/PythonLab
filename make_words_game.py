#Given a word, the game involves making as many words as possible using minimum 3 letters 
#to a maximum of all the letters in the wordof the given word. 
#If a player makes more words than in the reference dictionary (common english words), he gets bonus points
#If a player enters wrong words, points are not given
#Points are basically in the form of percentages
#Created by Vandana Rao on 2 Dec, 2019, Monday

i_string = input("\n Enter the letters in sequence without any delimiters: ")
i_string = i_string.upper()

l_blank_word = len(i_string)

j_words = list()
l=3

#Making all possible words less than or equal to (but greater than 2) from the given word
while l <= l_blank_word:

    dictionary = open ("common_words_eng.txt") # Easy and fewer words

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

        if j_match == l and d_word != i_string:
            j_words.append(d_word)

    l = l + 1

l=3

j_add_words = list()
#Making all possible words less than or equal to (but greater than 2) from the given word
while l <= l_blank_word:
    #print ("\n", l,l_blank_word)
    #if level == 'D':
    dictionary = open ("dictionary.txt") # Easy and fewer words

    for d_word in dictionary:
        d_word = d_word.strip()
        d_word = d_word.upper()
        t_word = i_string
        j_match = 0
    #print ("\n",d_word)


        if len(d_word) == l:
        #print ("\n",t_word,d_word)
            for letter in d_word: #from
                counted = 0
                for j_letter in t_word:#gfrom
                    if j_letter == letter:
                        t_word = t_word[:counted] + t_word[counted+1:] #To eliminate matching repeat letters
                        j_match = j_match + 1
                        break
                    counted = counted + 1

        if j_match == l and d_word != i_string:
            j_add_words.append(d_word)

    l = l + 1

#print("\n Possible words from the given words are: ",j_words)
#Creating a histogram of words as per their word length
w_freq = {}
length = 0
freq = 0
while length <= l_blank_word:
    for word in j_words:
        #print ("\n", length)
        if len(word) != length:
            continue
        else:
            key = str(length)+'-'+'letter words'
            if key not in w_freq:
                w_freq[key] = 1
            else:
                w_freq[key] = w_freq[key] + 1

    length = length + 1

#print("\n", w_freq)
#Printing the histogram so that the player can make words accordingly
for key in w_freq:
    print ("\n The maximum possible", key, "that can be made from the given word are: ", w_freq[key])


u_words = list(map(str, input("\n Enter possible words greater than 2 letters: ").split()))

#Removing duplicate words from the user list (if any)
temp_list = list()
for words in u_words:
    if words not in temp_list:
        temp_list.append(words)

u_words = temp_list

#print ("\n end",u_words)
#Checking if the words exist in the word list formed by the computer by refering to the dictionary
correct = 0
wrong = 0
bonus = 0
bonus_words = list()
wrong_words = list()
for c_word in u_words:
    c_word = c_word.upper()
    if c_word in j_words:
        correct = correct + 1
    else:
        if c_word in j_add_words:
            bonus = bonus + 1
            bonus_words.append(c_word)
            c_word = c_word.lower()
            u_words.remove(c_word)
            continue
        wrong = wrong + 1
        wrong_words.append(c_word)
        c_word = c_word.lower()
        u_words.remove(c_word)    #Removing the wrong words or words that don't exist in the main list created by the computer
                                #This means that the word is not present in the reference dictionary or is not of the proper length
#print ("\n You got", correct, "correct words and",wrong,"wrong words")
if wrong != 0:
    print ("\n You got",wrong,"wrong words")
    print ("\n The words that are not in the reference dictionary are: ", wrong_words)


#Creating a histogram of words as per their word length (for the user entered words)
uw_freq = {}
length = 0
freq = 0
while length <= l_blank_word:
    for word in u_words:
        #print ("\n", length)
        if len(word) != length:
            continue
        else:
            key = str(length)+'-'+'letter words'
            if key not in uw_freq:
                uw_freq[key] = 1
            else:
                uw_freq[key] = uw_freq[key] + 1

    length = length + 1

#Displaying the histogram in a way that is understandable to the user
#print("\n", uw_freq)
for u_key in uw_freq:
    print ("\n Number of", u_key, "that are correct and entered by you are: ", uw_freq[u_key])

#Calculating the score
all_freq = sum(w_freq.values())
all_u_freq = sum(uw_freq.values())

if all_u_freq > all_freq:
    all_u_freq = all_freq

points = (all_u_freq/all_freq)*100
points = round(points,2)
print ("\n Game Points: ", points)

if points < 100:
    u_words = [x.upper() for x in u_words]
    #print (j_words,"\n", u_words)
    words_to_know = list(set(j_words) - set(u_words))
    print("\n Words which you could have typed: ",words_to_know)

if bonus != 0:
    bonus = bonus*10
    print ("\n Bonus points: ", bonus,"\n")
    print ("\n Bonus words are: ", bonus_words)

print("\n Total Points: ", (bonus + points),"\n")
