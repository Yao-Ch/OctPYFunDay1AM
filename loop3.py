

while True:
    nb=input("Enter an int or 'stop': ")
    if nb == 'stop':
        break
    nb=int(nb)
    print(nb, "nb**2", nb**2)

print("The end")