# your code goes here!


# Anagram class
class Anagram:
    # init
    def __init__(self, word):
        self.word = word

    # is_anagram method
    def is_anagram(self, given_word):
        # returns boolean value that determines whether a __init__ word is an anagram to given word regardless of order
        return (
            sorted(self.word.lower()) == sorted(given_word.lower())
            and self.word.lower() != given_word.lower()
        )

    # match method
    def match(self, words_list):
        # responisble returning array of matching words if words provided in is_anagram are ture
        anagrams = [word for word in words_list if self.is_anagram(word)]
        return anagrams
