with open("6.txt", 'r') as f:
    orbits = f.readlines();

orbit_map = dict()
for orbit in orbits:
    orbit = orbit.strip().split(")")
    orbit_map[orbit[1]] = orbit[0]

orbit_count = 0
for obj in orbit_map.keys():
    while obj in orbit_map:
        obj = orbit_map[obj]
        orbit_count += 1

print(orbit_count)
