with open("1.txt", 'r') as f:
    masses = f.readlines()

def calculate_fuel(mass):
    fuel = 0
    extra = mass
    while True:
        extra = extra // 3 - 2
        if extra > 0:
            fuel += extra
        else:
            break;
    return fuel

masses = [int(mass) for mass in masses]
fuel = [calculate_fuel(mass) for mass in masses]
print(sum(fuel))
