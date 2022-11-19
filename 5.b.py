user = "It is often the small steps, not the giant leaps, that bring about the most lasting change."
counts = dict()
words = user.split()
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
