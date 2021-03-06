#!/usr/bin/python

import re

class Corpus(object):
  """A class to represent a corpus of text.

  Initialised with no parameters.

  Class constants:
  WORD_PATT - determines what sort of terms the corpus retains
  STOPFILE - the filename of the file containing the stop words
  STOPWORDS - the set of stop words extracted from the file
  """
  WORD_PATT = re.compile(r'([A-Za-z])+', re.IGNORECASE)
  STOPFILE = 'english.stop'
  STOPWORDS = set()

  def __init__(self):
    """Create a new, empty corpus of text."""
    self.doc_count = 0
    self.words = []
    self._populate_stopw()
  def _populate_stopw(self):
    """A helper method to extract the stop words from the stop words file."""
    f_handle = open(self.STOPFILE, 'rU')
    for word in f_handle.readlines():
      self.STOPWORDS.add(word)
  def get_stopwords(self):
    """Return the set of stop words used as a Python list."""
    return list(self.STOPWORDS)
  def get_words(self):
    """Get all the words for this corpus."""
    return self.words
  def get_df(self, word):
    """Get the document frequency (DF) for a particular word.
    
    If the word is not found, return 0."""
    if word in self.words:
      return word.get_df()
    else:
      return 0
  def add(self, text, fname):
    """Add a string of text to the corpus by first splitting it into features
    defined by WORD_PAT, and then removing stop words.

    Takes a string as its argument."""
    for match in re.finditer(self.WORD_PATT, text):
      if match:
        word = match.group(0)
        if word in self.STOPWORDS:
          continue
        self._add_word(word, fname)
  def _add_word(self, word, fname):
    """A helper method to add a word to the corpus. The word must be a string.
    """
    word = word.lower()
    if word in self.words:
      doc_freqs = self.words[word]
    else:
      word_obj = Word(word, fname)
      self.words.append(word_obj)
    if fname in doc_freqs:
      doc_freqs[fname] += 1
    else:
      doc_freqs[fname] = 1

class Word(object):
  def __init__(self, word, fname):
    """Create a new word object, for use in the Corpus.

    Arguments:
    word -- the actual word that this object holds
    fname -- the name of the file that this word first appeared in
    """
    self.freqs = {}
    self.word = word
    self.freqs[fname] = 1
  def update_freq(self, fname):
    """Update the value of the frequencies of this word.

    If the word has already been in the file, increment the counter.
    If not, add a new entry to indicate that is word has been seen in the file
    called fname."""
    if fname in self.freqs:
      self.freqs[fname] += 1
    else:
      self.freqs[fname] = 1
  def get_df(self):
    """Get the number of documents in the corpus that the word appears in."""
    return len(self.freqs)
  def get_freq(self, fname):
    """Get the number of occurences of this word in a particular file."""
    if fname in self.freqs:
      return self.freqs[fname]
    else:
      return 0
  def get_word(self):
    """Get the actual word that this object holds."""
    return self.word
  def get_filenames(self):
    """Returns a list of the filenames that this word appears in."""
    return self.freqs.keys()
  def __repr__(self):
    return self.word
  def __str__(self):
    return self.word
  def __eq__(self, other):
    if self.word == other.get_word():
    	return True
    return False
  def __ne__(self, other):
    if self.word != other.get_word():
    	return True
    return False

def df_select(corpus):
  selected = []
  lowest = 0
  highest = 0
  for word in corpus.get_words():
    pass

def tf_idf():
  pass
