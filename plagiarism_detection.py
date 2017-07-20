from string import punctuation
from itertools import chain


class PlagiarismDetection(object):
    """
    Plagiarism Detection Class

    Default Phrase Size is 3 if no Phrase Size is given.
    Call get_plagiarized_percentage() to get the percentage plagiarized of
    target file when compared to source file.
    """

    DEFAULT_PHRASE_SIZE = 3

    def __init__(self, source_path, target_path, synonyms_path,
                 phrase_length=DEFAULT_PHRASE_SIZE):
        """ Prepares all maps and lists of files """

        if phrase_length is None:
            phrase_length = self.DEFAULT_PHRASE_SIZE
        elif phrase_length <= 0:
            raise Exception("Tuple Size should be greater than 0")

        self.phrase_length = phrase_length
        self.synonyms = self.get_synonym_map(synonyms_path)
        self.source = self.file_to_phrase_map(source_path)
        words_in_target = self.words_in_file(target_path)
        self.target = self.word_list_to_phrases(words_in_target)

    def get_plagiarized_percentage(self):
        """ Returns the Plagiarized Percentage of the Target
        file compared to the Source file. """

        SIZE = len(self.target)
        total_plagiarized_phrases = 0
        for tupl in self.target:
            if tupl in self.source:
                total_plagiarized_phrases += 1

        total_plagiarized_phrases = float(total_plagiarized_phrases)

        # If the size is 0, we don't want the risk of dividing by 0.
        plagiarized = 0 if SIZE == 0 else total_plagiarized_phrases / SIZE

        plagiarized_percentage = plagiarized * 100

        return plagiarized_percentage

    def file_to_phrase_map(self, file_path):
        """ Returns a map of all the tuples from the file in the file path. """

        list_of_words = self.words_in_file(file_path)
        list_of_phrases = self.word_list_to_phrases(list_of_words)
        return self.get_phrase_map(list_of_phrases)

    def get_phrase_map(self, phrases):
        """ Creates and returns a map of tuples with values set as True
        by iterating through a list of tuples. """

        phrase_map = {}
        for phrase in phrases:
            phrase_map[phrase] = True
        return phrase_map

    def word_list_to_phrases(self, words):
        """ Returns a list of tuples obtained from a list of words that have
        gone through the check of being a possible synonym. """

        SIZE = len(words)

        """ If this exception is taken out phrase_length will automatically be
        equivalent to the SIZE. It was by choice to raise an Exception to
        make sure everything goes as it should be for the user. """
        if SIZE < self.phrase_length:
            raise Exception("Tuple is greater than the list of words in file")

        # Creates the first iteration of :phrase_length from the list of words.
        list_of_words = [self.word_to_synonym(word) for word
                         in words[:self.phrase_length]]
        phrases = [tuple(list_of_words)]

        """ Continuing from the first iteration, it will grab the next following word
        from the list, check if it can be converted to a synonym, append to the
        end of list, pop the word at index 0 of the list, create a tuple of the
        list, and append to tuple list until it reaches SIZE-1 of list. """
        for index in xrange(self.phrase_length, SIZE):
            end_word = words[index]
            end_word = self.word_to_synonym(end_word)
            list_of_words.append(end_word)
            list_of_words.pop(0)
            phrase_list = tuple(list_of_words)
            phrases.append(phrase_list)

        return phrases

    def get_synonym_map(self, file_path):
        """ Returns a map with all the possible synonyms as keys and have
        their first respective synonym according to the word as a value
        of the key. """

        synonym_map = {}
        with open(file_path, 'r') as file:
            for line in file:
                words = line.split()
                synonym_word = words[0]
                for word in words:
                    synonym_map[word] = synonym_word

        return synonym_map

    def word_to_synonym(self, word):
        """ Converts the word passed to its lowercase form with no punctuation,
        checks if the word is in the synonym map, and if so, assigns the
        word the value of its common synonym. Returns the modified word. """

        word = self.to_lowercase_alphas(word)
        if word in self.synonyms:
            word = self.synonyms[word]

        return word

    def to_lowercase_alphas(self, word):
        """ Converts and returns the word passed to its lowercase form
        with no punctuation. """

        word = word.lower()
        word = word.translate(None, punctuation)
        return word

    def words_in_file(self, file_path):
        """ Returns list of words from the file. """

        with open(file_path, 'r') as f:
            return list(chain.from_iterable(line.split() for
                        line in f if line.rstrip()))
