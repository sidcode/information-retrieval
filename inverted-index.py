'''
Inverted index construction

Contains:
  - slight background to data used, nltk
  - helper data structures used for searching
      > term frequency list
      > inverted_index
      > maximum term frequency for every document
  - inverted index construction
'''

import nltk
from nltk.corpus import gutenberg

# Project gutenberg has dataset of 25000 books
# 18 of those books are available within nltk as nltk.corpus.gutenberg

# Names of books
file_names = gutenberg.fileids()
print file_names

# Map from file names to file ids
indexer = 0
filename_map = {}
for book_name in file_names:
    filename_map[book_name] = indexer
    indexer = indexer+1


# Creating dictionary of term frequencies
term_frequency = {}
for book_name in file_names:
    for word in gutenberg.words(book_name):
        if term_frequency.has_key(word):
            term_frequency[word] = term_frequency[word] + 1
        else:
            term_frequency[word] = 1


# Inverted index containing document-wise frequency
inverted_index = {}

for book_name in file_names:
    for word in gutenberg.words(book_name):
        if inverted_index.has_key(word):
            posting_list = inverted_index[word]
            if posting_list.has_key(book_name):
                posting_list[book_name] = posting_list[book_name] + 1
            else:
                posting_list[book_name] = 1
        else:
            inverted_index[word] = {book_name:1}


# maximum term frequency for every document
max_frequency = {}
for book_name in file_names:
    max_frequency[book_name] = 0

for posting_list in inverted_index.values():
    for book_name in posting_list.keys():
        max_frequency[book_name] = max(max_frequency[book_name], posting_list[book_name])
