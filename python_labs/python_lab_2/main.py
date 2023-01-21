import json
import string
import argparse
import os


def separate_words(cur_string):
    word_array = []
    word_array = cur_string.split(" ")
    return word_array

def remove_special_chars(word_array):
    clean_words = []

    for word in word_array:
        stripped_word = word.strip("`~!@#$%^&*()_-+=[}{]|\:;\"\',<.>/?")
        clean_words.append(stripped_word)

    return clean_words

def words_to_lowercase(word_array):
    lowercase_words = []

    for word in word_array:
        cur_lowercase_word = word.lower()
        lowercase_words.append(cur_lowercase_word)

    return lowercase_words

def count_words(word_array):
    counted_words = []

    contained_words = []
    for word in word_array:
        if word not in contained_words: 
            contained_words.append(word)
            count = 0
            for cur_word in word_array:
                if (cur_word == word):
                    count += 1
            cur_count_and_word = [word, count]
            counted_words.append(cur_count_and_word)


    return counted_words


def main(inputString):
    # Write the code to count the number of words here
    # Remember to save the dictionary as a json file named "word-counts.json"

    #Separate each word in the input string (e.g., tokenization)
    separated_words = separate_words(inputString)
    #Remove punctuation and special characters
    removed_special_chars = remove_special_chars(separated_words)
    #Make each word lowercase
    lowercase_clean_words = words_to_lowercase(removed_special_chars)
    #Find the count of each unique word in the string
    counted_words = count_words(lowercase_clean_words)
    
    #result to a .json file
    word_counts = {}
    for row in counted_words:
        word_counts[row[0]] = row[1]

    #fpath = os.path("word-counts.json")
    with open("word-counts.json", "w") as f:
        json.dump(word_counts, f)
        

    return inputString

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Word Counter")
    parser.add_argument("-s","--string",type=str,required=True, help="Sentence to have the number of words counted")
    args = parser.parse_args()
    main(args.string)
    
