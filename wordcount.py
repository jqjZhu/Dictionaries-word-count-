def count_word(filename):
    data = open(filename)

    count_word = {}

    for i in data:
        if i not in count_word:
            count_word[i] = count_word.get(i) + 1
        else:
            count_word[i] = 1

    return count_word



count_word('twain.txt')


    # for word, count in data.items():
    #     print("key = {}, value = {}".format(word, count))
