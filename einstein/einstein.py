def calEnergy(m, c=300000000):
    E = m * c**2
    return E

def main():
    mass = int(input("Please enter a number as a value for mass: "))

    print(calEnergy(mass))





main()
