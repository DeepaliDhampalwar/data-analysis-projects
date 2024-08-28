proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

for i, s in enumerate(strings, 1):
    if ',' in s:
        print(f"String {i} contains commas (,)")
    if ';' in s:
        print(f"String {i} contains semicolons (;)")
    if ' ' in s:
        print(f"String {i} contains spaces")
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

for i, s in enumerate(strings, 1):
    if ',' in s:
        # Split the string into a list, reverse it, and join it back into a string
        reversed_string = ','.join(s.split(',')[::-1])
        print(f"Reversed String {i}: {reversed_string}")

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for i, s in enumerate(strings, 1):
    if ';' in s:
        # Split the string into a list, sort it alphabetically, and join it back into a string
        sorted_string = ','.join(sorted(s.split(';')))
        print(f"Alphabetized String {i}: {sorted_string}")
    if ',' in s:
        # Split the string into a list, sort it alphabetically, and join it back into a string
        sorted_string = ','.join(sorted(s.split(';')))
        print(f"Alphabetized String {i}: {sorted_string}")
    if ' ' in s:
        # Split the string into a list, sort it alphabetically, and join it back into a string
        sorted_string = ','.join(sorted(s.split(';')))
        print(f"Alphabetized String {i}: {sorted_string}")


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
string_1 = "united states"
string_array = string_1.split(" ")
print(string_array)
reversed_string1 = string_array[0]
reversed_string2 = string_array[1]
print(reversed_string1)
reversed_string1 = reversed_string1[::-1]
reversed_string2 = reversed_string2[::-1]
print (reversed_string1 + " " +reversed_string2)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
