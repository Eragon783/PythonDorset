import os
os.chdir("OneDrive\Documents\ESILV\S5\Python")

file = open(r"names.txt", "r")
for name in file: 
    name = name.strip()
    print("Hello {} !".format(name))
    
file = open(r"names.txt", "r")
for name in file: 
    if "a" in name:
        name = name.strip()
        print("Hello {} !".format(name))
        
file = open(r"names.txt", "r") #reading
file = open(r"names.txt", "w") #writing
file = open(r"names.txt", "a") #appending
file = open(r"names.txt", "r+") #reading and writing

print(file.name)
print(file.mode)

file.close()

with open(r"names.txt", "r") as file:
    print(file.read())
    
with open(r"names.txt", "r") as file:
    print(file.readlines())
    
with open(r"names.txt", "r") as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.readline())
    
with open(r"test.txt", "w") as file:
    file.write("Test")
    
with open(r"test.txt", "r") as file:
    print(file.read())
    
with open(r"test.txt", "w") as file:
    file.write("Hello World")
    file.seek(0)
    file.write("R")
    
with open(r"names.txt", "r") as file_r:
    with open(r"test.txt", "w") as file_w:
        for line in file_r:
            file_w.write(line)
                
with open(r"image.jpg", "rb") as file_r:
    with open(r"image_copy.jpg", "wb") as file_w:
        for line in file_r:
            file_w.write(line)
            
