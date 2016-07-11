def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    handCopy = hand.copy()
    for k in word:
        handCopy[k] = handCopy.get(k,0) - 1
    return handCopy

hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = "quail"