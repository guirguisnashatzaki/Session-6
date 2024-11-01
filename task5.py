def unique_and_count(list):
    unique_words = set(list)
    counts = {word: 0 for word in unique_words}
    for i in unique_words:
        for j in list:
            if i == j:
                counts[i] += 1
    return counts