string = '/home/Downloads/firefox/firefox'

print(string.rfind('/'))
string = string[0:string.rfind('/')]
print(string)
print(string[::-1])
print(string[::-1].find('/'))

# string[::-1].find('/') ou string[0:string.rfind('/')