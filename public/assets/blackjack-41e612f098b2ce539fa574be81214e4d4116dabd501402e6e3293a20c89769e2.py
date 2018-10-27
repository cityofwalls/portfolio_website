import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("https://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("https://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
deck = None	# Setting this to None because Deck is not defined yet, deal checks for this on first play

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print("Invalid card: ", suit, rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, 
                          CARD_SIZE, 
                          [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        s = "Hand contains "
        for card in self.hand:
            s += str(card) + " "
        return s

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        hand_value = 0
        has_ace = False
        for card in self.hand:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                has_ace = True
            
        if has_ace and hand_value + 10 <= 21:
            return hand_value + 10
        
        return hand_value
   
    def draw(self, canvas, pos):
        for i in range(len(self.hand)):
            self.hand[i].draw(canvas, [i * CARD_SIZE[0], pos])
            
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))
                
    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        card_index = random.randrange(len(self.deck))
        resulting_card = self.deck[card_index]
        self.deck.remove(resulting_card)
        return resulting_card
    
    def __str__(self):
        s = "Deck contains "
        for card in self.deck:
            s += str(card) + " "
        
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    
    # Hitting deal in the middle of a round causes a loss for the player
    if in_play:
        outcome = "You have forfeit this round. New Deal?"
        score -= 1
        in_play = False
        return
    
    outcome = "Hit or Stand?"
    
    """ Create new deck only if there has never been a deck (first play),
        or if there are less than 15 cards in the current deck. """
    if deck is None or len(deck) < 15:
        deck = Deck()
    deck.shuffle()
    player_hand, dealer_hand = Hand(), Hand()
    
    # Deal 2 cards to player and dealer
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    
    in_play = True

def hit():
    global player_hand, outcome, in_play, score
    
    # If not legal to ask for a hit, function should return
    if not outcome == "Hit or Stand?":
        return
    
    player_hand.add_card(deck.deal_card())
    
    if player_hand.get_value() > 21:
        outcome = "You have busted! Dealer wins. New Deal?"
        score -= 1
        in_play = False
        
def stand():
    global dealer_hand, outcome, in_play, score
    
    in_play = False
    
    # If not legal to ask to stand, function should return 
    if not outcome == "Hit or Stand?":
        return
    
    while dealer_hand.get_value() < 17:
        dealer_hand.add_card(deck.deal_card())
        
    if dealer_hand.get_value() > 21:
        outcome = "Dealer busts! You win! New Deal?"
        score += 1
    elif dealer_hand.get_value() >= player_hand.get_value():
        outcome = "Dealer wins. New Deal?"
        score -= 1
    else:
        outcome = "You win! New Deal?"
        score += 1

# draw handler    
def draw(canvas):
    player_hand.draw(canvas, 400)
    dealer_hand.draw(canvas, 200)
    
    # Hide dealer's hole card if 'in play'
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_SIZE, 
                          [CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], 
                           CARD_SIZE)
    
    # *** Blackjack ***
    canvas.draw_text("Blackjack", [50, 50], 40, "Crimson")
    
    # Player message
    canvas.draw_text(outcome, [50, 550], 30, "Black")
    
    # Score
    canvas.draw_text("Score: " + str(score), [500, 50], 20, "White")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deal()
frame.start()