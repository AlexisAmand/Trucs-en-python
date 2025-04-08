# Le mot le plus long

def longest_word(text):
    max_size = 0
    max_word = 0
    a_list = text.split()
    for word in a_list:
        if len(word) > max_size:
            max_size = len(word)
            max_word = word
    return max_word

