from autocomplete import Autocomplete
import sys, os

if __name__ == "__main__":

    ac = Autocomplete('test.txt')

    while True:
        user_input = raw_input("Enter input: ").strip('\n')
        if ac.is_word(user_input):
            print "lol it's a word"
        else:
            print ac.closest_word(user_input)

        if user_input == ':q':
            sys.exit(0)

