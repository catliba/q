def checkIfPangram(self, sentence):
    sentence = sentence.lower()
    letters = set()
    for c in sentence:
      if c.isalpha():
        letters.add(c)
    if len(letters) != 26:
      return False
    else:
      return True