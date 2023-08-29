def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text = "This is a simple sentence. This is another sentence."
word_freq = word_frequency(text)
print(word_freq)
