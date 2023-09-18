from sentences import get_determiner, get_noun, get_verb ,get_preposition, get_preposition_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["A", "One", "The"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["Some", "Many", "The"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    # 1. Test the single determiners.

    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_noun

    # 2. Test the plural determiners.

    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_noun

def test_get_verb():

    past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
        word = get_verb(quantity=1, tense="past")
        assert word in past_verb

    single_verb = ["drinks", "eats", "grows", "laughs", "thinks",
             "runs", "sleeps", "talks", "walks", "writes"]
   
    for _ in range(4):
        word = get_verb(quantity=1,tense="present")
        assert word in single_verb

    plural_verb = ["drink", "eat", "grow", "laugh", "think",
              "run", "sleep", "talk", "walk", "write"]
   
    for _ in range(4):
        word = get_verb(quantity=2,tense="present")
        assert word in plural_verb

    future_verb = ["will drink", "will eat", "will grow", "will laugh",
              "will think", "will run", "will sleep", "will talk",
              "will walk", "will write"]
   
    for _ in range(4):
        word = get_verb(quantity=1,tense="future")
        assert word in future_verb

def test_get_preposition():

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(4):

        words = get_preposition()

        assert words in prepositions

def test_get_preposition_phrase():
   
   prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
   
   single_determiners = ["A", "One", "The"]

   plural_determiners = ["Some", "Many", "The"]

   single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

   plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

    

   for _ in range(4):

        check = get_preposition_phrase(1).split(sep=" ")
        uno = check[0]
        dos = check[1]
        tres = check[2]

        assert uno in prepositions
        assert dos in single_determiners
        assert tres in single_noun

        check = get_preposition_phrase(2).split(sep=" ")
        uno = check[0]
        dos = check[1]
        tres = check[2]

        assert uno in prepositions
        assert dos in plural_determiners
        assert tres in plural_noun



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
