file_read = "sample.txt"
try:
    file = open(file_read, 'r')
    print("Reading file content: ")
    i = 1
    for line in file:
        print(f"Line {i}:",line.strip())
        i+=1
    file.close()
except FileNotFoundError:
    print(f"Error: The file '{file_read}' was not found.")
