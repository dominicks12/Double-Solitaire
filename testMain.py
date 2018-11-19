from board1 import Board
from card import Card
from pile import Pile

Board.start()

testPile = Pile()
testCard1 = Card()
testCard2 = Card()
testCard3 = Card()

list_of_cards = [testCard1]
list_of_cards2 = [testCard2, testCard3]

testPile.add(list_of_cards)
testPile.add(list_of_cards2)



# PROBLEM: only adding one card to testPile
