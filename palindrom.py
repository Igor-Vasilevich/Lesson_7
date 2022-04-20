Tuple = ('abba', 'privet', 'hello', 'kazak', 'python', 'ahaha', '0110')

result = list(filter(lambda x: x == "".join(reversed(x)), Tuple))
print(f"Palindromes: {result}")
