marks=int(input("enter marks"))

if marks>=80:
    print('A') #indentation followed
elif marks<80 and marks>=60:
    print('B')
elif marks<60 and marks>=40:
    print('C')
else:
    print("inavlid")