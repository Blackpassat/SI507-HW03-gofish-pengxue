import random

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

	def deal(self, hand_num, card_num):
		# cards = []
		hands = []
		if (hand_num * card_num > 52) or (card_num == -1):
			num = 52 // hand_num
			residual = 52 % hand_num
			for i in range(hand_num):
				cards.append(self.cards[i*num:(i+1)*num])
			for i in range(hand_num):
				hands.append(Hand(cards[i]))
			for i in range(residual):
				hands[i].add_card(self.pop_card())
		else:
			for i in range(hand_num):
				cards = []
				for j in range(card_num):
					cards.append(self.pop_card())
					j += 1
				hands.append(Hand(cards))
		return hands

class Hand:
	# create the Hand with an initial set of cards
	# param: a list of cards
	def __init__(self, init_cards):
		self.cards = []
		for card in init_cards:
			self.cards.append(card)

	# add a card to the hand
	# silently fails if the card is already in the hand
	# param: the card to add
	# returns: nothing
	def add_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			self.cards.append(card)

	# remove a card from the hand
	# param: the card to remove
	# returns: the card, or None if the card was not in the Hand
	def remove_card(self, card):
		card_strs = []
		for c in self.cards:
			card_strs.append(c.__str__())
		if card.__str__() not in card_strs:
			return None
		else:
			return self.cards.pop(self.cards.index(card))

	# draw a card from a deck and add it to the hand
	# side effect: the deck will be depleted by one card
	# param: the deck from which to draw
	# returns: nothing
	def draw(self, deck):
		card = deck.pop_card()
		self.add_card(card)

	def remove_pairs(self):
		ranks = []
		for card in self.cards:
			ranks.append(card.rank_num)
		new_card_ranks = []
		for i in ranks:
			if i not in new_card_ranks:
				new_card_ranks.append(i)
		cards = []
		for i in new_card_ranks:
			occur = ranks.count(i)
			if i%2 == 1:
				cards.append(self.cards[ranks.index(i)])
		self.cards = cards

	def showCard(self):
		for card in self.cards:
			print(card)



'''
This bolleen function will take in a hand object and check
if there is a book (4cards with same rank) in it, if there is,
remove the book from hand and add its rank to a given list
parameter: hand, list
return: Ture/ False
'''
def checkBook(hand, lst):
	counts = dict()
	for i in hand.cards:
		counts[i.rank_num] = counts.get(i.rank_num,0) + 1
	rk = 0
	for c in counts.keys():
		if counts[c] == 4:
			rk = c
			lst.append(c)
			for i in hand.cards:
				if i.rank_num == rk:
					hand.remove_card(i)
	if rk != 0:
		return True
	else:
		return False





'''
This bolleen function will check if there is a card in
this hand whose rank is same with the given card
parameter: card, hand
return: True/False
'''
def checkCard(card, hand):
	flag = 0
	for i in hand.cards:
		if i.rank_num == card.rank_num:
			flag = 1
	if flag == 0:
		return False
	else:
		return True




'''
This function will check if the input from player is valid
(There is a same input in the hand), if not valid, return an error
'''
def checkInput(rank, hand):
	if type(rank) is not int:
		print("Please enter a rank number")
		return False
	flag = 0
	for i in hand.cards:
		if i.rank_num == rank:
			flag = 1
	if flag == 0:
		print('There is no card in hand with this rank')
		return False
	else:
		return True



'''
This function print the given book and the length of them
parameter: a book list
'''
def showBook(lst1, lst2):
	print(lst1)
	print(lst2)
    print("Player0 has {} books, Player1 has {} books".format(len(lst1), len(lst2)))


'''
This function exchange the cards of given rank with two hands
parameter: rank, two hands
'''
def exchangeCard(rank, handReceive, handGive):
	pass



def play_gofish():
	deck = Deck()
	deck.shuffle()
	hands = deck.deal(2, 7)
	book0 = []
	book1 = []
	step = 0
	while((len(book0)+len(book1))<13):
		player = step % 2
		print("Player0's current book: " + str(book0))
		print("Player1's current book: " + str(book1))
		show_flag = str(input("Do you want to see your cards? [y/n]"))
		if show_flag == 'y':
			hands[player].showCard()




play_gofish()
