print("The ship's name is 'Brave'.")
# lines in comments are wromng

# print('Cat's paws.')
#
print('The word "Ciao" means "hello" in Italian.')
#
# print("And "Ciao" is Italian "Bye".")


print("WE NEED\nTO LEARN PYTHON\nAS QUICKLY AS POSSIBLE")


print("Sunday")
print()
print("Monday")
print()
print("Tuesday")
print()
print("Wednesday")
print()
print("Thursday")
print()
print("Friday")
print()
print("Saturday")

print("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", sep="\n\n")


weekday = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
for day in weekday:
    print(f'{day}\n')

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(*days, sep='\n\n')


weekdays = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday".split()
print("\n\n".join(weekdays))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in days:
    print(day)
    print()