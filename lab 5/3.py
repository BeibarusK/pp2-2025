import re

txt = "hello_world test_string Python_code simple_example Example_Test"

pattern = r"[a-z]+_[a-z]+"

matches = re.findall(pattern, txt)

print(matches)
