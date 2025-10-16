import re

txt = "Hello world This Is a Python Program Test example"

pattern = r"[A-Z][a-z]+"

matches = re.findall(pattern, txt)

print(matches)
