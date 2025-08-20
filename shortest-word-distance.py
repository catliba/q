def shortestDistance(self, words, word1, word2):
    min_distance = 11
    distance = 0
    pos1 = -1
    pos2 = -1
    for i, word in enumerate(words):
      if word == word1:
        pos1 = i
        if pos2 != -1:
          distance = abs(pos1-pos2)
          min_distance = min(distance,min_distance)
      if word == word2:
        pos2 = i
        if pos1 != -1:
          distance = abs(pos1-pos2)
          min_distance = min(distance,min_distance)
    return min_distance
