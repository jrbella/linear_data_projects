# import
from deck import Deck

# I want to create a deck
my_deck = Deck("Standard")


# add cards to dictionary
array_of_card_values = [
    "2", "3","4","5","6", "7", "8", "9", "10",
    "Jack", "Queen", "King", "Ace"
]

array_of_card_suites = [
    "hearts", "diamonds", "spades", "clubs"
]

# I need to push a set of cards onto the deck

def deck_builder(array_of_card_values, array_of_card_suites):

    for suite in array_of_card_suites:
        for card in array_of_card_values:
            my_deck.push(suite, card)



deck_builder(array_of_card_values, array_of_card_suites)

print(my_deck.size)





