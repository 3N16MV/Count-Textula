#
# Alexis '3N1GMV' Lariviere
# CYB216-10692 Final Project
# 04FEB2024
# 'Count Textula' Word Frequency Counter
# Written in Python 3.11 using PyCharm
#

#specify the python interpreter to use
#!/usr/bin/env python3

# Open text file in read mode and close the file
file_path = "/home/enigma/Desktop/CountTextulaMain/woodchuck.txt"
file = open(file_path, 'r')
content = file.read()
file.close()

# Define and null special characters using a translation table
special_chars = r"!?,@#$%^&*()_+=/.><`~]}[{"
translation_table = str.maketrans(dict.fromkeys(special_chars))
content_without_special_chars = content.translate(translation_table)

#Split the words in the file using the split() function
word_list = content_without_special_chars.split()

# Create dictionary of word frequency
word_count = {}
for word in word_list:
    if word in word_count:
        word_count[word] += 1

    else:
        word_count[word] = 1

# Create key value pairs to calculate word frequency in text file
for key, value in word_count.items():
    print(f"{key} occurs : {value}")

# Print Done and prompt user to exit the program
print("Done.")
print("Press any key to exit.")
input()
exit()