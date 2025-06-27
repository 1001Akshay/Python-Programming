data = input("Enter text to write to the file: ")
with open("output.txt", 'w') as file:
    file.write(data + "\n")
    print(f"Data successfully written to {file.name}\n")
with open("output.txt", 'a') as file:
    file.write(input("Enter additional text to append: "))
    print("Data successfully appended\n")

with open("output.txt", 'r') as file:
    print(f"Final content of {file.name}")
    for line in file:
        print(line.strip())
