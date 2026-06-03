import random

suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
deck = []

def create_deck():
    input("Press Enter to create a deck of cards: ")
    deck = []
    for s in suit:
        for r in rank:
            deck.append(f"{r} of {s}")
    print("Deck created!")
    return deck
    
def shuffle_deck():
    input("Press Enter to shuffle the deck: ")
    random.shuffle(deck)
    print("Deck shuffled!")
    return deck

def deal_cards(deck, num_cards):
    input("Press Enter to deal cards: ")
    if num_cards > len(deck):
        print("Not enough cards in the deck!")
        return []
    dealt_cards = deck[:num_cards]
    del deck[:num_cards]
    print(f"Dealt {num_cards} cards: {dealt_cards}")
    return dealt_cards


create_deck()
shuffle_deck()
deal_cards(deck, 5)
