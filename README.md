# tutedude-assignment-4-python
In this assignment  we can learn ,how to  use file handling.
# 1_module_4.py
(1) we can use try and  except  method.
(2) try:shows  the  code of the program while excepts:shows  ths type of error.
# Program

try:
# try shows the if file exists then it will print the output:

    file = open("sample.txt", "r") # in this line file is open in reading form:
    file.write("Reading file content:\n") # in this line file is print in a terminal:
    file.write("Line 1:This is a sample text file.\n")
    file.write("Line 2:It contains multiple lines.\n")
    file.close() # in this line file is close means no other line will be written: 
    print(file) # print the file:

except FileNotFoundError:
    print("error:the file'sample.txt'was not found.")
  # except shows if file is not exsits which type of error are formed shows:
# 2_module_4.py
(1) In this code,used append:
(2) And used the create the file:
# Program
file=open("output.txt","w") # in this line, it shows the file is open in write form:
data=input("enter write text to the file:")
print("data  is written in successfully  in output.txt")
file.write(data+"\n")# stored as a string:
file.close()

file=open("output.txt","a") # in this line, it shows the file is append: 
extra=input("enter the additional text to print:")
print("data  is written in successfully  in output.txt")
file.write(extra+"\n")
file.close()

file=open("output.txt","r") # in this line, file is read form:
content=file.read()
print("final content of output.txt")
print(content)
file.close()
