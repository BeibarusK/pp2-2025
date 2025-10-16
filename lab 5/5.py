import re

txt = "acb aXYZb ab a123b axb testb"

pattern = r"a.*?b"

matches = re.findall(pattern, txt)

print(matches)
