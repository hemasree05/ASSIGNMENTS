student_dict = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}
student_dict[103] = "Charlie Brown"

print("Dictionary after updating values:", student_dict)
student_name = student_dict.get(102)
print("Accessed value:", student_name)
nested_student_dict = {
    101: {"name": "Alice", "age": 20, "grade": "A"},
    102: {"name": "Bob", "age": 21, "grade": "B"},
    103: {"name": "Charlie", "age": 22, "grade": "A"},
    104: {"name": "David", "age": 23, "grade": "C"},
    105: {"name": "Eve", "age": 20, "grade": "B"}
}

print("Nested Dictionary:", nested_student_dict)
student_101_name = nested_student_dict[101]["name"]
print("Name of student with ID 101:", student_101_name)
keys = student_dict.keys()
print("Keys in the dictionary:", list(keys))
del student_dict[104]

print("Dictionary after deleting a value:", student_dict)

