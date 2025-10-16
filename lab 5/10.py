import re

txt = "convertThisStringToSnakeCase"

snake_str = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', txt).lower()

print(snake_str)
