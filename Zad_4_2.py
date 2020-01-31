'''Write a program that accepts a comma separated sequence of words as input and prints
the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''

words = input().split(',')

sorted_words = []

for i in words:
    sorted_words.append(str(i))

print(sorted_words.sort())