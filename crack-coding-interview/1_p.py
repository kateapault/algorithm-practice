words = ['cat', 'baby', 'tree', 'nap']
str1 = 'tacdfghjk'
str2 = 'baydfghjk'
str3 = 'eerthsfjfhj'

def string_check(words,string):
    string_letters = {}
    word_letters = {}
    for word in words:
        word_letters[word] = {}
        for letter in word:
            if letter in word_letters[word]:
                word_letters[word][letter] += 1
            else:
                word_letters[word][letter] = 1
    
    for letter in string:
        if letter in string_letters:
            string_letters[letter] += 1
        else:
            string_letters[letter] = 1
            
    for word in word_letters.keys():
        word_all_there = True
        for letter in word_letters[word].keys():
            if letter in string_letters:
                if word_letters[word][letter] != string_letters[letter]:
                    word_all_there = False
            else:
                word_all_there = False
        if word_all_there:
            return word
    return None

print(string_check(words,str1))
print(string_check(words,str2))
print(string_check(words,str3))