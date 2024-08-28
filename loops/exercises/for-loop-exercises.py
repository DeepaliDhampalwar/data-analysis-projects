# Exercise #1: Construct for loops that accomplish the following tasks:
    # a. Print the numbers 0 - 20, one number per line.
    # b. Print only the ODD values from 3 - 29, one number per line.
    # c. Print the EVEN numbers 12 to -14 in descending order, one number per line.
    # d. Challenge - Print the numbers 50 - 20 in descending order, but only if the numbers are multiples of 3. (Your code should work even if you replace 50 or 20 with other numbers).

for num in range (20):
    print(num)

text = "Strings_are_sequences_of_characters."
print(text[:12])

word = 'good'
max_index = len(word)-1
for index in range(max_index, -1, -1):
   print(word[index])

new_word = "tomato"
for index in range(max_index, -1, -1):
   new_word += word[index]

print(new_word)

