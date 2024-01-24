from collections import Counter

class WordFrequency:
    def __init__(self) -> None:
        pass

    def word_frequency(input_string):
        # Split the inpout into words
        words = input_string.split()
    
        # Count the frequency of each word
        word_count = Counter(words)

        # Sort the dictionary by keys alphanumerically
        sorted_word_count = dict(sorted(word_count.item()))   

        # Display the results
        for word, frequency in sorted_word_count.item():
            print(f'{word}: {frequency}')

    