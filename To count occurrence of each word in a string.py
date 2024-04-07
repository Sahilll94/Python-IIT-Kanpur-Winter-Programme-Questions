"""
Python Program to Count the Occurrences of Each Word in a Given String Sentence.
"""

#Solution
sentence = input("Enter a sentence: ")

word_count = {} #dictionary
for word in sentence.lower().replace(",", "").replace(".", "").split():
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"The word '{word}' appears {count} times in the given sentence.")


#Output
# The word 'my' appears 1 times in the given sentence.
# The word 'name' appears 1 times in the given sentence.
# The word 'is' appears 1 times in the given sentence.
# The word 'sahl' appears 1 times in the given sentence.
