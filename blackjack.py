class BlackJack:
    def __init__(self):
        self.deck = []

    def generate_cards(self):
        suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Queen", "King", "Jack", "Ace"]

        for suit in suits:
            for value in values:
                card = f"{value} of {suit}"
                self.deck.append(card)
        return self.deck

deck = BlackJack()
print(deck.generate_cards())

    