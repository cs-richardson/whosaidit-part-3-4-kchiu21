"""
Kolton Chiu
This program counts how many words are in two different text and prints them.
https://www.w3schools.com/python/python_file_handling.asp
https://www.w3schools.com/jsref/jsref_split.asp
https://www.w3schools.com/python/ref_file_close.asp
https://www.tutorialspoint.com/python/file_read.htm
---
assume that user inputs some text
"""
import math
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# normalize
# This function takes a word and returns the same word
# with:
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    total = 0
    result_dict = {}
    text = open(filename, "r")
    for key in text.read().split():
        next_key = normalize(key)
        if next_key:
            result_dict[next_key] = result_dict.get(next_key, 0) + 1
            total = total + 1
    result_dict.update( {'_total' : total} )
    text.close()
    return result_dict
 
# predict
# This function takes in three arguments and predict who said it
def predict(text, shakespeardict, austendict):
    shakespeare_score = 0
    austen_score = 0
    for key in text.split():
        next_key = normalize(key)
        if next_key:
            shakespeare_score = (get_score(next_key, shakespeardict))
            austen_score = (get_score(next_key, austendict))
    if shakespeare_score > austen_score:
        print ("I think that was written by Skakespeare.")
    elif shakespeare_score == austen_score:
        print ("not work")
    else:
        print ("I think that was written by Jane Austen.")
        
#MAIN
shakespeare_counts = get_counts("hamlet-short.txt")
austen_counts = get_counts("pride-and-prejudice-short.txt")        
user_input = input("Input Text Below: " + "\n")
predict(user_input, shakespeare_counts, austen_counts)
