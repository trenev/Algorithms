def find_words_in_target(index, target, words_by_index, words_count, solution):
    if index >= len(target):
        return print(*solution)
    if index not in words_by_index:
        return

    for word in words_by_index[index]:
        if words_count[word] < 1:
            continue

        solution.append(word)
        words_count[word] -= 1

        find_words_in_target(index + len(word), target,words_by_index, words_count, solution)

        solution.pop()
        words_count[word] += 1


words = input().split(', ')
target = input()

words_by_index = {}
words_count = {}

for word in words:
    if word not in words_count:
        words_count[word] = 0
    
    words_count[word] += 1
    index = 0

    while True:
        index = target.find(word, index)
        
        if index < 0:
            break
        if index not in words_by_index:
            words_by_index[index] = []
        if word not in words_by_index[index]:
            words_by_index[index].append(word)

        index += len(word)

find_words_in_target(0, target, words_by_index, words_count, [])
