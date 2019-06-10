
import sys
import argparse
import operator

# local
from mapper import mapper
from reducer import reducer
from mapReduce import MapReduce

parser = argparse.ArgumentParser(description="file to word mapper")
parser.add_argument('--input', help='input file')
args = parser.parse_args()

mr = MapReduce(mapper, reducer)


with open(args.input, 'r') as f:
  lines = f.readlines() # OPTIMIZE assuming it fits in memory 
  print(f'processing {len(lines)} lines')
  # TODO compute chunksize based on input size
  w_counts = mr(lines, chunksize=5000)
  w_counts.sort(key=operator.itemgetter(1), reverse=True)
  print(w_counts[:25])
