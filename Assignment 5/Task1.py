dict_stu = { "Alice" : 78, "Bob" : 87, "Mike" : 93, "Jack" : 67}
name = input("Enter the student's name: ")
if name in dict_stu:
    print("{}'s marks: {}".format(name, dict_stu[name]))
else:
    print("Student not found")