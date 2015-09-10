from __future__ import print_function
from nltk.tokenize import word_tokenize
import sys

print(sys.argv[1])
filename = sys.argv[1]
fileopen = open(filename, 'r')
source = fileopen.read()
source = source.decode('utf-8')
tokens_list = word_tokenize(source)

print(tokens_list)