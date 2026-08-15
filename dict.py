marks={"maths":99, "physivs":99, "chem":96}
print(marks, type(marks))

print(marks["maths"])

marks["maths"]=65

marks["english"]=88

print(marks["english"])

for key in marks:
    print(key, marks[key])