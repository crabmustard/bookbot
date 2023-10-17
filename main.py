current_book = 'books/frankenstein.txt'
with open(current_book) as f:
    file_contents = f.read()
fwords = file_contents.split()
sds = 0
letter_count = {}
letter_list = []
for f_word in fwords:
    f_lower = f_word.lower()
    for f_letter in f_lower:
        if f_letter.isalpha():
            if f_letter not in letter_count.keys():
                letter_count[f_letter] = 1
            else: 
                letter_count[f_letter] += 1




letter_list = sorted(letter_count.items(), key = lambda x:x[1], reverse = True)


print(f'--- Begin report of {current_book}')
print(f'{len(fwords)} words found in the document')
for pair in letter_list:
    print(f'The {pair[0]} character was found {pair[1]} times')
print('--- End report ---')