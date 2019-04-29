##----------------------------------------------------------------------------------------------------------
##Program: Assignemt 4.A Calendar Program
##Author:Sebastian Villate
##Date:April 24th
##Description: A program that recieves an input for the length of the month and the first day of the month,
##and generates a standard calendar within those parameters. The user inputs the length of month into the
##GetIntInput function, which checks for a valid integer input greater than or equal to 28 and less than 32.
##The function loops until a valid input is recieved, and once it is recieved it is returned to the LengthOfMonth
##variable. Then the user inputs the first day of the month into the DayOfWeekCheck function, which checks for
##a valid input within a list named ValidDays. The function loops until a valid input is entered, and once it
##is entered, a integer depending on the day of the week is returned. This is to allign the number 1 on the calendar
##with the corresponding first day of the month. These two inputs are used to generate the calendar, where values
##between 1 and 31 (inclusive) are printed a maximum of rows of 7 and values outside of that range are
##replaced with 5 character spaces.
##Input: Length of month and first day of the month
##----------------------------------------------------------------------------------------------------------


#Checks for a valid input for length of month and repeats loop until valid input is provided.
#When a valid input is entered, it is returned to the LengthOfMonth variable in the program
def GetIntInput(prompt,MinNumber,MaxNumber):
    isInvalid=True
    n=input(prompt)
    while isInvalid:
        if n.isdecimal():
            n=int(n)
            if MaxNumber>n and n>=MinNumber:
                isInvalid=False
            else:
                print("\nInput is invalid, please enter a number between",MinNumber,"and",MaxNumber-1,"inclusive\n")
                n=input(prompt)
        else:
            print("\nAnswer must be an integer\n")
            n=input(prompt)
    return n

# Returns a different value depending on the first day of the month entered. This is done to
#Allign the number 1 on the calendar with the day the month starts on, and to print blank spaces
#Earlier in the week
def DayOfWeekCheck(prompt):
    ValidDays=['sun','mon','tue','wed','thr','fri','sat']
    DayOfWeek=None
    while DayOfWeek not in ValidDays:
        DayOfWeek=input(prompt).lower()
        
        if DayOfWeek=="mon":
            return 0
        elif DayOfWeek=="tue":
            return -1
        elif DayOfWeek=="wed":
            return -2
        elif DayOfWeek=="thr":
            return -3
        elif DayOfWeek=="fri":
            return -4
        elif DayOfWeek=="sat":
            return -5
        elif DayOfWeek=="sun":
            return 1
        else:
            print("Invalid input, please enter a day of the week")
    
#LengthOfMonth is assigned the valid month length returned by the MonthLengthCheck function
LengthOfMonth=GetIntInput("How many days are there in the month?: ",28,32)
#dow is assigned the integer value returned by the DayOfWeekCheck function
dow=DayOfWeekCheck("What day does the month start on?\n(Enter: Sun, Mon, Tue, Wed, Thr, Fri, Sat): ")
print()
print('  SUN  MON  TUE  WED  THR  FRI  SAT\n------------------------------------')
#Loop repeats 6 times in case of a month that the max length of 6 partial weeks
for week in range(6):
#Loop repeats once for each day of the week
    for day in range(7):
    #dow is only printed if it is a positive integer between 1 and 31
        if dow>0 and dow<LengthOfMonth + 1:
            print(format(dow,'5'),end='')
    #If dow<1 and dow>31, a 5 character space is printed instead
        else:
            print("     ",end="")
    #Each time dow is printed, it is increased by 1 to print the next day of the month
        dow+=1
    print()
print("------------------------------------")
