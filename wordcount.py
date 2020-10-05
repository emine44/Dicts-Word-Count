input_file = open('./twain.txt')

# word_count = {}
# for line in input_file: 
#     line =line.rstrip()
#     words = line.split()
#     for word in words:
#         word_count[word]=word_count.get(word,0) +1

# for word, count in word_count.items():
#     print(word, count)

word_counts ={}
for line in input_file:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word_counts[word]=word_counts.get(word,0)+1

for word,count in word_counts.items():
    print(word,count)






