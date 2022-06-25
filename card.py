
class Card:
    
    def __init__(self, suite, value, next_card=None):
        self.suite= suite  # example diamond, club
        self.value = value # example 2, 3
        self.next_card = next_card
    
    # data
    def get_suite(self):
        return self.suite
    
    def get_value(self):
        return self.value
    
    # node functions
    # get next node
    def get_next_card(self):
        return self.next_card
    
    # set next node
    def set_next_card(self, card):
        self.next_card = card
    
    # helper function to print
    def get_card(self):
        return ("" + str(self.value) + " of " + str(self.suite) + "")

# debug
#new_card = Card("hearts", 3)
#print(new_card.get_card())