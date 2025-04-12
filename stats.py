def get_num_words(text):
    return len(text.split())

def count_characters(text):
    res = {}
    for char in text:
        char = char.lower()
        if char in res:
            res[char] += 1
        else:
            res[char] = 1

    return res

def sort_character_list(in_dict):
    return dict(sorted(in_dict.items(), key=lambda item: item[1], reverse=True))