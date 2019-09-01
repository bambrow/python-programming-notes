# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
ruleline1 = "Game Rules: Make the total value as high as possible, but no more than 21."
ruleline2 = "J,Q,K count as 10; A counts as either 1 or 11."
ruleline3 = "Dealer wins when you have busted, you have lower total value or there is a tie."
ruleline4 = "You win when dealer has busted or you have higher value."
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class_basics
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class_basics
class Hand:
    def __init__(self):
        self.cards = []
        # create Hand object

    def __str__(self):
        cardsinhand = ''
        for card in self.cards:
            cardsinhand = cardsinhand + str(card) + ' '
        return "Hand contains " + cardsinhand
        # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        cardsvalue = 0
        ace = False
        for card in self.cards:
            rank = card.get_rank()
            cardsvalue = cardsvalue + VALUES[rank]
            if rank == 'A':
                ace = True
        if ace and cardsvalue <= 11:
            cardsvalue = cardsvalue + 10
        return cardsvalue
        # compute the value of the hand
   
    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas, pos)
        # draw a hand on the canvas
        
# define deck class_basics
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()
        # deal a card object from the deck
    
    def __str__(self):
        cardsindeck = ''
        for card in self.cards:
            cardsindeck = cardsindeck + str(card) + ' '
        return "Deck contains " + cardsindeck
        # return a string representing the deck

#define event handlers for buttons
def deal():
    global outcome, in_play, score, player, dealer, result, deck
    if in_play:
        score = score - 1
        in_play = False
        result = 'Deal in play. You lose.'
        outcome = 'New Deal?'
    else:
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        outcome = 'Hit or stand?'
        result = ' '    
        in_play = True

def hit():
    global outcome, in_play, score, player, dealer, result, deck
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
            if player.get_value() > 21:
                score = score - 1
                in_play = False
                result = 'You have busted. You lose.'
                outcome = 'New Deal?'      
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome
       
def stand():
    global outcome, in_play, score, player, dealer, result, deck
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21:
            score = score + 1
            in_play = False
            result = 'Dealer has busted. You win.'
            outcome = 'New Deal?'
        elif player.get_value() > dealer.get_value():
            score = score + 1
            in_play = False
            result = 'Higher value. You win.'
            outcome = 'New Deal?'
        elif player.get_value() == dealer.get_value():
            score = score - 1
            in_play = False
            result = 'Tie. You lose.'
            outcome = 'New Deal?'
        else:
            score = score - 1
            in_play = False
            result = 'Lower value. You lose.'
            outcome = 'New Deal?'
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome

# draw handler    
def draw(canvas):
    canvas.draw_text("BLACKJACK", (180, 75), 40, "White")
    canvas.draw_text("DEALER", (40, 190), 30, "Aqua")
    canvas.draw_text("PLAYER", (40, 340), 30, "Aqua")
    canvas.draw_text(outcome, (250, 190), 30, "Black")
    canvas.draw_text(result, (250, 340), 30, "Black")
    canvas.draw_text("Score: " + str(score), (450, 150), 30, "Aqua")
    canvas.draw_text(ruleline1, (20, 500), 18, "Black")
    canvas.draw_text(ruleline2, (20, 520), 18, "Black")
    canvas.draw_text(ruleline3, (20, 540), 18, "Black")
    canvas.draw_text(ruleline4, (20, 560), 18, "Black")
    dealer.draw(canvas, [-50, 200])
    player.draw(canvas, [-50, 350])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [-50 + CARD_BACK_CENTER[0] + CARD_BACK_SIZE[0] + 20, 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

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

