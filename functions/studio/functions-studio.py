# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']
listTest1Count=len(list_test1)
listTest2Count=len(list_test2)
listTest3Count=len(list_test3)

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
def reverse_characters(s):
    reverseString=""
    if isinstance(s, str):
        reverseString= s[::-1]
    else:
        s=str(s)
        s=s[::-1]
        reverseString=int(s)
        
    return reverseString
       
# b) Within the function, use the 'list' function to split a string into a list of individual characters

listTest1Count=len(list_test1)
for num in range (listTest1Count):
    result=reverse_characters(list_test1[num])
    print(list(result))
# string_list = string_input.split()


# c) 'reverse' your new list.
list_test1.reverse()
print(list_test1)


# d) Use 'join' to create the reversed string and return that string from the function.
def join_reverse(pl):
    joined_string = "".join(pl)
    reversedString=joined_string[::-1]
    return reversedString
#joined_string.reverse() #joined_string[::-1]
#print(joined_string + " Reversed")

# e) Create a variable of type string to test your new function.
newReversedlist1=join_reverse(list_test1)
print("NewReversed:"+newReversedlist1)
# f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.

# Define a test string
newReversedChars= ""
# Call the function and print the result
newReversedChars=reverse_characters(newReversedlist1)
print(newReversedChars)

print("-----------------------------------")


# g) Use method chaining to reduce the lines of code within the function.


# Define a test string


# Call the function and print the result


# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.
list_test2 = [123, 8897, 42, 1168, 8675309]
for num1 in range (len(list_test2)):
    result=reverse_characters(list_test2[num1])
    print(result)
print("printresult------------------------------")

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
def whichList (listType):
    newList=[]
    if listType=="string":
        print("--------StringList----------")
        for num in range (listTest1Count):
            newList=reverse_characters(list_test1[num])
            print(newList)
        
    elif listType=="number":
        print("-------NumberList----------")
        for num in range (listTest2Count):
            newList=reverse_characters(list_test2[num])
            print(newList)

    else:
        print("---------MixedList------------")
        for num in range (listTest3Count):
            newList=reverse_characters(list_test3[num])
            print(newList)
    
whichList("string")
whichList("number")
whichList("mixed")



# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.




