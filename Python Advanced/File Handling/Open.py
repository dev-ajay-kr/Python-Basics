import os

f = open("demofile.txt", "rt")

for x in f:
    print(x)
f.close()

f = open("demofile.txt", "rt")
print(f.read())

f.close()

f = open("demofile.txt", "a")
#f = open("demofile3.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()


##creating file

f = open("myfile.txt", "x")

f = open("myfile.txt", "w")


if os.path.exists("demofile.txt"):
  os.remove("demofile1.txt")
else:
  print("The file does not exist")



os.rmdir("myfolder") #removes folder


# File Handling
# The key function for working with files in Python is the open() function.
#
# The open() function takes two parameters; filename, and mode.
#
# There are four different methods (modes) for opening a file:
#
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
# "a" - Append - Opens a file for appending, creates the file if it does not exist
#
# "w" - Write - Opens a file for writing, creates the file if it does not exist
#
# "x" - Create - Creates the specified file, returns an error if the file exists
#
# In addition you can specify if the file should be handled as binary or text mode
#
# "t" - Text - Default value. Text mode
#
# "b" - Binary - Binary mode (e.g. images)





