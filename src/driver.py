#!/usr/bin/env python3

import sys
import argparse
import operator

# local
from mapper import mapper
from reducer import reducer
from mapReduce import MapReduce
from stemming import merge_stems

parser = argparse.ArgumentParser(description="file to word mapper")
parser.add_argument('--input', help='input file')
args = parser.parse_args()

mr = MapReduce(mapper, reducer)


with open(args.input, 'r') as f:
  lines = f.readlines() # OPTIMIZE assuming it fits in memory 

  # removing empty lines could be ignored since mapper considers this case
  lines = [l.strip() for l in lines]
  lines = list(filter(lambda l: l != '', lines))

  print(f'processing {len(lines)} lines')
  # TODO compute chunksize based on input size
  w_counts = mr(lines, chunksize=5000)

  init_count = len(w_counts)
  w_counts = merge_stems(w_counts)
  print(f'considering stems merged {init_count - len(w_counts) } words')

  w_counts.sort(key=operator.itemgetter(1), reverse=True) # sort on value(count)
  print(w_counts[:25])
