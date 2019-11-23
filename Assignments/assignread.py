#copy in another file

f = open("demo.text", "r")
print("First: ", f.readline())  # first 3 chars
print("Second: ", f.readline())  # next 3 chars
print("Third: ", f.readline())  # next 3 chars
f.close()


f = open("demo.text", "r")
data = f.read()
print(data)
f.close()

f = open("demo.text", "r")
for line in f:
    print(line)
f.close()

with open("demo1.text", "w") as fo:
    fo.write(data)

f = open("demo.text", "r")
for line in f:
    print(line)
f.close()