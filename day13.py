# To check string contain certain sets
import re

str = input(">>>>>>>>>")

regex = re.compile('[abc, sudr, jhiw]+[AB]+[12]')

if(regex.findall(str) == None):
    print("Sting contain no set")
else:
    print("String contain given set")

# String matches word ab
import re

t = input("enter a text")
if re.search('[ab]',t):
    print("pattern matched")
else:
    print("didn't match")

# search number length b/w 1to3
import re

r =re.finditer("[0-9)]{1,3}",2, 22, 14)

print("number of length b/w 1to3")

for n in r:
    print((n.group()))

# match strings that contains only uppercase
m = re.finditer("[A-Z]", "ABCdefg")

for match in m:
    print(match.start(),match.group())

