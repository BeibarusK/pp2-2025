import re

txt = "SplitThisStringAtUpperCaseLetters"

pattern = r"[A-Z][^A-Z]*"

parts = re.findall(pattern, txt)

print(parts)
