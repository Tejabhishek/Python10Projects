'''Program to generate n names of 3 letters randomly based on user input

Output:
What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter.v
What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter.c
What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter.a
ila
isa
ufa
ona
axa
ama
eka
aha
era
uba
isa
eya
ada
ewa
ata
ura
aza
ula
ofa
ana

Process finished with exit code 0



'''


import random,string

vowels ='aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters=string.ascii_lowercase

letter_input_1=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter.")
letter_input_2=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter.")
letter_input_3=input("What letter do you want? Enter 'v' for vowels, 'c' for consonants, and 'l' for any letter.")


#print(letter_input_1+letter_input_2+letter_input_3)



#Function that generates names of length 3 Letters
def generator():

 #Letter 1 Input
    if letter_input_1 == 'v':
        letter1=random.choice(vowels)
    elif letter_input_1 == 'c':
        letter1 = random.choice(consonants)
    elif letter_input_1 == 'l':
        letter1 = random.choice(letters)
    else:
        letter1=letter_input_1



#Letter 2 Input
    if letter_input_2 == 'v':
        letter2=random.choice(vowels)
    elif letter_input_2 == 'c':
        letter2 = random.choice(consonants)
    elif letter_input_2 == 'l':
        letter2 = random.choice(letters)
    else:
        letter2=letter_input_2

# Letter 3 Input
    if letter_input_3 == 'v':
        letter3=random.choice(vowels)
    elif letter_input_3 == 'c':
        letter3 = random.choice(consonants)
    elif letter_input_3 == 'l':
        letter3 = random.choice(letters)
    else:
        letter3=letter_input_3


#Concatenating all 3 letters
    name = letter1+letter2+letter3
    return (name)


# calling function generator and printing the return value

numberoNames=int(input("Please Enter how many number of names you need:"))
for i in range(numberoNames):
    print(i+1,".",generator())