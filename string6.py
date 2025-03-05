import re
pattern = r"Amazing"
str1 = "Amazing Work"
match = re.match(pattern, str1)
print(bool(match))