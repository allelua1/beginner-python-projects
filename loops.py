age = 20
if age < 13:
    print(" Child ")
elif age < 18 :
    print("Teenager")
else:
    print("Adult")

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7 :
        print("I love weekends!")

# while loops
i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)
