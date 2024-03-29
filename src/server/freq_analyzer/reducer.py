#!/usr/bin/env python

import sys

# hashmap implementation
# mappedWords mapreduce key value pair
def reducer(mappedWords):
  word, occurances = mappedWords
  return (word, sum(occurances))

# WARN requires sorted input
def reducer2(mappedWords):

  word, occurances = item
  return (word, sum(occurances))
  current_word = None
  current_count = 0
  word = None

  for line in lines:
    line = line.strip()
    word, count = line.split(' ', 1)
    count = int(count)
    if current_word == word:
      current_count += count
    else:
      if current_word != None:
        yield (current_word, current_count)
      current_count = count
      current_word = word

  # don't miss the last word
  if current_word == word:
    yield (current_word, current_count)
