Assignment 4

Task 1:
Here we have used try and except for error handling i.e. if the sample.txt file not available to open then it will give an error "FILENOTFOUNDERROR".
Here in first line we have used a variable file_read to store sample.txt. so, as it will be available if the try will get error and except has to execute.
We are using "r" mode to read the file and for loop to print each line in the file.
As the lines were printed consecutively so to print them on next line we used strip() function.
At last we have to close the file, using close() function.


Task 2:
In this python file we have used a seperate mode each time when using the file to write "w", append "a" and read "r".
Although, we can input a text from user by initializing the new variable (in line 1) or by using the input function inside (in line 6).
Here the point is to be noted that the program itself creates a file if no file exist.
we have printed the successfull statement at the every execution of mode.
Here we have used with open() function so, we does not need to close the file. 