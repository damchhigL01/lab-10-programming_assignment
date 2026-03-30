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

    def print_report(self):
        for word in sorted(self._frequencies.keys()):
            print(f"{word:<10} :: {self._frequencies[word]}")

def main():
    files = {
        "1": "princess_mars.txt",
        "2": "Tarzan.txt",
        "3": "treasure_island.txt",
        "4": "monte_cristo.txt"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("1. Princess of Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. Monte Cristo")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        elif choice in files:
            filename = files[choice]
            print(f"\nProcessing '{filename}'...\n")

            analyzer = WordAnalyzer(filename)

            if analyzer.process_file():
                analyzer.print_report()

            input("\nPress Enter to return to the menu...")

        else:
            print("Invalid choice.")
            input("Press Enter to continue...")
            
if __name__ == "__main__":
    main()
