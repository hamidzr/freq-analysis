#!/usr/bin/env python

def mapper(lines):
  for line in lines:
    line = line.strip()
    words = line.split()
    for word in words:
      yield (word, 1) # emit the word


if __name__ == '__main__':
  import sys
  import argparse

  parser = argparse.ArgumentParser(description="file to word mapper")
  parser.add_argument('--input', help='input file')

  args = parser.parse_args()

  with open(args.input, 'r') as f:
    for word, count in mapper(f):
      print(word, count)
