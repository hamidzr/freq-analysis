import operator


# local
from freq_analyzer.mapper import mapper
from freq_analyzer.reducer import reducer
from freq_analyzer.mapReduce import MapReduce
from freq_analyzer.stemming import merge_stems

mr = MapReduce(mapper, reducer)

def analyze(lines):
  # print(f'processing {len(lines)} lines')
  # TODO compute chunksize based on input size
  w_counts = mr(lines, chunksize=5000)

  init_count = len(w_counts)
  w_counts = merge_stems(w_counts)
  # print(f'considering stems merged {init_count - len(w_counts) } words')

  w_counts.sort(key=operator.itemgetter(1), reverse=True) # sort on value(count)
  return w_counts
