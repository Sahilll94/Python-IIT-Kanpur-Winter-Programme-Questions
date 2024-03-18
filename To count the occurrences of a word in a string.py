#Question Description
"""
Python Program to Count the Occurrences of a Word in a Given String Sentence.
"""

#Solution
sentence=input("Enter the sentence: ")
word_to_count=input("Enter the word you need to count: ")

sentence_lower=sentence.lower()
word_lower=word_to_count.lower()

occurences=0
for w in sentence_lower.split():
    if w==word_lower:
        occurences+=1

print(f"The word {word_to_count} is appeared {occurences} times")

#Output
# Enter the sentence: Sahil is a good boy, he loves good food, his only need good grades in his life
# Enter the word you need to count: good
# The word good is appeared 3 times


