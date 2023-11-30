def find_substring_indices(haystack, needle):
    # Створення скінченного автомата
    transitions = {0: {needle[0]: 1}}
    fallbacks = [0]
    for i in range(1, len(needle)):
        transitions[i] = {}
        fallback = fallbacks[i - 1]
        while fallback > 0 and needle[i] != needle[fallback]:
            fallback = fallbacks[fallback - 1]
        fallbacks.append(fallback + 1 if needle[i] == needle[fallback] else fallback)
        for char, target in transitions[fallback].items():
            if char not in transitions[i]:
                transitions[i][char] = target
        transitions[i][needle[i]] = i + 1

    # Пошук підстрічки в стрічці
    state = 0
    index = []
    for i in range(len(haystack)):
        while state > 0 and haystack[i] != needle[state]:
            state = fallbacks[state - 1]
        if haystack[i] == needle[state]:
            state += 1
        if state == len(needle):
            index.append(i - (state - 1))
            state = fallbacks[state - 1]

    return index


