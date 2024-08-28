text = "Strings_are_sequences_of_characters."
print(text[:12])

word = 'good'
max_index = len(word)-1
for index in range(max_index, -1, -1):
   print(word[index])

new_word =  'tomato'
for index in range(max_index, -1, -1):
   new_word += word[index]

print(new_word)  