from enum import Enum


class Rank(Enum):
    ACE = ["ace", 0]
    ONE = ["one", 1]
    TWO = ["two", 2]
    THREE = ["three", 3]
    FOUR = ["four", 4]
    FIVE = ["five", 5]
    SIX = ["six" , 6]
    SEVEN = ["seven", 7]
    EIGHT = ["eight", 8]
    NINE = ["nine", 9]
    TEN = ["ten", 10]
    JACK = ["jack", 11]
    QUEEN = ["queen", 12]
    KING = ["king", 13]
    JOKER = ["joker", -1]


class Suit(Enum):
    DIAMONDS = ["diamonds", 'red']
    HEARTS = ["hearts", "red"]
    CLUBS = ["clubs", "black"]
    SPADES = ["spades", "black"]