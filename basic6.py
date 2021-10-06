nb =   input("Enter an integral number: ")

nb=int(nb)



# > < >= <= == != and 

if nb > 100 and nb < 1000:
    print(f"{nb} is in the range ]100,1000[  {nb**2}") # 3.6
    print(nb,"is in the range ]100,1000[")
else:
    print(nb,"is NOT in the range ]100,1000[")