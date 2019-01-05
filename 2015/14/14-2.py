class Reindeer():
    def __init__(self, name, speed, fly, rest):
        self.name = name
        self.speed = speed
        self.fly = fly
        self.rest = rest

        self.status = 1
        self.time = 0
        self.distance = 0
        self.points = 0

    def race(self):
        if self.status:
            self.distance += self.speed

        self.time += 1
        if self.time == [self.rest, self.fly][self.status]:
                self.status = 1 - self.status
                self.time = 0

with open("14.txt", 'r') as f:
    descriptions = f.readlines()

all_reindeer = []
for desc in descriptions:
    desc = desc.split()
    reindeer = Reindeer(desc[0], int(desc[3]), int(desc[6]), int(desc[-2]))
    all_reindeer.append(reindeer)

for t in range(2503):
    for reindeer in all_reindeer:
        reindeer.race()

    max_distance = max(reindeer.distance for reindeer in all_reindeer)
    for reindeer in all_reindeer:
        if reindeer.distance == max_distance:
            reindeer.points += 1

all_reindeer.sort(key=lambda reindeer: reindeer.points, reverse=True)
print(all_reindeer[0].points)
