def count_words(text):
    feedback = f"Found {len(text.split())} total words"
    return feedback

def count_char(text):
    char_stats = {}

    for c in text:
        c = c.lower()
        if c in char_stats:
            char_stats[c] +=1
        else:
            char_stats[c] = 1

    return char_stats
