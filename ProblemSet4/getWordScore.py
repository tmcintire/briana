VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {'a': 1,'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

def getWordScore(word, n):
    wordPoints = 0
    bonus = 0
    totWordScore = 0
    if word == '':
        return 0
    if len(word) == n:
        bonus = 50
    else:
        bonus = 0
    for l in word:
        wordPoints += SCRABBLE_LETTER_VALUES[l]
    totWordScore = wordPoints*len(word) + bonus
    return totWordScore
    print 'Total word score is: ' + str(totWordScore)

word = 'and'
n = ['a', 'b', 'n', 'e', 't', 'h', 'd']