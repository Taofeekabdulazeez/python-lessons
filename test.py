

def getUniqueValuesNaive(arr):
    set_values = set()
    for val in arr:
        set_values.add(val)
    return set_values

def getUniqueValues(arr):
    return set(arr);

numbers = [1, 3, 5, 4, 2];
matrix = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

# numbers.sort()
sort_numbers = sorted(numbers);

print(sort_numbers);
print(numbers);

# matrix.extend([[0, 1, 1], [1, 0, 1]])

# print(matrix.count([1, 0, 0]))
# print([0, 1, 1] in matrix)

# if [0, 1, 1] in matrix:
#     print("Yes, it exists")

# for row in matrix:
#     print(row);

# for num in list(range(21)):
#     print(num)

user = None;

if user is None:
    print("No user!")

student = {
    "firstName": "Taofeek",
    "lastName": "Abdulazeez",
    "email": "tao@gmail.com"
}

student['matric_number'] = '20/52HA003'

# print(student);

for value in student.items():
    print(value)

if student["email"] is "tao@gmail.com":
    print("Yes, correct")
else:
     print("No, incorrect")


unique_values = {1, 2, 3, 4, 5};

for i in unique_values:
    print(i)

print(getUniqueValues([1, 2, 3, 3, 4, 5, 9, 1]))