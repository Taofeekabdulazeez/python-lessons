def sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

isTrue = True
isAlsoTrue = True
isMale = True
gender = "Male" if isMale else "Female"
letter = "A" or "B"

print(letter)
print(gender)

if isTrue or isAlsoTrue:
    print('Yeah, It is true!')
else:
    print('Nope, It is false!')

student = {
    'firstName': 'Taofeek',
    'lastName': 'Abdulazeez',
    'matricNumber': '20/52HA003'
}

for (key, value) in student.items():
    print(f'Your {key} is: {value}')

print(sum(10))

for index, item in enumerate([2, 4, 6, 8, 10]):
    print(index, item)

i = 0
while i <= 10:
    print(i)
    i += 1