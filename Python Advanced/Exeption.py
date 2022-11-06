try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")




# when there is no exception else can be useed
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#finally



try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")






#example
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#--------Custom Exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
