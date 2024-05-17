# Given a list of words, write a function to return a set of all anagrams in the list.

# define the main function
def main():
    # define a list of words
    words_list = ["iceman", "bored", "united", "robed", "cinema", "untied", "be", "good", "person", "unedit"]
    # call the anagram_set function
    anagram_set(words_list)

# define the function to get the set of anagram words
def anagram_set(words_list):

    # create a set to store the anagram words
    anagram_words = set()
    # iterate through the list of words and check if each word is an anagram of another word in the list
    # select a word from the list
    for word1 in words_list:
        # select another word from the list
        for word2 in words_list:
            # check if the two words are different and have the same letters
            if word1 != word2 and sorted(word1) == sorted(word2):
                # add the words to the set of anagram words
                anagram_words.add(word1)
                anagram_words.add(word2)
            # if the words are not anagrams, continue the loop
            else:
                continue

    # check if there are no anagram words in the list
    if len(anagram_words) == 0:
        # print a message and end the program
        return print("There are no anagram words in the list")

    # print the set of anagram words
    return print(f"The set of anagram words are: {anagram_words}")

# call the main function
main()
