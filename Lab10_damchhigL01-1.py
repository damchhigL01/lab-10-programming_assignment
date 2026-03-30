"""
Program Name: Word Count Analyzer
Author: Damchhig Lama
Purpose: Count word frequency from selected text files using OOP.
Date: 03/26/2026
"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def process_file(self):
        try:
            if not self._filepath.exists():
                raise FileNotFoundError

            with self._filepath.open('r') as file:
                translator = str.maketrans('', '', string.punctuation)

                for line in file:
                    line = line.lower()
                    line = line.translate(translator)
                    words = line.split()

                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1

            return True

        except FileNotFoundError:
            print("File not found.")
            return False
