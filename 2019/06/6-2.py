with open("6.txt", 'r') as f:
    orbits = f.readlines();

orbit_map = dict()
for orbit in orbits:
    orbit = orbit.strip().split(")")
    orbit_map[orbit[1]] = orbit[0]

orbit_you = []
obj = "YOU"
while obj in orbit_map:
    obj = orbit_map[obj]
    orbit_you.append(obj)
orbit_you.reverse()

orbit_santa = []
obj = "SAN"
while obj in orbit_map:
    obj = orbit_map[obj]
    orbit_santa.append(obj)
orbit_santa.reverse()

i = 0
while orbit_you[i] == orbit_santa[i]:
    i += 1

print(len(orbit_you) + len(orbit_santa) - 2 * i)
