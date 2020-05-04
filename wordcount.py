def count_word(filename):
"""Count words in file."""
    input_file = open(filename)

    word_counts = {}

    for line in input_file:
    # The default argument in rstrip() and split()is whitespace.
        line = line.rstrip()
        words = line.split()

        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(word, count)

# count_word('test.txt')


