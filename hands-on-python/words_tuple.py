# Write a program that takes a sentence (string)
# and returns a tuple of the most frequent word and its frequency.

# define the main function
def main():

    # declare a string variable with a sentence
    sentence = "this is a test sentence to test the test"
    # call the function
    tuple_freq_word(sentence)

# define the function
def tuple_freq_word(sentence):

    # declare a variable to store the most frequent word, it will be defined by the max function
    # the first argument in the max function is the sentence splited in a list of words
    # and the second argument is the key parameter of the max() function and is set by sentence.split().count,
    # which counts the number of times each word appears in the list and return the word that appears the most
    most_freq_word = max(sentence.split(), key = sentence.split().count)
    # declare a variable to store the number of times the most frequent word appears in the sentence
    num_freq_word = sentence.split().count(most_freq_word)
    # declare a tuple with the most frequent word and its frequency
    freq_word = (most_freq_word, num_freq_word)
    # print the tuple with the most frequent word and its frequency
    return print(f"The tuple with the most frequent word is: {freq_word}.")

# call the main function
main()
