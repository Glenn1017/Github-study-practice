
name = input("Enter your expense name?")
num = int(input("Enter your expense num?"))
with open("calculate.txt","a")as file:
    file.write(f"\n{name} - {num}")
print(f"{name} - {num}")

with open("calculate.txt","r")as file:
    readline  = file.readlines()

for n in readline:
    n = int(n)
    total += n 
    
print(f"The total number is {total}")

