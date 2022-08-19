import re

txt = "The rain in Spain"
x = re.search("i", txt)

print("The first white-space character is located in position:", x.start())