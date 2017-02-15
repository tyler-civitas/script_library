
# Logic to utilize when parsing. This is from python-fundamentals
# day8 code. The _update_counts method logic is really elegant
# as far as how it handles seperating words and sentences on
# a character-by-character basis

# Essentially, it builds words into a string as it parses characters,
# then, returns the word to a set when it encounters a space

from collections import Counter

class ReportCreator():
    def __init__(self):
        self.vocabulary = set()
        self.master_counts_dict = Counter(sentences=0, words=0, characters=0)

    def create_reports(self, file_paths):
        for file_path in file_paths:
            self.create_report(file_path)

    def create_report(self, file_path):
        counts_dict = Counter(sentences=0, words=0, characters=0)
        with open(file_path) as txt_file:
            for line in txt_file:
                self._update_counts(line, counts_dict)
            self.master_counts_dict += counts_dict
        return counts_dict

    def _update_counts(self, line, counts_dict):

        def update_words(word):
            counts_dict['words'] += 1
            self.vocabulary.add(word)
            return ''

        word = ''
        for char in line:
            counts_dict['characters'] += 1
            if char in '?.!':
                counts_dict['sentences'] += 1
            elif char == ' ':
                word = update_words(word)
            else:
                word += char.lower()
        update_words(word)
