def word_count(text):
    words = text.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

text = "яблуко груша яблуко банан груша яблуко банан яблуко груша банан"

counts = word_count(text)
print("Кількість кожного слова:", counts)

frequent_words = []
for word, count in counts.items():
    if count > 3:
        frequent_words.append(word)

print("Слова, які зустрічаються більше 3 разів:", frequent_words)
