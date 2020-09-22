import re

text = 'Spiderman'
matches = re.findall('...', text)
result = len(matches[2])

print(result)
