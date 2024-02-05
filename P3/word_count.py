"""
Program to count the word frequency in a file.
"""
import sys
import time

def display_results(word_frequency_dict):
    """
    Function to display results.
    """
    print("Word\tFrequency")
    for word, frequency in word_frequency_dict.items():
        print(f"{word}\t{frequency}")

    with open('WordCountResults.txt', 'w', encoding="utf-8") as results_file:
        results_file.write("Word\tFrequency\n")
        for word, frequency in word_frequency_dict.items():
            results_file.write(f"{word}\t{frequency}\n")

def word_count(file_path):
    """
    Function to count the words in file.
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            data = file.read().split()

        if not data:
            raise ValueError("Error: Empty data set. Unable to count words.")

        word_frequency_dict = {}
        for word in data:
            word = word.lower()
            if word in word_frequency_dict:
                word_frequency_dict[word] += 1
            else:
                word_frequency_dict[word] = 1
        sorted_word_frequency = dict(
                sorted(word_frequency_dict.items(), key=lambda item: item[1], reverse=True)
            )
        return sorted_word_frequency

    except FileNotFoundError as exc:
        raise FileNotFoundError('Error: File not found.') from exc

if __name__ == "__main__":
    try:
        time_start = time.time()

        if len(sys.argv) != 2:
            raise ValueError("Error: Invalid number of arguments. Please provide a file path.")

        filename = sys.argv[1]
        word_frequency = word_count(filename)
        display_results(word_frequency)

        elapsed_time = time.time() - time_start
        print(f"Time elapsed: {elapsed_time} s")

    except ValueError as ve:
        print(ve)
