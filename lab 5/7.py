import re

snake_str = "this_is_a_snake_case_string"

components = snake_str.split('_')

camel_str = components[0] + ''.join(x.title() for x in components[1:])

print(camel_str)
