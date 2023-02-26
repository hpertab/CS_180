import argparse
import numpy as np

def get_words_array(text):
    all_words = []
    cur_word = ""
    for i in range(len(text)):
        cur_char = text[i]
        if cur_char == ' ' or cur_char == '\n' or i == (len(text) - 1):
            if i == (len(text) - 1) and cur_char != '\n':
                    cur_word = cur_word + cur_char
            if len(cur_word) != 0:
                cur_word = cur_word.lower()
                if cur_word in all_words:
                    cur_word = ""
                else:
                    all_words.append(cur_word)
                    cur_word = ""
        else:
            cur_word = cur_word + cur_char
    return all_words
    
def get_counts_arrays(text, words):
    all_counts = []
    cur_word = ""
    cur_counts = [0] * len(words)
    for i in range(len(text)):
        cur_char = text[i]
        if cur_char == '\n' or i == (len(text) - 1):
            if i == (len(text) - 1) and cur_char != '\n':
                cur_word = cur_word + cur_char
                cur_word = cur_word.lower()
                word_idx = words.index(cur_word)
                cur_counts[word_idx] = cur_counts[word_idx] + 1
                cur_word = ""
            all_counts.append(cur_counts)
            cur_counts = [0] * len(words)
        else: 
            if cur_char == ' ':
                if len(cur_word) != 0:
                    cur_word = cur_word.lower()
                    word_idx = words.index(cur_word)
                    cur_counts[word_idx] = cur_counts[word_idx] + 1
                    cur_word = ""
            elif (i != (len(text) - 1) and text[i + 1] == '\n'): 
                cur_word = cur_word + cur_char
                cur_word = cur_word.lower()
                word_idx = words.index(cur_word)
                cur_counts[word_idx] = cur_counts[word_idx] + 1
                cur_word = ""
            else:
                cur_word = cur_word + cur_char
    return all_counts

def print_rows(counts):
    print('[', end="")
    for i in range(len(counts)):
        if i != 0:
            print(' ', end="")
        print('[', end="")
        for j in range(len(counts[i])):
            if j == (len(counts[i])-1):
                print(counts[i][j], end="")
            else:
                print(counts[i][j], end=" ")
        print(']', end="")
        if i != (len(counts) - 1):
            print("\n", end="")
    print(']')

def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    words = get_words_array(documentsTxt)
    words.sort()
    #print(words)
    counts = get_counts_arrays(documentsTxt, words)
    print('# Features:')
    print_rows(counts)
    

    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())