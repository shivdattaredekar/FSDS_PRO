file = 'paragraph.txt'
with open(file, 'r') as f:
        word_count = {}
        for i in f:
            words = i.strip().split()
            for word in words:
                  if word in word_count:
                    word_count[word] += 1
                  else:
                    word_count[word] = 1
        #sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[0]))
        print(dict(sorted(word_count.items(), key=lambda x: x[0])))