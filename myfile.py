f = open("example.txt","w")
f.write("Hello, World!")
f.close()

f = open("example.txt","r")
print(f.read())