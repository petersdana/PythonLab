#FLAMES is a popular game named after the acronym: Friends, Lovers, Affectionate, Marriage, Enemies, Sibling.
# This game does not accurately predict whether or not an individual is right for you, but it can be fun to play this with your friends.
#There are two steps in this game:
#Take the two names.
#Remove the common characters with their respective common occurrences.
#Get the count of the characters that are left .
#Get the result :
#Take FLAMES letters as [“F”, “L”, “A”, “M”, “E”, “S”]
#Start removing letter using the count we got.
#The letter which last the process is the result.
#Problem statement copied from geeksforgeeks.org
#Program written by Vandana Rao on 20 Nov, 2019, Wednesday

print ("\n\t Welcome to FLAMES")
name1 = input ("\nEnter the first name: ")
name1 = name1.lower()
name2 = input ("\nEnter the second name: ")
name2 = name2.lower()

len1 = len(name1)
len2 = len(name2)

if len1 >= len2:
    longer_name = name1
    shorter_name = name2
else:
    longer_name = name2
    shorter_name = name1


count_common_letter = 0
#print ("\n", comp_name)
for letter in shorter_name:
    #print ("\n",letter)
    count = 0
    while count < len(longer_name):
        #print ("\n In while: ",longer_name[count])
        if letter == longer_name[count]:
            count_common_letter= count_common_letter+1
            longer_name = longer_name[:count]+longer_name[count+1:]
            #print ("\n Name to compare",longer_name)
            break
        else:
            count = count+1
            continue

#print ("\n", count_common_letter)

total_length = len1 + len2
game_length = total_length - (2*count_common_letter)

#print ("\n length",game_length)
flames = "FLAMES"



if game_length > len(flames):
    ini_count_to_strike = game_length - len(flames)
else:
    ini_count_to_strike = game_length

count_to_strike = ini_count_to_strike

count = 0


while count < total_length:

    if count_to_strike > len(flames):
        count_to_strike = count_to_strike - len(flames)
    else:
        count_to_strike = ini_count_to_strike


    #print ("\n", count_to_strike)

    flames = flames[count_to_strike:] + flames[:count_to_strike-1]
    #print ("\n",flames)
    count = count + 1

    if len(flames) == 2:
        if count_to_strike%2 ==1 :
            flames = flames[0]
        else:
            flames = flames[1]

    if len(flames) == 1:
        break
    else:
        continue

#print ("\n Result: ", flames)

full_form = ["Friends","Lovers","Affectionate","Marry","Enemy","Sibling"]
for letter in full_form:
    #print ("\n",letter[0])
    if flames == letter[0]:
        print ("\n RESULT: ",letter,"\n")
