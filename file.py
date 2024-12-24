my_file = open('note.txt')

output = my_file.read()

print(output)

my_file.close() # important

with open('note.txt') as my_file2:
    print(my_file.readlines())
