# create a stack of cards

from card import Card

class Deck:

    def __init__(self, name):
        self.size = 0
        self.top_card = None
        self.limit = 52  # can never have more than 52 cards
        self.name = name
    
    # peek
    def peek(self):
        if(self.top_card != None):
            print(self.top_card.get_card())
            return self.top_card.get_card()
            
        else:
            print("The deck is empty")

    # pop 
    def pop(self):
        if(not self.is_empty()):
            card_to_remove = self.top_card
            next_card = card_to_remove.get_next_card()
            self.top_card = next_card
            self.size -= 1
            return card_to_remove
        else:
            print("The deck is empty!")

    # push
    def push(self, suite, value):
        # debug
        #print("The suite of the card is " + suite + " The value of the card is " + str(value))
        if(self.has_room()):
            new_card = Card(suite, value)
            if self.is_empty():
                self.top_card = new_card
                print("Adding Card " + str(new_card.get_card()) + " to the top of the deck")
            else:
                current_card = self.top_card
                new_card.set_next_card(current_card)
                self.top_card = new_card
                print("Adding Card " + str(new_card.get_card()) + " to the top of the deck")
            self.size += 1

    # is empty
    def is_empty(self):
        return self.top_card == None

    # has_room 
    def has_room(self):
        return self.size < self.limit
        
   
   
