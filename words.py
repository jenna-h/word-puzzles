import re
# from num2words import num2words


SCRABBLE = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
  'd': 2, 'g': 2, 'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 
  'k': 5, 'j': 8, 'x': 8, 'q': 10, 'z': 10}

VOWELS = 'aeiou'

months = ['january', 'february', 'march', 'april', 'may', 'june', 
    'july', 'august', 'september', 'october', 'november', 'december']

scale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'ti']

MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 
  'g': '--.', 'h': '...', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--',
  'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
  'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}

ROMAN_NUMERAL_CHARACTERS = 'IVXLCDM'

def shift(w, amt):
    return ''.join((chr((ord(c)-ord('a')+amt)%26+ord('a')) for c in w))

def roman(number):
  num = [1, 4, 5, 9, 10, 40, 50, 90,
      100, 400, 500, 900, 1000]
  sym = ["I", "IV", "V", "IX", "X", "XL",
      "L", "XC", "C", "CD", "D", "CM", "M"]
  i = 12
  
  t = ''
  while number:
      div = number // num[i]
      number %= num[i]

      while div:
          t += sym[i]
          div -= 1
      i -= 1

  return t

# with open('/Users/jennahimawan/Documents/word-puzzles/UKACD17-processed.TXT') as f:
with open('/Users/jennahimawan/Documents/word-puzzles/twl06.txt') as f:
    words = f.read().splitlines()
    for w in words:
      pass