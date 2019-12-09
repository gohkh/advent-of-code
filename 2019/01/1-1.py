with open("1.txt", 'r') as f:
    masses = f.readlines()

masses = [int(mass) for mass in masses]
fuel = [mass // 3 - 2 for mass in masses]
print(sum(fuel))
