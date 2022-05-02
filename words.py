from num2words import num2words


SCRABBLE = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
  'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 
  'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}

VOWELS = 'aeiou'

months = ['january', 'february', 'march', 'april', 'may', 'june', 
    'july', 'august', 'september', 'october', 'november', 'december']

scale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti']

def shift(w, amt):
    return ''.join((chr((ord(c)-ord('a')+amt)%26+ord('a')) for c in w))


# with open('/Users/jennahimawan/Documents/word-puzzles/UKACD17-processed.TXT') as f:
# with open('/Users/jennahimawan/Documents/word-puzzles/pdl.txt') as f:
#     words = f.read().splitlines()
#     for w in words:
#         if w[0] not in fns:
#             continue
#         for w2 in words:
#             if w2[0] not in fns:
#                 continue
#             for w3 in words:
#                 if w3[0] not in fns:
#                     continue
#                 for w4 in spell_words:
#                     r = go(' '.join((w, w2, w3, w4)))
#                     if r in destinations:
#                         print(w, w2, w3, w4, r)