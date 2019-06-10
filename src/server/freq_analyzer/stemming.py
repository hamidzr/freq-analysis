# assumes x + all different endings defined below are the same word
def other_forms(word):
  endings = ['s', 'ing', 'ed', 'es', 'ings']
  for suffix in endings:
    yield word + suffix


# merges different forms of the same word
# in O(n) time and space
def merge_stems(w_counts):

  # create a dic out of it for quick lookup
  words_dic = {}
  for word, count in w_counts:
    words_dic[word] = count


  # OPT could be modified to only update the count for dic[word] only once
  for word, _ in w_counts:
    for child_form in other_forms(word):
      if (child_form in words_dic
          and word in words_dic):
        words_dic[word] = words_dic[word] + words_dic[child_form]
        words_dic.pop(child_form) # remove the child form

  return [(w, words_dic[w]) for w in words_dic]

