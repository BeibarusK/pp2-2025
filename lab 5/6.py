import re

txt = "Python is, an amazing. language to learn."

pattern = r"[ ,.]"

result = re.sub(pattern, ":", txt)

print(result)
