import re
import glob

is_word_regex = re.compile('^[a-z]+$')
word_set = {}

def CreateDictionary(filename):
    for word in open(filename, 'r').read().split():
        word = word.lower()
        if not is_word_regex.match(word):
            continue
        if word_set.has_key(word):
            word_set[word] += 1
        else:
            word_set[word] = 1

for filename in glob.glob(r"c:\project\TSR\*.txt"):
    CreateDictionary(filename);

dict_file = open('c:\dict.txt', 'w')
for (key, value) in word_set.items():
    dict_file.write(key + '\t' + str(value) + '\n')
dict_file.close()
