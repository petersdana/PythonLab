#Created to solve the daily answers for JUMBLE word game in the daily newspaper
#Program steps:
#  1. Enter the letters (circled letters in JUMBLE)
#  2. Enter the number of words in the phrase
#  3. Enter the word-length of each word (in sequence)
#  4. After the set of variations for the first word is found, user is asked to enter the most appropriate of the words
#  5. Repeat the program to get the next words in the phrase
#  6. The probable phrase is displayed as per the selected user-answers
#  7. The program iterates until the user finds a suitable phrase that matches the JUMBLE answer (which suits the picture best).

#Created to solve the daily answers for JUMBLE word game in the daily newspape
#Created to solve the daily answers for JUMBLE word game in the daily newspape
i_string = input("\n Enter the letters in sequence without any delimiters in between: ")
i_string = i_string.upper()

n_words = input("\nEnter number of words in the phrase: ")
n_words = int(n_words)

l_blank_word = list()
i = 0
j_phrase = list()
#t_i_string = i_string

def split(word):
    return [char for char in word]

while i < n_words:
    vl_blank_word = input("\n Enter the number of letters in the word: ")
    vl_blank_word = int(vl_blank_word)
    l_blank_word.append(vl_blank_word)
    i=i+1

#l_blank_word.sort()
j_words = list()
t_o_letters = list()
#j_match = 0

a = 0
rem_string = ""
j_answer = list()
c_word = ""
ans_found = "N"

while ans_found != 'Y':
    while a < n_words:
        dictionary = open ("dictionary.txt")
        #print ("\n counter:", a)
        #print("\n length",l_blank_word[a])

        if a == 0:
            t_i_string = i_string
        else:
            t_i_string = rem_string
        #print("\n",t_i_string)
        for d_word in dictionary:
        #print("\n length2",l_blank_word[d])
            l_wwn = l_blank_word[a]
            d_word = d_word.strip()
            t_word = t_i_string
            j_match = 0
    #print ("\n",d_word)


            if len(d_word) == l_wwn:
        #print ("\n",t_word,d_word)
                for letter in d_word: #from
                    counted = 0
                    for j_letter in t_word:#gfrom
                        if j_letter == letter:
                            t_word = t_word[:counted] + t_word[counted+1:] #To eliminate matching repeat letters
                            j_match = j_match + 1
                            break
                        counted = counted + 1

            if j_match == l_wwn:
                j_words.append(d_word.strip())
                t_o_letters.append(t_word)

        if len(j_words) != 0:
            print ("\n Set of possible variations of one of the words from the phrase is : ", j_words)
        else:
            print ("\n Variations not possible for the word-length: ", l_wwn)
            break

    #print ("\n Corresponding letters left:",t_o_letters)
        if len(j_words)!= 1:
            cd_word = input("\n Choose the most suitable word from the above array: ")
            cd_word = cd_word.upper()
            print("\n",cd_word)

    #tt_i_string = i_string

            tt_i_array = list()
            s=""


            if cd_word in j_words:
        #print("\n YESS!!")
                j_answer.append(cd_word)
                tt_i_string = t_i_string
                tt_i_array = list(tt_i_string)
                #print ("\n temp", tt_i_array)
                for letter in cd_word:
                    tt_i_array.remove(letter)
                #if a != (n_words-1):
                    rem_string = s.join(tt_i_array)
                print("\n Remaining letters are: ", tt_i_array)
            else:
                print("\n Entered word is wrong. Re-enter correctly")

        elif len(j_words) == 1:
        #print("\n Here 1")
            j_answer.append(j_words[0])
        elif len(j_words)== 0:
            print("\n No possible variations found")

        j_words.clear()
        a=a+1

    print("\n The phrase can be made up from a combination of these words: ",j_answer)

    ans_found = input("\n Did you find the required answer? ")
    ans_found = ans_found.upper()
    if ans_found == 'Y':
        print("\n I am a genius!\n")
        break
    elif ans_found == 'N':
        a = 0
        j_answer.clear()
        continue
    else:
        print("\n Entered answer is not valid. But assuming you are satisfied \n")
        break
