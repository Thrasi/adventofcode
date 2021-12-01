def calculate_fuel_for_mass(mass):
    return int((mass / 3.) - 2)

def calculate_fuel(mass):
    fuel = calculate_fuel_for_mass(mass)
    return max(0,fuel) if fuel <= 2 else fuel + calculate_fuel(fuel) 

with open('input.txt','r') as f:
    masses = map(int,f.readlines())
    fuel = sum([ calculate_fuel_for_mass(mass) for mass in masses])
    print("part 1: {}".format(fuel))
    fuel = sum([ calculate_fuel(mass) for mass in masses])
    print("part 2: {}".format(fuel))

