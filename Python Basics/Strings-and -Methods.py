x = 'Sample String using a single delimiters'
x = 'Single quotes'
y = "Double quotes"
z = '''Triple Quotes'''

# triple quotes string can extend multiple lines
z1 = """First Line
Second Line
Third Line"""
print(x, "\n", y, "\n", z, "\n", z1)

######################
#-Accessing Strings
######################

var1 = 'itsourcecode'
print('var1 = ', var1)

#first character
print('var1[0] = ', var1[0])

#last character
print('var1[-1] = ', var1[-1])

#slicing 2nd to 5th character
print('var1[1:5] = ', var1[1:5])

#slicing 2nd to 2nd last character
print('var1[5:-2] = ', var1[1:-2])

###########################
#-----Updating Strings
###########################
var1 = 'Hello World!'

print ("Updated String:", var1[:6] + 'Universe')
print("Update prior: ", "Byr", var1[6:])

################################
##---------Different Python String Methods
#############################################

'''Split
Replace
Join
Reverse
Uppercase
Lowercase'''

# The split() method divides a text into substrings if it detects the following separator:

names = "Prince, Grace, George"
print(names.split(","))

# The replace() method substitutes one string for another.

names = "Prince, Grace, George"
print(names.replace("George", "John"))

#Joining special symbols with string
print('$'.join('ITSOURCECODE'))

var1="happycode"
print("".join(reversed(var1)))

print(var1.upper())


##Escape sequences
# enclosed with double quotation marks
print("She said, \"How are you?\"")
# enclosed with single quotation marks
print('I said, \"I am fine\"')

'''Escape Characters	Description
\n   ewline	Backslash and newline ignored
\\	Backslash
\'	Single quote
\"	Double quote
\a	ASCII Bell
\b	ASCII Backspace
\f	ASCII Formfeed
\n	ASCII Linefeed
\r	ASCII Carriage Return
\t	ASCII Horizontal Tab
\v	ASCII Vertical Tab
\ooo	Character with octal value ooo
'''

###############################################
#-String Special Operators
###############################################
'''Operator	Description	Example
+	Concatenation – Adds values on either side of the operator	a + b will give HelloPython
*	Repetition – Creates new strings, concatenating multiple copies of the same string	a*2 will give HelloHello
[]	Slice – Gives the character from the given index	a[1] will give e
[ : ]	Range Slice – Gives the characters from the given range	a[1:4] will give ell
in	Membership – Returns true if a character exists in the given string	H in a will give 1
not in	Membership – Returns true if a character does not exist in the given string	M not in a will give 1
r/R	Raw String – Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter “r,” which precedes the quotation marks. The “r” can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.	print r'\n' prints \n and print R'\n'prints \n
%	Format – Performs String formatting	See at next section'''
