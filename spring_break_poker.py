# Identify the hand of poker.
#
# Given a set of five playing cards,
# your job is return a "value" for the hand.
#
# Poker hands, in increasing value, are:
#
# 1 - High card only
# 2 - Pair
# 3 - Two Pair
# 4 - Three of a Kind
# 5 - Straight
# 6 - Flush
# 7 - Full House
# 8 - Four of a Kind
# 9 - Straight Flush
# 10 - Royal Straight Flush

# Each card is represented with its rank (1 or 2 characters)
# and the suit (always 1 character).
#
# Cards are separated from each other with a single space.
class Hand:
  pass


assert 1 == Hand.value("5H 2S 7C 10H AS"),  "1: High Card Test"
assert 2 == Hand.value("5H 2S 7C 5C 9S"),   "2: Pair Test"
assert 3 == Hand.value("5H 7S 7C 5C 9S"),   "3: Two Pair Test"
assert 4 == Hand.value("5H 5S 7C 5C 9S"),   "4: Three of a Kind Test"
assert 5 == Hand.value("5H 6S 7C 8H 9S"),   "5: Straight Test"
assert 6 == Hand.value("5H 3H QH JH 4H"),   "6: Flush Test"
assert 7 == Hand.value("5H 6S 5C 6D 5S"),   "7: Full House Test"
assert 8 == Hand.value("5H 5S 5C 5D 9S"),   "8: Four of a Kind Test"
assert 9 == Hand.value("5H 6H 7H 8H 9H"),   "9: Straight Flush Test"
assert 10 == Hand.value("AH KH QH JH 10H"), "10: Royal Straight Flush Test"
