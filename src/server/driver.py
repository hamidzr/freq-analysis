#!/usr/bin/env python3

import sys
import argparse
import operator

from freq_analyzer.main import analyze

parser = argparse.ArgumentParser(description="file to word mapper")
parser.add_argument('--input', help='input file')
args = parser.parse_args()

with open(args.input, 'r') as f:
  lines = f.readlines() # OPTIMIZE assuming it fits in memory 

  # removing empty lines could be ignored since mapper considers this case
  lines = [l.strip() for l in lines]
  lines = list(filter(lambda l: l != '', lines))

  w_counts = analyze(lines)

  print(w_counts[:25])
