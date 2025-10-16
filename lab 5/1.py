import re

txt='abbb'

x = re.fullmatch('ab*', txt)
print(x)