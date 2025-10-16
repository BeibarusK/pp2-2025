import re

txt = "InsertSpacesBetweenWordsStartingWithCapitalLetters"

result = re.sub(r"([a-z])([A-Z])", r"\1 \2", txt)

print(result)
