def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
gcd = find_gcd(a, b)
print("GCD/HCF is:", gcd)