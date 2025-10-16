import re

txt = "abbb"

match = re.search(r"ab{2,3}", txt)

print(match)