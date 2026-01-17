try:

    file = open("sample.txt", "r")
    file.write("Reading file content:\n")
    file.write("Line 1:This is a sample text file.\n")
    file.write("Line 2:It contains multiple lines.\n")
    file.close()
    print(file)

except FileNotFoundError:
    print("error:the file'sample.txt'was not found.")