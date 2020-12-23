class Card:
    suits = ["spades",
             "hearts",
             "diamond",
             "clubs"]
    
    values = [None, None, "2", "3",
                "4", "5", "6", "7",
                "8", "9", "10",
                "Jack", "Queen",
                "King", "Ace"]
    
    def __init__(self, v, s):
        """
        both suit and value are integer
        """
        self.value = v
        self.suit = s
        pass

    def __lt__(self, c2):
        """
        docstring
        """
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
        pass

    def __gt__(self, c2):
        """
        docstring
        """
        if self.values > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
        pass

    def __repr__(self):
        """
        docstring
        """
        v = self.values[self.value] + " of " \+ self.suits[self.suit]
        return v
        pass