# Write a program that takes a sentence (string) and returns a
# dictionary with the count of each word in the sentence.

# define the main function
def main():

    # declare a string variable with a sentence
    sentence = "this is a test sentence"
    # call the function
    dict_num_words(sentence)

# define the function that takes a sentence (string) and returns a dictionary with the count of each word in the sentence
def dict_num_words(sentence):

    # create a dictionary with every word in the sentence and the count of each of them
    dict_words = {}
    # split the sentence into a list of words
    sentence = sentence.split()
    # iterate through the words in the sentence
    for word in sentence:
        # if the word is not in the dictionary, add it with a count of 1
        if word not in dict_words:
            dict_words[word] = 1
        # if the word is already in the dictionary, add 1 to the count
        else:
            dict_words[word] += 1

    # print the dictionary with the count of each word in the sentence
    return print(f"The dictionary with the count of each word in the sentence is: {dict_words}.")

# call the main function
main()
