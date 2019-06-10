#!/usr/bin/env python

# we load and define blacklist once as a set
# lookup O(1)
black_list = None

with open('config/blacklist.txt', 'r', encoding='utf-8') as f:
  lines = [line.strip() for line in f.readlines()]
  black_list = set(lines)

def _mapper(line, remove_stop_words=True):
  SERPARATOR=' '
  line = line.strip()
  line = line.lower()
  words = line.split(SERPARATOR)
  for word in words:
    # TODO make it optional
    if (not remove_stop_words) or (word not in black_list): # stop words
      yield (word, 1) # emit the word

def mapper(line):
  return [rv for rv in _mapper(line)]


if __name__ == '__main__':
  import sys
  import argparse

  parser = argparse.ArgumentParser(description="file to word mapper")
  parser.add_argument('--input', help='input file')

  args = parser.parse_args()

  with open(args.input, 'r') as f:
    for word, count in mapper(f):
      print(word, count)
