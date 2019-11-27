#Enter a word whose anagram you would like to know
#The computer gives a set of valid and meaningful anagrams

word = input ("\n Enter a word: ")
word = word.upper() # To match dictionary format
l_word = len(word)


ana_words = list()

dictionary = open ("dictionary.txt")

for d_word in dictionary:
    d_word = d_word.strip()
    t_word = word
    match = 0

    if len(d_word) == l_word:
        for d_letter in d_word:
            counted = 0
            for letter in t_word:
                if letter == d_letter:
                    t_word = t_word[:counted] + t_word[counted+1:] #To eliminate matching repeat letters
                    match = match + 1
                    break
                counted = counted + 1


        if match == l_word:
            if d_word != word:
                ana_words.append(d_word)



print("\n Anagrams of the given word are: ", ana_words)
print ("\n Total no. of meaningful anagrams are: ", len(ana_words),"\n")
