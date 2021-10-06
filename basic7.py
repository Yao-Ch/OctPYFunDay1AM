nb =   input("Enter an integral number: ")

nb=int(nb)

# > < >= <= == != and 

if nb > 100 and nb < 1000:
    print(f"{nb} is in the range ]100,1000[  {nb**2}") # 3.6
    print(nb,"is in the range ]100,1000[")
elif nb <= 100 and nb > 0:
    print(nb, "is a small positive number")
else:
    print(nb,"is NOT in the range ]100,1000[")