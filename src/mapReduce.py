import collections
import itertools
import multiprocessing

class MapReduce:
  def __init__(self, map_fn, reduce_fn):
    self.map_fn = map_fn
    self.reduce_fn = reduce_fn
    self.pool = multiprocessing.Pool()

  def partition(self, mapped_values):
    # create a dic with default empty lists
    partitioned_data = collections.defaultdict(list)
    for key, value in mapped_values:
      partitioned_data[key].append(value)
    return partitioned_data.items()

  def __call__(self, lines, chunksize=1):
    map_responses = self.pool.map(self.map_fn, lines, chunksize=chunksize)
    partitioned_data = self.partition(itertools.chain(*map_responses))
    reduced_values = self.pool.map(self.reduce_fn, partitioned_data)
    return reduced_values
