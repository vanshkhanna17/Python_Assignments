
import re
import os.path
#assign1- take input as the phone number and validate
pattern = '^[0-9]{10}$'
numb = input("Enter the number")

matches = re.search(pattern, numb)
if matches:
    print("matched")
else:
    print("not matched")

#assign2- from the current dire extract only .log files and read all email ids


li = os.listdir("C:\\Users\\ssingh722\\Documents\\Python\\demo")
print(li)
for i in li:
    net = os.path.splitext(i)
    if(net[1]==".log"):
        f = open("C:\\Users\\ssingh722\\Documents\\Python\\demo\\" +i, "rb")
        data = f.read().decode()
        pattern = '\S+@\S+'
        matches = re.findall(pattern, data)
        print(matches)
        f.close()
