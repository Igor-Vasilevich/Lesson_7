Tuple = ('abba', 'privet', 'hello', 'kazak', 'python', 'ahaha')

result = list(filter(lambda x: x == "".join(reversed(x)), Tuple))
print(f"Palindromes: {result}")
