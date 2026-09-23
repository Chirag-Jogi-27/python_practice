import pprint


def group_anagrams(words):
    anagram_slots = {}

    for word in words:
        sorted_blueprint = "".join(sorted(word))

        if sorted_blueprint not in anagram_slots:
            anagram_slots[sorted_blueprint] = []

        anagram_slots[sorted_blueprint].append(word)

    return anagram_slots


word_list = ["rat", "eat", "tar", "tea", "art", "ate", "oomn", "moon", "noon"]
result = group_anagrams(word_list)
pprint.pprint(result)
