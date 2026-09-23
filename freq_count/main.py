def freq_count(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq


print(freq_count("dkdvasfehewsl"))
