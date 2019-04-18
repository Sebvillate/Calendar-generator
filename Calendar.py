def MonthLengthCheck(prompt,MinNumber,MaxNumber):
    n=0
    while MaxNumber<=n or n<MinNumber:
        n=int(float(input(prompt)))
        if MaxNumber>n and n>=MinNumber:
            return n
        else:
            print()
            print("Input is invalid, please enter a valid month length")

def DayOfWeekCheck(prompt):
    while True:
        DayOfWeek=input(prompt)
        if DayOfWeek=="monday":
            return 0
            break
        elif DayOfWeek=="tuesday":
            return -1
            break
        elif DayOfWeek=="wednesday":
            return -2
            break
        elif DayOfWeek=="thursday":
            return -3
            break
        elif DayOfWeek=="friday":
            return -4
            break
        elif DayOfWeek=="saturday":
            return -5
            break
        elif DayOfWeek=="sunday":
            return 1
            break
        else:
            print("Invalid input, please enter a day of the week")
    
            

LengthOfMonth=MonthLengthCheck("How many days are there in the month?: ",28,32)
dow=DayOfWeekCheck("What day does the month start on?: ")
print()
print('  SUN  MON  TUE  WED  THR  FRI  SAT')
for week in range(6):
    for day in range(7):
        if dow>0 and dow<LengthOfMonth + 1:
            print(format(dow,'5'),end='')
        else:
            print("     ",end="")
        dow+=1
    print()
