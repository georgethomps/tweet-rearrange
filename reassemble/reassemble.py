# George Thompson
# N/A
# N/A
#
# CSE 101, Section 01 (Spring 2019)
# Homework 3-3
from heapq import heapify, heappop
from collections import namedtuple


def reassemble(tweets):
    """Heart of the program. Inner functions were used since the assignment requested for there to be only one
    outer function per file. I'm assuming this pertains to outer functions because it'd be ridiculous to not
    allow any additional functions"""

    # namedtuple to manage the order of the tweets (less overhead than a dict)
    TweetSequence = namedtuple('TweetSequence', 'sequence_number text')

    # define inner functions since the assignment said to have only one outer function per file (I don't like this).
    def tweet_gen(tweet_list):
        """yields target TweetSequences from a list of strings"""
        for tweet in tweets:
            if tweet[-1] == ')':
                # the heap can use the sequence_number to pop tweets in the proper order!
                rfind = tweet.rfind
                yield TweetSequence(sequence_number=int(tweet[rfind('(') + 1 : rfind('/')]),
                                    text=tweet[:tweet.find('(')])

    # research has shown heaps can perform very efficient sorting (useful for long tweets!)
    def heap_sort(sequence_list):
        """a generator that uses a heap to sort data"""
        heapify(sequence_list)  # in-place modification seems appropriate, no use for the input after sorting!
        while sequence_list:
            yield heappop(sequence_list)

    output = ''.join(tweet.text for tweet in heap_sort(list(tweet_gen(tweets))))
    return output


#############################################################
# DO NOT MODIFY OR REMOVE ANY OF THE CODE THAT FOLLOWS!

if __name__ == "__main__":
    print("Reassembling ['a group of planets known as the Twelve Colonies, (5/7)', 'to which they have migrated (6/7)', 'human civilization has extended to (4/7)', 'from their ancestral homeworld of Kobol. (7/7)', 'productions share the premise that (2/7)', 'All Battlestar Galactica (1/7)', 'in a distant part of the universe, a (3/7)']:")
    print()
    print(reassemble(['a group of planets known as the Twelve Colonies, (5/7)', 'to which they have migrated (6/7)', 'human civilization has extended to (4/7)', 'from their ancestral homeworld of Kobol. (7/7)', 'productions share the premise that (2/7)', 'All Battlestar Galactica (1/7)', 'in a distant part of the universe, a (3/7)']))
    print()
    print()

    print('Reassembling ["I agree", "the recipe, you can understand how the algorithm (7/8)", "Protection Regulation in the European Union, people have (2/8)", "This is an excellent idea", "algorithms use in their decisions. This legislation treats the (4/8)", "process of algorithmic decision-making like a recipe book. (5/8)", "\'a right to explanation\' of the criteria that (3/8)", "I don\'t think this is correct", "The thinking goes that if you understand (6/8)", "LOL", "As part of the recently approved General Data (1/8)", "affects your life. (8/8)"]:')
    print()
    print(reassemble(["I agree", "the recipe, you can understand how the algorithm (7/8)", "Protection Regulation in the European Union, people have (2/8)", "This is an excellent idea", "algorithms use in their decisions. This legislation treats the (4/8)", "process of algorithmic decision-making like a recipe book. (5/8)", "'a right to explanation' of the criteria that (3/8)", "I don't think this is correct", "The thinking goes that if you understand (6/8)", "LOL", "As part of the recently approved General Data (1/8)", "affects your life. (8/8)"]))
    print()
    print()

    print("Reassembling ['Where can I get some coffee now?', 'over-the-counter (10/12)', 'I never knew that about caffeine', 'The water can then be put back with the beans and evaporated (5/12)', 'tablets. (12/12)', 'Me too', 'and contributes to the flavor of coffee, is (3/12)', 'then passed through activated charcoal, which removes the caffeine. (4/12)', 'flavor. Coffee manufacturers (7/12)', 'use in soft drinks and (9/12)', 'Coffee beans are soaked in water. (1/12)', 'Tea has caffeine too', 'The water, which contains many other compounds in addition to caffeine (2/12)', 'caffeine (11/12)', 'recover the caffeine and resell it for (8/12)', 'dry, leaving decaffeinated coffee with its original (6/12)', 'I love coffee']:")
    print()
    print(reassemble(['Where can I get some coffee now?', 'over-the-counter (10/12)', 'I never knew that about caffeine', 'The water can then be put back with the beans and evaporated (5/12)', 'tablets. (12/12)', 'Me too', 'and contributes to the flavor of coffee, is (3/12)', 'then passed through activated charcoal, which removes the caffeine. (4/12)', 'flavor. Coffee manufacturers (7/12)', 'use in soft drinks and (9/12)', 'Coffee beans are soaked in water. (1/12)', 'Tea has caffeine too', 'The water, which contains many other compounds in addition to caffeine (2/12)', 'caffeine (11/12)', 'recover the caffeine and resell it for (8/12)', 'dry, leaving decaffeinated coffee with its original (6/12)', 'I love coffee']))
    print()
    print()

    print()

