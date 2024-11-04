#PRACTICAL 6
''' Read a text file and display the number of vowels
/consonants/uppercase/lowercase characters in the file'''
def count_characters():
    vowels = "aeiouAEIOU" # Initialize counters
    num_vowels = 0
    num_consonants = 0
    num_uppercase = 0
    num_lowercase = 0
    f=open("poem.txt", 'r')
    for line in f:
        for char in line:
            if char.isalpha():# Check if the char is an alphabet
                if char in vowels:
                    num_vowels += 1
                else:
                    num_consonants += 1
                if char.isupper():
                   num_uppercase += 1
                elif char.islower():
                     num_lowercase += 1
    print("Number of vowels: ",num_vowels)
    print("Number of consonants: ",num_consonants)
    print("Number of uppercase characters: ",num_uppercase)
    print("Number of lowercase characters: ",num_lowercase)
count_characters()
