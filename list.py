marks=[99,98,97,96,95]

print(marks, type(marks))

print(len(marks))

print(marks[3])
print(marks[-1])

print(marks[1:4])
print(marks[-4:-1])

for score in marks:
    print(score)

print(97 in marks)

marks.clear()
print(marks, type(marks))

marks.append(10)
print(marks)
marks.insert(2,30)
print(marks)
