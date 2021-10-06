
def stats(data):
    total = 0
    for value in data:
        total += value
    mean = total/len(data)
    total = 0
    for value in data:
        total += (mean - value)**2
    variance = total/len(data)
    return (mean, variance)

values=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    
m, v = stats(values)
print("The mean and variance of the values",
"from 1 to 9 inclusive are ",m, "and", v)
