#!/usr/bin/env python

def main():
    list_A = ['Tar', 'Arc', 'Elbow', 'State', 'Cider', 'Dusty', 'Night', 'Inch', 'Brag', 'Cat', 'Bored', 'Save',
              'Angel', 'bla', 'Stressed', 'Dormitory', 'School master', 'Awesoame', 'Conversation', 'Listen',
              'Astronomer', 'The eyes', 'A gentleman', 'Funeral', 'The Morse Code', 'Eleven plus two', 'Slot machines',
              'Fourth of July', 'Jim Morrison', 'Damon Albarn', 'George Bush', 'Clint Eastwood', 'Ronald Reagan',
              'Elvis', 'Madonna Louise Ciccone', 'Bart', 'Paris', 'San Diego', 'Denver', 'Las Vegas',
              'Statue of Liberty']
    list_B = ['Cried', 'He bugs Gore', 'They see', 'Lives', 'Joyful Fourth', 'The classroom', 'Diagnose', 'Silent',
              'Taste', 'Car', 'Act', 'Nerved', 'Thing', 'A darn long era', 'Brat', 'Twelve plus one', 'Elegant man',
              'Below', 'Robed', 'Study', 'Voices rant on', 'Chin', 'Here come dots', 'Real fun', 'Pairs', 'Desserts',
              'Moon starer', 'Dan Abnormal', 'Old West action', 'Built to stay free', 'One cool dance musician',
              'Dirty room', 'Grab', 'Salvages', 'Cash lost in me', "Mr. Mojo Risin'", 'Glean', 'Rat', 'Vase']
    specialLetters = "[@_!#$%^&*()<>?/\|}{~:]. "
    anagrams = []
    for word_in_a in list_A:
        # remove special characters from words in first list
        first_word = "".join([l for l in word_in_a if l not in specialLetters])
        for word_in_b in list_B:
            # remove special characters from words in second list
            second_word = "".join([l for l in word_in_b if l not in specialLetters])
            # the trick: using all the original letters exactly once
            if sorted(first_word.lower()) == sorted(second_word.lower()):
                anagrams.append((word_in_a ,word_in_b))
    # Print the results
    print(anagrams)

if __name__ == '__main__':
    main()

"""
# If both lists are much larger, would you change anything in your code? 
- I will use Pool from multiprocessing package and try to divide the upper list uniformly across the number of cores to speed up the iteration process
- anagrams list.append operation is a thread-safe operation, but I would usually use a locking mechanism like counter-based locking mechanism or more easily a queue 
data structure which is thread-safe for concurrent access, it became a habit or a programming style I usually take.

"""